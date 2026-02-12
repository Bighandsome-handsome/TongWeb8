# 原创TongWeb安装问题

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109540961

---

在Linux下字符界面安装TongWeb，执行 ./Install_TW7.0.4.1_Enterprise_Linux.bin -i console  仍报错如下：
=======================================================
Installer User Interface Mode Not Supported    或如图中文
Unable to load and to prepare the installer in console or silent mode.
=======================================================
根本原因是缺少Xorg补丁，为了快速安装，可采取如下办法：
解决办法一：
1.先执行 export DISPLAY= 注意是无值的
2. 再执行./InstallTongWeb.bin -i console 可解决。
解决办法二：去掉“转发X11连接到”
若以上办法都无效，则采用终极解决办法，用TW_7041_Enter_Liunx.tar.gz绿色版解压安装。
还有一种情况是操作系统默认为OpenJDK11, 运行TongWeb  bin安装程序报找不到Java虚拟机，这是因为目前bin安装程序还不支持高版本JDK，这时也可以用tar.gz解压安装，TongWeb启动运行可以支持OpenJDK11版本。