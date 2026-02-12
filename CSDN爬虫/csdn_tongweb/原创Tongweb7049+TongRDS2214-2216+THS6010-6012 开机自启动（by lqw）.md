# 原创Tongweb7049+TongRDS2214-2216+THS6010-6012 开机自启动（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/142789616

---

原理
配置rc.local（这个网上有很多示范，为了方便使用，在这里总结一下各个产品的配置）
Tongweb7049
Tongweb7049 本身自带开机自启动脚本（bin目录下的installxxx.sh），但是有时执行失败的话，可以参考这个。
chmod
+x /etc/rc.d/rc.local
chmod
755
/etc/rc.d/rc.local
su - root -c “cd tongweb安装目录的bin目录;./startservernohup.sh”，例如：
注意：
1.把root替换为tongweb安装目录所属用户。
2.startservernohup.sh这个脚本记得给执行权限。
TongRDS2214-2216
在/etc/rc.d/rc.local文件中加入TongRDS的启动命令，rc.local要有x权限,相关安装目录请自行替换并测试。
chmod
+x /etc/rc.d/rc.local
chmod
755
/etc/rc.d/rc.local
#启动管理控制台（如果没有可以不添加）
su
- root -c
"cd /home/tongweb/TongRDS/console/bin;nohup ./console.sh start >/dev/null &"
#启动节点管理器，（如果没有可以不添加）
su
- root -c
"cd /home/tongweb/TongRDS/node-mgr;nohup ./probe.sh start >/dev/null &"
#启动中心服务
su
- root -c
"cd /home/tongweb/TongRDS/console/apps/center89/bin; nohup ./StartCenter.sh >/dev/null &"
#启动节点
su
- root -c
"cd /home/tongweb/TongRDS/node-mgr/apps/node1/bin;nohup ./StartServer.sh >/dev/null &"
#启动哨兵节点，如果没有可以不添加
su
- root -c
"cd /home/tongweb/TongRDS/console/apps/sb01/bin;nohup﻿ ./StartServer.sh >/dev/null &"
注意：
1.把root替换为trds安装目录所属用户。
2.上述涉及的脚本记得给执行权限。
THS6010-6012
chmod
+x /etc/rc.d/rc.local
chmod
755
/etc/rc.d/rc.local
#启动节点
su
- root -c
"cd /opt/THS/bin; ./start.sh"
#启动agent（没有的话可以不用配）
su
- root -c
"cd /opt/THS/bin; ./startAgent.sh"
#启动HA（没有的话可以不用配）
su
- root -c
"cd /opt/THS/bin; ./startHA.sh"