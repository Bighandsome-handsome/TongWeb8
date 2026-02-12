# 原创TongWeb7的-DuseLegacyCookieProcessor=true

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109568910

---

问题描述
：应用报异常如下：
java.lang.IllegalArgumentException: An invalid path [/;httponly] was specified for this cookie 。
at com.tongweb.web.util.http.
Rfc6265CookieProcessor
.validatePath(Rfc6265CookieProcessor.java:207)
at com.tongweb.web.util.http.Rfc6265CookieProcessor.generateHeader(Rfc6265CookieProcessor.java:132)
原因：
对cookie 新版本标准而言，不能直接使用逗号这种特殊符号作为cookie的内容， 例如：空格，方括号，圆括号，等于号（=），逗号，双引号，斜杠，问号，@符号，冒号，分号都不能作为Cookie的内容。
解决办法：
TongWeb7带了两个实现类，com.tongweb.web.util.http.Rfc6265CookieProcessor、   com.tongweb.web.util.http.LegacyCookieProcessor。
前者是基于 RFC6265 ，而后者基于 RFC6265 、 RFC2109 、 RFC2616 。
TongWeb7启动脚本中设置
-DuseLegacyCookieProcessor=true
则支持老的方式,解决该问题。