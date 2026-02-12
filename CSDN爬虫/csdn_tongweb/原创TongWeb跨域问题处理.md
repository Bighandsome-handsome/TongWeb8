# 原创TongWeb跨域问题处理

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/142909950

---

这里写自定义目录标题
现象
排查思路
现象
f12控制台报错Access to XMLHttpRequest at ‘xxx’ from origin ‘xxxx’ has been blocked by CORS policy: Response to preflight request doesn’t pass access control check: No ‘Access-Control-Allow-Origin’ header is present on the requested resource.
排查思路
确认跨域的请求方式
，如果不是get,post请求，则需要在tongweb控制台放开；
确认后端项目有没有跨域配置
，常见的有过滤器CorsFilter，@CrossOrigin等，如果有则不需要在tongweb中配置跨域，
重复配置会导致冲突，跨域不生效
；
没有使用跨域配置，在项目web.xml或者tongweb/conf/default-web.xml中配置；
<filter>
	<filter-name>CorsFilter</filter-name>
	<filter-class>com.tongweb.catalina.filters.CorsFilter</filter-class>
	<init-param>
		<!-- 允许访问资源的源列表。可以指定*表示接受任意域名的请求 -->
		<param-name>cors.allowed.origins</param-name>
		<param-value>*</param-value>
	</init-param>
	<init-param>
		<!-- 以逗号分隔的HTTP方法列表 -->
		<param-name>cors.allowed.methods</param-name>
		<param-value>GET,POST,TRACE,OPTIONS,HEAD,DELETE,PUT,CONNNECT</param-value>
	</init-param>
	<init-param>
		<!-- 跨域允许包含的头 -->
		<param-name>cors.allowed.headers</param-name>
		<param-value>Content-Type,X-Requested-With,accept,Origin,Access-Control- Request-Method,Access-Control-Request-Headers</param-value>
	</init-param>
	<init-param>
		<param-name>cors.exposed.headers</param-name>
		<param-value>Access-Control-Allow-Origin,Access-Control-Allow-Credentials </param-value>
	</init-param>
	<init-param>
		<param-name>cors.support.credentials</param-name>
		<param-value>true</param-value>
	</init-param>
	<init-param>
		<param-name>cors.preflight.maxage</param-name>
		<param-value>10</param-value>
	</init-param>
</filter>
<filter-mapping>
	<filter-name>CorsFilter</filter-name>
	<url-pattern>/*</url-pattern>
</filter-mapping>