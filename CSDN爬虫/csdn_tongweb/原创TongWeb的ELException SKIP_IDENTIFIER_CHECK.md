# 原创TongWeb的ELException SKIP_IDENTIFIER_CHECK

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109683155

---

TongWeb出现以下异常：
[[2018-06-15 14:55:45] [SEVERE] [web-container] [Servlet.service() for servlet jsp threw exception]  javax.el.ELException: The identifier [class] is not a valid Java identifier as required by section 1.19 of the EL specification (Identifier ::= Java language identifier). This check can be disabled by setting the system property com.tongweb.el.parser.SKIP_IDENTIFIER_CHECK to true.
TongWeb6设置参数 -Dcom.tongweb.
web
.el.parser.SKIP_IDENTIFIER_CHECK=true
TongWeb7设置参数-Dcom.tongweb.el.parser.SKIP_IDENTIFIER_CHECK=true
有个web差别