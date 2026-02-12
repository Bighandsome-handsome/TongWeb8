# 原创TongWeb获取应用列表失败

> 原文地址: https://blog.csdn.net/realwangpu/article/details/110137426

---

问题现象：
TongWeb刚启动，进入控制台看应用，显示：获取应用列表失败:部署服务尚未启动完成，请稍后再试！
原因及解决办法：
这是因为TongWeb还没有启动完成，没有完全加载应用列表，需要等TongWeb启动完成后才能显示。  日志中有如下信息，表示TongWeb启动完成。
TongWeb server startup complete in 43325 ms