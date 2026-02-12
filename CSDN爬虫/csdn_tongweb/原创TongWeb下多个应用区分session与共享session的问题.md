# 原创TongWeb下多个应用区分session与共享session的问题

> 原文地址: https://blog.csdn.net/realwangpu/article/details/122528815

---

应用场景：
同一个TongWeb下部署了多个应用系统(如:应用A与应用B)，多个应用系统之间需要互相跳转。

需求一：需要互相访问应用上下文
解决办法:
跨上下文的访问，需要在启动脚本中配置参数
```bash
-Dopenejb.crosscontext=true
```
相当于tomcat的<Context path="/A" debug="0" reloadable="true"crossContext="true"/>
这样B应用的代码可用：req.getSession().getServletContext().getContext("/A") 获取A的上下文。

需求二：多个应用要区分开http头的jsessionid，以免混淆
解决办法：在应用的web.xml中自定义会话cookie的名字
```bash
<session-config>
<session-timeout>30</session-timeout>
<cookie-config>
<name>MYJSESSIONID</name>
</cookie-config>
</session-config>
```
需求三：
多个应用要共享一个jsessionid，但session中存的属性值不同
解决办法：在启动脚本中配置参数:`-DSharedSessionContext=true`这是复用http
请求里基于Cookie附带的jsessionid，不再生成新的ID，适用跨应用跳转和SSO应用。ID虽然相同，但session中的属性值是不同的。

需求四：
多个应用要共享一个jsessionid，session中存的属性值也相同
解决办法：在启动脚本中配置参数:`-DSharedSessionContext=true -DSharedSessionEnable=true`两个参数为true，表示多个应用共享session。