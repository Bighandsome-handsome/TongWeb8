# 原创TongWeb7-重置TongWeb账号密码

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/134267860

---

TongWeb 目录/bin 配置文件 external.vmoptions 中追加参数-Dnever.expire=on，如下截图：
删除tongweb 目录/conf/security 目录
将 tongweb 目录/domain_template/conf/security拷贝至tongweb 目录
/conf下，并重启TongWeb。
可使用默认账号密码登录 tongweb 控制台(thanos/thanos123.com)
可使用默认账号密码登录 tongweb 集中管理控制台(rig/rig123.com)
进入 TongWeb 控制台修改密码，步骤如下截图：