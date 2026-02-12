# 原创TongWeb的JVM线程监控为什么老是红的

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109673271

---

问题描述：
总是看到TongWeb的JVM线程监控图是红的。
原因:
因为这个图的计算方式是JDK  Mbean的 getThreadCount()   /  getPeakThreadCount() 比值。
getThreadCount()
返回活动线程的当前数目，包括守护线程和非守护线程。
getPeakThreadCount()
返回自从 Java 虚拟机启动或峰值重置以来峰值活动线程计数。
刚启动TongWeb时这两个方法返回的线程数相近，所以永远是红的。只有当TongWeb经历过线程高峰，线程回落后，这个图才不会为红色。
解决办法：
这不是个问题，线程多监控http通道的线程池即可，这个JVM总线程数监控对分析性能帮助不大。正确方式为查看http通道的线程。