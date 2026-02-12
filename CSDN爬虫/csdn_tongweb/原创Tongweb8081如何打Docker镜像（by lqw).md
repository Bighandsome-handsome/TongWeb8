# 原创Tongweb8081如何打Docker镜像（by lqw)

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/144719253

---

文章目录
Tongweb7跟Tongweb8081 的区别
安装准备
如何使用Tongweb8081打Docker镜像并运行
如何测试打好的docker镜像
Tongweb7跟Tongweb8081 的区别
安装准备
1.已有docker环境，并且已经拉取了操作系统镜像和jdk镜像，如下图所示：
上图拉取的是centos7和openjdk8的镜像。
如果遇到docker镜像无法拉取的情况，可以参考这个帖子：
解决docker: Error response from daemon: Get “https://registry-1.docker.io/v2/“:连接超时问题
如果是国产的操作系统（例如麒麟），请联系对应厂商获取相关镜像。
2.已经搭建了Tongweb8081控制台，并且能正常运行。
搭建参考：
Tongweb8080企业版安装（by lqw）
3.确认生成的版本。
Tongweb8081里的版本生成，如下图所示：
里面会有区分企业版和轻量版，以及在java使用上，会区分javax和jakarta。
所以在制造镜像之前，必须确认使用哪种。
如何使用Tongweb8081打Docker镜像并运行
确认了docker里已经拉取了操作系统和jdk镜像后，来到控制台，找到版本生成这个功能：
点击创建，选择好对应的版本，并把Docker镜像这个开关打开：
然后在基础镜像里，填写上jdk的基础镜像（例如我拉取的镜像是openjdk 8，那就是openjdk:8）,这里示范的是轻量版，请根据需求选择对应的版本。
一般只需要等待一段时间，列表就会出现对应的镜像包的名称：
也可以自己用docker images指令查看：
另外对应的镜像包也可以在这里找一找
如何测试打好的docker镜像
以下是我本地测试的指令,将容器里的8088和9060映射到宿主机：
docker
run
-d
--name
my_tongweb_console
-p
8089
:8088
-p
9061
:9060 tongweb-enterprise-javax-console:8.0.8.1
其中my_tongweb_console 是我起的名字，tongweb-enterprise-javax-console是我打好的镜像名称：
由于我创建镜像的时候勾选了控制台，所以在浏览器上访问https://服务器ip：9061/console进行测试：
如果不熟悉目录结构，或者后期有绑定目录结构的需求，可以通过dockers ps -a 找到对应的CONTAINER ID，然后使用这个指令，进去容器内部查看里面的结构：
docker
exec
-it
CONTAINER ID /bin/bash
也可以自行部署应用进行测试，例如Tongweb8081安装包里的version.zip里的example.war：
由于docker容器里本身没有这个war，我们需要借助文件上传的形式进行部署，需要先放开文件上传的限制：
放开后重启容器，上传这个war包进行部署：
部署后用服务器ip：映射端口/访问前缀进行访问：
备注：
1.打镜像的时候，Tongweb8081的授权会同步被打入到镜像里，所以请确保授权的使用时间还没过期，避免后期更换麻烦。