# 原创TongWeb及应用系统安全加固

> 原文地址: https://blog.csdn.net/realwangpu/article/details/115348676

---

前言
本文档主要面向运维人员说明常见的TongWeb6、TongWeb7安全加固的配置方法。
TongWeb配置
一、首先建议TongWeb升级到最新版本，早期版本存在一些代码级安全漏洞，无法通过配置解决。截止2021年4月15日TongWeb最新版本号为7.0.4.3。
二、TongWeb禁用
不安全的
HTTP方法，可登录控制台，进入
“http
通道管理
”
进行设置。
若用的TongWeb控制台上无此配置，则
需在应用的
web.xml
中增加如下内容，并重新部署生效。（
二选一，应用配web.xml最佳
）
<?xml?version="1.0"?encoding="UTF-8"?>
.......
 <security-constraint>
    <web-resource-collection>
       <url-pattern>/*</url-pattern>
      <!--  加入禁用的方法 -->
       <http-method>DELETE</http-method>
       <http-method>HEAD</http-method>
       <http-method>OPTIONS</http-method>
       <http-method>TRACE</http-method>
    </web-resource-collection>
    <auth-constraint>
    </auth-constraint>
 </security-constraint>
三、远程访问过滤，限制客户端访问的IP，可在虚拟主机中设置。
登录控制台，进入
“
虚拟主机管理
”
的相应虚拟主机进行设置。具体参考
TongWeb
用户手册。
四、TongWeb控制台与应用访问端口由http改为https，见：
https://blog.csdn.net/realwangpu/article/details/109527473
五、TongWeb老版本默认带AJP端口，修改配置见：
https://blog.csdn.net/realwangpu/article/details/109636309
六、TongWeb防SDOS攻击和HOST头攻击，见：
https://blog.csdn.net/realwangpu/article/details/109553849
七、使用X-Frame-Options防止网页被Frame。
TongWeb6、TongWeb7在启动脚本设置参数：-Dtongweb.X_Frame_Options，防止网页被Frame。可设置参数值如下：
参数值
说明
DENY
浏览器拒绝当前页面加载任何Frame页面
SAMEORIGIN
frame页面的地址只能为同源域名下的页面
ALLOW-FROM
允许frame加载的页面地址
八、HTTP头不暴露应用服务器名称
不要在HTTP头中暴露所用的应用服务器名称,如：
HTTP/1.1 200 OK
Content-Type: text/javascript;charset=utf-8
Content-Length: 631
Server: TongWeb Server
TongWeb6,TongWeb7在控制台的http通道中，相应端口的“其它property属性”设置server值，如下：
TongWeb6.0.6.0及以下老版本改法，如下：
# TongWeb5改http头的server名：
将lib下twns-ee.jar中的com\tongweb\advance\server\Version.properties文件
product.name=TongWeb Server  中TongWeb Server改为其它名字即可。
#TongWeb6改http头的server名：
将lib下common.jar中Version.properties 的TongWeb Server改为其它名字即可。
product.name=TongWeb Server
abbrev.product.name=TongWeb Server
九、TongWeb7.0.4.2打开控制台登录验证码，将-DdisableVerCode=true改为false。更改TongWeb控制台密码、有效期,  见：
https://blog.csdn.net/realwangpu/article/details/109509933
十、通过HTTP Referer头禁用指定的来源，在http通道中对HTTP Referer内容进行过滤。
开启验证HTTP Rererer 请求头，不被允许的 Referer请求将被禁止，返回 HTTP状态码 403，默认不开启。开启后可填写允许的主机和允许的IP地址。如果允许的主机和允许的IP地址都为空，将禁止所有的Referer请求,但是来自服务器本机的Referer请求仍然可以处理。
十一、TongWeb7控制台实行三员分立
“ 三员分立” 要求系统管理员、 安全保密管理员、 安全审计员三者之间的关系相互独立、 互相制约， 加强涉密信息系统保密管理， 减少泄密风险。
角色
用户名
密码
默认系统管理员
thanos
thanos123.com
默认安全保密管理员
security
security123.com
默认安全审计员
auditor
auditor123.com
十二、设置TongWeb7审计日志
审计日志文件存储目录为 TW_HOME/logs/audit-log/， 当前使用的日志文件名称为 audit.log， 轮转的日志文件按轮转时刻的日期和时间命名。通过-D 参数可以配置日志相关功能。
参数
含义
-Daudit.log.enabled
审计日志开关， boolean 类型， true 表示开启审计日志记录功能， false 表示关闭审计日志记录功能， 默认值为 true。
-Daudit.log.file.maxSize
审计日志文件按大小轮转阈值，长整数类型， 单位“KB”， 默认值为 1048576， 即10 MB。
-Daudit.log.file.retentionDays
审计日志文件按日期清理阈值， 整数类型， 单位为“天”， 默认值为180， 即 6 个月。
十三、没有用JMS则删除TongWeb的apache-activemq目录，没有用session复制则删除TongWeb的TongDataGrid或Hazelcast目录、samples例子目录也可以删。 这些里面含一些开源组件可能会扫出漏洞。
十四、防止利用sysweb应用上传文件，可以将TongWeb6/7安装目录下applications\sysweb\WEB-INF\web.xml里的upload  servlet删除，如下：
<servlet>
<servlet-name>
upload
</servlet-name>
<servlet-class>com.tongweb.admin.jmx.remote.server.servlet.
AppUploadServlet
</servlet-class>
</servlet>
<servlet-mapping>
<servlet-name>
upload
</servlet-name>
<url-pattern>/upload</url-pattern>
</servlet-mapping>
#关闭该功能后仅是不能通过commandstool命令行远程部署应用，commandstool本地部署应用和通过控制台本地和远程部署应用不受影响。
如果要修改commandstool命令行工具的用户密码，可通过bin目录下的commandstool命令修改，具体可参考对应版本手册。
#TongWeb6.1.5.12及之后版本用户为cli，密码为cli123.com
commandstool> change-admin-password --user cli
Please enter the old admin password>cli123.com
Please enter the new admin password>cli456.com
Please enter the new admin password again>cli456.com
#TongWeb6.1.5.12之前版本用户为root，密码为root
commandstool> change-admin-password --user root
Please enter the old admin password>root
Please enter the new admin password>cli456.com
Please enter the new admin password again>cli456.com
以上配置完成后，重启TongWeb即可。
应用配置
一、 设置应用JSESSIONID、httponly属性，见：
https://blog.csdn.net/realwangpu/article/details/109711846
二、增加安全头信息
某些应用根据安全需求需要在http头上增加X-Content-Type-Options、X-XSS-Protection、Content-Security-Policy等安全信息，可在应用中加filter。TongWeb自带com.tongweb.catalina.filters.CorsFilter可配在应用中，具体请参考《TongWeb7用户使用手册》
public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
   if ((response instanceof HttpServletResponse)) {
       HttpServletResponse httpResponse = (HttpServletResponse)response;
       httpResponse.setHeader("X-Content-Type-Options", "nosniff");
       httpResponse.setHeader("X-XSS-Protection", "1; mode=block");
       httpResponse.setHeader("Content-Security-Policy", "default-src 'self';");
    }
   chain.doFilter(request, response);
}
三、web.xml配置错误页面
在应用WEB-INF/web.xml中增加如下信息和相应页面。如果访问非应用前缀出现404错误，可部署一个前缀为 /  的应用，拦截后做错误页跳转。
<error-page>  
    <error-code>403</error-code>  
    <location>/403.html</location>  
</error-page>  
<error-page>  
    <error-code>404</error-code>  
    <location>/404.html</location>  
</error-page>
四、特定的URL请求由http强制调转到https端口
1. 首先在TongWeb上配置http、https端口，http通道中做重定向https端口配置。
2.应用web.xml里配置重定向的URL规则。
<security-constraint>
  <web-resource-collection >
    <web-resource-name >SSL</web-resource-name>
    <url-pattern>/*</url-pattern>
  </web-resource-collection>
  <user-data-constraint>
    <transport-guarantee>CONFIDENTIAL</transport-guarantee>
  </user-data-constraint>
</security-constraint>
五、升级应用中有安全漏洞的开源框架，如：spring、ActiveMQ等，可在
https://www.cnvd.org.cn
查询。