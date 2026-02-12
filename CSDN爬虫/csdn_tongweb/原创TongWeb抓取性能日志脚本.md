# 原创TongWeb抓取性能日志脚本

> 原文地址: https://blog.csdn.net/realwangpu/article/details/123060655

---

通过之前的文章可以看到，在出现性能问题时除了开启TongWeb监控功能，还需要手工执行一系列性能分析命令来排查问题，因为TongWeb的监控功能不足以分析问题。而这种手工操作对于项目运维人员有难度，往往急于恢复系统，重启TongWeb来解决。下面提供一个脚本，尽可能执行一次就抓取全部日志。
#本脚主要针对在性能出现问题时，一次执行抓取日志命令不全，甚至参数不加全的问题。
#将该脚本放在TongWeb的bin目录下，当发生慢时一次执行记录CPU,netstat,句柄，jstack,kill -3,busy,jmap，执行出错的跳过去继续执行。
#若在涉密机下无权限执行，则通过   . ./slowlog.sh的方式来执行，注意两点有空格。
#执行完把TongWeb的logs目录打包留底。
#若JDK环境变量不对，记得设PATH变量。要有jstack、jmap、jstat命令不能只装jre。

```bash 
tongwebhome=`pwd`
export tongwebhome
tongpid=`ps -ef | grep java | grep $tongwebhome | awk '{print $2}'`
export tongpid
echo "execute top command"
top -H -b -d 3 -n 3 > ../logs/top`date +%Y%m%d%H%M`.log
echo "execute nestat command"
netstat -antlp  > ../logs/netstat`date +%Y%m%d%H%M`.log
echo "execute lsof command"
lsof -p $tongpid > ../logs/lsof`date +%Y%m%d%H%M`.log
echo "execute jstat command"
jstat -gcutil $tongpid 1000  10 > ../logs/jstat`date +%Y%m%d%H%M`.log
echo "execute jstack command"
jstack  $tongpid > ../logs/jstack`date +%Y%m%d%H%M`.log
echo "execute kill -3 command"
kill -3 $tongpid >/dev/null 2>&1
cp ../logs/jvm.log ../logs/jvm`date +%Y%m%d%H%M`.log
echo "execute thread-profiler.sh command"
./thread-profiler.sh -F -p $tongpid -c 500 -a ../logs/busy`date +%Y%m%d%H%M`.log  3 3   >/dev/null 2>&1
echo "execute jmap command"
jmap -histo $tongpid  > ../logs/heap`date +%Y%m%d%H%M`.log
jmap -dump:live,format=b,file=../logs/heap`date +%Y%m%d%H%M`.bin $tongpid 
echo "complete......... "
```