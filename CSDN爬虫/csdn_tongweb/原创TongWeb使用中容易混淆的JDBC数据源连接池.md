# 原创TongWeb使用中容易混淆的JDBC数据源连接池

> 原文地址: https://blog.csdn.net/realwangpu/article/details/115036184

---

问题：
在应用开发、运维过程中，开发、运维人员常分不清采用的哪种JDBC数据源，有的直接答复是用的hibernate、MyBatis，这是上层的持久化框架。JDBC数据源常用的有：应用服务器自身的JNDI数据源、开源数据源 DBCP、 C3P0、Druid、hikari等。接下来我们介绍如何使用和配置。
数据源使用说明：
第一种：采用TongWeb的JNDI数据源，可自学下关于JNDI的知识。
1. 先将数据库驱动包放在TongWeb的lib目录下，并在控制台配置JDBC连接池。
注意：数据库JDBC驱动包由数据库厂家提供。
2. 通常代码调用方式
```java
//与控制台数据源名对应
Context initialContext=new InitialContext();
DataSource dataSource=(DataSource)initialContext.lookup("jdbc/testdb");  
Connection con=dataSource.getConnection();
```
3. 采用类似tomcat调用数据源方式
```java
//通过java:comp/env方式调用， 可自学下关于JNDI的知识。
Context initialContext=new InitialContext();
DataSource dataSource=(DataSource)initialContext.lookup("java:comp/env/jdbc/testdb");  
Connection con=dataSource.getConnection();
```
应用的web.xml中需增加如下配置
```xml
<resource-ref>
    <description>jdbc/testdb</description>
    <res-ref-name>jdbc/testdb</res-ref-name>
    <res-type>javax.sql.DataSource</res-type>
    <res-auth>Container</res-auth>
</resource-ref>
```
如果只是在lookup前加上java:comp/env可以不用像手册说明一样加tongweb-web.xml， 若需要改变lookup名再增加tongweb-web.xml。如：
```xml
//注意一下JNDI名对应关系
(DataSource)initialContext.lookup("java:comp/env/jdbc/testdb2");
//将tongweb-web.xml放在应用的WEB-INF目录  
<?xml version="1.0" encoding="UTF-8"?>
<tongweb-web-app> 
     <resource-links>
     <resource-link name="jdbc/testdb2" type="javax.sql.DataSource" global="jdbc/testdb" />
   </resource-links>
</tongweb-web-app> 

//web.xml增加如下：
<resource-ref>
    <description>jdbc/testdb</description>
    <res-ref-name>jdbc/testdb</res-ref-name>
    <res-type>javax.sql.DataSource</res-type>
    <res-auth>Container</res-auth>
</resource-ref>
```
4. 切记：特殊的TongWeb7.0.C容器版跟tomcat一样，通过java:comp/env方式。
如果要问为什么跟TongWeb企业版、标准版不一样？ 答：思想意见不统一。
```java
Context initialContext=new InitialContext();
DataSource dataSource=(DataSource)initialContext.lookup("java:comp/env/jdbc/testdb");  
Connection con=dataSource.getConnection();
```
```xml
//对应tongweb.xml配置文件中link-name
 <jdbc-connection-pool link-name="jdbc/testdb" name="jdbc/testdb2" 
jdbc-driver="com.mysql.jdbc.Driver" 
jdbc-url="jdbc:mysql://localhost:3316/platform?serverTimezone=UTC&amp;useSSL=false"  ......./>
```
第二种：采用开源数据源
应用采用开源数据源 DBCP、 C3P0、Druid、hikari等无需在TongWeb上进行配置，直接参考官网说明进行开发配置即可。如：DBCP官网`DBCP – Overview`；C3P0官网`https://www.mchange.com/projects/c3p0/`

Spring配置数据源
在实际项目中通常采用spring方式配置数据源，
这种方式的优势是可以在任一开源数据源、JNDI数据源之间切换。
//在jdbc.properties属性文件中定义属性值：
  jdbc.driverClassName= com.mysql.jdbc.Driver 
  jdbc.url= jdbc:mysql://localhost:3309/sampledb 
  jdbc.username=root 
  jdbc.password=1234
  jdbc.initialSize=10
  jdbc.maxActive=50
......

//在spring中配置，读取jdbc.properties属性值，或是将值直接设置在spring xml中。
<bean id="propertyConfigurer"  class="org.springframework.beans.factory.config.PropertyPlaceholderConfigurer">      
    <property name="location" value="/WEB-INF/jdbc.properties"/>      
