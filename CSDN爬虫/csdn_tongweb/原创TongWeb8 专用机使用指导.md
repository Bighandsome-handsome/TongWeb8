# 原创TongWeb8 专用机使用指导

> 原文地址: https://blog.csdn.net/realwangpu/article/details/133122117

---

前言
专用机要求软件以deb、rpm安装包形式提供，通过三合一安全管理工具进行安装，否则软件的可执行程序无法运行，所以TongWeb6、7版本的专用机版本遵循此原则。
TongWeb8安装使用方式
TongWeb8除可以提供deb、rpm安装包形式外，还支持以解压安装方式运行，因为TongWeb8可以不依赖启动脚本运行。步骤如下：
1. 直接通过ftp上传TongWeb8安装包，
tar -zxvf TongWeb.x.x.x.x.tar.gz 解压在某一用户目录下，并放入license.dat文件。
2. bin下启、停命令脚本是无权限运行的，这时可以通过java命令运行TongWeb。
#TongWeb8.0.6.2及之前版本需要先执行下环境变量, 之后版本不再需要
export tongweb_home=/opt/tongweb
#TongWeb启动
java -jar /opt/tongweb/bin/tongweb-launcher.jar server start domain1
#TongWeb停止
java -jar /opt/tongweb/bin/tongweb-launcher.jar server stop domain1
3. 若每次输入命令过长，可将该启、停命令写入shell脚本，该shell脚本无可执行权限，但可以以source命令运行。如：
source ./starttw.sh
starttw.sh 文件内容如：
#需要的环境变量，启动命令
export tongweb_home=/opt/tongweb
ulimit -n 65536 >/dev/null 2>&1
nohup  java -jar /opt/tongweb/bin/tongweb-launcher.jar server start domain1  &