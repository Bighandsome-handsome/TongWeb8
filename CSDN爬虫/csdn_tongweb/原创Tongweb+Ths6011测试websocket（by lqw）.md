# 原创Tongweb+Ths6011测试websocket（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/140209512

---

本次使用的tongweb版本7049m4，测试包ws_example.war（在tongweb安装目录的samples/websocket下），ths版本6011
首先在tongweb控制台部署一下ws_example.war,部署后测试是否能访问：
然後ths上的httpserver.conf的參考配置如下(由于tongweb和ths都在同一个服务器上，所以用127.0.0.1)：
http
{
server
{
listen
8080
;
server_name localhost
;
access_log logs/access.log main
;
location /
{
proxy_pass http://127.0.0.1:8088
;
}
location ~*.*echoAnnotation$
{
proxy_set_header Upgrade
$http_upgrade
;
proxy_set_header Connection
"upgrade"
;
proxy_pass http://127.0.0.1:8088
;
}
}
}
点击这里
点击第一个
在输入框输入以下内容，ip替换为自己的，如果跟上图所示一致，就说明测试成功
ws://192.168.10.93:8080/ws_example/websocket/echoAnnotation