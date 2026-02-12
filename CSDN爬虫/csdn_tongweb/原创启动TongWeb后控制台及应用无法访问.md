# 原创启动TongWeb后控制台及应用无法访问

> 原文地址: https://blog.csdn.net/realwangpu/article/details/111085958

---

启动TongWeb后控制台无法访问该如何处理：
1. 先确认TongWeb已经启动成功，通过JDK的jps –v命令或ps –ef|grep java命令查看TongWeb的进程是否存在，如下：`7044 ThorBootstrap -Xmx512m -XX:MaxPermSize=192m -XX:+UnlockDiagnosticVMOptions -XX:+LogVMOutput`
2. TongWeb日志server.log中已显示启动完成，只有启动成功才能访问控制台。
```bash
#日志中这句话表示启动完成
[INFO] [core] [TongWeb server startup complete in 72757 ms]
```
3. 检查conf/tongweb.xml中的配置，确认控制台和应用使用端口，并通过netstat 命令确认端口已启动。
#TongWeb控制台访问端口，若有ssl-enabled为true说明是https协议。
<http-listener name="system-http-listener" port="9060" ssl-enabled="true"
4.  在浏览器所在机器上通过`ping  <TongWeb机器IP>`和`telnet  <TongWeb机器IP>  9060`
命令测试是否通？ 常见原因：(1).网络不通。(2). 网络通，但端口不通，这通常是防火墙导致端口不通。请确认网络连通，防火墙端口开启。
注：(1)  <TongWeb机器IP>换成实际的IP地址，有人直接复制ping  <TongWeb机器IP>执行。
(2) 有telnet命令则想办法安装。
(3)  在TongWeb本机用火狐浏览器  127.0.0.1地址访问控制台，若可以则说明是网络问题。
5.某些windows系统下，需要把控制台站点加入IE的受信任站点才可以。
低级错误：别在浏览器上输入`http://TongWebIP:9060/console`访问控制台。TongWebIP要换为实际IP，别直接复制粘贴手册中的内容。