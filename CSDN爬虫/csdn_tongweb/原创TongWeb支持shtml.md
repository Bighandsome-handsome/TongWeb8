# 原创TongWeb支持shtml

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109591883

---

TongWeb支持shtml语言，只需打开conf/default-web.xml文件中的对应配置即可。将如下描述的注释  <!--   -->去掉即可。
<servlet>
<servlet-name>ssi</servlet-name>
<!--  TongWeb6类名  -->
<servlet-class>com.tongweb.web.thor.ssi.SSIServlet</servlet-class>
<!--  TongWeb7类名，注意类名不同，只选其一。    为什么不整成一样的呢？  -->
<servlet-class>com.tongweb.catalina.ssi.SSIServlet</servlet-class>
<init-param>
<param-name>buffered</param-name>
<param-value>1</param-value>
</init-param>
<init-param>
<param-name>debug</param-name>
<param-value>0</param-value>
</init-param>
<init-param>
<param-name>expires</param-name>
<param-value>666</param-value>
</init-param>
<init-param>
<param-name>isVirtualWebappRelative</param-name>
<param-value>0</param-value>
</init-param>
<load-on-startup>4</load-on-startup>
</servlet>
<servlet-mapping>
<servlet-name>ssi</servlet-name>
<url-pattern>*.shtml</url-pattern>
</servlet-mapping>
<filter>
<filter-name>ssi</filter-name>
<!--  TongWeb6类名  -->
<filter-class>com.tongweb.web.thor.ssi.SSIFilter</filter-class>
<!--  TongWeb7类名，注意类名不同，只选其一。  -->
<filter-class>com.tongweb.catalina.ssi.SSIFilter</filter-class>
<init-param>
<param-name>contentType</param-name>
<param-value>text/x-server-parsed-html(;.*)?</param-value>
</init-param>
<init-param>
<param-name>debug</param-name>
<param-value>0</param-value>
</init-param>
<init-param>
<param-name>expires</param-name>
<param-value>666</param-value>
</init-param>
<init-param>
<param-name>isVirtualWebappRelative</param-name>
<param-value>0</param-value>
</init-param>
</filter>
<filter-mapping>
<filter-name>ssi</filter-name>
<url-pattern>*.shtml</url-pattern>
</filter-mapping>