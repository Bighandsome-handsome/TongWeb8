# 原创关于TongWeb数据源兼容mysql驱动的注意事项

> 原文地址: https://blog.csdn.net/realwangpu/article/details/148352220

---

问题现象：
TongWeb数据源在采用mysql驱动的国产数据库时，因数据库慢报超时为数据源配置参数的 validation-query-timeout值5秒，而不是期望的maxwait、connectiontimeout值。
```bash
The last packet successfully received from the server was 5,017 milliseconds ago.  The last packet sent successfully to the server was 5,011 milliseconds ago.
	at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
	at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
	at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
	at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
	........
	at com.tongweb.hulk.pool.ProxyPreparedStatement.executeQuery(ProxyPreparedStatement.java:66)
	at com.tongweb.hulk.pool.HulkProxyPreparedStatement.executeQuery(HulkProxyPreparedStatement.java)
	at com.ruimin.ifs.rql.executor.RqlPreparedExecutor.executeQueryPage(RqlPreparedExecutor.java:118)
	... 23 more
Caused by: java.net.SocketTimeoutException: Read timed out
	at java.net.SocketInputStream.socketRead0(Native Method)
	at java.net.SocketInputStream.socketRead(SocketInputStream.java:116)
	at java.net.SocketInputStream.read(SocketInputStream.java:171)
	at java.net.SocketInputStream.read(SocketInputStream.java:141)
	```
解释说明：
TongWeb7.0的hulk数据源的连接验证机制是采用validation-query-timeout的值做connection.setNetworkTimeout(Executors, validation-query-timeout) 网络超时校验，而不是执行的SQL， 校验连接完成后会将NetworkTimeout值恢复为原默认值。而mysql驱动在实现setNetworkTimeout方法时是通过异步方式设置的超时时间，所以有可能导致恢复默认值失败。于是TongWeb7.0对mysql做了处理: 若是mysql驱动则不采用setNetworkTimeout方法。
```java
//TongWeb数据源代码判断
private void createNetworkTimeoutExecutor(final DataSource dataSource, final String dsClassName, final String jdbcUrl)
   {
// Temporary hack for MySQL issue: http://bugs.mysql.com/bug.php?id=75615   
//源码注释中有对mysql驱动bug的说明。只要class, url里有mysql关键字，则按同步处理。
      if ((dsClassName != null && dsClassName.contains("Mysql")) ||
          (jdbcUrl != null && jdbcUrl.contains("mysql")) ||
          (dataSource != null && dataSource.getClass().getName().contains("Mysql"))) {
         netTimeoutExecutor = new SynchronousExecutor();
      }
```
但是由于基于mysql驱动的国产数据库厂商对driverclass, url做了处理，无mysql关键字，导致TongWeb数据源无法判断，从而引起问题。
解决方法：
先确认国产数据库提供的JDBC驱动是不是基于mysql的。若是的话TongWeb7.0进行以下配置解决：
方式一：在TongWeb数据源的url中增加mysql关键字，如：`jdbc:XXXXXXX://localhost:3306/nbmsdb?virtual mysql=true`
方式二：升级为TongWeb7.0.4.9_M6，增加了对mysql驱动兼容的配置。
