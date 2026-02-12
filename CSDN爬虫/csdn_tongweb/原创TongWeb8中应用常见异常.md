# 原创TongWeb8中应用常见异常

> 原文地址: https://blog.csdn.net/realwangpu/article/details/129199953

---

问题一：cookie异常字符报错如下
2022-06-14 11:07:31 [WARN] - java.lang.IllegalArgumentException:
An invalid domain [.test.com] was specified for this cookie
2022-06-14 11:07:31 [WARN] -    at com.tongweb.web.util.http.Rfc6265CookieProcessor.validateDomain(Rfc6265CookieProcessor.java:202)
2022-06-14 11:07:31 [WARN] -    at com.tongweb.web.util.http.Rfc6265CookieProcessor.generateHeader(Rfc6265CookieProcessor.java:137)
2022-06-14 11:07:31 [WARN] -    at com.tongweb.server.connector.Response.generateCookieString(Response.java:960)
解决办法：
应用配置中开启 "使用老版 Cookie 处理器"
问题二：url中有非法字符报错如下
2022-06-14 10:16:24 [INFO] - Error parsing HTTP request header
Note: further occurrences of HTTP request parsing errors will be logged at DEBUG level. java.lang.IllegalArgumentException:
Invalid character found in the request target
[/dbpool/?aa=|ddd]].
The valid characters are defined in RFC 7230 and RFC 3986
at com.tongweb.coyote.http11.Http11InputBuffer.parseRequestLine(Http11InputBuffer.java:470)
at com.tongweb.coyote.http11.Http11Processor.service(Http11Processor.java:212)
解决办法：
http
通道中 “路径中允许使用的未编码字符” “参数中允许使用的未编码字符” 配
" < > [ \ ] ^ ` { | }
问题三：JSP编译报错如下
2022-06-14 11:24:55 [WARN] - com.tongweb.jasper.JasperException: /index2.jsp (line: [11], column: [45]) Attribute value [String.valueOf("aa")] is
quoted with ["] which must be escaped when used within the value
2022-06-14 11:24:55 [WARN] -    at com.tongweb.jasper.compiler.DefaultErrorHandler.jspError(DefaultErrorHandler.java:26)
2022-06-14 11:24:55 [WARN] -    at com.tongweb.jasper.compiler.ErrorDispatcher.dispatch(ErrorDispatcher.java:276)
解决办法：
应用部署的“Strict Quote Escaping ” 关闭即可。
问题四：应用部署缓存不足警告
2022-06-14 12:16:39 [WARN] - Unable to add the resource at [/WEB-INF/classes/org/oasis_open/docs/wsrf/rp_2/jaxb.properties] to the cache for web application [cxf]
because there was insufficient free space available after evicting expired cache entries - consider increasing the maximum size of the cache
2022-06-14 12:16:39 [WARN] - Unable to add the resource at [/WEB-INF/classes/org/oasis_open/docs/wsrf/rp_2/jaxb.properties] to the cache for web application [cxf] because there was insufficient free space available after evicting expired cache entries - consider increasing the maximum size of the cache
解决办法：
应用部署增大 “
最大缓存大小”， 通常大于应用所有jar的大小，通过应用监控缓存使用情况。
够不够用，看资源缓存量。
典型的毛病：99999999, 拼命调大
。
问题五：
WebService处理异常
Caused by: org.xml.sax.SAXParseException: 文件提前结束。
at com.sun.org.apache.xerces.internal.parsers.DOMParser.parse(DOMParser.java:262)
at com.sun.org.apache.xerces.internal.jaxp.DocumentBuilderImpl.parse(DocumentBuilderImpl.java:339)
at
com.tongweb.ws.commons.schema
.XmlSchemaCollection$2.run(XmlSchemaCollection.java:651)
at com.tongweb.ws.commons.schema.XmlSchemaCollection$2.run(XmlSchemaCollection.java:649)
at java.security.AccessController.doPrivileged(Native Method)
at com.tongweb.ws.commons.schema.XmlSchemaCollection.parseDoPriv(XmlSchemaCollection.java:649)
at com.tongweb.ws.commons.schema.XmlSchemaCollection.read(XmlSchemaCollection.java:618)
... 64 more
解决办法：
从异常看TongWeb的WebService参与了应用的xml处理，在部署应用时勾选加载应用的“webservice” 或"web兼容"即可。
问题六：与应用类冲突
Caused by: java.lang.AbstractMethodError: javax.ws.rs.core.UriBuilder.uri(Ljava/lang/String;)Ljavax/ws/rs/core/UriBuilder;
at javax.ws.rs.core.UriBuilder.fromUri(UriBuilder.java:96)
at com.sun.jersey.spi.container.servlet.ServletContainer.service(ServletContainer.java:669)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:590)
解决办法：
在开启”web兼容模式“的情况下依旧加载tongweb-jee-api.jar中的类，可以设置”强制从应用加载的类“来解决。
问题七：通过request.getServletContext().getContext("/app")获取另一应用上下文为空
解决办法：
开启"跨应用支持"
问题八：JSP编译报错如下：
JasperException: /index.jsp (line: [1], column: [84]) The JSP specification requires that an attribute name is preceded by whitespace
解决办法：
增加-D参数：-Dcom.tongweb.jasper.compiler.Parser.STRICT_WHITESPACE=false
TongWeb8.0.8.0上增加了界面配置