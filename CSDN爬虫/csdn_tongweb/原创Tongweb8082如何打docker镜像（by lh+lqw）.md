# 原创Tongweb8082如何打docker镜像（by lh+lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/145035070

---

说明
8082新增了以下机制：
目前直接使用8081版本的方式在8082控制台生成镜像并运行，会有如下报错(也就是说8081版本的方法暂时不适用于8082，得等后续通知)：
安装准备
1.本地已有对应的Tongweb8082的安装包，并且已经根据自身需求在控制台上生成对应的Tongweb8082的版本并且运行没有问题。
Tongweb8082的控制台版本生成，可根据自身需求生成例如轻量版，企业版以及javax和jakarta命令空间的版本，需要先确认对应的版本，在本地安装运行没问题后再打成镜像。
2.docker已拉取对应的操作系统和jdk镜像：
如果遇到docker镜像无法拉取的情况，可以参考这个帖子：
解决docker: Error response from daemon: Get “https://registry-1.docker.io/v2/“:连接超时问题
如果是国产的操作系统（例如麒麟），请联系对应厂商获取相关镜像。
安装
以本地安装tongweb8目录为/opt/TongWeb为例：
编写Dockerfile，并将Dockerfile放在opt：
# 操作系统镜像
FROM centos:7
# jdk镜像
FROM openjdk:8
COPY ./TongWeb /opt/TongWeb
WORKDIR /opt/TongWeb
EXPOSE
9060
8088
VOLUME
[
"/opt/TongWeb/domains/domain1"
]
CMD
[
"java"
,
"-server"
,
"-Xms2048M"
,
"-Xmx2048M"
,
"-Dtongweb.home=/opt/TongWeb"
,
"-Dtongweb.base=/opt/TongWeb/domains/domain1"
,
"-Djava.io.tmpdir=/opt/TongWeb/domains/domain1/temp"
,
"-Djava.util.logging.manager=com.tongweb.logger.JulLogManager"
,
"-javaagent:/opt/TongWeb/version8.0.8.2/boot/tongweb-bootstrap.jar"
,
"-classpath"
,
"/opt/TongWeb/version8.0.8.2/boot/tongweb-bootstrap.jar"
,
"com.tongweb.main.TongWebMain"
,
"start"
]
Dockerfile的权限如下所示：
cd 到opt，执行以下指令：
docker
build
-t
my-tongweb-app
.
并用docker images查看：
然后可以执行以下指令启动容器：
docker
run
-d
--name
my_tongweb
-p
8089
:8088
-p
9061
:9060
-v
/opt/TongWeb/domains/domain1:/opt/TongWeb/domains/domain1 my-tongweb-app
之后可以用docker ps -a 查看是否运行：
用docker ps -a查看到的CONTAINER ID查看日志：
部分版本的镜像还可以访问控制台：
如果需要访问容器内部，可以执行：
docker
exec
-it
CONTAINER ID /bin/bash