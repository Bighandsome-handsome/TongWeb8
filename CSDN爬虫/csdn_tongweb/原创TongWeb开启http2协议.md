# 原创TongWeb开启http2协议

> 原文地址: https://blog.csdn.net/realwangpu/article/details/122537982

---

TongWeb开启http2协议的条件：
1. http通道类型改为https。
2. IO默认改为apr。
3.
开启 openssl 选项。
通过方问https://IP:8088/index.jsp 可以从响应头看到开启了http2协议
HTTP/2 200 OK
set-cookie: JSESSIONID=405EEA78A3545EB54AB55FE2612B7AEF;path=/;Secure;HttpOnly
content-type: text/html;charset=GBK
date: Mon, 17 Jan 2022 05:25:39 GMT
在前端有负载均衡THS5.0(TongHttpServer)的情况下，通过THS配置。
#开启SSL后，标红为开启http2
ProtocolsHonorOrder On
Protocols h2 h2c http/1.1
SSLProtocol TLSv1.2
SSLCertificateFile "crt/common_cert/server.crt"
SSLCertificateKeyFile "crt/common_cert/server.key"
SSLEngine on
SSLProxyEngine on
SSLProxyVerify none
SSLProxyCheckPeerCN off
SSLProxyCheckPeerName off