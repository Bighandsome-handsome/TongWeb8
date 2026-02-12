# 原创TongWeb上jCacheCacheManager异常

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109530774

---

TongWeb报 jcache 相关的错，是因为TongWeb企业版的lib下的hazelcast-3.10.5.jar或tongdatagrid-1.2.jar中含有\META-INF\services\ javax.cache.spi.CachingProvider这个文件。
解决办法：
方式一：将hazelcast-3.10.5.jar或tongdatagrid-1.2.jar中META-INF\services\ javax.cache.spi.CachingProvider这个文件删除。
方式二：直接删除hazelcast-3.10.5.jar或tongdatagrid-1.2.jar ，但不能用session复制了。
方式三：改用TongWeb标准版，不带hazelcast-3.10.5.jar或tongdatagrid-1.2.jar。
日志通常如下：
```bash
Caused by: org.springframework.beans.BeanInstantiationException: Failed to instantiate [javax.cache.CacheManager]: Factory method 'jCacheCacheManager' threw exception; nested exception is javax.cache.CacheException: Error opening URI [hazelcast]
Caused by: javax.cache.CacheException: Error opening URI [hazelcast]
Caused by: java.lang.IllegalStateException: Unable to connect to any address! The following addresses were tried: [[127.0.0.1]:5703, [127.0.0.1]:5702, [127.0.0.1]:5701]