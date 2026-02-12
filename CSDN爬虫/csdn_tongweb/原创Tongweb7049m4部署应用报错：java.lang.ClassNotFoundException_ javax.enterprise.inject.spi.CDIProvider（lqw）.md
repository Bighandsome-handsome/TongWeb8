# 原创Tongweb7049m4部署应用报错：java.lang.ClassNotFoundException: javax.enterprise.inject.spi.CDIProvider（lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/145679256

---

问题描述
用户同一台服务器环境，使用jdk1.8，部署应用在tomcat8.5能正常运行，部署在tongweb7049m4，将启动参数webonly调整为true后，报以下错误：
Caused by: java.lang.NoClassDefFoundError: javax/enterprise/inject/spi/CDIProvider
	at java.lang.ClassLoader.defineClass1
(
Native Method
)
at java.lang.ClassLoader.defineClass
(
ClassLoader.java:756
)
at java.security.SecureClassLoader.defineClass
(
SecureClassLoader.java:142
)
at java.net.URLClassLoader.defineClass
(
URLClassLoader.java:473
)
at java.net.URLClassLoader.access
$100
(
URLClassLoader.java:74
)
at java.net.URLClassLoader
$1
.run
(
URLClassLoader.java:369
)
at java.net.URLClassLoader
$1
.run
(
URLClassLoader.java:363
)
at java.security.AccessController.doPrivileged
(
Native Method
)
at java.net.URLClassLoader.findClass
(
URLClassLoader.java:362
)
at java.lang.ClassLoader.loadClass
(
ClassLoader.java:418
)
at com.tongweb.server.TWServerURLClassLoader.loadClass0
(
TWServerURLClassLoader.java:46
)
at com.tongweb.server.TWServerURLClassLoader.access
$000
(
TWServerURLClassLoader.java:11
)
at com.tongweb.server.TWServerURLClassLoader
$1
.loadClass
(
TWServerURLClassLoader.java:40
)
at com.tongweb.common.LoadClassCache.cacheLoadClass
(
LoadClassCache.java:63
)
at com.tongweb.server.TWServerURLClassLoader.loadClass
(
TWServerURLClassLoader.java:37
)
at java.lang.ClassLoader.loadClass
(
ClassLoader.java:405
)
at com.tongweb.server.TWServerURLClassLoader.loadClass0
(
TWServerURLClassLoader.java:46
)
at com.tongweb.server.TWServerURLClassLoader.access
$000
(
TWServerURLClassLoader.java:11
)
at com.tongweb.server.TWServerURLClassLoader
$1
.loadClass
(
TWServerURLClassLoader.java:40
)
at com.tongweb.common.LoadClassCache.cacheLoadClass
(
LoadClassCache.java:63
)
at com.tongweb.server.TWServerURLClassLoader.loadClass
(
TWServerURLClassLoader.java:37
)
at java.lang.ClassLoader.loadClass
(
ClassLoader.java:351
)
at com.tongweb.tongejb.core.ConnectorClassLoader.loadClass
(
ConnectorClassLoader.java:146
)
at java.lang.ClassLoader.loadClass
(
ClassLoader.java:351
)
at java.lang.Class.forName0
(
Native Method
)
at java.lang.Class.forName
(
Class.java:348
)
at com.tongweb.catalina.loader.WebappClassLoaderBase.loadClass
(
WebappClassLoaderBase.java:1293
)
at com.tongweb.tomee.catalina.ThanosTomEEWebappClassLoader.access
$201
(
ThanosTomEEWebappClassLoader.java:23
)
at com.tongweb.tomee.catalina.ThanosTomEEWebappClassLoader
$1
.loadClass
(
ThanosTomEEWebappClassLoader.java:95
)
at com.tongweb.common.LoadClassCache.cacheLoadClass
(
LoadClassCache.java:63
)
at com.tongweb.tomee.catalina.ThanosTomEEWebappClassLoader.loadClass
(
ThanosTomEEWebappClassLoader.java:80
)
at com.tongweb.catalina.loader.WebappClassLoaderBase.loadClass
(
WebappClassLoaderBase.java:1176
)
at java.lang.Class.forName0
(
Native Method
)
at java.lang.Class.forName
(
Class.java:348
)
at java.util.ServiceLoader
$LazyIterator
.nextService
(
ServiceLoader.java:370
)
at java.util.ServiceLoader
$LazyIterator
.next
(
ServiceLoader.java:404
)
at java.util.ServiceLoader
$1
.next
(
ServiceLoader.java:480
)
at java.lang.Iterable.forEach
(
Iterable.java:74
)
at javax.enterprise.inject.spi.CDI.findAllProviders
(
CDI.java:125
)
at javax.enterprise.inject.spi.CDI.getCDIProvider
(
CDI.java:82
)
at javax.enterprise.inject.spi.CDI.current
(
CDI.java:64
)
at org.eclipse.yasson.internal.components.JsonbComponentInstanceCreatorFactory.getComponentInstanceCreator
(
JsonbComponentInstanceCreatorFactory.java:48
)
..
.
55
more
Caused by: java.lang.ClassNotFoundException: javax.enterprise.inject.spi.CDIProvider
	at java.net.URLClassLoader.findClass
(
URLClassLoader.java:387
)
at java.lang.ClassLoader.loadClass
(
ClassLoader.java:418
)
at com.tongweb.server.TWServerURLClassLoader.loadClass0
(
TWServerURLClassLoader.java:46
)
at com.tongweb.server.TWServerURLClassLoader.access
$000
(
TWServerURLClassLoader.java:11
)
at com.tongweb.server.TWServerURLClassLoader
$1
.loadClass
(
TWServerURLClassLoader.java:40
)
at com.tongweb.common.LoadClassCache.cacheLoadClass
(
LoadClassCache.java:63
)
at com.tongweb.server.TWServerURLClassLoader.loadClass
(
TWServerURLClassLoader.java:37
)
at java.lang.ClassLoader.loadClass
(
ClassLoader.java:351
)
..
.
97
more
#问题分析和解决思路
看到最后的报错信息是ClassNotFoundException，得确认一下，是找不到class文件，还是已有的class文件跟tongweb自身带的起冲突了（毕竟前面也报了个NoClassDefFoundError）。
参考：
TongWeb78处理应用自身JAR包冲突思路
根据报错信息我们分别尝试在tomcat和tongweb的安装目录执行了以下指令，确认是否缺少了对应的class
grep-Rn
"javax.enterprise.inject.spi.CDIProvider"
/usr/local/tong
grep-Rn
"javax.enterprise.inject.spi.CDIProvider"
/usr/local/tomcat
可以看到是有的，其中tongweb的在lib下的cdi-api.jar，tomcat的在应用的lib目录下的cdi-api-2.0.jar。
这就说明其实并不是class文件没找到，有可能是tongweb和应用的jar包在这一块的代码不一致，导致的冲突和报错。
然后用jar包查看工具查看了一下这两个jar包，发现在CDIProvider上，代码逻辑有点不一样（应用的是extends Prioritized，tongweb的没有）：
所以让客户尝试备份好后，把应用的lib下的cdi-api-2.0.jar后删掉再重启，问题解决。