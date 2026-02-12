# 原创TongWeb的日志输出阻塞

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109637446

---

问题描述：
并发情况下查看TongWeb线程大部分阻塞在日志输出上。日志如下：
"http-nio2-8080-exec-397" #850571 daemon prio=5 os_prio=0 tid=0x00000058dc0a0000 nid=0x7614 waiting for monitor entry [0x0000005908e30000]
java.lang.Thread.State:
BLOCKED
(on object monitor)
at org.apache.log4j.Category.callAppenders(Category.java:201)
- waiting to lock <0x00000003c1c33640> (a org.apache.log4j.Logger)
at org.apache.log4j.Category.forcedLog(Category.java:388)
at org.apache.log4j.Category.log(Category.java:853)
at org.apache.commons.logging.impl.
Log4JLogger.debug
(Log4JLogger.java:171)
at org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:863)
at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:967)
at org.springframework.web.servlet.FrameworkServlet.doPost(FrameworkServlet.java:869)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:648)
原因：
应用log4j日志配置为DEBUG级别日志输出，这样在大并发的情况下，会导致多线程大量的日志输出到日志文件中造成日志输出阻塞，造成系统性能问题。
解决办法：
1. 在性能测试或生产系统上运行时，应用log4j日志级别不能设为DEBUG级别， 理应为INFO级别日志。
2. 若应用设为INFO级别后仍然日志阻塞，TongWeb7.0.4.1及之后版本增加了异步日志输出功能， 增加启动参数
-DlogThreads=1
可开启异步日志输出。