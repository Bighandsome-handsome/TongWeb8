# 原创TongWeb异常宕机问题分析

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/156774410

---

TongWeb异常宕机问题分析
声明：两台服务器TongWeb崩溃问题均为jdk崩溃后导致TongWeb崩溃，均由jdk生成hs_error文件。
一、服务器1TongWeb/domain_2崩溃，并有hs文件生成。
Jvm配置：xmx2024m xms2024m
服务器内存mem：total 509g used 41g free 366g
swap total 4g used0 free4g
此处为崩溃问题所在，JVM 本地内存分配失败，具体由系统资源不足和 JVM 配置不合理共同导致。
核心问题：1、系统层面：物理内存或交换空间耗尽，无法满足 JVM 对本地内存的申请需求。查看过服务器，物理内存资源充足。交换空间为4G，需要扩展。建议16G。
2、应用层面：ActiveMQ 连接未合理释放，导致 Transport 线程持续累积，叠加线程池线程阻塞，进一步加剧内存占用。
建议：应用 需要限制 ActiveMQ 连接数：配置连接池最大连接数，避免无限制创建 Transport 线程（例如设置maxConnections参数。
3、JVM层面：增加jdk参数-Xss 512k，文件中有提到设置-XX:ReservedCodeCacheSize=0x100000000参数（即 4GB 虚拟地址以上），
该参数强制 Java 堆从 4GB 以上地址开始分配，彻底避开本地堆的低地址扩展区域，解决地址冲突问题。
可以把-XX:ReservedCodeCacheSize=0x100000000参数添加到启动参数中
启动后通过jinfo 查看，确保HeapBaseMinAddress值为0x100000000。
二、服务器2TongWeb崩溃，并有生成hs文件
Jvm配置：xmx为131072m xms为65536m、MaxMetaspaceSize=8192m
服务器内存mem：total 509g used 41g free 366g
swap total 4g used0 free4g
结合完整崩溃日志、JVM 配置（-Xmx131072m/-Xms65536m、CICompilerCount=6、MaxMetaspaceSize=8192m）及服务器资源（内存 509G、空闲 366G，swap 空闲 4G），崩溃核心矛盾并非 “系统资源不足”，而是JVM 线程管理失控 + 虚拟地址空间分配冲突。
1、此处明显线程泄露，且 99% 以上线程处于_thread_blocked状态。
调整：1、减少线程栈：-Xss512k，降低jvm大小改为Xmx64g -Xms64g，-XX:MaxMetaspaceSize改为4096m。
2、调整tongweb/conf/tongweb.xml，tong-http-listener处两个参数，max-threads=“1000” min-spare-threads=“50”。
3、检查服务器系统内存配置，建议增加swap为16g