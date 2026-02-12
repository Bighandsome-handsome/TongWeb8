# 原创TongWeb关于AJP问题的解决方案

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109636309

---

关于
Apache Tomcat
文件包含问题（
CNVD-2020-10487
，
CVE-2020-1938
）
，TongWeb6、TongWeb7.0中间件也有集成AJP功能，因此如果系统所在服务器的TongWeb中间件配置并启用了AJP功能，则系统所在服务器有可能被此影响。
解决办法：
方法一 、系统没有配置AJP端口集群的情况，直接删除conf/tongweb.xml中的AJP端口配置即可，如下：
<ajp-listener name="tong-ajp-listener" address="0.0.0.0" default-virtual-host="server" port="8009" status="started" redirect-port="443" block-enabled="true" uri-encoding="GBK" use-body-encoding-for-uri="false" max-parameter-count="10000" max-post-size="2097152" parse-body-methods="POST" create-time="2020-01-15 14:47:54"></ajp-listener>
方法二、系统有配置AJP端口集群的情况，需要升级到有“ajp secret”配置的TongWeb版本。
同时Apache的worker.properties文件要设置对应的密码项, 如：
worker.worker1.secret=密码，  对应TongWeb AJP通道的ajp secret。