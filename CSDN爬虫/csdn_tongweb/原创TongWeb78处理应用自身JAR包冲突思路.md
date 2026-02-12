# 原创TongWeb78处理应用自身JAR包冲突思路

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/144137972

---

通常应用运行时报错如果出现java.lang.NoClassDefFoundError，那么首先需要看报错日志下方的Caused by内容是什么，如果是ClassNotFoundException，那么原因就是缺少某个类。如果仍然是NoClassDefFoundError，那么很大可能是类冲突导致的。此时就需要继续排查是哪些jar包冲突。
第二种类冲突的报错不是那么明显，需要反编译jar包查看源码，比如下面两张图中的报错。
图一中显示的是NoSuchMethodError，说javax.mail.internet.ParameterList类中没有combineSegments方法。如果已知这个类在哪个jar包中，只需要查看源码就行。如果发现该类有这个方法，那么基本可以判断是类冲突，在其他jar包中会有一个相同的类但是没有这个方法。
如果查看的jar包中的类没有这个方法，往往会造成误判，认为是应用使用的jar包问题，因为事实情况与报错信息一致。但是不能忽略一种可能，在其他jar包中有一个相同的类，并且这个类有这个方法，只是应用启动时加载的类不是它而已。此时就需要去搜索是否有这个相同类存在。
可以通过这个命令查询：find ./ | xargs grep "类名" > 11.txt
图一
图二的情况与图一类似，也不是很明显的能判断出是类冲突造成的问题。从报错信息看是说子类没有实现抽象父类的方法。实际通过jar包查看源码也确实如报错信息所述一致。但是通过搜索子类和父类后发现，父类UriBuilder分别在两个jar包中出现，由此可以判断是类冲突导致的问题。
图二
其他方式检测类冲突：
如果使用TongWeb7.0产品，可以通过控制台==》类加载分析工具==》类资源分析/类冲突检测
如何处理冲突的jar包：
1、最直接的方法是将冲突的jar包删除
2、修改TongWeb配置
TongWeb7.0：在应用WEB-INF里面加入tongweb-web.xml文件。内容如下：需要优先加载的jar包放在前面。
<?xml version="1.0" encoding="UTF-8"?>
<tongweb-web-app>
<jar-orders>
<jar-order jar-name="a.jar" />
<jar-order jar-name="b.jar" />
</jar-orders>
</tongweb-web-app>
TongWeb8.0：部署应用的时候，在资源加载界面中设置加载顺序。