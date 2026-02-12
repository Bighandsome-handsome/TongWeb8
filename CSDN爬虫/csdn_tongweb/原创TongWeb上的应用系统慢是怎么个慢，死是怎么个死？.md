# 原创TongWeb上的应用系统慢是怎么个慢，死是怎么个死？

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109442393

---

一：问题现象
常见的反馈问题说法：现在TongWeb上的应用好慢呀，好像死了，宕了，挂了。这种问题描述不够清晰，慢有多种慢的现象，“死”也不是一个专业的说法。下面我们将对这类问题进行分类说明，不同的“死”法，慢法有不同的分析方式。
土语：TongWeb“死”、“宕”、“挂”的描述，这通常是对TongWeb进程没了的表述。实际是指进程不存在或变为僵尸进程这两类情况。“慢”的问题，是指TongWeb进程还在，应用系统虽慢但还能访问，这是应用系统性能问题。 所以在描述问题时，要把“死、宕、挂”与“慢”区分开，在第一步做出准确的现象描述。
基本要求：熟悉Linux基本操作、Java/JavaEE编程、JDK基本命令、TongWeb使用，后面我们会用到。其实还有很多专业的分析工具，如：JProfiler、APM等，但由于项目实际情况没有安装这些软件，且运维人员不一定会使用，所以我们后面的讲解主要以Linux和JDK自带的分析命令为主。
此文较长，请耐心看完。
二：“死”、“宕”、“挂”的问题
情况1. 最低级的“死”法
(1) 有人偷偷停了TongWeb或kill  -9杀掉了TongWeb，别的运维人员不知道。通过history命令或TongWeb生成的nohup.out文件，可以看看到执行过kill -9 命令。
[2021-12-23 13:40:52 793] [INFO] [main] [systemout] [tuserport:0;jcport:0]
./startserver.sh: 行 129: 20496 已杀死 /home/jdk8/bin/java -classpath
/home/jdk8/lib/tools.jar:"/home/TW_7041_Enter_Liunx"/lib/bootstrap.jar:"/home/TW_7041_Enter_Liunx"/lib/jdk-api.jar -Xms2048m -X
(2) 把系统慢当成了“死”，TongWeb还在运行，只是慢的跟"死"一样，其实还没死，误报。
(3) TongWeb不是以nohup ./startserver.sh & 或 startservernohup.sh后台方式启动，造成ssh或telnet断开后，TongWeb进程停止。
(4) 应用代码里有System.exit(0)代码，危险代码。这是退进程的，会导致整个TongWeb进程退出。从TongWeb日志中可以明显看到明显的stop日志：这种问题有两种解决办法：
方法一： 找出应用代码用System.exit的地方并删掉，需要人员能处理应用代码。
方法二：在TongWeb启动脚本external.vmoptions中加如下参数：
```bash
#按conf/tongweb.policy规则，禁止执行System.exit代码。
-Djava.security.manager
#TongWeb7.0.4.1及之后可增加如下参数只拦截exit方法。
-Djava.security.manager=com.tongweb.checkcode.CheckSystemExitSecurityManager
```
说明：
1. -Djava.security.manager参数表示使用
-Djava.security.policy=${TongWeb_Base}/conf/tongweb.policy文件的安全策略。
2. -Djava.security.manager=com.tongweb.checkcode.CheckSystemExitSecurityManager参数则拦截System.exit。
注意：在使用该参数时改为nio线程池，若使用nio2线程池则有：  Exception in thread "InnocuousThread-1516" java.lang.SecurityException: setContextClassLoader 异常，导致端口不可访问。
3. 可以将TongWeb7.0.4.1  lib下bootstrap.jar\com\tongweb\checkcode中的CheckSystemExitSecurityManager.class和ExitException.class拷贝到老TongWeb7版本的bootstrap.jar中使用。
日志可以看到如下异常，拦截了System.exit代码。
```bash
[com.tongweb.checkcode.ExitException: found System.exit(0) !]
[    at com.tongweb.checkcode.CheckSystemExitSecurityManager.checkExit(CheckSystemExitSecurityManager.java:25)]
[    at java.lang.Runtime.exit(Runtime.java:107)]
[    at java.lang.System.exit(System.java:971)]
```
情况2. 进程崩溃问题
排除以上低级死法，发现TongWeb的Java进程确实崩溃了，通常是由于JVM本身不稳定造成的，这时在TongWeb的进程起始目录（通常是TongWeb的bin目录）会生成hs开头的文本文件，收集这个hs文件分析。
情况3. 僵尸进程
进程会变成僵尸进程(defunct)，ps可看到进程被标识为defunct，具体说明可百度。解决办法：A.找到其父进程并杀掉。B. 若杀不掉，只能重启机器。
三：慢的问题
TongWeb上的应用系统慢也分多种情况，需要根据不同的现象进行不同的分析处理，重点是先要理清慢的现象，在慢时抓取相应日志，一旦盲目重启则无法分析。同时，某些人员还会反馈成：应用系统慢，重启TongWeb就好了，所以是TongWeb的问题。
请切记：TongWeb与应用同在一个JVM进程中共享资源，所以出问题重启TongWeb后，TongWeb与应用的资源都会清理掉并重建。 这种方式可以恢复应用，但并不表明为TongWeb问题。 正如当电脑、手机不好用时，可重启机器来解决问题，但并不能确定是哪方软、硬件造成的。
情况1. 最低级的慢是因为没做基本优化
(1)TongWeb没有做基本的优化，三大影响性能的参数:
参数一：没有改启动脚本JVM内存，至少先设2G（-Xms2048m -Xmx2048m) ，但是JVM内存并非越大越好。
参数二：linux 系统没有改open files值(默认1024)，通常改法是修改/etc/security/limits.conf,在文件中加上两行：
*  soft  nofile 65535
*  hard  nofile 65535
修改完后通过linux系统命令ulimit -a查看open files值生效后重启 TongWeb。
另外TongWeb启动脚本也默认增加了ulimit -n 65535， 以防忘记修改open files。
参数三：TongWeb默认快照阈值设置不合理，在未产生性能问题的情况下执行快照功能。无性能问题时关闭快照功能，有性能问题配置合适的阈值。
(2) 数据库没有做基本优化。
(3) 应用没有做基本优化，如：数据源连接池配置过小、日志还是DEBUG级别输出大量日志。
(4) 网速不够。通过网络测试软件，带宽太小，或是在TongWeb本机上访问(linux也可以用firefox)看慢不慢？ 若本机快，能过其它网段访问慢，则基本可以判断是网络问题。
(5) 基本的性能测试都不做，直接上线，肯定出问题。

