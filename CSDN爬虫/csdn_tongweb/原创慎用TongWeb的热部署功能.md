# 原创慎用TongWeb的热部署功能

> 原文地址: https://blog.csdn.net/realwangpu/article/details/115264043

---

TongWeb的热部署功能可以在应用的web.xml、class、jar发生变化时自动重部署应用，该功能在应用测试阶段可以用，但在生产环境中一定要关闭"热部署功能"。 否则应用web.xml、class、jar一更新，就会触发自动重部署，造成正在访问的用户中断。甚至可能引发此问题：
TongWeb上反复重部署应用后异常：application instance has been stopped already 或OutOfMemoryError：Metaspace_realwangpu的博客-CSDN博客
从server.log可以看到，应用在重复加载：
```bash
[2021-03-27 13:32:59 325] [INFO] [ContainerBackgroundProcessor] [web-container] [Reloading context [TC_examples]]
[2021-03-27 13:32:59 328] [INFO] [ContainerBackgroundProcessor] [core] [Reloading Context with name [TC_examples] has started]
[2021-03-27 13:32:59 383] [INFO] [ContainerBackgroundProcessor] [core] [SessionListener: contextDestroyed()]
[2021-03-27 13:32:59 384] [INFO] [ContainerBackgroundProcessor] [core] [ContextListener: contextDestroyed()]