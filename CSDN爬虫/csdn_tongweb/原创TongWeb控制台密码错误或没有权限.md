# 原创TongWeb控制台密码错误或没有权限

> 原文地址: https://blog.csdn.net/realwangpu/article/details/121585788

---

现象：
登录TongWeb控制台提示密码错误或没有权限，如下图：
问题原因 ：
1.TongWeb控制台密码忘记
2.TongWeb的conf\security中文件损坏，报密码或权限不对。
解决办法：
重置TongWeb密码
方式一：
<TongWeb_home>/domain_template/conf/security为TongWeb的domain模板目录，存放的是TongWeb原始配置文件。
<TongWeb_home>/conf/security目录为TongWeb用户密码相关的文件。
利用 <TongWeb_home>/domain_template/conf/security 中的文件模版去覆盖TongWeb根下的<TongWeb_home>/conf/security目录，或是域下的conf/security目录对应文件即可， 重启TongWeb恢复原始密码。
方式二：
若是老版本没有domain功能，则在测试机上安装一个全新的同版本TongWeb，将<TongWeb_home>/conf/security目录文件拷贝到忘记密码的TongWeb同级目录下，覆盖原文件，重启TongWeb恢复原始密码。