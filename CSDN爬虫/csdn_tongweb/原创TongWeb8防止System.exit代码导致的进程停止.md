# 原创TongWeb8防止System.exit代码导致的进程停止

> 原文地址: https://blog.csdn.net/realwangpu/article/details/129021619

---

现象：
当应用中存在System.exit 、Runtime.exit代码执行时，会导致TongWeb进程停止，从而产生如下日志：
2023-02-14 09:47:36 [WARN] -
The web application [webtest01] is still processing a request that has yet to finish. This is very likely to create a memory leak. You can control the time allowed for requests to finish by using the unloadDelay attribute of the standard Context implementation. Stack trace of request processing thread:
[
java.lang.Object.wait(Native Method)
java.lang.Thread.join(Thread.java:1257)
java.lang.Thread.join(Thread.java:1331)
java.lang.ApplicationShutdownHooks.runHooks(ApplicationShutdownHooks.java:107)
java.lang.ApplicationShutdownHooks$1.run(ApplicationShutdownHooks.java:46)
java.lang.Shutdown.runHooks(Shutdown.java:123)
java.lang.Shutdown.sequence(Shutdown.java:170)
java.lang.Shutdown.exit(Shutdown.java:216)
java.lang.Runtime.exit(Runtime.java:109)
java.lang.System.exit(System.java:971)
com.tong.TestServlet.doGet(TestServlet.java:41)
javax.servlet.http.HttpServlet.service(HttpServlet.java:503)
javax.servlet.http.HttpServlet.service(HttpServlet.java:590)
com.tongweb.server.core.ApplicationFilterChain.enterApp(ApplicationFilterChain.java:365)
解决方式：
方式一：修改应用代码，将System.exit 、Runtime.exit代码删除。
方式二：开启TongWeb的安全策略功能，禁止System.exit退出。
开启后拦截日志有如下输出：
System exit request has been denied.
java.lang.Thread.getStackTrace(Thread.java:1564)
java.lang.Shutdown.exit(Shutdown.java)
java.lang.Runtime.exit(Runtime.java:109)
java.lang.System.exit(System.java:971)
com.tong.TestServlet.doGet(TestServlet.java:41)
javax.servlet.http.HttpServlet.service(HttpServlet.java:503)
javax.servlet.http.HttpServlet.service(HttpServlet.java:590)