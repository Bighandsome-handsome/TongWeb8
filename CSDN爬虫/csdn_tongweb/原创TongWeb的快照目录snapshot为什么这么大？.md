# 原创TongWeb的快照目录snapshot为什么这么大？

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109684248

---

snapshot为TongWeb的快照生成目录，如图在满足阈值条件时会收集相应的日志。默认快照影响的几个方面是：
1. jmap内存镜像日志会较大，占用磁盘空间。
2. 默认预警策略较低，当http线程使用量为10时，则很容易达到触发条件，生成快照。
3.在生成快照时系统会有一段时间变慢，是因为快照中的jmap等命令操作导致系统当时变慢，所以在需要快照时不打开jmap就不会有太大影响。
注：快照并不能100%保证在出现问题时抓取到日志，因为快照功能的处理线程在同一个TongWeb进程中，当TongWeb进程假死时，快照线程也可能无法执行。就像一个病人要自己给自己动手术一样。
解决办法：
方式一：.若无性能问题可关闭默认快照。 在控制台上将快照default1的“策略之间的关系”设为"所有"，则基本不再生成。也可以将default1删除，并将conf/tongweb.xml中<snapshot> /<contents 标签 中设为false，如下：
<auto-snapshot interval-second="5" relation="and"> 
<contents jstack="false" jmap="false" config="false" monitor="false" system-log="false" access-log="false" gc-log="false"/>
方式二：若还有性能问题依赖快照分析，则设置合理的值。如：http线程设为200，内存无问题可关闭jmap生成。
snapshot下的快照文件可以随时删除，不影响TongWeb。