# 原创tongweb安全整改（by cz）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/143994838

---

一 禁止以root账号运行tongweb服务
1 如果是首次安装须创建普通用户安装tongweb
2 如果已经使用root账号安装了tongweb
2.1 创建普通用户
2.2 使用root账号授予tongweb安装目录宿主权限为普通用户
2.3赋权成功后，后续启动tongweb服务必须为普通用户
二 tongRDS隐藏FLUSHALL、SHUTDOVN、CONFIC、FLUSHDE等危险命令
1 进入tongRDS安装目录pmemdb/etc找到cfg.xml配置文件
2 编辑cfg.xml文件，添加或修改以下配置
如下图所示：
<
DangerousCommandFilter
>
true
<
/DangerousCommandFilter
>
<
DangerousCommands
>
flushall，shutdown,config,flushdb
<
/DangerousCommands
>
3.保存修改后的配置文件，并重启TongRDS服务以使配置生效。
三 配置tongweb控制台访问白名单
3.1 登录tongweb控制台进入WEB容器配置>虚拟主机管理 选择需要配置的虚拟机
3.2 点击进入虚拟机管理开启远程过滤，可以配置允许的IP地址也可以配置禁止的IP地址，用或者||配置多个IP，也可以使用通配符的正则表达式表示 168.1.103.0 到 168.1.103.99 的远程
地址：168.1.103.([0-9]|[1-9][0-9])（“.”为“.”的转义字符，“|”
为“或”选择符）用逗号分隔一个正则表达式。
四 配置tongwb错误页重定向，（指定错误页的绝对路径），（指定错误号），（指定错误原因）
4.1在应用 WEB-INF/web.xml 中增加如下信息和相应页面。
若访问的 URL 地址非应用前缀，同样会导致 404 错误，这样 web.xml 中的错误页起不到作用。可编写一个 web 应用，里面只含有 404 错误 html 页面和 web.xml 中相应描述，部署TongWeb 上，“应用前缀”设为/，则所有错误请求都会被拦截
五 开启tongweb访问日志
5.1 登录tongweb控制台进入WEB容器配置>虚拟主机管理 选择需要配置的虚拟机
5.2 点击开启访问日志
5.3 开启后会在tongweb/logs/access的目录下生成访问日志文件，记录了客户端访间的本机IP、访问时间、访问的资源、请求使用的协议以及返回的状态码等内容，著发现有攻击现象可以打开访问日志，通过分析访问日志可以知道哪此IP访问了系统资源
六 配置tongweb安全证书支持https协议安全访问
6.1 登录tongweb控制台进入WEB容器配置>HTTP通道管理 选择需要配置的http通道
6.2 选择http通道类型为https
6.2 下拉到ssl属性，填写正确的证书类型，证书存放路径和证书密码点击保存配置完成