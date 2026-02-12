# 原创tongweb7部署应用后应用卡顿的参考思路（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/136687564

---

文章目录
1.优化jvm和openfile相关参数
2.排除网络延迟（仅供参考）
3 查看服务器资源的使用情况
3.1查看方式
3.1.1cpu占用过高
方法1：使用脚本show-busy-java-threads.sh进行分析
方法2：使用jstack
3.1.2内存占用过高
3.1.1线程阻塞
3 数据源原因
4.应用代码层面
5.查看并杀掉僵尸进程（仅供参考）
1.优化jvm和openfile相关参数
上图是控制台的jvm参数的配置位置，在这里请确保至少2048m（这里配的是xmx和xms参数）。
Openfile（专用机的话请无视这一步）：在服务器上的命令行工具输入：`ulimit -a`
建议调整为65535，可通过vi /etc/security/limits.conf，添加以下两行：
`soft nofile 65535`
`hard nofile 65535`
修改完后通过linux系统命令ulimit a查看open files值生效后重启 TongWeb
2.排除网络延迟（仅供参考）
可访问服务器ip的电脑上cmd然后ping 域名或者服务器ip：
可访问服务器ip的电脑上cmd ，tarcert 域名或者服务器ip
如果应用本身有其他服务器或者ip交互的配置（例如应用a在服务器a上部署，配置的是b服务器上的数据库或者其他中间件）,可以尝试使用traceroute 域名或者服务器ip，看看响应时间是否超时或者过长：
3 查看服务器资源的使用情况
3.1查看方式
可以在tongweb的控制台查看
重点关注以下内容：
1.内存使用率和cpu使用率
2.使用中堆内存和下面的线程相关的参数，或者在服务器命令行页面执行:`top`，然后执行：`1`
最后执行：`c`。相当于执行了一次top命令，展示当前系统的资源使用情况。之后根据查看的结果，主要有以下几种情况：cpu占用过高，内存占用过高，线程阻塞。
3.1.1cpu占用过高
方法1：使用脚本show-busy-java-threads.sh进行分析
以下是脚本的内容，可以自己建一个sh脚本，将内容复制粘贴进去，然后改名为show-busy-java-threads.sh（使用前提：服务器已配置jdk环境变量，支持例如jmap和jstack指令）
> **工具说明**：该脚本用于快速找出 Java 进程中消耗 CPU 最高的线程，并打印其堆栈信息（jstack），直接定位到耗时的代码行。
> **脚本来源**：[oldratlee/useful-scripts](https://github.com/oldratlee/useful-scripts)
```bash
#!/bin/bash
# Find out the highest cpu consumed threads of java processes, and print the stack of these threads.

readonly PROG="`basename $0`"
readonly -a COMMAND_LINE=("$0" "$@")
readonly USER="`whoami`"

# util functions
readonly ec=$'\033'
readonly eend=$'\033[0m'

colorEcho() {
    local color=$1; shift
    [ -t 1 ] && echo "$ec[1;${color}m$@$eend" || echo "$@"
}

colorPrint() {
    local color=$1; shift
    colorEcho "$color" "$@"
    [ -n "$append_file" -a -w "$append_file" ] && echo "$@" >> "$append_file"
    [ -n "$store_dir" -a -w "$store_dir" ] && echo "$@" >> "${store_file_prefix}$PROG"
}

normalPrint() {
    echo "$@"
    [ -n "$append_file" -a -w "$append_file" ] && echo "$@" >> "$append_file"
    [ -n "$store_dir" -a -w "$store_dir" ] && echo "$@" >> "${store_file_prefix}$PROG"
}

redPrint() { colorPrint 31 "$@"; }
greenPrint() { colorPrint 32 "$@"; }
yellowPrint() { colorPrint 33 "$@"; }
bluePrint() { colorPrint 36 "$@"; }
die() { redPrint "Error: $@"; exit 1; }

logAndRun() { echo "$@"; echo; "$@"; }
logAndCat() { echo "$@"; echo; cat; }

usage() {
    local -r exit_code="$1"
    shift
    [ -n "$exit_code" -a "$exit_code" != 0 ] && local -r out=/dev/stderr || local -r out=/dev/stdout
    cat <<EOF >$out
Usage: ${PROG} [OPTION]... [delay [count]]
Example:
  ${PROG}       # show busy java threads info
  ${PROG} 1     # update every 1 second
  ${PROG} -c 10 # show top 10 busy threads
EOF
    exit $exit_code
}

# Check OS support
uname | grep '^Linux' -q || die "$PROG only support Linux!"

# Parse options
ARGS=`getopt -n "$PROG" -a -o p:c:a:s:S:Pd:Fmlh -l count:,pid:,append-file:,jstack-path:,store-dir:,use-ps,top-delay:,force,mix-native-frames,lock-info,help -- "$@"`
[ $? -ne 0 ] && { echo; usage 1; }
eval set -- "${ARGS}"

while true; do
    case "$1" in
        -c|--count) count="$2"; shift 2 ;;
        -p|--pid) pid="$2"; shift 2 ;;
        -a|--append-file) append_file="$2"; shift 2 ;;
        -s|--jstack-path) jstack_path="$2"; shift 2 ;;
        -S|--store-dir) store_dir="$2"; shift 2 ;;
        -P|--use-ps) use_ps=true; shift ;;
        -d|--top-delay) top_delay="$2"; shift 2 ;;
        -F|--force) force=-F; shift ;;
        -m|--mix-native-frames) mix_native_frames=-m; shift ;;
        -l|--lock-info) more_lock_info=-l; shift ;;
        -h|--help) usage ;;
        --) shift; break ;;
    esac
done

count=${count:-5}
update_delay=${1:-0}
[ -z "$1" ] && update_count=1 || update_count=${2:-0}
top_delay=${top_delay:-0.5}
use_ps=${use_ps:-false}

# Check jstack path
if [ -n "$jstack_path" ]; then
    [ -x "$jstack_path" ] || die "$jstack_path is NOT executable!"
elif which jstack &> /dev/null; then
    jstack_path="`which jstack`"
else
    [ -x "$JAVA_HOME/bin/jstack" ] && jstack_path="$JAVA_HOME/bin/jstack" || die "jstack not found!"
fi

# Biz Logic
readonly run_timestamp="`date "+%Y-%m-%d_%H:%M:%S.%N"`"
readonly uuid="${PROG}_${run_timestamp}_${RANDOM}_$$"
readonly tmp_store_dir="/tmp/${uuid}"
mkdir -p "$tmp_store_dir"

if [ -n "$store_dir" ]; then
    readonly store_file_prefix="$store_dir/${run_timestamp}_"
else
    readonly store_file_prefix="$tmp_store_dir/${run_timestamp}_"
fi

trap "rm -rf $tmp_store_dir" EXIT

findBusyJavaThreadsByPs() {
    local -a ps_cmd_line=(ps ${pid:+-p $pid} ${pid:- -C java -C jsvc} -wwLo pid,lwp,pcpu,user --sort -pcpu --no-headers)
    ps "${ps_cmd_line[@]}" | head -n "${count}"
}

findBusyJavaThreadsByTop() {
    local -a top_cmd_line=(top -H -b -d $top_delay -n 2)
    HOME="$tmp_store_dir" top -H -b -d $top_delay -n 2 | awk -v count="$count" '
    BEGIN { blockIndex = 0; lineCount = 0; }
    /top - / { blockIndex++; }
    blockIndex == 2 && ($NF == "java" || $NF == "jsvc") {
        if(lineCount < count) { print $1, $9; lineCount++; }
    }' | while read line_top; do
        local tid=$(echo $line_top | awk '{print $1}')
        local pcpu=$(echo $line_top | awk '{print $2}')
        ps -wwLo pid,lwp,user -p ${pid:-$(pgrep -d, -u $USER java)} --no-headers | awk -v tid="$tid" -v pcpu="$pcpu" '$2==tid {printf "%s %s %s %s\n", $1, tid, pcpu, $3}'
    done
}

printStackOfThreads() {
    while read line_info; do
        local pid=$(echo $line_info | awk '{print $1}')
        local tid=$(echo $line_info | awk '{print $2}')
        local tid0x="0x`printf %x $tid`"
        local pcpu=$(echo $line_info | awk '{print $3}')
        local user=$(echo $line_info | awk '{print $4}')

        bluePrint "Busy ($pcpu%) thread ($tid/$tid0x) stack of java process ($pid) under user ($user):"
        
        local jstackFile="${tmp_store_dir}/jstack_${pid}"
        if [ "$user" == "$USER" ]; then
            "$jstack_path" $force $mix_native_frames $more_lock_info $pid > "$jstackFile"
        else
            sudo -u "$user" "$jstack_path" $force $mix_native_frames $more_lock_info $pid > "$jstackFile"
        fi

        if [ -n "$mix_native_frames" ]; then
            sed -n "/$tid/,/^--/p" "$jstackFile"
        else
            sed -n "/nid=$tid0x/,/^$/p" "$jstackFile"
        fi
        echo
    done
}

main() {
    for (( i = 0; update_count <= 0 || i < update_count; ++i )); do
        (( i > 0 )) && sleep "$update_delay"
        if $use_ps; then findBusyJavaThreadsByPs; else findBusyJavaThreadsByTop; fi | printStackOfThreads
    done
}

main
```
这个指令会将查出来的结果输出位xx.txt文件输出到opt目录下，方便后面追踪。主要看 Busy里的占比，看看有没有占比比较高的，以及busy里较高的日志信息，有没有相关提示，详细可参考：
how-busy-java-threads脚本初体验，快速排查Java的CPU性能问题
方法2：使用jstack
参考：
记一次java程序CPU占用过高问题排查大致思路：top查一下系统资源占用情况，找出pid
或者也可以跟之前一样，通过监听9060端口和jps指令确认tongweb进程，拿到tongweb的pid
通过这个指令看一下占用和tid：`ps-mp pid -o THREAD,tid,time`找到tid后，通过指令得到16位进制的数字（方便之后使用）`printf“%x\n” tid`之后拿找到的pid和tid转换过来的数字，进行精确定位（红色框第一个是pid，第二个是tid转换过来的数字）：`jstack pid|grep`。tid转换的十六位进制数字，其中显示出了较为详细的代码信息。另外为了方便追踪，也可以执行：`jstack pid | grep`tid转换的数字
上面显示的内容会存入到jstack.txt里面，然后把这个文件交给开发，让开发来排查一下是否是应用代码层面的问题。
3.1.2内存占用过高
这种现象通常是TongWeb控制台和应用访部都很慢，日志中有“OutOfMemoryError：Java heap space”，就跟前面说的“死”一样，但进程还在。通过查看bin下gc.log日志，或通过jstat
命令，查看内存是否占满，Full GC是否频繁。首先，请参考tw7配置gc日志和阈值可执行`jstat ­gcutil 进程号 2000 20`当确认内存满了，执行以下操作：
(1) 要求出现OutOfMemoryError：Java heap space时不要重启Java进程，保留进程继续执行如
下操作。
(2) 利用JDK的jps –v命令查出Java的进程号（或者查看一下tongwbe的进程id）。
(3) 通过jmap –histo > mem.txt 打出文本日志，生成过程很快，文件很小。
(4) 采用jmap生成完整的内存镜像文件
`jmap -dump: format= b,file=/opt/heap.hprof<PID>` 或
`jmap ­dump:live,format = b,file=heap.bin<PID>`
在当前执行命令目录下生成，如果内存设为2G，则生成的内存镜像文件也有2G。
(5) 生成的mem.txt文件可以用文本工具打开直接看，内存镜像文件可以用MemoryAnalyzer内
存分析工具分析。下载地址如： http://www.eclipse.org/mat。 分析这些文件需要用大内存机
器才行，建议用64位windows机器，安装64位MemoryAnalyzer软件，物理内存至少为内存镜
像文件的3倍。
MemoryAnalyzer使用指引参考：
【JVM】日志分析工具一Memory Analyzer Mat介绍和使用
tongweb生成hprof文件并结合Memory Analyzer Mat分析内存溢出
3.1.1线程阻塞
这种现象通常表现为CPU使用不高，TongWeb控制台访问正常，但应用所有页面访问都慢，这种情况通常是应用的http线程池出现阻塞导致的。
出现这种问题时可使用JDK的jstack命令打出线程栈来分析。 如：jstack <java进程id> > log.txt， 输出到指定文件。
重点看：
1.是不是BLOCKED线程很多，这些线程是不是lock在同一地址上， 偶尔几个BLOCKED线程对系统不影响。
如果多次出现这种提示，最好将打印出的文件发给开发来进行排查。
2.有时不一定是BLOCKED，表现为控制台日志一直没有实时滚动，看控制台的线程使用率已满，但是jstack日志信息里没有BLOCKED。
查看jstack日志，有多个 TIMED WAITING (parking)的话，可以看看里面是否有例如数据源相关的代码（ctrl+f搜关键字看看多不多），每段线程下的描述都可以提取关键字进行搜索然后分析：
3 数据源原因
这种现象通常表现为CPU使用不高，TongWeb控制台访问正常，但应用跟数据库无关的页面访问正常，跟数据库有关的页面访问慢。这种分种情况：
(1). 数据源连接池占满，TongWeb的server.log中可以看到数据源占满的日志(开源和
TongWeb数据源都会有)，通过jstack可以看到线程阻塞在数据源上。可能是连接数过小引起的，若加大后还出现就有可能是存在连接泄露问题了，找应用代码泄露的地方改掉。 改不了应用代码就把“泄漏超时”“泄漏回收”同时设置上，这样到达超时时间后，强制回收数据库连接。开源连接池也有这参数。
(2).查看慢sql日志，优化慢sql语句。
4.应用代码层面
1.可记录下应用卡顿的场景，看看应用对应场景的代码，是否设置超时时间（设置过长的超时时间，或者没有设置超时时间，都有可能导致卡顿甚至没有响应）。
2.应用代码里有System.exit(0)代码（找出应用代码用System.exit的地方并删掉，或者启动参数加入­-Djava.security.manager）。
3.使用jstack指令（前面章节有介绍）进行排查。
4.查看日志，例如tongweb的安装目录的logs目录下的日志文件（例如：server.log）。
5.看看应用是否存在重复的类，冲突的jar包和代码。
5.查看并杀掉僵尸进程（仅供参考）
参考：
【Linux】如何杀掉defunct进程-僵尸进程