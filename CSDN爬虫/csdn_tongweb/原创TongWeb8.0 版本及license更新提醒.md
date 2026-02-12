# 原创TongWeb8.0 版本及license更新提醒

> 原文地址: https://blog.csdn.net/realwangpu/article/details/143872626

---

一、TongWeb8.0安装包
1. TongWeb8.0提供通用安装包，并通过license来控制版本为企业版、标准版、教学版、轻量版、容器云版。不同版本功能不同，详见手册。
2. 默认TongWeb8.0支持javax命令空间应用，若需要支持Jakarta EE9及以上规范的应用，或需要安装体积更小的轻量版，则可以利用版本生成功能生成相应安装包。
3. 关于版本说明：
(1) TongWeb8.0与TongWeb7.0.8均为TongWeb8.0版本，因为有名录要求所以同步发布TongWeb7.0.8版本。
(2) TongWeb8.0与TongWeb7.0.8均需要TongWeb8.0的license， TongWeb7.0.4版本的license无法用于TongWeb8.0与TongWeb7.0.8上。
(3) 版本号命名对应规则：TongWeb8.0.a.b等于TongWeb7.0.8.ab，如:TongWeb8.0.7.2对应的版本是TongWeb7.0.8.72。
二、关于license更新
对于大规模使用的场景，有通过license server方式统一授权更新，有通过注册中心批量更新，见：
TongWeb8.0注册中心的使用示例-批量更新license_tongweb license-CSDN博客
这里我们说明下常用的license更新方式。
方式一：
将license.dat文件放入TongWeb8.0安装根目录下，重启TongWeb完成更新。
方式二：
通过控制台更新license。
三、license到期提醒
临时license在到期前提供多种提醒方式，
若在到期后仍不更新license，则TongWeb默认会在早上6点自动停止。
提醒方式一：东方通公司在用户license到期15天前，会通过预留给东方通的手机号和邮箱向用户发送提醒短信和邮件。
提醒方式二：TongWeb日志和控制台会有license到期提醒。
============================================================
^^^^^^^^^^^^^^^ TongWeb License Expiration Notice ^^^^^^^^^^^^^^^
The license will expire in 6 days. TongWeb will stop on 2024-12-06.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
============================================================
提醒方式三：用户自行在TongWeb上配置邮箱和短信提醒， 但需要确保TongWeb可以发邮件和短信。