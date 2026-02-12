# 原创Tongweb7+Tongweb8+Ths6.0.1.0+TongRDS2214 常用指令和初始账号密码(by lqw)

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/136481102

---

Tongweb7
启动
cd到安装目录的bin目录，执行：
sh startservernohup.sh 或./startservernohup.sh
查看日志
cd到安装目录的logs目录，执行：
tail -f server.log
关闭
cd到安装目录的bin目录，执行：
./stopserver.sh quick
查看版本和授权过期时间
./version.sh
开机自启动
cd到安装目录的bin目录，执行：
./installservice.sh
关闭开机自启动
先停止tongweb服务，然后cd到安装目录的bin目录，执行：
systemctl disable tongweb.service
然后删掉以下文件：
rm /etc/systemd/system/tongweb.service
rm /usr/lib/systemd/system/tongweb.service
最后重载
systemctl daemon-reload
控制台访问url和初始账号密码
链接:http://tongweb所在服务器ip:9060/console
账号：thanos
初始密码: thanos123.com
初次登录需要修改密码。
集中管理工具访问url和初始账号密码
链接：http//tongweb所在服务器ip:9060/heimdall/
账号：rig
初始密码: rig123.com
初次登录需要修改密码。
Tongweb8
启动
cd到安装目录的bin目录，执行
./startserver.sh
关闭
cd到安装目录的bin目录，执行
./stopserver.sh
开机自启动
cd到安装目录的bin目录，执行
/admin.sh systemd install
卸载自启服务
请根据自己的安装目录进行修改，以下是装在opt/tw8下的参考
java -jar /opt/tw8/TongWeb8.0.7.0/bin/tongweb-launcher.jar  systemd uninstall
管控台访问url和初始账号密码
链接：https://<TongWebIP>:9060/console
系统管理员账号：thanos
初始密码：thanos123.com
Ths6.0.1.0
启动管控台
cd到安装目录的bin目录，执行
./startManager.sh start
关闭管控台
./startManager.sh stop
启动ths节点
cd到ths的安装节点目录的bin目录（一般节点安装在/opt/THS）
#启动节点
./start.sh
#启动agent，方便控制台识别（需要配置agent相关文件）
./startAgent.sh
#启动高可用（需配置高可用）
./startHA.sh
关闭ths节点
cd到ths的安装节点目录的bin目录（一般节点安装在/opt/THS）
./start.sh stop
./startHA.sh stop
./startAgent.sh stop
管控台访问url和初始账号密码
链接：
https//服务器ip地址：端口号（默认8000）/admin
账号：admin
密码:Ths#123.com
TongRDS2214
启动管控台
cd到管控太安装目录的bin目录（解压后一般目录名为console），执行
./console.sh start
关停管控台
cd到管控太安装目录的bin目录（解压后一般目录名为console），执行
./console.sh stop
查看管控台状态
./console.sh status
管控台访问url和初始账号密码
链接：http://服务器所在ip地址:8083
用户名：admin
密码：admin123