# 原创如何判断TongWeb是否支持某种数据库？

> 原文地址: https://blog.csdn.net/realwangpu/article/details/131370614

---

起因：
数据库连接池本是一项成熟的技术，但随着数据库厂家、种类的增加，常常被问到TongWeb是否支持XX数据库？
说明：
数据库连接池的基本思路是，平时建立适量的数据库的连接，放在一个集合中，当有用户需要建立数据库连接的时候，直接到集合中取出一个数据库连接对象（Connection），这样不用再需要重新创建，这样会节省大量的资源，当用户不需要在对数据库进行访问了，那么就将数据库连接对象（Connection）重新放回到集合中，以便方便下次使用。
数据源的使用参见：
https://blog.csdn.net/realwangpu/article/details/115036184
所以判断TongWeb是否支持该数据库，可以基于以下几点来判断？
是关系型数据库、还是非关系型数据库？ 非关系型数据库通常不是JDBC接口。
是否提供标准的JDBC驱动包?  即实现了java.sql.*接口，JDBC驱动程序通常由数据库供应商提供。
还有一些数据库是基于PostgreSQL、 MySQL封装的，可以直接用PostgreSQL 、MySQL的驱动包，这一类的肯定支持。
是采用TongWeb数据源，还是采用开源JDBC数据源( DBCP、 C3P0、Druid、hikari等),  其它开源池  ?   这便于从其配置项判断。 如下：
#采用开源数据源的JDBC数据源
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

```java
import org.apache.hadoop.hbase.client.*;
//HBase为非关系型数据库，有自己的连接API，不能配JDBC数据源
public class HBaseTest {
 
	// 声明静态配置，配置zookeeper
	static Configuration configuration = null;
	static Connection connection = null;
	static {
		configuration = HBaseConfiguration.create();
		configuration.set("hbase.zookeeper.quorum", "study-90:2181,study-91:2181,study-92:2181");
		try {
			connection = ConnectionFactory.createConnection(configuration);
            Table table = connection.getTable(TableName.valueOf(tableName));
            .......
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
```
关于“支持”的定义：支持并不一定指非要配置在TongWeb上的数据源，通过应用中集成开源池可以运行在TongWeb上，也可以认为是支持。
TongWeb本身只是提供数据源的连接，只要是提供JDBC驱动的数据库问题都不大。其实适配数据库最主要的是TongDXP、TongETL这类产品。
常见错误问题：
1. 问：TongWeb是否支持XX数据源？
首先用词不准确："支持"与“提供”是两种不同含义，提供是指产品本身所具有的功能;  支持可以是产品本身不提供，但可以通过其它方式支持。
错误之处：只提供几个字母是无法判断，要问清用户，数据库类型，提供JDBC驱动等。 通病： 往往用户再问是否支持XX技术时，往往还没有问清该技术是什么，就直接转发给同事问：“我们产品是否支持XX”,  这类仅凭几个字母是无法回答的。要进一步问清该技术全称是什么、有什么技术要求等等。
2. 问：TongWeb数据源列表中只有这几种数据库，那是否只支持这几种数据库？
错误之处：只是列出常用数据库，未列出的不代表不支持，还可以通过JDBC模版增加数据源种类。
3. 问：TongWeb数据源是否能配redis池？
错误之处：想想redis是JDBC接口的？