</bean>      
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource"       
        destroy-method="close">      
    <property name="driverClassName" value="${jdbc.driverClassName}" />      
    <property name="url" value="${jdbc.url}" />      
    <property name="username" value="${jdbc.username}" />      
    <property name="password" value="${jdbc.password}" /> 
    <property name="initialSize" value="${jdbc.initialSize}" /> 
    <property name="maxActive" value="${jdbc.maxActive}" />    
......  
</bean>
//采用TongWeb数据源，spring其本质还是通过(DataSource)initialContext.lookup("jdbc/testdb");   
<bean id="dataSource" class="org.springframework.jndi.JndiObjectFactoryBean">
     <property name="jndiName">            
       <!-- TongWeb企业版、标准版方式 -->
       <value>jdbc/testdb</value>
    </property>
</bean> 
或
<bean id="dataSource" class="org.springframework.jndi.JndiObjectFactoryBean">
    <property name="jndiName">            
      <!-- tomcat与TongWeb7.0.C容器版方式 -->
       <value>java:comp/env/jdbc/testdb</value>
    </property>
</bean>

数据源优化参数必选项：
最后说明一点：无论采用哪种数据源，在使用过程中一定要配置最小连接数、最大连接数、连接验证、测试SQL、连接超时这几项:
最大连接数：一定要先检查数据库剩余的可用连接数，不能超过数据库可用的连接数。
常见问题：不查数据库还允许多少个连接，直接配一个比数据库允许连接数还大的值。
测试SQL:用于验证所取连接是否有效，一定要配置最简单、执行效率最快的SQL。
连接验证：用于获取连接时发送“测试SQL”，以验证连接是否有效， 通常配合TongWeb的 “获取连接时验证”、DBCP的“testOnBorrow ”使用。若不配置，会导致当该连接池与数据库断开时，无法恢复有效的连接。
连接超时：必须配置一个时间。TongWeb默认30秒， DBCP的maxWait、C3P0的checkoutTimeout默认为无限。若不配置，会导致当无法从连接池获取连接时一直等待，造成线程阻塞。

```java
//典型的TongWeb无敌浩克hulk数据源满
java.sql.SQLTransientConnectionException: testdb - Numbers of connections  reached pool maxsize: {testdb}stats (total=10}, active={10} idle={0} waiting={0}) ,so request timed out after 30000ms.]
	at com.tongweb.hulk.pool.HulkPool.createTimeoutException(HulkPool.java:581)]
	at com.tongweb.hulk.pool.HulkPool.getConnection0(HulkPool.java:185)]
	at com.tongweb.hulk.pool.HulkPool.getConnection(HulkPool.java:118)]
	at com.tongweb.hulk.pool.HulkPool.getConnection(HulkPool.java:113)]
	at com.tongweb.hulk.HulkDataSource.getConnection(HulkDataSource.java:66)]
// 典型的DBCP取连接阻塞
"httpWorkerThread-9060-63" #104 daemon prio=10 os_prio=0 tid=0x0000007ec007c800 nid=0x700e waiting for monitor entry [0x0000007deebfb000]
   java.lang.Thread.State: BLOCKED (on object monitor)
         at org.apache.commons.dbcp.PoolableConnectionFactory.makeObject(PoolableConnectionFactory.java:294)
         - waiting to lock <0x00000006830e72c8> (a org.apache.commons.dbcp.PoolableConnectionFactory)
         at org.apache.commons.pool.impl.GenericObjectPool.borrowObject(GenericObjectPool.java:1148)
         at org.apache.commons.dbcp.PoolingDataSource.getConnection(PoolingDataSource.java:96)
         at org.apache.commons.dbcp.BasicDataSource.getConnection(BasicDataSource.java:882)
//典型的C3P0死锁，注意看后面的APPARENT DEADLOCK!!!
[2021-03-27 09:56:43 938] [INFO] [Timer-1] [systemout] [2021-03-27 09:56:43,938 WARN [com.mchange.v2.async.ThreadPoolAsynchronousRunner] - com.mchange.v2.async.ThreadPoolAsynchronousRunner$DeadlockDetector@1798288e -- APPARENT DEADLOCK!!! Complete Status: 
	Managed Threads: 3
	Active Threads: 3
	Active Tasks: 
		com.mchange.v2.resourcepool.BasicResourcePool$AsyncTestIdleResourceTask@3ae1c4e (com.mchange.v2.async.ThreadPoolAsynchronousRunner$PoolThread-#1)
		com.mchange.v2.resourcepool.BasicResourcePool$AsyncTestIdleResourceTask@55a498ed (com.mchange.v2.async.ThreadPoolAsynchronousRunner$PoolThread-#2)
		com.mchange.v2.resourcepool.BasicResourcePool$AsyncTestIdleResourceTask@40aa8f31 (com.mchange.v2.async.ThreadPoolAsynchronousRunner$PoolThread-#0)
	Pending Tasks: 
```