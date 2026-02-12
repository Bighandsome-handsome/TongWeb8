# 原创TongWeb上不同应用使用不同域名或不同端口的的办法

> 原文地址: https://blog.csdn.net/realwangpu/article/details/111944937

---

场景一：TongWeb上不同应用使用不同端口:
如果有app1、app2、app3三个应用，需要分别使用8081，8082，8083三个HTTP端口访问，可以这样配。
方式一：
1. 通过domain create命令建三个域，默认端口自动+1。
2. 通过startdomain 域名分别启动三个域，进入三个域控制台分别部署一个应用。
这种方式最大的好处是:：每个域为独立java进程，各自部署一个应用互不影响。
方式二：
1. 一个TongWeb实例上分别建8081，8082，8083三个HTTP端口。
2. 在TongWeb分别再建三个虚拟主机server1,server2, server3。
注意：其中虚拟主机别名为TongWeb本机要访问的IP地址。每个虚拟主机分别只绑定其中一个端口。
3.  将app1、app2、app3三个应用分别部在server1,server2,server3上即可。
场景二：TongWeb上不同应用使用不同域名:
如果有app1、app2、app3三个应用，分别使用www.abc.com,test01.abc.com,test02.abc.com三个域名访问，可以这样配。
1. 建HTTP 80端口。
2. 在TongWeb上分别再建三个虚拟主机server1,server2, server3. 其中虚拟主机别名分别为三个域名，同时绑定80端口。应用要通过此域名访问，不能是IP。
3.  将app1、app2、app3三个应用分别部在server1,server2,server3上即可。
注意： “应用前缀” 为/。