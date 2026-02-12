# 原创TongWeb的session复制原理

> 原文地址: https://blog.csdn.net/realwangpu/article/details/110295588

---

session
复制是指
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
亲和的同时配置
session 复制，session信息在TongDataGrid中存储，这样客户端请求跳转到另一个TongWeb
节点上时session 信息不丢失，从TongDataGrid中恢复，但同时需要维护会话服务器
TongDataGrid
。
session复制只是解决session中的信息同步问题，应用的数据在各个TongWeb节点之间的同步依赖于应用自身完成，如：ehcache二级缓存的同步。
正确的配置方式是：
在session亲和下的session复制
，这样可以保证TongWeb内存中的session与TongDataGrid中的session同步。若前端负载产品功能太差，不能保证session亲和，则会发生什么？如下图：
不亲和的情况下运行会是以下结果：
先访问TongWeb B执行了session.setAttribute("a","1")产生session，并存入值。
session同步到TongDataGrid各个节点上。
由于不亲和访问TongWeb A，但不存在该session。
从TongDataGrid中恢复该session，并执行了session.setAttribute("b","2")。
TongWeb A与TongDataGrid同步该session中值a=1,b=2。
由于不亲和再访问TongWeb B，执行session.getAttribute("b")。由于判断TongWeb B中已有该session对象，但不会校验存的值，不会从TongDataGird中恢复，所以取b值取不到。
该设计的初衷是为了避免频繁从TongDataGrid中存取session造成性能瓶颈，从而在TongWeb处理session时，若TongWeb内存中有该session对象，则不再从TongDataGrid中获取。但是若前端负载实在不争气，就是不能保证session亲和，则必须配session复制，且要开启非亲和情况下的session复制。
TongWeb启动脚本增加参数：-Dwebcluster.session.sticky=false。
某些版本可以在tongweb-web.xml中设置<property name="tongdatagrid-stick" value="false"/>
至少有一个参数设置则 TongWeb集群将运行在非亲和模式下，TongWeb将不再缓存任何session，所有session将从TongDataGrid中直接读取，这无疑增加了性能开销。
题外话：
1. session复制已经是一种过时的免登录方案，目前应用常以单点登录(SSO)作为解决方案。
2. 当采用Apahce shiro应用框架时，session是由shiro产生和管理的，这时session复制需要在shiro中配，见：
shiro使用ehcache实现集群同步和session复制_坚持-CSDN博客
误区：tomcat是通过redis实现session复制，而TongWeb是通过TongDataGrid。可实现session复制即可，无需纠结用的是不是redis。