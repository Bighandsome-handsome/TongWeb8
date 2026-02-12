# 原创TongWeb6、7开启WebDAV的支持

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109697304

---

在应用的web.xml里加如下内容：
<servlet>
    <servlet-name>webdav</servlet-name> 
    <!-- TongWeb 6的类 -->
    <servlet-class>com.tongweb.web.thor.servlets.WebdavServlet</servlet-class>
    <!-- TongWeb 7的类, 二选一 -->
    <servlet-class>com.tongweb.catalina.servlets.WebdavServlet</servlet-class>
      <init-param>
         <param-name>debug</param-name>
         <param-value>0</param-value>
      </init-param>
      <init-param>
          <param-name>listings</param-name>
          <param-value>true</param-value>
      </init-param>
      <!-- Read-Write Access Settings -->
      <init-param>
          <param-name>readonly</param-name>
          <param-value>false</param-value>
      </init-param>
</servlet>
<!-- URL Mapping -->
<servlet-mapping>
      <servlet-name>webdav</servlet-name>
      <url-pattern>/*</url-pattern>
</servlet-mapping>