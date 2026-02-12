# 原创TongWeb8数据源相关问题

> 原文地址: https://blog.csdn.net/realwangpu/article/details/129022754

---

问题一：数据源连接不足
当TongWeb数据源连接用完时，除了监控中看到连接占用高以外，日志中会有如下提示信息。
2023-02-14 10:24:43 [WARN] - com.tongweb.web.jdbc.pool.PoolExhaustedException: [TW-0.0.0.0-8088-3]
Timeout: Pool empty. Unable to fetch a connection in 30 seconds, none available[size:10; busy:10; idle:0; lastwait:786
].
2023-02-14 10:24:43 [WARN] - at com.tongweb.web.jdbc.pool.ConnectionPool.borrowConnection(ConnectionPool.java:660)
2023-02-14 10:24:43 [WARN] - at com.tongweb.web.jdbc.pool.ConnectionPool.getConnection(ConnectionPool.java:171)
2023-02-14 10:24:43 [WARN] - at com.tongweb.web.jdbc.pool.DataSourceProxy.getConnection(DataSourceProxy.java:117)
2023-02-14 10:24:43 [WARN] - at com.tong.TestServlet.testDB(TestServlet.java:61)
2023-02-14 10:24:43 [WARN] - at com.tong.TestServlet.doGet(TestServlet.java:38)
2023-02-14 10:24:43 [WARN] - at javax.servlet.http.HttpServlet.service(HttpServlet.java:503)
2023-02-14 10:24:43 [WARN] - at javax.servlet.http.HttpServlet.service(HttpServlet.java:590)
造成这一问题的原因有两个：
数据源的"最大连接数" 设置过小，无法满足并发需求，适当调大"最大连接数"即可。但不可超过：
数据库可用的连接数=数据库设置的最大连接数-其它系统已用的连接数。
应用存在连接泄露或SQL执行时间过长，导致连接耗光。在接下来的说明中介绍分析方法。
问题二：应用存在连接泄露的情况
针对应用存在连接泄露的情况，可以开启TongWeb的"连接泄漏检查"，“泄漏时记录日志”。可以从堆栈检查出应用哪里打开Connection，而没有close()。
2023-02-14 10:53:27 [WARN] -
Connection leak detected,
PooledConnection[com.mysql.cj.jdbc.ConnectionImpl@4c9438e4]:java.lang.Exception
at com.tongweb.web.jdbc.pool.ConnectionPool.getThreadDump(ConnectionPool.java:102)
at com.tongweb.web.jdbc.pool.ConnectionPool.borrowConnection(ConnectionPool.java:747)
at com.tongweb.web.jdbc.pool.ConnectionPool.borrowConnection(ConnectionPool.java:610)
at com.tongweb.web.jdbc.pool.ConnectionPool.getConnection(ConnectionPool.java:171)
at com.tongweb.web.jdbc.pool.DataSourceProxy.getConnection(DataSourceProxy.java:117)
at com.tong.TestServlet.testDB(TestServlet.java:61)  #检查这部分代码并修改
at com.tong.TestServlet.doGet(TestServlet.java:38)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:503)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:590)
若应用不能修改代码，则可以再开启"泄漏时关闭连接", 将在达到“泄漏判定时间”,"泄露判定比例"后，强制回收连接。
注意“泄漏判定时间”要大于正常的SQL执行时间。针对个别后台长时间SQL任务占用几个连接，若达不到泄露判定比例则不会强制回收连接。
问题三：应用存在未关闭的statement,导致数据库游标不足的情况
针对应用存在未关闭的statement,导致数据库游标不足的情况，可开启"跟踪语句"。这样在connection.close()时会关闭相应的statement。
若想修改应用代码关闭statement，可开启"跟踪未关闭堆栈",从中可看到哪里没有关闭。如下：
2023-02-14 11:09:30 [WARN] -
Statement created, but was not closed
at: java.lang.Throwable: Statement created at stack
at com.tongweb.web.jdbc.pool.interceptor.StatementFinalizer$StatementEntry.<init>(StatementFinalizer.java:92)
at com.tongweb.web.jdbc.pool.interceptor.StatementFinalizer.createStatement(StatementFinalizer.java:31)
at com.tongweb.web.jdbc.pool.interceptor.AbstractCreateStatementInterceptor.invoke(AbstractCreateStatementInterceptor.java:57)
at com.tongweb.web.jdbc.pool.JdbcInterceptor.invoke(JdbcInterceptor.java:90)
at com.tongweb.web.jdbc.pool.interceptor.AbstractCreateStatementInterceptor.invoke(AbstractCreateStatementInterceptor.java:55)
at com.tongweb.web.jdbc.pool.JdbcInterceptor.invoke(JdbcInterceptor.java:90)
at com.tongweb.web.jdbc.pool.DisposableConnectionFacade.invoke(DisposableConnectionFacade.java:60)
at com.sun.proxy.$Proxy38.prepareStatement(Unknown Source)
at com.tong.TestServlet.testDB(TestServlet.java:66)
at com.tong.TestServlet.doGet(TestServlet.java:38)
问题四：连接有效性验证无SQL配置
TongWeb8数据源会看到没有配SQL语句， 连接验证不再配SQL语句，而是通过connection.isValid(timeout)  API来验证(TongWeb7也是有这功能的)，开启验证日志后，若验证失败会有如下日志输出。
2022-06-07 13:55:45 [ERROR] - isValid() returned false.
2022-06-07 13:55:45 [ERROR] - isValid() returned false.
2022-06-07 13:55:45 [ERROR] - isValid() returned false.
connection.isValid(timeout) 为JDK1.6后增加的方法，有些老的JDBC驱动没有实现这个方法会报错：
2023-06-12 15:06:46 [WARN] -
java.lang.AbstractMethodError
com.tongweb.web.jdbc.pool.
ConnectionPool.isValid(
ConnectionPool.java:83)
com.tongweb.console.server.DataSource.validateDS(DataSource.java:68)
com.tongweb.console.server.DataSource.listInternal(DataSource.java:220)
com.tongweb.ext.manager.ListProcessor.list(ListProcessor.java:28)
sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
或
Exception in thread "TW-Pool Cleaner[1179381257:1689644291207]"
java.lang.AbstractMethodError: org.hsqldb.jdbc.jdbcConnection.isValid(I)Z
at com.tongweb.web.jdbc.pool.PooledConnection.validate(PooledConnection.java:436)
at com.tongweb.web.jdbc.pool.PooledConnection.validate(PooledConnection.java:383)
at com.tongweb.web.jdbc.pool.ConnectionPool.testAllIdle(ConnectionPool.java:1043)
at com.tongweb.web.jdbc.pool.ConnectionPool$PoolCleaner.run(ConnectionPool.java:1138)
at java.util.TimerThread.mainLoop(Timer.java:555)
at java.util.TimerThread.run(Timer.java:505)
问题五：慢SQL的检查
若怀疑有慢SQL可以开启"慢SQL监视"。
可以在监控和日志中看到慢的SQL。
2023-02-14 14:16:57 [WARN] -
Slow Query Report SQL
=select  * from test01,testd  where  test01.test01=testd.test01 and test01.test01 like "%b6%";
time=9075 ms
;
获取慢SQL后可进行优化，或进行SQL超时设置，这取决于JDBC驱动支持API Statement.setQueryTimeout(int timeout)
Failed Query Report SQL
=select  * from test01,testd  where  test01.test01=testd.test01 and test01.test01 like "%b6%"; time=5024 ms;
com.mysql.cj.jdbc.exceptions.
MySQLTimeoutException: Statement cancelled due to timeout or client request
at com.mysql.cj.jdbc.exceptions.SQLExceptionsMapping.translateException(SQLExceptionsMapping.java:113)
at com.mysql.cj.jdbc.StatementImpl.checkCancelTimeout(StatementImpl.java:2189)
at com.mysql.cj.protocol.a.NativeProtocol.sendQueryPacket(NativeProtocol.java:1033)
at com.mysql.cj.protocol.a.NativeProtocol.sendQueryString(NativeProtocol.java:897)
at com.mysql.cj.NativeSession.execSQL(NativeSession.java:1073)
at com.mysql.cj.jdbc.StatementImpl.executeQuery(StatementImpl.java:1166)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
at java.lang.reflect.Method.invoke(Method.java:498)
at com.tongweb.web.jdbc.pool.interceptor.AbstractQueryReport$StatementProxy.invoke(AbstractQueryReport.java:219)
at com.sun.proxy.$Proxy41.executeQuery(Unknown Source)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
at java.lang.reflect.Method.invoke(Method.java:498)
at com.tongweb.web.jdbc.pool.StatementFacade$StatementProxy.invoke(StatementFacade.java:97)
at com.sun.proxy.$Proxy41.executeQuery(Unknown Source)
at com.tong.TestServlet.testDB(TestServlet.java:67)
at com.tong.TestServlet.doGet(TestServlet.java:38)
问题六：采用 java:comp/env/jdbc/testdb方式引用数据源
(1)   配置数据源jdbc/testdb
（2）代码 dataSource = (DataSource) initialContext.lookup("java:comp/env/jdbc/testdb");
（3）应用web.xml中配如下内容
<resource-ref>
    <description>jdbc/testdb</description>
    <res-ref-name>jdbc/testdb</res-ref-name>
    <res-type>javax.sql.DataSource</res-type>
    <res-auth>Container</res-auth>
</resource-ref>
问题七：监控开源数据源
TongWeb8可以监控应用采用的开源数据源
开启监视应用数据源。
在监控管理里“应用数据源”
问题八：JTA事务支持
若需要支持JTA事务、EJB容器事务，需要在配置数据源时开启JTA。同时规则如下：
(1) JTA事务中有两个及以上数据源，必须配置为XA数据源，否则不能保证事务完整性。
(2) JTA事务默认只允许有一个非XA数据源，这样在事务处理上没有问题。若有两个非XA数据源报错如下：
java.lang.IllegalStateException:
Local transaction already has 1 non-XA Resource: cannot add more resources.
at com.tongweb.tongejb.resource.jdbc.managed.local.ManagedConnection.checkNonXA(ManagedConnection.java:107)
at com.tongweb.tongejb.resource.jdbc.managed.local.ManagedConnection.invoke(ManagedConnection.java:190)
at com.sun.proxy.$Proxy75.prepareStatement(Unknown Source)
at com.tong.TestEJB.testdb(TestEJB.java:53)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
at java.lang.reflect.Method.invoke(Method.java:498)
(3) JTA事务严格情况应配置为0， 不建议为解决(2)中的异常设置为2。