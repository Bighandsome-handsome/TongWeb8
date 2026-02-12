# 原创tongweb迁移工具从tomcat迁移到tongweb下（by liuhui）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/139423498

---

说明：tongweb使用版本7049m3,tomcat版本8.5版本
1,先把a.jar下面的TongWebStarter.class覆盖到tongweb工作目录下tools/TW-toolkit/TW-toolkit.jar
2,把需要迁移的tomcat项目放到webapps目录下启动tomcat解压war包，如下图TC_examples项目
3，进入到tongweb目录下执行（ linux下classpath 是 冒号： 不是分号 ; 间隔jar 。windows下classpath 是 分号; 不是冒号 ： 间隔jar  其中com.tongweb.migration.TongWebStarter  8   /dft/apache-tomcat-8.5.100   /dft/TongWeb7.0.4.9_M3_Enterprise_Linux      三个参数依次为tomcat版本，路径，tongweb版本）如下图
java  -Dhome="/dft/TongWeb7.0.4.9_M3_Enterprise_Linux/tools/TW-toolkit"   -classpath "/dft/TongWeb7.0.4.9_M3_Enterprise_Linux/tools/TW-toolkit/TW-toolkit.jar:/dft/TongWeb7.0.4.9_M3_Enterprise_Linux/lib/bootstrap.jar;/dft/TongWeb7.0.4.9_M3_Enterprise_Linux/lib/tongweb.jar:/dft/TongWeb7.0.4.9_M3_Enterprise_Linux/lib/jdk-api.jar:/dft/TongWeb7.0.4.9_M3_Enterprise_Linux/lib/jdk-impl.jar:/dft/TongWeb7.0.4.9_M3_Enterprise_Linux/lib/activation-api.jar"  com.tongweb.migration.TongWebStarter  8   /dft/apache-tomcat-8.5.100   /dft/TongWeb7.0.4.9_M3_Enterprise_Linux
4，启动tongweb 报错如下
报错原因由于tongweb.xml下出现file
进入到tongweb.xml中修改为大写File,项目启动成功
进行访问控制台以及应用