# 原创tongweb7控制台无法访问

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/146342881

---

tongweb7控制台无法访问
排查
1.首先确认版本，如果版本是轻量级版本，轻量版不支持会话(session)的备份和复制、管理控制台、APM 运维工具等企业级增量功能。
2.查看端口
命令：ss -tnlp 或者netstat -tnlp  确认控制台端口是否开启
3.在conf下面查看tongweb-xml查看web-app下其是否存在console应用，查看其应用上下文前缀，另外也关注下其绑定的虚拟主机和端口，以及是否启动，如下图所示，主机和端口一般不做更改。