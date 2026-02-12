# 原创Tongweb7049m4+THS6010-6012版本 传真实ip到后端（by yjm+lwq）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/143184916

---

遇到客户需要通过ths传真实ip到后端也就是部署到tongweb的需求，在ths的httpserver.conf里的location块配置了以下内容：
proxy_set_header Host
$host
;
proxy_set_header X-Real-IP
$remote_addr
;
proxy_set_header X-Forwarded-For
$proxy_add_x_forwarded_for
;
proxy_set_header X-Forwarded-Proto
$scheme
;
配置后，重启ths，发现后端没有获取到真实ip。
参考
负载场景下TongWeb如何获取真实的客户端IP地址
发现可以在应用层面修改代码，或者tongweb层面配置实现这一效果。
如果要从tongweb层面的着手的话，可以登录控制台进行配置，如下图所示：
com.tongweb.catalina.valves.RemoteIpValve,protocolHeader
=
X-Forwarded-Proto,remoteIpHeader
=
X-Forwarded-For,protocolHeaderHttpsValue
=
https
记得双击保存，然后测试一下应用。