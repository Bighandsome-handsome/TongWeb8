# 原创TongWeb生产环境配置规范之一：安装环境配置

> 原文地址: https://blog.csdn.net/realwangpu/article/details/148352626

---

一、硬件环境
物理机、虚拟机、POD推荐分配的最低配置为4核CPU、4G内存、20G硬盘。主要考虑系统并发访问量消耗CPU的情况，TongWeb与应用生成日志的存储空间大小。
二、操作系统
建立TongWeb的安装用户，如：tongweb。
检查常用top、nmon、netstat、lsof、ps等监控命令齐全。
根据不同的linux调整open files值为65535 , 比如：在/ect/security/limits.conf文件中加上两行，并确认生效。
```bash
*  soft  nofile 65535 
*  hard  nofile 65535​
```
根据不同的linux优化tcp/ip参数，比如：
1. 在/etc/sysctl.conf中加入`net.ipv4.tcp_syncookies = 1 `表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭；
2. `net.ipv4.tcp_tw_reuse = 1` 表示开启重用。允许将`TIME-WAIT sockets`重新用于新的TCP连接，默认为0，表示关闭；
3. `net.ipv4.tcp_tw_recycle = 1` 表示开启TCP连接中`TIME-WAIT sockets`的快速回收，默认为0，表示关闭。
```bash
net.ipv4.tcp_fin_timeout=10 
net.ipv4.tcp_keepalive_time=30
```
三、JDK选择与安装
目前国产操作系统平台主要默认提供OpenJDK1.8、OpenJDK11、OpenJDK17或毕昇JDK、TongJDK等，不要采用Oracle JDK以免引起商务问题。
确认应用需要采用的JDK大版本，并检查小版本号尽量为新版本。如：JDK1.8.0_211为2019年版本，为避免JDK引起的bug问题，建议升级为当前较新的JDK1.8.0小版本。
检查操作系统自带完整的JDK，而非jre。否则无jstack、jmap等分析命令。
设置JDK环境变量:
`export  JAVA_HOME=/home/JDK`
`export  PATH=/home/JDK/bin:$PATH`

四、TongWeb选择与安装
优先选择TongWeb当前发布最新版本安装。 若应用系统已经与TongWeb进行过完整适配，则评估下与最新版本的差距，考虑适合的版本。
安装后，将license.dat放在TongWeb下，若为临时license，则要嘱咐用户license过期时间。
启动访问控制台，修改用户密码后将密码告知用户保存。
按用户要求是否做成开机自启动。
按之前性能测试时定下的JVM参数设置，或是做最基本的调优，主要为堆内存大小。上线初期建议打开GC日志，以便分析内存。
建议配置参数
-Xms2048m -Xmx2048m最大，最小堆内存
-XX:+UnlockDiagnosticVMOptions
-XX:+LogVMOutput
-XX:LogFile=../logs/jvm.log

当jstack不可用时，用kill -3 PID记录线程堆栈。
-XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath= ../logs/heap.hprof

当JVM出现内存溢出时自动生成heapdump文件
-XX:+PrintGCDetails
-XX:+PrintGCDateStamps
-Xloggc:/logs/gc-%t.log
-XX:+UseGCLogFileRotation
-XX:NumberOfGCLogFiles=10
-XX:GCLogFileSize=10M

开启GC日志，记录JVM的GC情况，并且将GC日志设置为可轮转，可限制大小的。

常见错误:
1. 未对安装过程做文档记录，事后用户不知安装情况。
2. 操作系统只装了jre，当出现问题时无法通过jstack分析问题。
3. 装的JDK小版本号过低，遇到JVM崩溃问题，需要重新安装JDK 版本。
4. 采用TongWeb嵌入版，未优化open files值，未设置JVM内存，直接java -jar springboot.jar运行系统，导致出现性能问题。
5. 未主动询问用户是否新建系统用户安装TongWeb，配成开机自启动，导致事后又返工重新安装。