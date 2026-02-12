# 原创TongWeb8-TongWeb密码重置

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/147063630

---

将TongWeb目录/domains/domain1/conf/console.xml中以下标签删除
TongWeb目录/domains/domain1/conf/console.xml中,重新添加以下标签
重新启动TongWeb8
执行以下命令重新对密码进行修改即可。
./commandstool.sh --model=password --action=update --username=thanos --password=thanos123.com --acceptAgreement=true originalPassword=thanos123.com newPassword=wang135.COM confirmPassword=wang135.COM