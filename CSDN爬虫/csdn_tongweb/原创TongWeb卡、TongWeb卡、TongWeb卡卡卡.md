# 原创TongWeb卡、TongWeb卡、TongWeb卡卡卡

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109534310

---

问题描述：
现象一. TongWeb启动时卡住了起不来、启动慢。
现象二：TongWeb部署应用时卡在70%不动了。
现象三：TongWeb访问量大时，CPU也不高，JVM内存也够，但就是慢。
现象四：执行stopserver.sh无效，停不下来TongWeb。
问题原因：
多数是由于TongWeb中的应用阻塞导致的。
解决办法：
一定要善用JDK的jstack命令，这是一个分析Java线程的常用命令。
一定要在当前进程卡或慢时执行如下操作，
注意：过了这村就没这店了。千万不要重启TongWeb后再操作，此时已无效。
1. 执行：  jstack  <PID>   >  tongweb.log    把线程栈输出到文件中分析。
注：  <PID>替为TongWeb的进程号，千万别直接输<PID>。
2. 极端情况 Java进程反应不过来，执行jstack无效或没装JDK，没有jstack命令。  这时可以执行 ：kill -3  <PID> ，日志输出在TongWeb的logs/jvm.log中。
注：kill -3不是杀进程。注意保存jvm.log，重启TongWeb后该文件重写。
生成文件后重点看BLOCKED或WAITING线程，间隔几秒多执行几次jstack，若看到BLOCKED或WAITING在同一位置，多个线程锁在同一个地址则可能是这里的原因。
重点查看线程:
1. 如果是应用运行过程中存在线程问题，多关注以端口类型和端口号命名的线程池，如："http-nio-8088-exec-342"
"http-nio-8088-exec-342"
#3049 daemon prio=5 os_prio=0 tid=0x00007f539006f800 nid=0x48da runnable [0x00007f537d4af000]
java.lang.Thread.State: RUNNABLE
at java.net.SocketInputStream.socketRead0(Native Method)
at java.net.SocketInputStream.socketRead(SocketInputStream.java:116)
at java.net.SocketInputStream.read(SocketInputStream.java:171)
at java.net.SocketInputStream.read(SocketInputStream.java:141)
at com.mysql.jdbc.util.ReadAheadInputStream.fill(ReadAheadInputStream.java:101)
at com.mysql.jdbc.util.ReadAheadInputStream.readFromUnderlyingStreamIfNecessary(ReadAheadInputStream.java:144)
at com.mysql.jdbc.util.ReadAheadInputStream.read(ReadAheadInputStream.java:174)
- locked <0x00000006c4718ab8> (a com.mysql.jdbc.util.ReadAheadInputStream)
at com.mysql.jdbc.MysqlIO.readFully(MysqlIO.java:3011)
at com.mysql.jdbc.MysqlIO.reuseAndReadPacket(MysqlIO.java:3472)
2. 如果是通过控制台部署应用卡，则多关注以控制台端口命名的线程池，且含有
deploy
关键字的线程，如："http-nio2-9060-exec-9060-63"。
部署卡到70%常见的主要情况为：应用采用开源数据源，但没有配连接超时参数，在部署应用、大并发时获取到不连接，一直卡在获取数据库连接上。
"http-nio2-9060-exec-63"
#104 daemon prio=10 os_prio=0 tid=0x0000007ec007c800 nid=0x700e waiting for monitor entry [0x0000007deebfb000]
java.lang.Thread.State: BLOCKED (on object monitor)
at org.apache.commons.dbcp.PoolableConnectionFactory.makeObject(PoolableConnectionFactory.java:294)
- waiting to lock <0x00000006830e72c8> (a org.apache.commons.dbcp.PoolableConnectionFactory)
at org.apache.commons.pool.impl.GenericObjectPool.borrowObject(GenericObjectPool.java:1148)
at org.apache.commons.dbcp.PoolingDataSource.getConnection(PoolingDataSource.java:96)
at org.apache.commons.dbcp.BasicDataSource.getConnection(BasicDataSource.java:882)
3. 如果是TongWeb启动慢，则重点看main主线程即可。
"main"
#1 prio=5 os_prio=0 tid=0x0000ffffb404f000 nid=0x7486 runnable [0x0000ffffbba2b000]
java.lang.Thread.State: RUNNABLE
at java.net.Inet6AddressImpl.lookupAllHostAddr(Native Method)
at java.net.InetAddress$2.lookupAllHostAddr(InetAddress.java:928)
at java.net.InetAddress.getAddressesFromNameService(InetAddress.java:1323)
at java.net.InetAddress.getLocalHost(InetAddress.java:1500)
- locked <0x00000005c008eb50> (a java.lang.Object)
at dm.jdbc.dbaccess.DbPureAccess.isLocalHost(DbPureAccess.java:220)
4. 要善于利用文本工具Notepad++等的统计功能，查看多个线程是否BLOCKED或WAITING在同一地址。
注意：(1). 多线程锁在同一地址的才有问题。(2). 偶尔一、两个BLOCKED或WAITING不是问题。(3).千万别一看到locked就认为有问题。
如上图是一个典型的数据源满在等数据源连接的一个性能问题。 而如下则没有问题，只是http线程池的空闲等待。
"http-nio2-8088-exec-3" #32 daemon prio=5 os_prio=0 tid=0x000000001bf2a000 nid=0x2198 waiting on condition [0x0000000022dbe000]
java.lang.Thread.State: WAITING (parking)
at sun.misc.Unsafe.park(Native Method)
- parking to wait for  <0x0000000080c5a5d8> (a java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject)
at java.util.concurrent.locks.LockSupport.park(LockSupport.java:175)
at java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject.await(AbstractQueuedSynchronizer.java:2039)
at java.util.concurrent.LinkedBlockingQueue.take(LinkedBlockingQueue.java:442)
at com.tongweb.web.util.threads.TaskQueue.take(TaskQueue.java:103)
at com.tongweb.web.util.threads.TaskQueue.take(TaskQueue.java:31)
at com.tongweb.web.util.threads.TWThreadPoolExecutor.getTask(TWThreadPoolExecutor.java:1094)
at com.tongweb.web.util.threads.TWThreadPoolExecutor.runWorker(TWThreadPoolExecutor.java:1156)
at com.tongweb.web.util.threads.TWThreadPoolExecutor$Worker.run(TWThreadPoolExecutor.java:628)
at com.tongweb.web.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
at java.lang.Thread.run(Thread.java:748)
另外推荐一个show-busy-java-threads.sh脚本，可以分析每个线程占用的CPU。
https://github.com/oldratlee/useful-scripts/blob/master/docs/java.md#beer-show-busy-java-threadssh