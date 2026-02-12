# 原创TongWeb7的JPA、validation异常

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109503498

---

TongWeb7的JPA、validation异常：
(1)
javax.validation
.spi.ConfigurationState.getValueExtractors()Ljava/util/Set;
(2) [FAIL ... : Missing required
persistence.xml
for @PersistenceContext ref "em" to unit ""]
(3) 找不到javax.persistence.或 javax.validation里的类或方法
原因
通常是TongWeb自带validation，JPA与应用冲突。
只要看到如上异常, 解决办法：
方法一：TongWeb7.0.2.5及之前版本，需要将TongWeb的lib下
validation-api.jar、persistence-api.jar里的javax.persistence.*目录删除，把应用的validation jar ，JPA jar放在TongWeb的lib下
.
方法二：TongWeb7.0.3.0及之后版本,将bin目录下external.vmoptions中的
-DWebModuleOnly=false
设为true则屏蔽TongWeb自带validation 、JPA、CDI、EJB、mail。