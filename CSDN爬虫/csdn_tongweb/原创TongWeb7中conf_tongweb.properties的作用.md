# 原创TongWeb7中conf/tongweb.properties的作用

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109490040

---

TongWeb在加载类应用类时，会做一些没有必要的annontation扫描导致异常，可以在TongWeb的conf目录下tongweb.properties中过滤相应的jar。
TongWeb7的tongweb.properties中找到如下
Tongweb.util.scan.StandardJarScanFilter.jarsToSkip
键值增加jar名:
tongweb.util.scan.StandardJarScanFilter.jarsToSkip
=\
byte-buddy-1.9.5.jar,
bootstrap.jar,classmate-1.5.1.jar,commons-daemon.jar,\
annotations-api.jar,el-api.jar,jsp-api.jar,servlet-api.jar,websocket-api.jar,\
jaspic-api.jar,\
TongWeb6的tongweb.properties中找到如下增加jar名:
tongweb.util.scan.DefaultJarScanner.jarsToSkip
=
byte-buddy-1.9.5.jar,
bootstrap.jar,commons-daemon.jar,annotations-api.jar,el-api.jar
常见异常如下，把相应的jar名写入tongweb.properties中即可，
但尽量不要配*.jar，这样会导致正常使用的annontation失效。
1. 应用中带了JDK9的类，需将该jar加在StandardJarScanFilter.jarsToSkip中。
[Unable to process Jar entry [META-INF/versions/9/module-info.class] from Jar [file:/D:/a/WEB-INF/lib/byte-buddy-1.9.3.jar] for annotations]
com.tongweb.web.util.bcel.classfile.
ClassFormatException: Invalid byte tag in constant pool: 19
at com.tongweb.web.util.bcel.classfile.Constant.readConstant(Constant.java:97)
at com.tongweb.web.util.bcel.classfile.ConstantPool.<init>(ConstantPool.java:54)
at com.tongweb.web.util.bcel.classfile.ClassParser.readConstantPool(ClassParser.java:174)
at com.tongweb.web.util.bcel.classfile.ClassParser.parse(ClassParser.java:83)
2. org.bouncycastle.asn1.ASN1EncodableVector，org.bouncycastle.asn1.DEREncodableVector两个类互为父子，需将该jar加在StandardJarScanFilter.jarsToSkip中，否则TongWeb判断可能导致异常报如下：
Caused by: java.lang.IllegalStateException: Unable to complete the scan for annotations for web application [ecology] due to a StackOverflowError. Possible root causes include a too low setting for -Xss and illegal cyclic inheritance dependencies. The class hierarchy being processed was
[org.bouncycastle.asn1.ASN1EncodableVector->org.bouncycastle.asn1.DEREncodableVector->org.bouncycastle.asn1.ASN1EncodableVector]
at com.tongweb.catalina.startup.ContextConfig.checkHandlesTypes(ContextConfig.java:2118)
at com.tongweb.catalina.startup.OpenEJBContextConfig.checkHandlesTypesSuper(OpenEJBContextConfig.java:759)
at com.tongweb.catalina.startup.ThanosOpenEJBContextConfig.checkHandlesTypes(ThanosOpenEJBContextConfig.java:53)
at com.tongweb.catalina.startup.ContextConfig.processAnnotationsStream(ContextConfig.java:2062)
at com.tongweb.catalina.startup.OpenEJBContextConfig.processAnnotationsStreamSuper(OpenEJBContextConfig.java:753)
at com.tongweb.catalina.startup.ThanosOpenEJBContextConfig.processAnnotationsStream(ThanosOpenEJBContextConfig.java:40)
at com.tongweb.catalina.startup.ContextConfig.processAnnotationsJar(ContextConfig.java:2008)
at com.tongweb.catalina.startup.ContextConfig.processAnnotationsUrl(ContextConfig.java:1978)
at com.tongweb.catalina.startup.OpenEJBContextConfig.processAnnotationsUrlSuper(OpenEJBContextConfig.java:772)
3. 实际上应用没用这个类, hadoop-hdfs*.jar中有引用这个类导致，需将该jar加在StandardJarScanFilter.jarsToSkip中。否则报错：
Caused by: java.lang.
ClassNotFoundException: com.sun.jersey.spi.inject.InjectableProvider
4. db2jcc.jar引起的异常。
[2015-09-24 10:37:09] [SEVERE] [core] [Unable to process Jar entry [COM/ibm/db2os390/sqlj/custom/DB2SQLJEntryInfo.class] from Jar [jar:file:/home/tongweb/TongWeb/deployment/bbsp/WEB-INF/lib/
db2jcc-0.0.1.jar
!/] for annotations]
com.tongweb.web.webutil.util.bcel.classfile.
ClassFormatException: null is not a Java .class file
at com.tongweb.web.webutil.util.bcel.classfile.ClassParser.readID(ClassParser.java:238)
at com.tongweb.web.webutil.util.bcel.classfile.ClassParser.parse(ClassParser.java:114)
5. 像这种情况不报jar或class文件名，只能通过*.jar或 * 全部过滤掉。
Caused by: java.lang.ArrayIndexOutOfBoundsException: 56
at com.tongweb.xbean.
asm5.ClassReader.readClass
(ClassReader.java:2462)
at com.tongweb.xbean.asm5.ClassReader.accept(ClassReader.java:543)
at com.tongweb.xbean.asm5.ClassReader.accept(ClassReader.java:507)
at com.tongweb.xbean.finder.AnnotationFinder.readClassDef(AnnotationFinder.java:1171)
at com.tongweb.xbean.finder.AnnotationFinder.<init>(AnnotationFinder.java:148)
at com.tongweb.xbean.finder.AnnotationFinder.<init>(AnnotationFinder.java:161)
at com.tongweb.tongejb.config.FinderFactory$OpenEJBAnnotationFinder.<init>(FinderFactory.java:546)
等价：
tomcat配置：tomcat.util.scan. StandardJarScanFilter.jarsToSkip
说明：
A list of comma-separated file name patters that is used as the default value for pluggabilitySkip and tldSkip attributes of the standard JarScanFilter implementation.
The coded default is empty, however the system property is set in a default Tomcat installation via the $CATALINA_BASE/conf/catalina.properties file.