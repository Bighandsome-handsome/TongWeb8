# 原创TongWeb通过CGI支持PHP的方法

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109591564

---

通俗一句话：等同于tomcat的CGIServlet。  配置方法如下：
1. 前提是要先安装好PHP运行环境，这一步是必须的，请从PHP: Hypertext Preprocessor下载编译安装合适的PHP版本。如果是国产平台，请确保已安装PHP程序，TongWeb不带PHP运行程序。关于PHP更多配置请查相关资料。
2. TongWeb通过CGIServlet调用PHP，配置如下：
在PHP应用目录里建个WEB-INF目录，建个web.xml中加入如下内容，改造成一个JavaEE应用的war结构包。注：有的文章可能写在conf/default-web.xml中配置，其实也可以。 加在应用web.xml中的好处是一次配完，可随意拷贝到其它地方用。
<?xml version="1.0" encoding="UTF-8"?>
<web-app>
	<servlet>
		<servlet-name>cgi</servlet-name>
		<!-- TongWeb6 配置如下类名 -->
		<servlet-class>com.tongweb.web.thor.servlets.CGIServlet
		</servlet-class>
		 <!-- TongWeb7 配置如下类名, 注意类包差别，只选其一。 为什么不整成一样的呢？ -->
		<servlet-class>com.tongweb.catalina.servlets.CGIServlet
		</servlet-class>
		<init-param>
			<param-name>cgiPathPrefix</param-name>
			<!-- 部一个web应用，把php页面放在这个目录，或是根本不配这个参数，直接把PHP页面放在应用根下， 放在应用根下更好 -->
			<param-value>WEB-INF/cgi</param-value>
		</init-param>
		<init-param>
			<param-name>executable</param-name>
			<!-- 指到php-cgi命令 -->
			<param-value>D:/php7.2/php-cgi.exe</param-value>
		</init-param>
		<init-param>
			<param-name>passShellEnvironment</param-name>
			<param-value>true</param-value>
		</init-param>
		<load-on-startup>5</load-on-startup>
	</servlet>
	<servlet-mapping>
		<servlet-name>cgi</servlet-name>
		<!-- 访问应用http://IP:port/前缀/index.php ，只处理php -->
		<url-pattern>*.php</url-pattern>
	</servlet-mapping>
</web-app>
3.  将该PHP目录当JavaEE应用部署在TongWeb上即可访问。
4. 相关PHP问题，还需配置PHP配置文件php.ini, 此处省略。
注：该方式为TongWeb支持PHP的一种变通方式，至于该方式到底实不实用，待看。