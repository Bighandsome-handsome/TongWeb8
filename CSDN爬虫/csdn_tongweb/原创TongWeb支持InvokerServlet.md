# 原创TongWeb支持InvokerServlet

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109592292

---

InvokerServlet功能早在tomcat7之后已经废除，但由于很多老应用依旧采用而且不想改造，所以TongWeb也增加了该功能。
TongWeb6、TongWeb7 默认不开启InvokerServlet， 需在conf/default-web.xml中增加如下servlet打开InvokerServlet功能。
<servlet> 
    <servlet-name>invoker</servlet-name> 
    <!-- TongWeb6 配置如下类名 -->
    <servlet-class>com.tongweb.web.thor.servlets.InvokerServlet</servlet-class> 
    <!-- TongWeb7 配置如下类名,  注意类包差别，只选其一。    为什么不整成一样的呢？--> 
    <servlet-class>com.tongweb.catalina.servlets.InvokerServlet</servlet-class>
    <init-param> 
       <param-name>debug</param-name> 
       <param-value>0</param-value> 
    </init-param> 
    <load-on-startup>2</load-on-startup> 
</servlet>       
<servlet-mapping> 
    <servlet-name>invoker</servlet-name> 
    <url-pattern>/servlet/*</url-pattern> 
</servlet-mapping>