# 原创TongWeb The temporary upload location [tmp tongweb.xxx] is not valid-yjm

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/135170817

---

应用使用Multipart（form-data）的方式上传文件时会在/tmp下生成临时文件，但是临时文件会被系统定时删除，因此访问应用时会报如下错误：
/tmp目录的清理规则主要取决于/usr/lib/tmpfiles.d/tmp.conf文件的设定，默认的配置如下：
解决方法：
1、修改tmp.conf配置文件，排除清除tongweb开头的配置文件。
x /tmp/tongweb.*
2、如果使用的是TongWeb嵌入版，可以修改如下参数：
#配置TongWeb运行日志和临时文件的目录。 若不配置，则默认使用系统的临时目录
server.tongweb.basedir=
3、在SpringBoot的配置之中设定Profile信息
#指定上传文件临时目录
spring.http.multipart.location=/opt/data/upload
4、应用在代码中指定自有上传文件目录