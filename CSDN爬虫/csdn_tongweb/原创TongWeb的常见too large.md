# 原创TongWeb的常见too large

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109710743

---

1. TongWeb5 日志  java.lang.IllegalStateException: PWC4662: Request header is too large。将如下request改为8192，如果还不行再增大。TongWeb6，7报 Request header is too large， 不好意思忘记做在控制台上了，需要手工修改conf/tongweb.xml文件，将对应的http通道的max-http-header-size
值加大，重启TongWeb生效。注意：若在控制台修改http通道后该配置恢复原值。
<http-options compression="on" compressable-mime-type="text/html,text/plain,text/xml" compression-min-size="2048" no-compression-user-agents="" disable-upload-timeout="true"
max-http-header-size="8192"
max-keep-alive-requests="100"/>
2. TongWeb5 、6、7 日志Post too large。将http通道如下值改大。