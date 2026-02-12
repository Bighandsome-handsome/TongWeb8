# 原创TongWeb8编码设置说明

> 原文地址: https://blog.csdn.net/realwangpu/article/details/129057522

---

应用场景：
在遇到中文问题时，常需要通过设置编码格式来解决问题。下面介绍TongWeb8的编码设置及优先级。
一、web.xml中请求、响应编码的配置优先级最高
在JavaEE8规范中web.xml增加了request, response编码配置，该配置优先级最高。
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://xmlns.jcp.org/xml/ns/javaee"
    xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
    id="WebApp_ID" version="4.0">
    <display-name>charset</display-name>
    <default-context-path>/testde</default-context-path>
    <request-character-encoding>GBK</request-character-encoding>
    <response-character-encoding>GBK</response-character-encoding>
以往项目中request, response编码通常通过filter来设置，如：
<filter-name>EncodingFilter</filter-name>
    <filter-class>
        org.springframework.web.filter.CharacterEncodingFilter
    </filter-class>
    <init-param>
        <param-name>encoding</param-name>
        <param-value>UTF-8</param-value>
    </init-param>
    <init-param>
        <param-name>forceEncoding</param-name>
        <param-value>true</param-value>
    </init-param>
二、TongWeb8控制台编码设置
在部署应用时通过配置"编码"来完成。
参数
参数说明
应用请求编码
应用程序的默认 HTTP 请求编码，优先级低于web.xml。
应用响应编码
应用程序的默认HTTP响应体编码，优先级低于web.xml。
JSP 文件编码
指定 JSP 文件编码, 相当于javaEncoding。
静态文件编码
使用指定的编码解析应用的文件资源，如 *.html 等静态资源，可用于解决文件编码和 JVM 默认编码不一致引起的乱码问题。相当于fileEncoding
三、URL编码设置
为兼容tomcat编码，http通道中"其它" 中的"URI 编码" 相当于tomcat的URIEncoding  ；“URI 使用 Content-Type 解码" 相当于tomcat的useBodyEncodingForURI。
若tomcat下不乱码，而在TongWeb下乱码，则可参考tomcat配置来配置TongWeb。
URIEncoding  : This specifies the character encoding used to decode the URI bytes, after %xx decoding the URL. The default value is UTF-8.
useBodyEncodingForURI :
This specifies if the encoding specified in contentType should be used for URI query parameters, instead of using the URIEncoding. This setting is present for compatibility with Tomcat 4.1.x, where the encoding specified in the contentType, or explicitly set using Request.setCharacterEncoding method was also used for the parameters from the URL. The default value is false.
Notes:
1) This setting is applied only to the query string of a request. Unlike URIEncoding it does not affect the path portion of a request URI. 2) If request character encoding is not known (is not provided by a browser and is not set by SetCharacterEncodingFilter or a similar filter using Request.setCharacterEncoding method), the default encoding is always "ISO-8859-1". The URIEncoding setting has no effect on this default.