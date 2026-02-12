# 原创TongWeb上应用部署方式

> 原文地址: https://blog.csdn.net/realwangpu/article/details/110230970

---

TongWeb上可部署的web应用结构可分为两种：
1. 打成war包形式的文件。2. 以文件夹目录方式的web应用。 这两种方式必须要有WEB-INF目录才是一个合法web应用结构，方可部署。
特殊情况：某些应用是在apache 、nginx上跑的静态文件，如:vue。只需在其目录下建一个WEB-INF目录，便可当应用部署在TongWeb上。
TongWeb上应用部署方式可分为单节点部署和集中管理部署两种：
单节点部署适用于不需要集群的单机环境，或在单机应用测试阶段使用。
集中管理部署适用于集群环境，把应用批量部署到各个TongWeb节点上。
单机部署有三种常用方式：
将应用包直接放入TongWeb的autodeploy目录下，自动解压在deployment目录下完成部署。
通过bin下commandstool命令行进行部署。
通过console控制台部署，
推荐以目录方式部署
。先将应用通过FTP上传到TongWeb所在机器以目录方式展开，再通过控制台指向该目录。优点是避免因应用包过大通过控制台上传解压占用TongWeb本身资源，且应用更新文件，只需要更新该目录即可。
注意：以war/ear包部署的应用会解压在deployment目录下，当卸载应用时会将deployment目录下应用删除，所以建议目录方式部署。
企业版通过集中管理
heimdall
控制台部署方式：
通过
heimdall
控制台
最佳部署方式
是先将应用目录上传到每台
TongWeb
机器相同目录下，然后再通过
heimdall
控制台选“
节点已有应用目录
”部署。
以Web应用为例，说明应用包注意事项：
Web应用包/目录下必须要有WEB-INF目录才是一个合法应用结构。
若打成war包，必须是zip格式。
常见的奇葩错误打包方式：(1). 用winrar工具打包成rar格式的包，注意用
jar xvf webapp.war
命令校验war包是否能正常解压。（2）多打了一层目录，war包下的某个目录中才有WEB-INF目录。
如果不能保证打包的正确性，就乖乖的用目录方式部署。
不合法的应用包报错：java.lang.IllegalArgumentException: The main resource set specified [/root/TongWeb7.0/deployment/daq]
is not valid
若部署应用想通过域名或IP直接访问，而不用输入端口和应用前缀，则配置http通道为80或https通道为443， 应用前缀为/即可。
若因应用问题导致TongWeb无法启动，进入不了控制台卸载应用，则可以直接将conf/tongweb.xml文件中的应用配置删除再启动TongWeb即可。
<web-app name="ROOT" original-location="/usr/hcit/ROOT" location="/usr/hcit/ROOT" context-root="/ROOT" vs-names="server" is-directory="true" enabled="true" deploy-order="100" object-type="user" jsp-compile="false" dtd-validate="false" is-autodeploy="false" version="" ......./>