情况2. CPU占用高引起的慢
现象：通过top命令查看到TongWeb的java进程占用CPU很高。
这时可以通过阿里的分析脚本show-busy-java-threads.sh来分析， 该脚本可用于快速排查Java的CPU性能问题(top us值过高)，自动查出运行的Java进程中消耗CPU多的线程，并打印出其线程栈，从而确定导致性能问题的方法调用。 用法：
`show-busy-java-threads.sh -p <Java进程Id> -c <要显示的线程栈数> -a <输出记录到的文件>TongWeb bin目录下自带命令thread-profiler.sh等同于show-busy-java-threads.sh`
如：`/thread-profiler.sh -p <Java进程ID> -c 500 -a cpulog.txt`
要点：正确查看CPU是否高，有些Linux   CPU若为64核，则CPU为6400%表示满，别以为800%就认为CPU高了。要在出现CPU高的问题时打该命令，学会看线程栈。

情况3. 线程阻塞引起的慢
这种现象通常表现为CPU使用不高，TongWeb控制台访问正常，但应用所有页面访问都慢或不能访问应用端口，这种情况通常是应用的http线程池大部分出现阻塞导致的。出现这种问题时可使用JDK的jstack命令打出线程栈来分析。 如：jstack <java进程id> > log.txt，输出到指定文件。 重点看是不是BLOCKED线程很多，这些线程是不是lock在同一地址上， 偶尔几个BLOCKED线程对系统不影响。
要点：会用jstack命令，要在出现慢的问题时执行该命令，并学会看线程栈，
重点查看这种"http-nio-0.0.0.0-8080-exec-XX" 以通道类型、绑定IP、端口号为命名规则的线程池堆栈。

