# 原创TongWeb集群部署方案

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109533346

---

概念
TongWeb集群是由多个同时运行的JavaEE应用服务器组成，在外界看来就像一个服务器一样，这多台服务器共同来为客户提供更高性能的服务。而负载均衡器的任务就是负责多个服务器之间实现合理的请求分配，使这些服务器不会出现因某一台超负荷、而其他的服务器却没有充分发挥处理能力的情况，即便其中一台服务器宕机，其它服务器就会继续接管请求进行处理。通常我们所说的集群、负载均衡、反向代理是一个意思。
在JavaEE应用的集群模式下有session亲和、session复制两个概念需要解释下：
session
亲和
(session
保持
)
是指在集群环境下，同一
IE
客户端的请求会被始终分发到同一个
TongWeb
节点上，这是集群配置时负载软件必须实现的。通常保证
session
亲和的有以下几种方式：基于客户端IP
的
session
亲和、基于cookie
的
session
亲和、基于session id
的
session
亲和。
session
复制(session共享)是指
TongWeb
之间
session
信息可以实现共享。
TongWeb
集群可以只配
session
亲和，不配
session
复制，这样只会造成客户端请求跳转到另一个
TongWeb
节点上时
session
信息丢失。也可以配
session
亲和的同时，也配置
session
复制，这样客户端请求跳转到另一个
TongWeb
节点上时
session
信息不丢失，但同时需要维护会话服务器。目前应用常以单点登录
(SSO)
作为解决方案。
环境说明：
负载设备的选择, 只要是支持http协议的负载均衡设备TongWeb均可支持。硬件负载设备如：F5、深信服、东方通TongADC；软件负载设备如：开源nginx、apache、haproxy、东方通TongHttpServer（THS）。
负载设备部署在前端，客户端访问的是负载设备地址，负载设备作为单点需要HA主备。THS自身即支持集群，也支持HA主备。开源nginx、apache、haproxy需要做主备的话，需要额外配置开源的keepalive或heartbeat这两款HA软件。
若配置https，则通常是SSL证书配在负载设备上，指向后台TongWeb的http端口。SSL证书无需在TongWeb上配置。
至少准备两台服务器安装TongWeb，若是软件负载也可以跟TongWeb安装在同一台服务器上，或独立服务器。
追求高并发量的情况下采用硬负载，并发量不高的情况下采用软负载。
可以采用TongWeb的集中管理一次将THS+TongWeb集群搭起，也可以手配配置TongWeb集群。
采用TongDataGrid集群做为session的存储库，当其中一个TongWeb节点宕机时，其它TongWeb节点可以从TongDataGrid中恢复session数据，从而保证session不丢失。
TongDataGrid的session复制不是必配项，若应用有单点登录(SSO)功能，则完全可以不配session复制功能，SSO为最佳选择。
集群中负载设备、TongWeb、TongDataGrid可以任意增加节点，无启动顺序要求。
部署架构图如下：
具体可参考《TongWeb企业版用户手册.pdf》
https://download.csdn.net/download/realwangpu/18461429