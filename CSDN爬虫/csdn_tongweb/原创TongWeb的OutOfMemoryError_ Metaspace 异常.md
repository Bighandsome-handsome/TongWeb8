# 原创TongWeb的OutOfMemoryError: Metaspace 异常

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109711497

---

问题描述:
TongWeb报错OutOfMemoryError: Metaspace， 但是用JDK8没有设置-XX:MaxMetaspaceSize值，怎么还会内存溢出？
问题原因：
-XX:MaxMetaspaceSize这个参数用于限制Metaspace增长的上限，防止因为某些情况导致Metaspace无限的使用本地内存，影响到其他程序，默认无上限。但是TongWeb判断若使用JDK8，则启动时自动增加参数-XX:MaxMetaspaceSize=
192m（限制在了192m）
。所以可能存在查看控制台、external.vmoptions文件配置时无-XX:MaxMetaspaceSize， 但ps -ef|grep java查看进程时能看到-XX:MaxMetaspaceSize参数。
解决办法：
在TongWeb配置中显示写明-XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=512m值即可，该值通常比应用WEB-INF下lib和classes目录大2-3倍即可。若增大Metaspace还会出现该问题，则可能是
TongWeb上反复重部署应用后异常：application instance has been stopped already 或OutOfMemoryError：Metaspace_realwangpu的博客-CSDN博客
问题。