# 原创TongWeb日志报Too many open files

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109711145

---

问题现象：
大量如下日志：
```bash
[2020-05-08 14:39:25] [SEVERE] [web-container] [Http listener ServerSocket[addr=/0.0.0.0,port=0,localport=9060] shutdown by exception: java.net.SocketException:Too many open files]
[2020-05-08 14:39:25] [SEVERE] [web-container] [Http listener ServerSocket[addr=/0.0.0.0,port=0,localport=9060] shutdown by exception: java.net.SocketException:Too  many open files]
```
问题原因：
open files为Linux操作系统下进程允许打开的文件句柄数，若超过此值，则会报此异常。
解决办法：
1. 通过linux系统命令ulimit -a查看open files值为默认的1024，这个值偏小，建议值为65535。
#登录linux系统，输入命令`ulimit –a`。
```bash
[root@5 ~]# ulimit -a
core file size (blocks, -c) 0
data seg size (kbytes, -d) unlimited
scheduling priority (-e) 0
file size (blocks, -f) unlimited
pending signals (-i) 4096
max locked memory (kbytes, -l) 32
max memory size (kbytes, -m) unlimited
open files (-n) 1024      !重点查看此值
max user processes (-u) 4096
```
不同系统可能修改方式不同，  linux将操作系统的open files值改为65535。比如：修改/etc/security/limits.conf,在文件中加上两行：
*  soft  nofile 65535
*  hard  nofile 65535
2. TongWeb6, 7的startserver.sh启动脚本已默认增加了：`ulimit -n 65536 >/dev/null 2>&1`对当前TongWeb进程生效。
3. 若确认了修改open files值为65535后，还报Too many open files，则应用可能存在打开文件句柄过多的情况。 通过操作系统的`lsof -p  <PID>`命令查看打开什么文件多，具体分析。