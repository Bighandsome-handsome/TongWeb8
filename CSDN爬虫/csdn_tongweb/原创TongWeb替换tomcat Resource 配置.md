# 原创TongWeb替换tomcat Resource 配置

> 原文地址: https://blog.csdn.net/realwangpu/article/details/122534654

---

TongWeb的“JNDI资源” 功能用以替换tomcat Resource 配置，该配置常用于JMS、数据源配置.
场景一：JMS配置
tomcat集成ActiveMQ方式
<Resource name="queue/connectionFactory"    
                auth="Container"    
                type="org.apache.activemq.ActiveMQConnectionFactory"  
                description="JMS Connection Factory"  
                factory="org.apache.activemq.jndi.JNDIReferenceFactory"  
                brokerURL="tcp://localhost:61616"  
                brokerName="LocalActiveMQBroker" />  
<Resource name="queue/queue0"    
                auth="Container"    
                type="org.apache.activemq.command.ActiveMQQueue"  
                description="My Queue"  
                factory="org.apache.activemq.jndi.JNDIReferenceFactory"  
                physicalName="Queue" />
TongWeb JNDI资源配置方式如下，这种方式优于genericra方式。
1. 将activemq-all.jar放在TongWeb的lib下或控制台选择jar路径。
2. 队列及队列工厂的配置如下：JMS 连接工厂, JMS 队列
3.可以看到JNDI树上有相应配置
4.在代码上与tomcat区别如下：

```java
InitialContext context = new InitialContext();
/*
 * tomcat方式 QueueConnectionFactory conFactory =
 * (QueueConnectionFactory)
 * context.lookup("java:comp/env/queue/connectionFactory");
 */
// TongWeb方式
QueueConnectionFactory conFactory = (QueueConnectionFactory) context.lookup("queue/connectionFactory");

/*
 * tomcat方式 Queue queue = (Queue)
 * context.lookup("java:comp/env/queue/queue0");
 */
// TongWeb方式
Queue queue = (Queue) context.lookup("queue/queue0");
QueueConnection queConn = conFactory.createQueueConnection();
```

场景二：数据源场景
正常情况下采用JNDI数据源是通过TongWeb的“JDBC配置” ，若想集成第三方开源数据源，且通过JNDI调用方式引用的话也可以配置。以建阿里druid数据源为例的代码使用方式：
```java
Context env = new InitialContext();
DataSource dataSource = (DataSource) env.lookup("jdbc/test");
Connection con = dataSource.getConnection();
```
注：这种是数据源的一种非正常使用方式，非特殊要求尽量少用。