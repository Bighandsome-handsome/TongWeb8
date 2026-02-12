# 原创TongWeb下 javax.management.InstanceAlreadyExistsException异常

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109542378

---

当在TongWeb上部署多个应用时会报 javax.management.InstanceAlreadyExistsException异常，多见于两个以上SpringBoot应用。
```bash
Caused by:javax.management.InstanceAlreadyExistsException: com.alibaba.druid.filter.stat:name=statFilter,type=StatFilter
Caused by:javax.management.InstanceAlreadyExistsException: org.springframework.cloud.context.environment:name=environmentManager,type=EnvironmentManager
```

原因：
SpringBoot项目默认开启了自身的JMX服务用于监控管理。此时如果两个SpringBoot部署在同一个TongWeb上时会报MBean实例已经存在的错误。
解决办法：
1. 修改注册的MBean名称。
2. SpringBoot应用可以修改domain名或关闭JMX。
spring.jmx.default-domain指定JMX domain name。
spring.jmx.enabled是否开启jmx，默认为true。