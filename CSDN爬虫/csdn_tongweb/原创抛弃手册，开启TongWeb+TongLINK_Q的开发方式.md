# 原创抛弃手册，开启TongWeb+TongLINK/Q的开发方式

> 原文地址: https://blog.csdn.net/realwangpu/article/details/115248937

---

问题：
当使用TongWeb+TongLINK/Q产品，想用JMS开发消息服务时，不知如何使用？
1.当你看TongLINK/Q手册《JMS编程参考》时，在给你讲TongWeb5.0+TongLINK/Q8.1的消息驱动bean（Message-Driven Bean，MDB）配置。
2.当你去看TongWeb7的《用户手册》时，在给你讲TongWeb7.0+TongLINK/Q8.1的消息驱动bean（Message-Driven Bean，MDB）配置。
3. TongWeb5.0太老了，MDB开发、配置过程太繁琐。
正确的使用方式：
采用spring  jms框架，抛弃了TongLINK/Q的TongJMS_ra.rar包，省略了一层层的TongWeb配置和MDB开发，单纯的可以通过spring的bean配置快速完成开发，并且可以在ActiveMQ、IBM MQ等JMS服务器之间任意切换，TongWeb无需要任何更改。大致步骤如下：
1.配置TongLINK/Q的jms，只列出片段。如果细讲TLQ配置过程会又臭又长。

```bash
#tlqjndi.conf配置片段
[JndiSystem]		# 
[Factory]		# 连接工厂
#
[FactoryRecord]		# 
FactoryName = RemoteConnectionFactory		# 连接工厂名称
FactoryType = xqf		#  连接工厂类型
tmqiAddressList = tlq://192.168.32.100:10024	# 远程方式的连接url
#
############################################################
[JndiQueue]		# Jndi队列
#
[JndiQueueRecord]		# 
JndiQueueName = lq		# jndi队列名
TlqQueueName = lq		# TLQ的队列名
```
2. spring bean配置文件内容如下：
<?xml version="1.0" encoding="UTF-8"?>
<beans>
	<!-- 配置TLQ的JNDI上下文 -->
	<bean id="jndiTemplate" class="org.springframework.jndi.JndiTemplate">
		<property name="environment">
			<props>
				<prop key="java.naming.factory.initial">tongtech.jms.jndi.JmsContextFactory</prop>
				<prop key="java.naming.provider.url">tlkq://192.168.32.100:10024</prop>
			</props>
		</property>
	</bean>
	<!-- 配置TLQ的JMS连接工厂 -->
	<bean id="JmsQueueConnectionFactory" class="org.springframework.jndi.JndiObjectFactoryBean">
		<property name="jndiTemplate" ref="jndiTemplate" />
		<property name="jndiName" value="RemoteConnectionFactory" />
	</bean>
	<!-- 配置发送队列 -->
	<bean id="sendDestination" class="org.springframework.jndi.JndiObjectFactoryBean">
		<property name="jndiTemplate" ref="jndiTemplate" />
		<property name="jndiName" value="sendq" />
	</bean>
	<!-- 配置接收队列 -->
	<bean id="receDestination" class="org.springframework.jndi.JndiObjectFactoryBean">
		<property name="jndiTemplate" ref="jndiTemplate" />
		<property name="jndiName" value="lq" />
	</bean>
	<!-- 配置JMS模版 -->
	<bean id="jmsTemplate" class="org.springframework.jms.core.JmsTemplate">
		<property name="connectionFactory" ref="JmsQueueConnectionFactory" />
	</bean>
	<!-- 消息监听器，相当于MDB类 -->
	<bean id="myTextListener" class="com.tong.jms.TextListener">
	</bean>
	<!-- jms消费 -->
	<bean id="javaConsumer"
		class="org.springframework.jms.listener.DefaultMessageListenerContainer">
		<property name="connectionFactory" ref="JmsQueueConnectionFactory" />
		<property name="destination" ref="receDestination" />
		<property name="messageListener" ref="myTextListener" />
	</bean>
</beans>
```
3.编写com.tong.jms.TextListener接收消息，相当于MDB

```java
//接受lq队列消息
public class TextListener implements MessageListener {
    public void onMessage(Message message) {
        TextMessage msg = null; 
        try {
            if (message instanceof TextMessage) {
                msg = (TextMessage) message;
                System.out.println("Reading message: " + msg.getText());
            } else {
                System.out.println("Message of wrong type: "
                        + message.getClass().getName());
            }
        } catch (JMSException e) {
            System.out.println("JMSException in onMessage(): " + e.toString());
        } catch (Throwable t) {
            System.out.println("Exception in onMessage():" + t.getMessage());
        }
    }
}
```
4.编写发送消息的bean
```java
//发送sendq队列消息片段
JmsTemplate template = (JmsTemplate) ctx.getBean("jmsTemplate");
Destination destination = (Destination) ctx.getBean("sendDestination");
template.send(destination, new MessageCreator() {
	  public Message createMessage(Session session) throws JMSException {
		  return session.createTextMessage("发送消息：Hello TongLINK/Q  Text Message！");
	  }
});
```
5. 完成，是不是比手册的配置过程简单的多？