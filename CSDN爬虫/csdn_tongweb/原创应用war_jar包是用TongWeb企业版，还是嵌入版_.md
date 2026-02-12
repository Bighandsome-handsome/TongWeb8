# 原创应用war/jar包是用TongWeb企业版，还是嵌入版?

> 原文地址: https://blog.csdn.net/realwangpu/article/details/149772005

---

在判断应用应该采用TongWeb哪个版本时，存在一种错误的观点：如果应用包是jar包，则需要采用TongWeb嵌入版；如果应用包是war包，则需要采用TongWeb企业版。
正确的判断方法：
1.  首先应用为jar包，且符合以下目录结构，则采用TongWeb嵌入版，通过java  -jar webapp.jar方式运行。
2.
若应用包为war包，则不能简单判断为需要运行在TongWeb企业版上。
咨询下用户之前的使用方式，检查下war包结构如下图也可以采用java -jar webapp.war嵌入版方式运行。  如果war包中没有TongWeb、tomcat、jetty、undertow  jar，则是以web应用部署的方式运行。
所以在做替换时要判断以下几点：
1. 若应用是jar包，之前一定运行在嵌入版上。
2. 若应用是war包，要了解用户之前使用方式或检查war包结构，war包有可能运行在嵌入版上，也有可能运行在企业版上。不能以简单的应用包后缀名判断。
3. 再了解用户的运维管理方式适合用嵌入版，还是企业版。 Spring Boot应用的jar与war之间可以互相转化的，转化为war应用在TongWeb企业版上部署时，一定要清除应用里tomcat、jetty、undertow  jar。