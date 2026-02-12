# 原创TongWeb支持spring websocket问题

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109636708

---

问题描述：
应用部署在TongWeb上spring的websocket插件报错 "No suitable default RequestUpgradeStrategy found" 。
原因：
spring websocket组件有针对不同应用服务器的判断，但恰恰没有TongWeb项。
解决办法：
TongWeb7.0.3.0及之后版本增加了org.apache.tomcat.websocket.server.WsHttpUpgradeHandler相关类，这样spring websocket当TongWeb判断为tomcat处理，保证兼容性。
若您使用TongWeb6.1版本， 请升级到TongWeb7.0.3.0之后版本。