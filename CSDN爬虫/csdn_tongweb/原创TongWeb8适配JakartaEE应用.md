# 原创TongWeb8适配JakartaEE应用

> 原文地址: https://blog.csdn.net/realwangpu/article/details/131045862

---

历史：
2017年 Oracle将Java EE（Java SE还自己保留）交给开源组织，Eclipse基金会接手。但Oracle不允许开源组织使用Java名号，所以Jakarta EE名称于2018.02.26应运而生。
版本
发布日期
焦点说明
Java EE 8
2017.08
增加了JSON绑定和安全相关。Servlet 4.0、Bean Validation 2.0、CDI 2.0、JPA 2.2
Jakarta EE 8
2019.09
规范与Java EE 8完全相同。Maven的GAV变了：javax.servlet:javax.servlet-api:4.0.1 -> jakarta.servlet:jakarta.servlet-api:4.0.2，但
命名空间没变依旧还是javax.*
，算是个小过度吧
Jakarta EE 9
2020.11
没有加入新功能，Eclipse基金会的首个正式版本。
命名空间从javax.*迁移到jakarta.*
，前者从此成为历史。所有模块大版本号+1，如Servlet 4.0.2 -> Servlet 5以表示其断层式升级
Jakarta EE 9.1
2021.06
相较于9 没有 加入新API。主要提供对Java SE 11的运行支持
Jakarta EE10
2022.09
这个版本旨在交付一组规范，用于跨 Jakarta EE 技术（如 Jakarta EE Platform、Web 和新的 Core Profile）构建现代化、简化和轻量级的云原生 Java 应用程序。
这也就导致了从JakartaEE9与之前JavaEE应用的不兼容。
解决办法：
针对JakartaEE应用必须采用TongWeb8 版本，默认TongWeb8采用“
javax
”命名空间以兼容JavaEE规范应用。
支持JakartaEE应用，则生成JakartaEE版本。
生成后启动TongWeb，进入控制台查看其命名空间为"
jakarta
"。
TongWeb8.0.9.0及之后的版本增加了"切换命名空间"的功能，可以在javax与jakarta之间自由切换。同时集中管理支持同时管理 javax 和 jakarta 命名空间的实例。
如何快速判断应用是否为JakartaEE应用?
1. 检查其应用是否引入jakarta相关代码，如：
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
2. 应用是否引用开源组件Spring Framework 6.x、Spring Boot3.x版本？
Spring Framework6.x 和 Spring Boot3.x 则需要JDK17+，jakarta命名空间的应用服务器支持。通常情况下因为应用采用新的Spring版本，而需要升级JDK与JakartaEE应用服务器。
As of
Spring Framework 6.0
, Spring has been upgraded to the
Jakarta EE 9
level (e.g. Servlet 5.0+, JPA 3.0+), based on the
jakarta
namespace instead of the traditional
javax
packages. With EE 9 as the minimum and EE 10 supported already, Spring is prepared to provide out-of-the-box support for the further evolution of the Jakarta EE APIs. Spring Framework 6.0 is fully compatible with Tomcat 10.1, Jetty 11 and Undertow 2.3 as web servers, and also with Hibernate ORM 6.1.
Spring Boot 3.x System Requirements
Spring Boot 3.1.2 requires
Java 17
and is compatible up to and including Java 20.
Spring Framework 6.0.11
or above is also required.
Explicit build support is provided for the following build tools:
Build Tool
Version
Maven
3.6.3 or later
Gradle
7.x (7.5 or later) and 8.x
Servlet Containers
Spring Boot supports the following embedded servlet containers:
Name
Servlet Version
Tomcat 10.1
6.0
Jetty 11.0
5.0
Undertow 2.3
6.0
You can also deploy Spring Boot applications to any servlet 5.0+ compatible container.
3. 应用是否运行在tomcat10.x版本上？
若运行在该版本上，则说明肯定用的是JakartaEE应用。
基于以上规律可判断应用的JakartaEE规范。
典型的错误日志：
Caused by: java.lang.ClassNotFoundException:
jakarta
.servlet.ServletContextListener
说明：
1. TongWeb8.0/7.0.8支持Jakarta EE应用并通过认证，见：
Jakarta EE Compatible Products | Enterprise Java Application and Web Servers | Jakarta EE | The Eclipse Foundation
2. TongWeb7.0.4及以下版本不支持Jakarta EE应用，需要升级版本。