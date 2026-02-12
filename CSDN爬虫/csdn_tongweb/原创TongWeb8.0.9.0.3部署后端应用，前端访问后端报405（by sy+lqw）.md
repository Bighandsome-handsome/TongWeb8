# 原创TongWeb8.0.9.0.3部署后端应用，前端访问后端报405（by sy+lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/149194217

---

问题描述：
客户前端部署在nginx上，后端部署在tongweb8上（相当于前后端分离），登录的时候报错，f12看network，状态码405，如下所示：
看console，如下所示：
解决方案
Web容器 > 通道 > 目标通道 > HTTP属性，把需要支持的全选，点击 更新，配置立即生效（无需重启）。