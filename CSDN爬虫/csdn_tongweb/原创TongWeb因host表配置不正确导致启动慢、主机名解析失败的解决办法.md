# 原创TongWeb因host表配置不正确导致启动慢、主机名解析失败的解决办法

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109503682

---

现象一：
在部署上应用后，TongWeb启动慢，这时可以查看TongWeb的server.log日志看执行时间慢在哪里。 当日志走到这部分时，通过jstack  <PID>   命令打印出线程栈，可以查看到具体信息。
如下可以明显看到数据库驱动在执行getLocalHost代码，若host表配置不对会导致getLocalHost执行时间长。
```bash
"main" #1 prio=5 os_prio=0 tid=0x0000ffffb404f000 nid=0x7486 runnable [0x0000ffffbba2b000]
java.lang.Thread.State: RUNNABLE at java.net.Inet6AddressImpl.lookupAllHostAddr
(Native Method)
at java.net.InetAddress$2.lookupAllHostAddr(InetAddress.java:928)
at java.net.InetAddress.getAddressesFromNameService(InetAddress.java:1323)
at java.net.InetAddress.getLocalHost(InetAddress.java:1500)
- locked <0x00000005c008eb50> (a java.lang.Object)
at dm.jdbc.dbaccess.DbPureAccess.isLocalHost(DbPureAccess.java:220)
at dm.jdbc.dbaccess.DbPureAccess.setHostName(DbPureAccess.java:201)
at dm.jdbc.dbaccess.DbPureAccess.<init>(DbPureAccess.java:105)
at dm.jdbc.dbaccess.DbAccess.<init>(DbAccess.java:50)
at dm.jdbc.driver.DmdbConnection_bs.tryConnInner(DmdbConnection_bs.java:629)
at dm.jdbc.driver.DmdbConnection_bs.tryConnRandom(DmdbConnection_bs.java:692)
at dm.jdbc.driver.DmdbConnection_bs.tcpIpProtocal(DmdbConnection_bs.java:722)
at dm.jdbc.driver.DmdbConnection_bs.conCommLayer(DmdbConnection_bs.java:751)
at dm.jdbc.driver.DmdbConnection_bs.openConnection(DmdbConnection_bs.java:763)
at dm.jdbc.driver.DmdbConnection_bs.commInit(DmdbConnection_bs.java:736)
at dm.jdbc.driver.DmdbConnection_bs.initialize(DmdbConnection_bs.java:460)
at dm.jdbc.driver.DmdbConnection_bs.<init>(DmdbConnection_bs.java:341)
at dm.jdbc.driver.DmDriver_bs.connect(DmDriver_bs.java:100)
at dm.jdbc.driver.DmDriver.connect(DmDriver.java:86)
at java.sql.DriverManager.getConnection(DriverManager.java:664)
```
现象二：
应用程序报主机名找不到
```bash
Caused by: java.net.UnknownHostException: xxxxxxxx
at java.net.Inet6AddressImpl.lookupAllHostAddr(Native Method)
at java.net.InetAddress$1.lookupAllHostAddr(InetAddress.java:901)
at java.net.InetAddress.getAddressesFromNameService(InetAddress.java:1293)
at java.net.InetAddress.getLocalHost(InetAddress.java:1469)
... 41 more
```
通常host表主机名与IP映射不正确，TongWeb启动慢、主机名解析失败的解决方法如下：
1. 确定本机实际IP是多少，譬如：192.168.75.1
2. 敲命令hostname, 看输出主机名，譬如： host01。
3.  ping host01,  看是否能ping通，且ping出的IP是不是192.168.75.1。
4.  如果不对，就在/etc/hosts文件第一行写上主机名与IP
如：host01  192.168.75.1
5. 若是只用IPv4，则把external.vmoptions文件中的-Djava.net.preferIPv4Stack=false改为true
6. 再ping 主机名，ping通了就可以了。