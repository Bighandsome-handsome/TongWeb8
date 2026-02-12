# 原创TongWeb7-漏洞相关

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/134465331

---

1.  东方通应用服务器请求走私漏洞(Tomcat CVE-2021-33037)
该漏洞在 HTTP1.0 协议下，TongWeb 未对
Transfer-Encoding: chunked 头进行解析，而是以 Content-Length 作
为请求体内容划分。
已确认受影响版本：
TongWeb7.x <=TongWeb 7.0.4.9_M1
TongWeb7.0.C.3 至 7.0.C.5 版本
TongWeb6.1.7.x <=TongWeb6.1.8.6
未受影响版本：TongWeb6.1.5.x 系列、TongWeb8.0 系列、
TongWeb7.0.E 系列
根据该描述应为之前已解决的远程代码执行问题，该
问题已在最新版本 TongWeb7.0.4.9_M2、
TongWeb7.0.C.6 解决，或打
TongWeb7049M1_ITAIT5745 补丁。
链接：https://pan.baidu.com/s/1CnJxebOXaC1STrQwIyPmCw
提取码：7t8v