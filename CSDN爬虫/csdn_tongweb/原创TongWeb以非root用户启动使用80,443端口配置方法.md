# 原创TongWeb以非root用户启动使用80,443端口配置方法

> 原文地址: https://blog.csdn.net/realwangpu/article/details/113111709

---

需求：
想用http://IP或https://IP访问访问应用，而不用输入80,443端口，但基于安全考虑又不能用root用户启动TongWeb。注：Linux下只有root用户能使用80,433端口。
解决办法：
假如TongWeb只能以tongweb用户启停而不能用root用户，但需要使用80、443端口。
将JDK的bin下java命令文件属主改成root用户（通过chown命令）。
给JDK的bin下java命令文件加上s权限`chmod  +s  java`，这一步很重要。
s权限：设置使文件在执行阶段具有文件所有者的权限，相当于临时拥有文件所有者的身份。
以tongweb用户启动TongWeb，配置80、443端口就可以了。
这时通过ps –ef|grep java看到的java进程是root用户的，生成的相关文件(例如：tongweb日志)也是root用户的。
注意：只有对权限熟悉的运维人员才可以这样搞，否则会搞乱TongWeb和应用的文件权限，出现各种权限问题。
可能遇到的问题：启动tongweb时如果报错缺少so的库文件，这时需要从操作系统中找出到相应so文件加到LD_LIBRARY_PATH库的环境变量上即可，不同系统可能不同。