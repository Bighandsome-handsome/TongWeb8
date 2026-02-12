# 原创TongWeb对IPv4、IPv6的支持

> 原文地址: https://blog.csdn.net/realwangpu/article/details/111952963

---

问题：
TongWeb是否支持IPv4、IPv6双栈？
答复：
支持，细则如下：
在说明TongWeb如何支持IPv4、IPv6的，先来说明下JDK对IPv4、IPv6两个重要支持参数
：-Djava.net.preferIPv4Stack=false    -Djava.net.preferIPv6Stack=false
java.net.preferIPv4Stack（默认值false）
官方文档解释：
If IPv6 is available on the operating system, the underlying native socket will be an IPv6 socket. This allows Java applications to connect to, and accept connections from, both IPv4 and IPv6 hosts.
当
java.net.preferIPv4Stack
为默认值false时，在支持IPv6的双栈系统上，使用Java的Socket会默认通过底层native方法创建一个IPv6 Socket，这个IPv6 Socket可以同时支持和IPv4或IPv6主机通信。如果设置为true，Java程序将无法使用IPv6进行网络通信，也就是仅支持IPv4。
java.net.preferIPv6Addresses（默认值false）
官方文档解释：
By default, IPv4 addresses are preferred over IPv6 addresses, for example, when querying the name service (for instance, DNS service), IPv4 addresses would be returned ahead of IPv6 addresses.
当
java.net.preferIPv6Addresses
为默认值false时，IPv4地址会优先使用，例如在DNS通过域名查询IP地址时，会优先使用IPv4地址，反之设为true，则会优先使用IPv6地址。
因此TongWeb默认
bin/external.vmoptions中-Djava.net.preferIPv4Stack=false
以同时支持IPv4、IPv6。
但是往往招标需求与实际使用不符，截止目前还有很多实际生产环境还没有采用IPv6，而服务器网卡却有IPv6地址，导致IPv6引起的各种启动问题，例如：
Caused by: java.lang.IllegalArgumentException: cannot use an unresolved DNS server
address: [fe80::1%enp125s0f1]:53
at io.netty.resolver.dns.DnsServerAddresses.sanitize(DnsServerAddresses.java:179)
at io.netty.resolver.dns.DnsServerAddresses.sequential(DnsServerAddresses.java:67)
at io.netty.resolver.dns.DefaultDnsServerAddressStreamProvider.<clinit>(DefaultDnsServerAddressStreamProvider.java:109)
... 170 more
main" #1 prio=5 os_prio=0 tid=0x0000ffffb404f000 nid=0x7486 runnable [0x0000ffffbba2b000]
java.lang.Thread.State: RUNNABLE
at java.net.
Inet6AddressImpl
.lookupAllHostAddr(Native Method)
at java.net.InetAddress$2.lookupAllHostAddr(InetAddress.java:928)
at java.net.InetAddress.getAddressesFromNameService(InetAddress.java:1323)
at java.net.InetAddress.getLocalHost(InetAddress.java:1500)
要是想禁用IPv6怎么办？
解决办法：bin/external.vmoptions中-Djava.net.preferIPv4Stack设为true。
要是一定要用IPv6,但绑定的是错误的IPv6，导致7200端口启动不起来，怎么办?
解决办法：bin/external.vmoptions中加参数绑定IPv6 -Djava.rmi.server.hostname=[fe80::b0ce:dbf7:2644:dfca]  记得要有中括号。
注意:TongWeb一些老版本还需在conf/tongweb.xml中<jmx-service port="7200" address="[fe80::b0ce:dbf7:2644:dfca]" protocol="rmi"/>绑定IP。
课外知识：要学习IPv6的地址格式。如：http://[::1]:9060/console  中 [::1] 相当于127.0.0.1