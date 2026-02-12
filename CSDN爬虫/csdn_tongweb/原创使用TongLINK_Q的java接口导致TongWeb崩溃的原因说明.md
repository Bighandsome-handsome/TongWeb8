# 原创使用TongLINK/Q的java接口导致TongWeb崩溃的原因说明

> 原文地址: https://blog.csdn.net/realwangpu/article/details/110296489

---

问题一：TongWeb不能加载jtlq_client动态库
1. 现象描述如下：TongWeb上的应用日志中报错信息：java.lang.UnsatisfiedLinkError: no jtlq_client in java.library.path
2. 原因分析及解决方案：可能windows的path路径下找不到jtlq_client动态库，或在Linux的LIB_LIBRARY_PATH环境变量中找不到jtlq_client动态库，或是java进程启动参数中缺少-Djava.library.path指向该so目录。（对于安装包安装的TLQ，出现此种情况的概率比较小）由于JDK 32位或64位不能与安装的TLQ81的版本相匹配。例如JDK32位的，而TLQ81安装了一个64位的版本。这样也会报上述现象错误。
3. 解决方法：TongWeb使用64位JDK则采用TLQ 64位版本，并配置相应的环境变量。

问题二：TongWeb进程异常退出或数据包错乱
1. 现象描述如下：TongWeb 异常退出，会产生虚拟机的日志文件hs*****.log，内容大概如下：
调用TlqQCU类里putMessage或getMessage方法，调用方法抛出错误信息“receive first packet, head doesn't match(<C,2>, <1,1>)”
2. 原因分析及解决方案：由于使用TlqQCU，TlqConnection里面的方法没有实现串行化，即要对这两个类的所有方法的调用要进行排队。因为TongLINK/Q手册里有说明，这两个类实例的所有方法只能在一个线程里使用。如果多个线程同时使用这两个类同一实例的所有方法的就要对这两个类的所有方法的调用进行加锁，否则就容易造成TongWeb崩溃。在TongWeb这种多线程应用的场景下，该规则已经显的不合时宜，期望TongLINK/Q下一版本进行改进。