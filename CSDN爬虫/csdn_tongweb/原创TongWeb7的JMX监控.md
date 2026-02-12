# 原创TongWeb7的JMX监控

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109506744

---

通过JMX监控TongWeb7有rmi和jmxmp两种方式
方式一：rmi方式
1. 先看TongWeb的server.log中JMX日志url，可通过该URL使用jconsole连接。
[2020-11-05 10:12:54 025] [INFO][URL for the Standard JMXConnectorServer : (
service:jmx:rmi:///jndi/rmi://192.168.163.1:7200/jmxrmi
)]
用户名：thanos 密码：thanos123.com  (不同版本还可能不同，具体请参考手册)
2. rmi协议只能绑定本机一个IP地址， 若TongWeb所在机器有多个IP，而server.log中绑定的不是需要的IP地址则连不上，同时若远程访问有防火墙，需要再增加以下配置：
(1) tongweb.xml中 127.0.0.1改为要绑定的本机实际IP地址 <jmx-service port="7200" address="127.0.0.1" protocol="rmi"/>
(2) 在startserver或external.vmoptions中增加 JMX绑定IP参数：
-Djava.rmi.server.hostname=要绑定本机实际IP
(3) TongWeb还会起两个随机端口，若有防火墙则增加两个参数固定端口，开放防火墙。
-Dtongweb.jconsole.cbport=5555
-Dtongweb.rmijmx.cbport=7777
(4) 配置完以上后，依旧用原URL格式连接： service:jmx:rmi:///jndi/rmi://192.168.163.1:7200/jmxrmi
3. 这样rmi其本质是固定住了7777端口，但客户端的连接不用指明7777端口，依旧用如上连接。 因为rmi的工作方式:客户端连接到rmiregistry上得到真实服务器的stub（如:rmi://192.168.163.1:7200），然后客户端再根据该stub连接到真实的服务器上（如:rmi://192.168.163.1:7777）。如果jmx服务端省略了rmi://192.168.163.1:7777部分，默认的通信端口是随机产生的。
[systemout] [tuserport:7777;jcport:5555]
[admin] [URL for the Standard JMXConnectorServer : (service:jmx:rmi://
192.168.163.1:7777
/jndi/rmi://192.168.163.1:7200/jmxrmi)]
老TongWeb6版本还隐藏了另 一个JMX连接： service:jmx:rmi://
192.168.163.1:5555
/jndi/rmi://192.168.163.1:7200/internal,   不再多做介绍，所以-Dtongweb.jconsole.cbport在最新版本上是无用的。
4. 为了减少端口占用，还可以相同全为7200。
-Dtongweb.jconsole.cbport=7200
-Dtongweb.rmijmx.cbport=7200
service:jmx:rmi://
192.168.163.1:7200
/jndi/rmi://192.168.163.1:7200/jmxrmi
TongWeb7.0.4.6及之后版本只有7200端口。
方式二：jmxmp方式
若有网络映射，通过远程连接JMX的地址不是TongWeb的地址，则rmi方式中-Djava.rmi.server.hostname要绑定的不是TongWeb本机实际IP，而是客户端要远程连接的IP。说起来绕口，配起来麻烦。一种简单的方式就是改用jmxmp方式：
1.  tongweb.xml中 rmi改为 mp <jmx-service port="7200" address="127.0.0.1" protocol="
mp
"/>
日志中JMX地址为：
service:jmx:jmxmp://192.168.163.1:7200
jmxmp协议TongWeb本机所有IP均可访问，不需-Djava.rmi.server.hostname固定IP，没有随机端口。DXP即采用的这种。
2. 客户端JMX 代码连接依赖   jmxremote_optional-*.jar，把该jar放在JDK的类路径 \jre\lib\ext上才能用jconsole连接，放在应用的CLASSPATH上才能用代码访问。
3. TongWeb增加参数 -Djmxmp.authenticator=false 关验证。
参考：
jmx rmi 穿越防火墙问题及jmxmp的替代方案_yangyan19870319的专栏-CSDN博客
最后若想关闭TongWeb的JMX怎么办?
tongweb.xml中enabled设为false   <jmx-service port="7200" address="127.0.0.1" protocol="rmi"
enabled="false"
/>