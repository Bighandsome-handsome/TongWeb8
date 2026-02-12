# 原创TongWeb7-java.lang.NoSucMethodError: Ljava/lang/reflect/Constructor

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/133807897

---

应用适配tongweb7报如下错误
java.lang.NoSucMethodError: org.springframework.util.Reflectionutils.accessibleconstructor(Ljava/lang/Class; [Ljava/lang/class;)Ljava/lang/reflect/Constructor报错类为spring相关的包冲突导致，应用导报时排除一下依赖即可