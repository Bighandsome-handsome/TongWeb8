# 原创一台服务器上能装几套TongWeb，一个TongWeb能跑几个应用？

> 原文地址: https://blog.csdn.net/realwangpu/article/details/110293306

---

常问问题：
1. 一台服务器上能不能装多套TongWeb？
2.装多套TongWeb是按几套产品算费用？
3.专用机默认只能装在/opt/TongWeb下，能不能装在别的目录下用？
4.一个TongWeb上能部署多少个应用？
5.一个TongWeb设多大内存最优？
答复：
一台机器上装一套TongWeb即可，一套可建多个domain域，这样多个TongWeb  domain域实例可充分利用机器资源。一个TongWeb  domain域 能运行的应用并不是以应用个数来计算的。
解释：
概念：一套TongWeb：指一个完整TongWeb物理安装位置。
domain域或实例: 指在TongWeb下能过domain.sh create命令建的一个运行实例，除共用lib下库、license授权、console控制台等之外，其它配置文件、日志、脚本为domain域自有文件，domain域之间是相互独立的Java进程，互不影响。
所以：
1. 一套TongWeb可以通过域domain方式新建并启动多个TongWeb实例，各个实例之间独立运行互不影响，没必要安装多套TongWeb。
2 TongWeb的bin目录下的domain.sh为新建、删除domain的命令。startdomain.sh为启动domain的命令。stopdomain.sh为停止domain的命令。
3. 专用机默认装在/opt/TongWeb，但可以通过 ./domain.sh create  /home/tongweb（绝对路径） 命令将domain建在合适的目录下来用。
4. 应用系统按功能区分： 有的一个应用包含成百上千个功能模块，有的应用系统将各个应用模块独立拆分成十几个应用包，应用功能差别很大；   应用系统按用户量区分，有的应用系统用户量几十万，有的应用系统扔在那没人用； 应用系统按程序来区分，有的应用程序互相冲突并不能在一个JVM进程中运行。所以一台机器启多少个TongWeb实例，一个TongWeb能部多少个应用要按以下规则来判断：
(1)  应用之间互相冲突的，不能部在一个TongWeb  domain域上。
(2）应用有内存溢出或占用线程资源多，频繁出问题的放一个TongWeb domain域上运行，别影响其它应用。
(3)  并发访问量大的应用，还要多个TongWeb domain域上部同一个应用组成集群。
(4)   访问量小又不冲突的应用，可以在一个TongWeb  domain域 上部署多个。
(5)  只要服务器的CPU和内存够用，就可以启多个TongWeb实例。
5.  一个domian 域配多大JVM内存为最优？
误区一：-Xmx设置的内存与top命令看到Java进程占用的不一致。
答：Java程序时会把它所管理的内存划分为若干个不同的运行时数据区域，主要包括：程序计数器、方法区、虚拟机栈、本地方法栈和堆。 -Xmx只是设堆内存，所以通过top看到的Java进程占用内存往往比-Xmx值大。
误区二：JVM内存参数-Xms  -Xmx值越大，性能越高。
答：JVM的性能主要取决于GC(垃圾回收)的效率，GC特别是Full GC执行的越快，则JVM的效率越高。 配置多大内存，取决于应用并发量、业务复杂度。
JVM内存优化这块内容较多，具体可参考：
JVM内存优化、垃圾回收、内存分析知识-Web开发文档类资源-CSDN下载