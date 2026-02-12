# 原创TongWeb的session超时设置以及不依赖于TongWeb session的场景

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109697973

---

TongWeb 的 session 超时设置按优先级从高到低依次为：
方式一：
在应用代码中设置 session 超时时间 session.setMaxInactiveInterval(60);//单位为秒。
方式二：
在应用的 web.xml 中设置 session 超时时间，单位为分钟。
<session-config>
<session-timeout>30</session-timeout>
</session-config>
方式三：
在 TongWeb 控制台上设置 session 超时时间，单位为分钟。 tongweb-web.xml 的 session超时配置可忽略，基本不用。
应用若不设置，默认 30 分钟。通常 session 超时时间值为 1-1440 分钟即可， 实际环境中客户每天会打开新的 IE 访问， 产生新的 session。而某些配置人员将 session 设为永久或 1 个月等更长超时， 试想极少存在用户打开IE 后， 一天或连续几天都不访问一次应用的，甚至连 IE 也不关闭的。 这样配置反而导致无用 session 长期存在， 应用服务器产生过多的 session，有内存溢出的可能。
TongWeb的session 不是决定应用会话状态的唯一因素，在SSO、Apache shiro应用场景下，session不起主要作用。这时在TongWeb上配session的超时时间、session共享、复制已无用。
1. 单点登录SSO应用
以CAS应用为例，登录验证的是ticken，而不是session。配置因CAS版本不同而不同，相关超时配置如以下：
<bean id="grantingTicketExpirationPolicy" class="org.jasig.cas.ticket.support.RememberMeDelegatingExpirationPolicy">
<property name="sessionExpirationPolicy">
<bean class="org.jasig.cas.ticket.support.
TimeoutExpirationPolicy
">
<constructor-arg index="0" value="1800000"></constructor-arg>
</bean>
</property>
<property name="rememberMeExpirationPolicy">
<bean class="org.jasig.cas.ticket.support.
TimeoutExpirationPolicy
">
<constructor-arg index="0" value="2592000000"></constructor-arg>
</bean>
</property>
</bean>
2. Apache shiro应用
Shiro提供了三个默认session管理实现，在shiro应用中有时可能会看到产生的session都不是TongWeb所生成的，配session复制更没用。
实现一：DefaultSessionManager：DefaultSecurityManager使用的默认实现；
实现二：ServletContainerSessionManager：用于Web环境，其直接使用Servlet容器的会话；
实现三：DefaultWebSessionManager：用于Web环境的实现，可以替代ServletContainerSessionManager,自己维护着会话,直接废弃了Servlet容器的会话管理。
<bean id="sessionManager" class="org.apache.shiro.web.session.mgt.
DefaultWebSessionManager
">
<!-- 设置超时时间 -->
<property name="globalSessionTimeout" value="1800000"/>
<property name="deleteInvalidSessions" value="true"/>
<property name="sessionValidationSchedulerEnabled" value="true"/>
<property name="sessionIdCookieEnabled" value="true"/>
<property name="sessionIdCookie" ref="sessionIdCookie"/>
</bean>