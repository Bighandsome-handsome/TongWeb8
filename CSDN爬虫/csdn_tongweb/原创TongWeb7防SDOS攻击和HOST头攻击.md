# 原创TongWeb7防SDOS攻击和HOST头攻击

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109553849

---

一、防SDOS攻击
所谓的慢攻击就是相对于DDOS的快而言的，并不是只有量大速度快才能把服务器搞挂，使用慢攻击有时候也能到达同一效果。比如：在POST提交方式中，允许在HTTP的头中声明content-length，也就是POST内容的长度。 在提交了头以后，将后面的body部分卡住不发送，这时服务器在接受了POST长度以后，就会等待客户端发送POST的内容，攻击者保持连接并且以10S-100S一个字节的速度去发送，就达到了消耗资源的效果，因此不断地增加这样的链接，就会使得服务器的资源被消耗。
TongWeb7版本配置防SDOS攻击方式如下，
注意配置参数合理，若配置过小，则可能拦截正常请求。若配置过大，则可能无法起到防攻击效果。
属性名称
对应tongweb.xml 配置属性
属性说明
完整请求时间
complete.message.timeout.seconds
完整请求时间，通过配置完整请求时间来判断是否为慢攻击,时间单位为秒,如果配置值大于 0，则认为开启慢攻击检测，默认值为 0，关闭慢攻击检测。
慢攻击容忍次数
max.attack.times
慢攻击容忍次数，为防止处理掉正常请求，支持配置容忍次数，同一个 IP 地址超过配置数，则加入黑名单，默认配置为 3
黑名单移除时间
blacklist.expired.hours
黑名单移除时间，通过配置时间来清除已经加入到黑名单中的 IP 地址，时间单位为小时，默认配置为 12 小时
中断当前连接
interrupt.current.connect
中断当前连接，布尔类型，配置为 true 表示如果当前发送消息的连接处于黑名单中，则中断，默认配置为 true
早期TongWeb的版本是通过四个-D参数来配置的，加在启动参数中如下：
参数名称
参数说明
-DcontentLength.limit
设置 POST 请求中的 content length 限制(单位：字节)，避免一直占住这个连接不断开，一般针对 POST 请求的攻击，默认值为Integer 的 最 大 值 ， 例 如-DcontentLength.limit=10000。
-Dread.http.header.timeout
读一个字节耗费的毫秒数(单位：毫秒/字节)，超过或等于这个速率算超时，默认值为 Long 的 最 大 值 ， 例 如 : -Dread.http.header.timeout=500。与-DcontentLength.limit参数配合使用。
-Dread.http.header.timeout.limit
请求头读取超时次数，超过次数将其列入黑名单，开始拒绝请求(连接)，默认值为 Integer 的 最 大 值 ， 例 如 ：
-Dread.http.header.timeout.limit=3。与-Dread.http.header.timeout 配合使用。
-Dblacklist.expired
对清理黑名单解锁时间进行设置，默认值为 12 （单 位： 小时 ），例 如 ：-Dblacklist.expired=1。与-Dread.http.header.timeout.limit 配合使用。
不适用的场景：对于前端有负载设备的场景，该配置不适合配置在TongWeb上，因为拦截的是负载设备的IP。
二、防HOST头攻击
HTTP规范中在增加了HOST头信息，用于存储服务端与客户端的路由信息。
如果前端或者后台正好用到这个值，比如jsp的String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort();那么黑客就可以通过修改HOST里域名值以达到攻击的目的。比如request.getServerName()改成：www.abc.com，这样页面内引用后请求就会被转接了。
防 Host 头攻击：开启或关闭防 Host 头攻击，开启时，需要配置正确的主机名白名单，若HOST头与配置中的值不对应则请求会被拦截。