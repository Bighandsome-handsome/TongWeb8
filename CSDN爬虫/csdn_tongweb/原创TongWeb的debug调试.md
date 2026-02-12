# 原创TongWeb的debug调试

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109504286

---

TongWeb的eclipse、IDEA开发插件在某些版本上不一定好用，这时我们可以采用JDK本身的远程debug模式来进行调试。方法如下：
1. 通过
./startserver.sh debug 49812
， 启动TongWeb，其中48912为远程debug的端口号。
其本质就是在启动参数中加入了：
-Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=端口
2. TongWeb启动完成后就可以在eclipse配置进行远程调试，如下图，具体请参考JDK，eclipse相关文档。