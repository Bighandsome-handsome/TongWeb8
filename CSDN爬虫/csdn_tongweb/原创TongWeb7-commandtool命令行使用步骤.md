# 原创TongWeb7-commandtool命令行使用步骤

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/133808044

---

重置密码并重新设置命令行密码，使用TongWeb自带的password.sh对新密码进行加密后写入密码文件即可，步骤如下：
a.升级后, TongWeb目录/bin配置文件external.vmoptions中追加参数-Dnever.expire=on，如下截图：
b.重置TongWeb密码：将TongWeb目录/domain_template/conf/security目录覆盖tongweb目录/conf/security目录后，重启TongWeb。
c.通过命令行修改cli用户密码,执行以下命令
注：	9060为当前TongWeb的控制台访问端口。
passwordfil文件位于TongWeb目录/bin下，也可自行放置，但命令中需要写全路径。
passwordfil文件内容为: AS_ADMIN_password=AjLAlFlxbAed3VLKrpDZ4g==
AjLAlFlxbAed3VLKrpDZ4g==为cli用户默认密码cli123.com，通过TongWeb目录/bin
下的password.sh加密而来，如下图：
d.修改cli密码成功后，使用password.sh对新密码进行加密处理,并将加密串复制到passwordfil文件中，如下图：
e.通过命令行部署测试应用测试成功，如下图：