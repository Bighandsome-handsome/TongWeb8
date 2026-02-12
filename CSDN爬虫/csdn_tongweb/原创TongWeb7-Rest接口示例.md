# 原创TongWeb7-Rest接口示例

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/134295162

---

1. 获取通道信息：
curl  --user thanos:thanos123.com http://192.168.178.131:9062/console/rest/api/listener_detail?operatorName=count:tong-http-listener,stat:tong-http-listener
2.获取应用资源缓存信息
curl --user thanos:@Karthus195819  “http://192.168.150.128:9060/console/rest/api/application_resource_cache?pathValue=TC_examples&vhost=server&attrName=size,maxSize,hitCount,lookupCount,ttl”