情况4. 数据源引起的慢
这种现象通常表现为CPU使用不高，TongWeb控制台访问正常，但应用跟数据库无关的页面访问正常，跟数据库有关的页面访问慢。
这种分种情况：
(1). 数据源连接池占满，TongWeb的server.log中可以看到数据源占满的日志(开源和TongWeb数据源都会有)，通过jstack可以看到线程阻塞在数据源上。可能是连接数过小引起的，若加大后还出现就有可能是存在连接泄露问题了，开启"泄露日志"找到应用代码泄露的地方改掉。 改不了应用代码就把“泄漏超时”“泄漏回收”或”即时回收“设置上，这样到达超时时间后，强制回收数据库连接。开源连接池也有这参数。当超时后，以WARNING级别将该堆栈信息输出到日志。从日志中可以分析到哪里存在未关闭的连接。日志示例如下：
（2). 若部分数据库业务慢，TongWeb数据源可记录下执行时间长的SQL，针对SQL进行优化。通常情况下采用hibernate、mybatis框架不会有连接泄露问题，更多问题的是获取一个连接后SQL执行时间长引起的。
(3). 采用开源连接池c3p0、DBCP、Druid等也有类似配置，请注意应用中的开源数据源配置。如druid连接池满导致的异常。
Caused by: com.alibaba.druid.pool.GetConnectionTimeoutException: wait millis 60000, active 100, maxActive 100, creating 0, createErrorCount 24
要点：熟悉TongWeb数据源和开源数据源的配置，并会从数据库端分析。
情况5. 内存引起的慢
这种现象通常是TongWeb控制台和应用访部都很慢，日志中有“OutOfMemoryError”，就跟前面说的“死”一样，但进程还在。
通过GC日志或jstat命令，查看内存是否占满，Full GC是否频繁。
#gc.log中有Full GC过于频繁的日志如下：
```bash
1004277.657: [Full GC 7442688K->7326004K(7909312K), 14.7484964 secs]
1004292.491: [Full GC 7442688K->7234814K(7909312K), 17.6059770 secs]
1004310.273: [Full GC 7442687K->7327296K(7909312K), 14.6444008 secs]
1004325.036: [Full GC 7442687K->7328115K(7909312K), 14.6859322 secs]
```
jstat：用于输出java程序内存使用情况，包括新生代、老年代、元数据区容量、垃圾回收情况。
例：`jstat -gcutil 进程号 2000 20`
上述命令输出进程ID为3618的内存使用情况（每2000毫秒输出一次，一共输出20次）
S0：幸存1区当前使用比例 S1：幸存2区当前使用比例
E：伊甸园区使用比例 O：老年代使用比例
M：元数据区使用比例 CCS：压缩使用比例
YGC：年轻代垃圾回收次数 FGC：老年代垃圾回收次数
FGCT：老年代垃圾回收消耗时间 GCT：垃圾回收消耗总时间
当确认内存满了，执行以下操作：
(1)  要求出现OutOfMemoryError：Java heap space时不要重启Java进程，保留进程继续执行如下操作。
(2) 利用JDK的jps –v命令查出Java的进程号。
(3) 通过
jmap –histo <PID>  >  mem.txt
打出文本日志，生成过程很快，文件很小。
(4) 采用jmap生成完整的内存镜像文件 :
jmap -dump:live,format=b,file=heap.hprof  <PID>
在当前执行命令目录下生成，如果内存设为2G，则生成的内存镜像文件也有2G。
若生成文件比-Xmx值小很多，则没有分析的必要。
(5) 若出现问题来不及或不会用jmap生成参数，可在TongWeb启动脚本external.vmoptions中增加如下参数，在内存溢出时自动生成内存镜像文件。
-XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath=../logs/heap`date +%Y%m%d%H%M`.hprof
-XX:+PrintGCDateStamps
-XX:+PrintGCDetails
-Xloggc:../logs/gc`date +%Y%m%d%H%M`.log
(6) 生成的mem.txt文件可以用文本工具打开直接看，内存镜像文件可以用MemoryAnalyzer内存分析工具分析。下载地址如：
Eclipse Memory Analyzer Open Source Project | The Eclipse Foundation
。 分析这些文件需要用大内存机器才行，建议用64位windows机器，安装64位MemoryAnalyzer软件，物理内存至少为内存镜像文件的3倍。
误区：JVM内存够不够用主要看GC(垃圾回收)情况，JVM内存并非设越大越好、JVM内存并非设越大越好、JVM内存并非设越大越好。
要点：熟悉JVM的GC机制、会用jstat、jmap、MemoryAnalyzer分析JVM内存。
情况6. "大部分业务正常，只有个别业务慢"， 这是应用该部分业务的问题，与中间件无关。推荐TongAPM、阿里开源的 java 诊断工具-Arthas，可做源码级性能分析。
通过arthas的monitor命令查看方法调用次数和时间。
通过arthas的trace命令分析方法耗时。
四: 如何一次收集全性能分析日志
最糟糕的情况是说不清以上慢的情况，出问题时着急重启TongWeb解决没有收集日志。这种情况下，只能将TongWeb该开启的日志全开启，企盼在出现问题时能尽量抓取的日志全些。对TongWeb进行以下配置：
1.  在bin/external.vmoptions文件中打开GC日志和生成内存溢出镜像的参数。
-XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath=../logs/heap`date +%Y%m%d%H%M`.hprof
-XX:+PrintGCDateStamps
-XX:+PrintGCDetails
-Xloggc:../logs/gc`date +%Y%m%d%H%M`.log
2. 修改快照生成默认值，只生成jstack日志。若http最大线程数设300,  则可在快照的通道设置中将该http通道“最大线程数”设为250。 在线程使用量高时打出jstack。
3. 开启超时线程日志，在server.log中记录该线程栈信息。
```bash
[2021-03-29 14:13:16 977] [INFO]
[ThanosStandardService hung thread check
[1174290147:1616998336906]] [core] [Request Info: Url=http://127.0.0.1/dbpool/ Parameters
Thread Info: "http-nio2-0.0.0.0-80-exec-2" id=223 state=TIMED_WAITING
- waiting on <0x067b630c> (a java.util.concurrent.SynchronousQueue$TransferQueue)
- locked <0x067b630c> (a java.util.concurrent.SynchronousQueue$TransferQueue)
at sun.misc.Unsafe.park(Native Method)
at java.util.concurrent.locks.LockSupport.parkNanos(LockSupport.java:215)
at java.util.concurrent.SynchronousQueue$TransferQueue.awaitFulfill(SynchronousQueue.java:764)
at java.util.concurrent.SynchronousQueue$TransferQueue.transfer(SynchronousQueue.java:695)
at java.util.concurrent.SynchronousQueue.poll(SynchronousQueue.java:941)
at com.tongweb.hulk.util.ConcurrentBag.borrow(ConcurrentBag.java:137)
at com.tongweb.hulk.pool.HulkPool.getConnection0(HulkPool.java:148)
at com.tongweb.hulk.pool.HulkPool.getConnection(HulkPool.java:118)
at com.tongweb.hulk.pool.HulkPool.getConnection(HulkPool.java:113)
```
4. 若采用TongWeb数据源，则开启“泄露日志”，“SQL日志”。开源连接池也可以开启泄露。
5. 如果还会操作些命令，在TongWeb机器上通过`netstat -an|grep  http端口`，在数据库机器上通过`netstat -an|grep  数据库端口`查看端口状态。
6. 如果还会操作些命令， 执行bin下 `./thread-profiler.sh -p <Java进程ID> -c 500 -a cpulog.txt` 。最后提供收集日志给相关人员，并说明出现问题的时间点，提供logs下所有日志，以及1-6步产生的日志。千万别只会说一句：重启就没事了。

五：总结
通过以上说明，主要是让各位了解一下出现系统问题时，该如何描述问题，针对不同的问题现象该如何处理。处理这些问题的最基本要求是：
1. 理清问题现象。
2. 会通过Linux基本命令、jstack、jstat、jmap、show-busy-java-threads.sh、jpsArthas、MemoryAnalyzer等工具和命令收集日志。具体使用方法可百度 。
3. 会查看GC日志、线程日志、内存镜像日志，并熟悉JVM、TongWeb参数的调优、应用代码的优化。