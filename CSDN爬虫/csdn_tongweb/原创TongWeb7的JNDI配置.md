# 原创TongWeb7的JNDI配置

> 原文地址: https://blog.csdn.net/realwangpu/article/details/122539481

---

Java命名和目录接口（Java Naming and Directory Interface，JNDI）是用于从Java应用中访问名称 和目录服务的一组API。
从其它应用服务器移植涉及到JNDI资源的配置的变更，这些配置常在spring中配置。常用到JNDI的地方：数据源、事务、EJB。
场景一：数据源的JNDI配置
#jndi.properties, weblogic的JNDI配置为例

jndiName=jdbc/testdb
jndiUrl=t3://192.168.1.10:7001
jndiInitial=weblogic.jndi.WLInitialContextFactory
#spring applicationContext.xml

<bean id="dataSource" class="org.springframework.jndi.JndiObjectFactoryBean">
   <property name="jndiName">
		<value>${jndiName}</value>
   </property>
   <property name="jndiEnviroment">
	 <props>
		 <prop key="java.naming.provider.url">${jndiUrl}</prop>
		 <prop key="java.naming.factory.initial">${jndiInitial}</prop>
	 </props>
	</property>
</bean>
如上为weblogic上的数据源配置,若迁移到TongWeb上有两种解决方式
方式一：直接去掉jndiEnviroment 采用TongWeb默认JNDI, applicationContext.xml改为如下
<bean id="dataSource" class="org.springframework.jndi.JndiObjectFactoryBean">
   <property name="jndiName">
		<value>${jndiName}</value>
   </property>
</bean>
注意：通常在同一JVM进程内调用数据源不需要写JNDI上下文。
方式二：若某些配置情况下无法删除jndiEnviroment, 则写明TongWeb的JNDI。如下：
#jndi.properties

jndiName=jdbc/testdb
jndiUrl=http://192.168.1.10:5100/ejbserver/ejb
jndiInitial=com.tongweb.naming.java.javaURLContextFactory

applicationContext.xml配置不变
场景二：事务的JNDI配置
#weblogic配置
<bean id="txManager" class="org.springframework.transaction.jta.WebLogicJtaTransactionManager">
   <property name="userTransactionName"  value="weblogic/transaction/UserTransaction">
   </property>
</bean>
#spring没有针对TongWeb的事务bean类，所以用JtaTransactionManager
<bean id="transactionManager" class="org.springframework.transaction.jta.JtaTransactionManager">
  <property name="userTransactionName" value="java:comp/UserTransaction" />
  <property name="transactionManagerName" value="tongweb:/TransactionManager"/>
</bean>
注意：TongWeb不同版本的事务JNDI名可能不同，具体看对应版本的手册。
场景三：EJB远程调用
EJB本地调用也不需要指明JNDI上下文，只有EJB服务端与EJB客户端不在同一JVM中，需要远程调用时指明JNDI，其EJB客户端代码如下：
Properties props = new Properties(); 
props.setProperty("java.naming.factory.initial","com.tongweb.tongejb.client.RemoteInitialContextFactory"); 
props.setProperty("java.naming.provider.url", "http://192.168.0.11:5100/ejbserver/ejb"); 
Context jndiContext = new InitialContext(props); 
HelloHome home = (HelloHome)jndiContext.lookup("myHello");

#还可以以EJB服务端集群方式使用
Properties props = new Properties(); 
props.setProperty("java.naming.factory.initial","com.tongweb.tongejb.client.RemoteInitialContextFactory"); 
props.setProperty("java.naming.provider.url", "http://192.168.0.11:5100/ejbserver/ejb?readTimeout=60000,http://192.168.0.12:5100/ejbserver/ejb?readTimeout=60000"); 
props.setProperty("remote.loadbalance", "random");
Context jndiContext = new InitialContext(props); 
HelloHome home = (HelloHome)jndiContext.lookup("myHello");
说明：
#访问本地资源的初始化上下文环境属性
java.naming.factory.initial=com.tongweb.naming.java.javaURLContextFactory

#远程的InitialContext所需的环境属性配置如下。其中，<IP>需要修改为TongWeb所在的IP, <port>为EJB远程调用端口，默认是5100。
java.naming.factory.initial=com.tongweb.tongejb.client.RemoteInitialContextFactory
java.naming.provider.url=http://<ip>:<port>/ejbserver/ejb