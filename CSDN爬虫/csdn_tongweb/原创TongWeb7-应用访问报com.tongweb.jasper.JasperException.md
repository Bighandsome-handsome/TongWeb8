# 原创TongWeb7-应用访问报com.tongweb.jasper.JasperException

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/134502207

---

问题报错如下：
com.tongweb.jasper.JasperException: /WEB-INF/tags/doLogin.tag (line: 136, column: 15) Attribute value  (domain != null && domain.length() > 0)  is quoted with > which must be escaped when used within the value
解决办法：
TongWeb目录/bin/external.vmoptions中追加以下参数：
-Dcom.tongweb.web.jasper.compiler.Parser.STRICT_QUOTE_ESCAPING=false
-Dcom.tongweb.web.jasper.compiler.Parser.STRICT_WHITSPACE=false
tongweb目录/conf/default-web.xml中com. tongweb.web.jasper.servlet.ThanosJspServlet位置下面追加如下配置：