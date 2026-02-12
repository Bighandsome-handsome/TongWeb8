# 原创zabbix通过jmx监控Tongweb7企业版（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/137110803

---

一.tongweb配置相关启动参数
参考
Zabbix 监控 Tomcat 服务
可以在控制台页面，或者在tongweb的安装目录的bin目录下，找到external.vmoptions，进行配置：
配置内容如下：
-Dcom.sun.management.jmxremote
-Dcom.sun.management.jmxremote.ssl=false
-Dcom.sun.management.jmxremote.authenticate=false
-Dcom.sun.management.jmxremote.registry.ssl=false
-Dcom.sun.management.jmxremote.port=7201
-Djava.rmi.server.hostname=192.168.10.51
其中7201选用没有占用的端口，hostname填写服务器ip
配置后重启tongweb，然后下载cmdline-jmxclient-0.10.3.jar。
下载后，cd到cmdline-jmxclient-0.10.3.jar所在目录，执行：
java -jar cmdline-jmxclient-0.10.3.jar - 192.168.10.51:7201 java.lang:type=Memory NonHeapMemoryUsage
其中192.168.10.51:7201是在external.vmoptions里配置的ip和端口，一般配置成功的话，执行指令会有以下信息显示：
二.部署安装zabbix
参考
https://www.cnblogs.com/m-zhuang/p/17615179.html#2-%E9%83%A8%E7%BD%B2-zabbix-%E6%9C%8D%E5%8A%A1%E7%AB%AF
（1）安装 Zabbix 源
# 获取 zabbix 的下载源
rpm -ivh https://mirrors.aliyun.com/zabbix/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm 

# 更换 zabbix.repo 为阿里云
sed -i 's#http://repo.zabbix.com#https://mirrors.aliyun.com/zabbix#' /etc/yum.repos.d/zabbix.repo

# 清除yum缓存及创建缓存元数据
yum clean all && yum makecache
（2）安装 Zabbix服务端及mysql、客户端
yum -y install zabbix-server-mysql zabbix-agent

yum install zabbix-server-mysql
（3）安装SCL(Software Collections)，便于后续安装高版本的 php，默认 yum 安装的 php 版本为 5.4，版本过低，zabbix 5.0 版本对 php 版本最低要 7.2.0 版本。SCL 可以使得在同一台机器上使用多个版本的软件，而又不会影响整个系统的依赖环境。软件包会安装在 /opt/rh 目录下。
# 开启安装源
sed -i 's/enabled=0/enabled=1/' /etc/yum.repos.d/zabbix.repo

yum install -y zabbix-web-mysql-scl zabbix-apache-conf-scl
如果有下图的报错：
则根据错误提示，需要安装高版本的php，解决方法是安装 Software Collections，再去安装SCL
# yum install centos-release-scl -y
  
# yum install zabbix-web-mysql-scl zabbix-apache-conf-scl
（4）安装 zbbix 所需的数据库
yum -y install mariadb-server mariadb
systemctl enable --now mariadb

# 初始化数据数据库,并设置密码，如 123123
mysql_secure_installation
初始话数据库的时候，第一个按回车
第二个输y
输入新密码，这里用的123123，需要输入两次，然后提示成功：
由于是本地测试，剩余的一直输入n
5）添加数据库用户以及 zabbix 所需的数据库信息
# 登录数据库
mysql -u root -p123123

# 创建zabbix数据库并设置编码为utf-8
create database zabbix character set utf8 collate utf8_bin;

# 给用户赋权 
grant all on zabbix.* to 'zabbix'@'%' identified by 'zabbix';

CREATE USER 'zabbix'@'localhost' IDENTIFIED BY 'zabbix';
GRANT ALL PRIVILEGES ON zabbix.* TO 'zabbix'@'localhost';


# 刷新
flush privileges;

# 退出数据库界面
\q
6）导入数据库信息（注意查到sql文件路径后要对比和替换掉，不然会报错）
# 查询sql文件的位置
rpm -ql zabbix-server-mysql

# 导入数据库信息
zcat /usr/share/doc/zabbix-server-mysql-5.0.36/create.sql.gz | mysql -u root -p123123 zabbix
（7）修改 zabbix server 配置文件，修改数据库密码
vim /etc/zabbix/zabbix_server.conf
把注释去掉，配成下图所示：
（8）修改 zabbix 的 php 配置文件
# 找到对应的zabbix.conf文件
find / -name "zabbix.conf"
# 修改下述文件
vim /etc/opt/rh/rh-php72/php-fpm.d/zabbix.conf
# 25行，取消注释，修改时区
php_value[date.timezone] = Asia/Shanghai
（9）启动 zabbix 相关服务,然后访问服务器ip/zabbix
systemctl restart zabbix-server zabbix-agent httpd rh-php72-php-fpm
systemctl enable zabbix-server zabbix-agent httpd rh-php72-php-fpm
查看日志
cat /var/log/zabbix/zabbix_server.log
如果有下图的提示，关闭防火墙和修改SELINUX=disabled修改配置文件永久关闭（修改后需要reboot）
setenforce 0 && sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config
另外建议给对应的目录赋权
sudo chown zabbix:zabbix /var/run/zabbix 
sudo chmod 755 /var/run/zabbix
直接next
输入zabbix，然后next：
输入名称，其他别动，next
账号：Admin
密码：zabbix
切换中文：
三.部署zabbix_java_getaway和修改相关配置
安装指令：
yum -y install zabbix-java-gateway.x86_64
修改配置：
vim /etc/zabbix/zabbix_java_gateway.conf
检查是否配对zabbix_java的pid（这里用默认的）
第九行放开注释，使用默认配置：
第17行放开注释，使用默认配置：
第三十五行放开注释，使用默认配置（开启的工作线程数量）
修改配置：
vim /etc/zabbix/zabbix_server.conf
JavaGateway这里配成geteway安装的服务器ip，如下图所示：
配上javagatewayPort(建议使用默认的10052)
配StartJavaPollers=5（采集数据的进程数）
执行以下指令启动zabbix-java-gateway.service
systemctl start zabbix-java-gateway.service 
systemctl enable zabbix-java-gateway.service
四.导入模版
之后到zabbix的控制台，导入模版（模版是网上找的jvm相关模版，这个有很多，按需自己去百度下载和修改）。
之后找到要配置的主机：
点击配置
添加jmx,配上之前tongweb配的ip和端口：
选择Templates：
选择刚刚导入的模版：
等一两分钟，刷新页面，有jmx标志说明配置成功
到主机页面查看(图里的promblem请无视，是本地应用代码的问题)：