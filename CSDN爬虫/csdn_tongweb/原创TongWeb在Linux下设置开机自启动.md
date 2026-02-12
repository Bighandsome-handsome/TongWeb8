# 原创TongWeb在Linux下设置开机自启动

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109715096

---

TongWeb在Linux下设置开机自启动：
1. 在专用机下TongWeb安装完成即是开机自启动，无需设置。
2. 在TongWeb  bin目录下installservice.sh命令可做成自启动，具体请看doc目录下TongWeb用户手册。
注：自TongWeb7.0.4.2开始直接运行TongWeb  bin目录下的installservice.sh命令，即完成systemd服务注册。
具体说明：
方式一  专用机和执行installservice.sh命令：
专用机和执行installservice.sh命令是以systemd⽅式管理TongWeb服务，installservice.sh命令需要以root用户执行，该方式是将TongWeb 的service/linux/tongweb.service文件修改复制到/etc/systemd/system/、/usr/lib/systemd/system目录下，其内容如下：
[Unit]
Description=TongWeb Server
After=network.target
[Service]
Type=forking
Environment="JAVA_HOME=/home/jdk8"
#ExecStart=/home/tongweb7/bin/startserver.sh restart
ExecStart=/home/tongweb7/bin/boot.sh
#ExecStop=/home/tongweb7/bin/stopserver.sh stop
PrivateTmp=false
# Disable service start and stop timeout logic of systemd for tongweb service.
TimeoutSec=0
[Install]
WantedBy=multi-user.target
注：boot.sh为自启动该TongWeb所有域，所以只能启动，不能查看运行状态和停止。
方式二：修改systemd⽅式管理TongWeb服务
如果想修订systemd⽅式的启动参数，可直接修改TongWeb 的service/linux/tongweb.service文件，重新执行installservice.sh命令以生效。
[Unit]
Description=TongWeb Server
#在数据库后启动
After=database.target
[Service]
Type=forking
#指定启动用户
User=wangchao
Environment="JAVA_HOME=/home/jdk8"
#进程文件
PIDFile=/home/tongweb7/tongweb.pid
ExecStart=/home/tongweb7/bin/startservernohup.sh
ExecStop=/home/tongweb7/bin/stopserver.sh
PrivateTmp=false
# Disable service start and stop timeout logic of systemd for tongweb service.
TimeoutSec=0
[Install]
WantedBy=multi-user.target
注意如上方式：
1. 启动改为startservernohup.sh单实例启动，同时TongWeb7.0.4.5及之后版本有了 -Dpid_file_path=/home/tongweb7/tongweb.pid参数，于是可以设置服务的PIDFile，通过systemctl status tongweb   命令能查看该实例真实的运行状态。
2. 若需要自启动多个域，可建多个TongWeb  自启动服务，这样每个域的启动、停止、运行状态都可以分别操作。
3. 其它命令：systemctl disable tongweb  注销自启动； systemctl enable tongweb  开机自启动；journalctl -u tongweb 查看服务日志。
方式三：
在/etc/rc.d/rc.local文件中加入TongWeb的启动命令即可。rc.local要有x权限，内容如下：
#切到TongWeb用户
su - ｛TongWeb用户名｝
#设置JAVA_HOME, 设了环境变量也要设，因为这时环境变量还没生效
export JAVA_HOME=/home/jdk7
#进入tongweb目录启动
cd /home/tongweb7/bin
nohup ./startserver.sh &
#这样写脚本最简单。rc.d的目录受启动级别的影响。有的linux下不能换行写，这样写一行
su - root -c  "export JAVA_HOME=/home/jdk7 ; cd /home/tongweb7/bin ; nohup ./startserver.sh &"
注：自启动方式环境变量可能没有生效，所以需要将JAVA_HOME、LD_LIBRARY_PATH等相关环境变量写入启动脚本中。