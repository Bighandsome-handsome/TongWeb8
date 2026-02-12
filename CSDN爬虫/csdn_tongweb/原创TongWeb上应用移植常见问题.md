# 原创TongWeb上应用移植常见问题

> 原文地址: https://blog.csdn.net/realwangpu/article/details/99542654

---

本文章适用TongWeb6， TongWeb7版本
一、JPA引起的问题
TongWeb自带JPA实现，但实际应用中多采用hibernate的JPA，这样就导致TongWeb的JPA与应用自带JPA冲突，处理方法：
1.应用使用JPA，则TongWeb增加参数：-DenableJPA=false，不启动TongWeb的JPA，否则会报一些OpenJPA异常。
2.出现如下类似异常，缺少javax.persistence中的类或方法，说明应用带的JPA版本比TongWeb新。则把应用的javax.persistence.*包放在TongWeb的lib下，同时将TongWeb6或TongWeb7的lib下javaee-api-*.jar中 javax\persistence目录删除。
Caused by: java.lang.ClassNotFoundException: javax.persistence.Converter
java.lang.NoSuchMethodError: javax.persistence.JoinColumn.foreignKey
二、validation引起的问题
因为tomcat不带javax.validation，而TongWeb带javax.validation,但不带具体实现，所以tomcat上应用移植到TongWeb上后，常会遇到validation相关问题。
1. 出现如下类似异常，说明应用带的validation版本比TongWeb新。则把应用里的validation-XXXX.jar 放在TongWeb的lib\endorsed下，并把TongWeb的lib\endorsed 里validation-api.jar 删除（这里优先级最高）
java.lang.NoSuchMethodError:javax.validation.spi.ConfigurationState.getValueExtractors()Ljava/util/Set;
Caused by: java.lang.ClassNotFoundException: javax.validation.ParameterNameProvider
2.出现如下类似异常，应用里要放javax.validation的实现类，通常为hibernate-validator 实现类，主要有classmate-*.jar、 hibernate-validator-*l.jar 、jboss-logging-*.jar要根据hibernate版本来放
Caused by: javax.validation.ValidationException: Unable to create a Configuration, because no Bean Validation provider could be found. Add a provider like Hibernate Validator
(RI) to your classpath.
三、annotation引起的问题
JavaEE CDI等规范经常性的对应用jar包的annotation进行扫描，导致的一些异常。例如：
[COM/ibm/db2os390/sqlj/custom/DB2SQLJEntryInfo.class] from Jar [jar:file:/home/tongweb/TongWeb6.0/deployment/bbsp/WEB-INF/lib/db2jcc-0.0.1.jar!/] for annotations]
com.tongweb.web.webutil.util.bcel.classfile.ClassFormatException: null is not a Java .class file
[2016-11-13 15:29:21] [WARNING] [System.out] [Caused by: java.lang.StackOverflowError]
[2016-11-13 15:29:21] [WARNING] [System.out] [ at com.tongweb.web.thor.startup.ContextConfig.populateSCIsForCacheEntry(ContextConfig.java:2265)]
[2016-11-13 15:29:21] [WARNING] [System.out] [ at com.tongweb.web.thor.startup.ContextConfig.populateSCIsForCacheEntry(ContextConfig.java:2278)]
所以当看到一些annotation相关的异常时，可先试着把出错的jar加在conf/tongweb.properties中，对指定的jar不进行annotation。
#TongWeb6, 也可以用通配符common*.jar过滤大部分jar
tongweb.util.scan.DefaultJarScanner.jarsToSkip=db2jcc-0.0.1.jar,.....
四、支持jersey1.X版本的问题
部署带有jersey1.X版本的应用包，报错如下：
java.lang.RuntimeException: javax.naming.NameNotFoundException: Name "com" not found.
at com.sun.jersey.server.impl.cdi.CDIExtension.getInitializedExtension(CDIExtension.java:182)
at com.sun.jersey.server.impl.cdi.CDIComponentProviderFactory.<init>(CDIComponentProviderFactory.java:95)
jersey CDI提供一个使用外部BeanManager的办法，在TongWeb启动脚本中加上-Dcom.sun.jersey.server.impl.cdi.lookupExtensionInBeanManager=true  参数即可