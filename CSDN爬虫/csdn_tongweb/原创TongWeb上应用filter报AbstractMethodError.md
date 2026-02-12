# 原创TongWeb上应用filter报AbstractMethodError

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109810207

---

问题描述：
TongWeb上应用filter报AbstractMethodError， 日志如下：
```bash
java.lang.AbstractMethodError at com.tongweb.catalina.core.ApplicationFilterConfig.initFilter(ApplicationFilterConfig.java:279)
at com.tongweb.catalina.core.ApplicationFilterConfig.getFilter(ApplicationFilterConfig.java:260)
java.lang.AbstractMethodError: filter.TestFilter.destroy()
at com.tongweb.catalina.core.ApplicationFilterConfig.release(ApplicationFilterConfig.java:311)
at com.tongweb.catalina.core.StandardContext.filterStop(StandardContext.java:4682)
at com.tongweb.catalina.core.StandardContext.stopInternal(StandardContext.java:5498)
```
问题原因：
这是采用JavaEE8 servlet4.0规范开发的filter无init 和 destory方法。 见JavaEE8 API说明两个方法为default。 extension methods—虚拟扩展方法，是指在接口内部包含了一些默认的方法实现。而在TongWeb上还需要调用这两个方法。

解决办法：
1. 在filer中增加init、destory两个方法。
2. 将来升级到TongWeb最新版本。