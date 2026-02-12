# 原创TongWeb8 应用慢线程检测

> 原文地址: https://blog.csdn.net/realwangpu/article/details/129027674

---

应用场景：
在应用运行过程中，难免会有一些线程因等待锁、阻塞导致执行时间慢。这时可以开启TongWeb8的"慢线程检测"功能来排查问题。
当http线程超过"阻塞阈值"时，则日志输出相应线程堆栈。 通过大量收集该日志样本，以判断线程慢的原因。
注：仅收集一、两个该日志，不能说明线程慢在该处。
2023-02-14 15:29:53 [WARN] - Thread [TW-0.0.0.0-8088-1] (id=[61])
has been active for [20,131] milliseconds
(since [2/14/23 3:29 PM]) to serve the same request for [
http://192.168.55.159:8088/webtest01/TestServlet]
and may be stuck (
configured threshold for this StuckThreadDetectionValve is [20] seconds
). There is/are [1] thread(s) in total that are monitored by this Valve and may be stuck. java.lang.Throwable
at java.lang.Thread.sleep(Native Method)
at com.tong.TestServlet.doGet(TestServlet.java:41)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:503)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:590)
at com.tongweb.server.core.ApplicationFilterChain.enterApp(ApplicationFilterChain.java:365)
"中断阈值" 通常不建议开启，因为实际应用场景中线程有业务相关逻辑，中断线程可能造成业务的不完整。 若能确保中断线程无问题，则可开启。相关日志如下：
2023-02-14 15:29:59 [WARN] - Thread [TW-0.0.0.0-8088-1] (id=[61])
has been interrupted because it was active for [26,177] milliseconds
(since [2/14/23 3:29 PM]) to serve the same request for [
http://192.168.55.159:8088/webtest01/TestServlet]
and was probably stuck (configured interruption threshold for this StuckThreadDetectionValve is [25] seconds). java.lang.Throwable
at java.lang.Thread.sleep(Native Method)
at com.tong.TestServlet.doGet(TestServlet.java:41)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:503)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:590)
at com.tongweb.server.core.ApplicationFilterChain.enterApp(ApplicationFilterChain.java:365)
。。。。。。。
2023-02-14 15:30:01 [WARN] - Thread [TW-0.0.0.0-8088-1] (id=[61])
was previously reported to be stuck but has completed. It was active for approximately [26,177] milliseconds.
"中断阈值"只中断TongWeb的http线程，若应用自建线程出现阻塞，可通过"监视管理"->"阻塞线程"查看，该功能为监控的JVM所有线程。"强停"功能同样谨慎使用。
重点说明：当遇到线程阻塞类问题时，主要通过TongWeb提供的线程堆栈来分析问题，从应用侧来解决。对于"中断阈值", "阻塞线程"的"强停"功能需谨慎使用。
若http通道的线程和队列占满则报错如下：
2023-02-24 13:58:57.963 [WARN] [TW-0.0.0.0-8088-ClientPoller] [com.tongweb.web.util.threads] - Executor rejected socket [
com.tongweb.web.util.net
.NioEndpoint$NioSocketWrapper@fa310e2:
com.tongweb.web.util.net
2023-02-24 13:58:57.963 [WARN] [TW-0.0.0.0-8088-ClientPoller] [com.tongweb.web.util.threads] - Executor rejected socket [com.tongweb.web.util.net.NioEndpoint$NioSocketWrapper@fa310e2:com.tongweb.web.util.net.NioChannel@12bd59a6:java.nio.channels.SocketChannel[connected local=/127.0.0.1:8088 remote=/127.0.0.1:64068]] for
processing java.util.concurrent.RejectedExecutionException: Queue capacity is full
at com.tongweb.web.util.threads.ThreadPoolExecutor.execute(ThreadPoolExecutor.java:138)
at com.tongweb.web.util.threads.ThreadPoolExecutor.execute(ThreadPoolExecutor.java:109)
at
com.tongweb.web.util.net
at com.tongweb.web.util.net.AbstractEndpoint.processSocket(AbstractEndpoint.java:938)
at
com.tongweb.web.util.net
at com.tongweb.web.util.net.NioEndpoint$Poller.processKey(NioEndpoint.java:1366)
at
com.tongweb.web.util.net
.NioEndpoint$Poller.run(NioEndpoint.java:1338)
at java.lang.Thread.run(Thread.java:750)