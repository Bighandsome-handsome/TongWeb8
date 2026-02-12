# 原创TongWeb相关http安全头设置方式

> 原文地址: https://blog.csdn.net/realwangpu/article/details/121973952

---

一、X-Frame-Options响应头配置
X-Frame-Options HTTP 响应头是用来给浏览器指示允许一个页面可否在 <frame>, </iframe> 或者 <object> 中展现的标记。网站可以使用此功能，来确保自己网站的内容没有被嵌套到别人的网站中去，也从而避免了点击劫持 (clickjacking) 的攻击。在TongWeb bin目录下external.vmoptions中设置该参数：
-Dtongweb.X_Frame_Options=SAMEORIGIN
有四个值：
DENY：浏览器拒绝当前页面加载任何 Frame 页面。
SAMEORIGIN：页面只能加载入同源域名下的页面(默认值)。
ALLOW-FROM：只能被嵌入到指定域名的框架中。(部分浏览器不支持)
NONE：关闭该功能
显示结查如下：
HTTP/1.1 200
X-Frame-Options: SAMEORIGIN
Content-Type: text/html;charset=GBK
Content-Length: 160
Date: Thu, 16 Dec 2021 06:19:09 GMT
Server: webserver
二、CORS跨域配置
在应用的web.xml (只对本应用生效) 或TongWeb的conf/default-web.xml(对所有应用生效) 中加入如下filter。
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
			<param-value>GET,POST</param-value>
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
当应用访问请求头中含有Origin时
Origin: http://api.test.com
http响应头则含有cors头相关配置
```bash
HTTP/1.1 200
Access-Control-Allow-Origin: http://api.test.com
Access-Control-Allow-Credentials: true
Access-Control-Expose-Headers: Access-Control-Allow-Origin,Access-Control-Allow-Credentials
X-Frame-Options: SAMEORIGIN
Content-Type: text/html;charset=UTF-8
```
注意：TongWeb的CORS跨域配置默认是不开启的，若是在不配置的情况下，还有防跨域配置则多数是由应用spring开启了
CORS跨域配置.
三、预防http host头攻击漏洞
预防非法篡改http host头的值
Host: 192.168.0.33:8080
可以在TongWeb7的web容器配置中设置host头的白名单，非白名单的Host值将被拦截。