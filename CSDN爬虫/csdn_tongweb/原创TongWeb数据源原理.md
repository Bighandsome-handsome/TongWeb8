# 原创TongWeb数据源原理

> 原文地址: https://blog.csdn.net/realwangpu/article/details/110385749

---

TongWeb数据源原理：通过连接复用减少了创建数据库连接的次数，提高系统的性能。
这类文章很多，就不再细讲了。但在实际使用过程中仍会遇到很多数据源相关问题，接下来介绍几个处理数据源问题常用参数的实现机制。
参数一：泄露超时，打印泄露超时日志是如何实现记录的？
在应用从TongWeb数据源获取数据库连接时，TongWeb记录下当前的stack trace信息，在达到泄露超时时间后，发现该连接还没有回收到连接池，则认为该连接存在泄露的可能性，并将该stack trace信息打印出来。所以看到的stack trace信息是应用获取连接时的代码，此时需要检查该代码在获取连接后有没有执行connection.close()关闭连接。
```bash
[2020-11-30 09:09:52 601] [WARNING] [testdb jdbc-scheduler] [data-source] [java.lang.Exception: A potential connection leak detected for connection pool testdb
at com.tongweb.hulk.HulkDataSource.getConnection(HulkDataSource.java:66)
at com.tongweb.tongejb.resource.jdbc.DecoratorDS.getConnection(DecoratorDS.java:26)
at com.tongweb.tongejb.resource.jdbc.managed.local.ManagedConnection.newConnection(ManagedConnection.java:208)
at com.tongweb.tw.thanos.ThanosManagedConnection.invoke(ThanosManagedConnection.java:70)
at com.sun.proxy.$Proxy153.createStatement(Unknown Source)
at Test.doGet(Test.java:53)   #检查应用处代码有没有close。
at javax.servlet.http.HttpServlet.service(HttpServlet.java:622)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:729)
at com.tongweb.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:230)
at com.tongweb.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:165)
at com.tongweb.web.websocket.server.WsFilter.doFilter(WsFilter.java:53)
at com.tongweb.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:192)
at com.tongweb.catalina.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:165)
at com.tongweb.catalina.core.StandardWrapperValve.invoke(StandardWrapperValve.java:198)
at com.tongweb.catalina.core.StandardContextValve.invoke(StandardContextValve.java:108)
at com.tongweb.catalina.core.ThanosStandardContextValve.invoke(ThanosStandardContextValve.java:108)
at com.tongweb.tomee.catalina.OpenEJBValve.invoke(OpenEJBValve.java:44)
at com.tongweb.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:450)
at com.tongweb.catalina.core.StandardHostValve.invoke(StandardHostValve.java:140)
at com.tongweb.tomee.catalina.OpenEJBSecurityListener$RequestCapturer.invoke(OpenEJBSecurityListener.java:97)
at com.tongweb.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:80)
at com.tongweb.catalina.core.StandardEngineValve.invoke(StandardEngineValve.java:87)
at com.tongweb.catalina.core.ThanosStandardEngineValve.invoke(ThanosStandardEngineValve.java:43)
at com.tongweb.catalina.realm.RealmValve.invoke(RealmValve.java:21)
at com.tongweb.catalina.connector.ThanosCoyoteAdaptor.service(ThanosCoyoteAdaptor.java:432)
at com.tongweb.coyote.http11.Http11Processor.service(Http11Processor.java:776)
at com.tongweb.coyote.http11.ThanosHttp11Processor.service(ThanosHttp11Processor.java:19)
at com.tongweb.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:66)
at com.tongweb.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:913)
at com.tongweb.web.util.net.Nio2Endpoint$SocketProcessor.doRun(Nio2Endpoint.java:1610)
at com.tongweb.web.util.net.SocketProcessorBase.run(SocketProcessorBase.java:49)
at com.tongweb.web.util.net.AbstractEndpoint.processSocket(AbstractEndpoint.java:842)
at com.tongweb.web.util.net.Nio2Endpoint$Nio2SocketWrapper$4.completed(Nio2Endpoint.java:640)
at com.tongweb.web.util.net.Nio2Endpoint$Nio2SocketWrapper$4.completed(Nio2Endpoint.java:618)
at sun.nio.ch.Invoker.invokeUnchecked(Invoker.java:126)
at sun.nio.ch.Invoker$2.run(Invoker.java:218)
at sun.nio.ch.AsynchronousChannelGroupImpl$1.run(AsynchronousChannelGroupImpl.java:112)
at com.tongweb.web.util.threads.TWThreadPoolExecutor.runWorker(TWThreadPoolExecutor.java:1172)
at com.tongweb.web.util.threads.TWThreadPoolExecutor$Worker.run(TWThreadPoolExecutor.java:628)
at com.tongweb.web.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:61)
at java.lang.Thread.run(Thread.java:748)
```
参数二："即时泄漏回收”  或 老版本-Dtongweb.resource.leakCheck是如何实时回收连接的？
在应用从TongWeb数据源获取数据库连接时，将数据源连接记录在当前http线程的ThreadLocal中，当http线程处理完请求后，将该线程ThreadLocal中记录的Connection关闭，以此来达到实时关闭连接的目的。该功能仅限TongWeb自身管理线程，应用线程无法管理。 所以有时还需要结合泄露超时回收一块处理。当前应用多采用hibernate、MyBatis框架下本身应不会出现泄露连接的情况，多数是因为SQL执行时间过长，导致的连接占满。

参数三：“语句超时”参数是如何让SQL超时中断执行的？
本质上就是设置JDBC的 java.sql.Statement的setQueryTimeout(int seconds) 方法。该方法用于中断长时间执行的SQL，但是该方法取决于数据库厂家提供的JDBC驱动包是否支持，并非所有数据库厂家的JDBC驱动支持该方法，所以该功能并非 100%有效。

参数四："SQL执行时间过滤" "SQL日志"参数是如何记录的？
大致的记录过程是记录statement执行SQL的前后时间差，以此来判断SQL执行时间，并将大于"SQL执行时间过滤"的SQL语句和执行时间输出在日志中，以便来分析SQL性能影响。 但是该时间包含JDBC处理时间，并非等于SQL在数据库中执行的时间，多数情况该时间大于SQL在数据库中执行的时间。
```java
long start = System.currentTimeMillis();
Statement.executeQuery(SQl);
long end = System.currentTimeMillis();
log.warn("Slow Query Report SQL="+(end-start));
```
参数五：“线程连接关联”  使用场景。
线程连接关联是将一个数据源连接connection对象存在http线程的ThreadLocal中，让数据源连接与线程一一绑定，不真正归还到连接池中。这样做的好处是：1. 从当前线程池中获取连接，提高获取效率。 2. 当应用存在执行connection.close()后，还去执行statement时报  "Connection has already been closed."，勾选上“ 线程连接关联”后，connection对象依然可用。