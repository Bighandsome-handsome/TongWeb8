# 原创TongWeb的超时线程日志

> 原文地址: https://blog.csdn.net/realwangpu/article/details/121670707

---

问题:
在多数情况下，请求处理慢需要查看线程信息，但是多数情况下：不会用jstack命令打线程、打jstack线程不及时、打出线程不会看。
解决办法：
开启TongWeb的超时线程日志功能。
当http线程执行超时时，server.log中会打出相应日志，如下：
[2021-12-02 09:53:43 117] [INFO] [
ThanosStandardService hung thread check
[2121744517:1638408782579]] [core] [Request Info: Url=http://127.0.0.1:8088/web/Test Parameters
Thread Info: "http-nio2-8088-exec-10" id=39 state=TIMED_WAITING
at java.lang.Thread.sleep(Native Method)
at com.tong.Test.doGet(Test.java:47)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:622)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:729)
at com.tongweb.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:230)
at com.tongweb.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:165)
at com.tongweb.web.websocket.server.WsFilter.doFilter(WsFilter.java:53)
at com.tongweb.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:192)
at com.tongweb.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:165)
at com.tongweb.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:198)
at com.tongweb.catalina.core.StandardContextValve.invoke(StandardContextValve.java:108)
at com.tongweb.catalina.core.ThanosStandardContextValve.invoke(ThanosStandardContextValve.java:107)
at com.tongweb.tomee.catalina.OpenEJBValve.invoke(OpenEJBValve.java:44)
at com.tongweb.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:452)
at com.tongweb.catalina.core.StandardHostValve.invoke(StandardHostValve.java:344)
at com.tongweb.tomee.catalina.OpenEJBSecurityListener$RequestCapturer.invoke(OpenEJBSecurityListener.java:97)
at com.tongweb.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:625)
at com.tongweb.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:80)
at com.tongweb.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:87)
at com.tongweb.catalina.core.ThanosStandardEngineValve.invoke(ThanosStandardEngineValve.java:43)
at com.tongweb.catalina.realm.RealmValve.invoke(RealmValve.java:21)
at com.tongweb.catalina.connector.ThanosCoyoteAdaptor.service(ThanosCoyoteAdaptor.java:469)
at com.tongweb.coyote.http11.Http11Processor.service(Http11Processor.java:867)
at com.tongweb.coyote.http11.ThanosHttp11Processor.service(ThanosHttp11Processor.java:19)
at com.tongweb.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:66)
at com.tongweb.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:921)
at com.tongweb.web.util.net.Nio2Endpoint$SocketProcessor.doRun(Nio2Endpoint.java:1625)
at com.tongweb.web.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
at com.tongweb.web.util.net.AbstractEndpoint.processSocket(AbstractEndpoint.java:857)
at com.tongweb.web.util.net.Nio2Endpoint$Nio2SocketWrapper$4.completed(Nio2Endpoint.java:631)
at com.tongweb.web.util.net.Nio2Endpoint$Nio2SocketWrapper$4.completed(Nio2Endpoint.java:609)
at sun.nio.ch.Invoker.invokeUnchecked(Invoker.java:126)
at sun.nio.ch.Invoker$2.run(Invoker.java:218)
at sun.nio.ch.AsynchronousChannelGroupImpl$1.run(AsynchronousChannelGroupImpl.java:112)
at com.tongweb.web.util.threads.TWThreadPoolExecutor.runWorker(TWThreadPoolExecutor.java:1172)
at com.tongweb.web.util.threads.TWThreadPoolExecutor$Worker.run(TWThreadPoolExecutor.java:628)
at com.tongweb.web.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
at java.lang.Thread.run(Thread.java:748)
Locked synchronizers: count = 1
- com.tongweb.web.util.threads.TWThreadPoolExecutor$Worker@1322b575
]