# 原创Tongweb7049m4集中管理session报java.lang.ClassNotFoundException: java.util.List$$EnhancerByCGLIBxxx（lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/145829339

---

现象描述
用户使用tongweb7049m4+集中管理工具+nginx，报错：
java.lang.IllegalStateException: get session: 023EE405E22DF01DCE7DEE39F78B3FE6-32 fail,
find
session: 023EE405E22DF01DCE7DEE39F78B3FE6 fail, redis session uninitialized
看到最后一个case by，是找不到class：
Caused by: java.lang.ClassNotFoundException:
$java
.util.List
$$
EnhancerByCGLIB
$$
c3d9653a
	at com.tongweb.tomee.catalina.ThanosTomEEWebappClassLoader
$1
.loadClass
(
ThanosTomEEWebappClassLoader.java:98
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
at com.tongweb.serializer.kryo.util.DefaultClassResolver.readName
(
DefaultClassResolver.java:136
)
..
.
49
more
原因分析
在反序列化过程中，应用程序试图加载一个增强的代理类（即
java.util.Listjava.util.List
ja
v
a
.
u
t
i
l
.
L
i
s
t
EnhancerByCGLIBEnhancerByCGLIB
E
nhan
cer
B
y
CG
L
I
B
$c3d9653a），但该类未被加载到当前的 ClassLoader 中。
原因：增强类（通常是由 CGLIB 创建的代理类）在序列化环境中创建，但在反序列化环境中不可用，可能因为它是动态生成且未持久化的。
解决方案
1.配置启动参数：-Dwebcluster.session.sticky=false。
2.修改应用代码，如下为示范：