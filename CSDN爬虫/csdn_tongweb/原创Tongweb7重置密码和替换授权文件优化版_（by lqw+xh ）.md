# 原创Tongweb7重置密码和替换授权文件优化版*（by lqw+xh ）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/139529435

---

重置密码
如图所示，输入初始密码是会报错的，说明已经修改了密码
首先我们先备份一下tongweb的安装目录，避免因为修改过程中出现的差错而导致tongweb无法启动：
备份好了之后，我们关闭掉tongweb。
方式一：
Cd 到tongweb安装目录bin目录下，执行
./forcestopserver.sh
方式二：
输入jps，查看tongweb进程，然后kill掉（jps显示如下图，这个ThorBootstrap 就是tongweb的进程了）
方式三：
输入ps -ef |grep tongweb，查看对应进程id，然后kill掉
配置参数-Dnever.expire=on，配置在tongweb安装目录bin目录下的external.vmoptions
覆盖文件，将安装目录下domain_template/conf/security覆盖到安装目录的conf目录下（cp -r /opt/TongWeb7.0.4.9_M3_Enterprise_Linux/domain_template/conf/security  /opt/TongWeb7.0.4.9_M3_Enterprise_Linux/conf）
覆盖完检查一下，如果security目录下有这种文件，直接删除（很多重置失败的都是因为tongweb进程没关，參數沒配，或者是这两个备份文件没删，导致重置失败）：
删除后看一下twusers.properties，看看里面的thanos密码是不是这样的：
3d6391e41e9c4319
$3
$6774c6fc94b9d29478de176c4e1b9ddfdf741bba57a75ec8b97f0a7221cef769
$SM3
$$
0
$$
0
$30
$44r3azwdq5xc52e5wdgqv7yj2komtplz
然后启动一下tongweb（cd到安装目录的bin目录，执行./startservernohup.sh）,访问控制台，输入一下初始密码：thanos123.com ，成功登录
替换授权文件
当容器日志报授权还有…天到期,请及时联系商务申请新的授权文件
1、进入tongweb安装根目录
图中红色框的就是授权文件 license.dat ，删除旧的文件，复制新文件到tongweb的根目录下
执行bin目录下的version.sh脚本
替换前：
替换后：
检查end_date时间，判断是否替换成功，如果是永久授权时间则为-1。
替换授权文件不必重启容器，tongweb本身会在每日凌晨自动读取license.dat