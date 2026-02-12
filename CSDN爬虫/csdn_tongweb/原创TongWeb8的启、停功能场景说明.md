# 原创TongWeb8的启、停功能场景说明

> 原文地址: https://blog.csdn.net/realwangpu/article/details/133789201

---

前言：
TongWeb8除了正常的startserver.sh、stopserver.sh启停功能外，还有开机自启、宕机重启、定时重启、内存溢出重启、禁止非法退出等功能，以适应不同场景，保证应用系统的可靠性。
场景一：开机自启
前提条件：1. Linux系统提供
systemd服务。 2.  TongWeb启动用户有root权限建立该服务。
如图，开启该服务是将自启动脚本写入/etc/systemd/system 或 /usr/lib/systemd/system目录中。若需要在自启动中设定其它环境变量、指定其他用户，可直接编辑该自启动脚本。
场景二：宕机重启
为解决JVM进程崩溃问题而设置，开启该功能，当TongWeb的JVM进程崩溃时，自动启动TongWeb。
还有一种情况是因为OutOfMemoryError异常导致JVM进程假死，这时可以增加如下两个参数其一，配合“宕机重启”功能实现内存溢出重启。
-XX:+ExitOnOutOfMemoryError      发生oom立即退出，无任何信息文件生成，不建议使用
-XX:+CrashOnOutOfMemoryError    发生oom后立即退出，JVM还会生成文本和二进制崩溃文件
场景三：定时重启
针对存在内存泄露、连接泄露等问题，而又无法从应用层面彻底解决问题的情况，可以设置定时重启功能，通常晚上或凌晨自动重启TongWeb。
场景四：禁止应用代码System.exit()导致的TongWeb停止
场景五：TongWeb启动用户限制
为防止操作人员在root与普通用户之间启、停TongWeb，可限制启动TongWeb的用户及umask值。
场景六：安全停止功能
为防止操作人员误停TongWeb，开启该功能后，停止时TongWeb需要输入管理员密码。
前提：操作系统也禁用kill命令。
场景七：license到期提期，TongWeb自动停止功能
默认情况下东方通会根据用户申请产品时预留的手机和邮箱，在license到期15天前发送到期提醒短信，并在控制台示TongWeb停止日期。
同时设置license每天检查的时间点。在有条件的情况下，还可以自行设置发送邮件和短信。