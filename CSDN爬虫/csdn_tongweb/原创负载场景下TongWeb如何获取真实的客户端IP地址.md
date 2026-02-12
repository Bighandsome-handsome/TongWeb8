# 原创负载场景下TongWeb如何获取真实的客户端IP地址

> 原文地址: https://blog.csdn.net/realwangpu/article/details/110137907

---

问题描述：
通过负载设备后，TongWeb上的应用通过request.getRemoteAddr()方式得到的是负载设备的IP，而得不到真实的客户端IP。
解决办法一：
经过代理以后，由于在客户端和服务之间增加了中间层，因此服务器无法直接拿到客户端的 IP，服务器端应用也无法直接通过转发请求的地址返回给客户端。但是在转发请求的HTTP头信息中，增加了X-FORWARDED-FOR信息。用以跟踪原有的客户端 IP地址和原来客户端请求的服务器地址。所以通过 request.getRemoteAddr()的方法获取的IP实际上是代理服务器的地址，并不是客户端的IP地址。应该采用
request.getHeader("x-forwarded-for")
方式。完整的方法如:
```java
public String getRemortIP(HttpServletRequest request) {
if (request.getHeader("x-forwarded-for") == null) {
return request.getRemoteAddr();
}
return request.getHeader("x-forwarded-for");
}
```
如果说应用写死request.getRemoteAddr()方式获取IP，应用不能改呀，不想改呀等等理由。可以在应用所在虚拟主机中配置自定义 valve。RemoteIPValve就是利用X-Forwarded-For和X-Forwarded-Proto等字段，得到最原始的客户端的IP和请求信息.
注意：TongWeb6与TongWeb7类名不同。
TongWeb7自定义 valve：com.tongweb.catalina.valves.RemoteIpValve,protocolHeader=X-Forwarded-Proto,remoteIpHeader=X-Forwarded-For
TongWeb6自定义 valve：com.tongweb.web.thor.valves.RemoteIpValve,protocolHeader=X-Forwarded-Proto,remoteIpHeader=X-Forwarded-For

另外TongWeb的访问日志若想记录真实IP。需要在访问日志格式中加入 如下配置：
%{yyyyMMddHHmmssSSS}t %U %m %a %D
%{X-Forwarded-For}i

用扩展日志格式，用 cs(X-Forwarded-For) 方式就可以
cs-method cs-uri-query c-ip s-ip time
cs(X-Forwarded-For)

解决办法二：
如果已确认获取代理的IP，port，http或https协议，可以在http通道中写明代理服务器地址，这样request.getScheme()，request.getServerName()获取的就是代理的值。