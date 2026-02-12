# 原创TongWeb的JMX线程过多

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109683291

---

通过JMX采集TongWeb监控值后，长时间运行导致JMX线程不断增加，导致 OutOfMemoryError：unable to create new native thread异常。
通过jstack命令分析主要是JMX的server线程越来越多，而不退出。
JMX server connection timeout 207874&quot; daemon prio=10 tid=0x00007f709474c000 nid=0x457b in Object.wait() [0x00007f70626e6000]
java.lang.Thread.State: TIMED_WAITING (on object monitor)
at java.lang.Object.wait(Native Method)
- waiting on &lt;0x00000000d20fbdf8&gt; (a [I)
at com.sun.jmx.remote.internal.ServerCommunicatorAdmin$Timeout.run(ServerCommunicatorAdmin.java:150)
- locked &lt;0x00000000d20fbdf8&gt; (a [I)
at java.lang.Thread.run(Thread.java:662)
主要原因是”JMX server connection timeout”这个超时监测线程增长过快，根据jstack信息来看已经达到800多个，这是因为每个RMIConnection对象都会对应一个单独的”JMX server connection timeout”线程，用来检测该RMIConnection对象的使用是否超时(默认超时时间是2分钟)，达到超时时间后会关闭该RMIConnection并且结束掉对应的timeout线程。通过-Dtongweb.jmx.remote.connection.timeout把超时时间设置的足够小就可以及时释放用过的RMIConnection对象及对应的timeout线程。
-Dtongweb.jmx.remote.connection.timeout=100
(单位：毫秒)，其本质是设置JMX的服务器端Timeout线程超时时间 jmx.remote.x.server.connection.timeout=120000值。