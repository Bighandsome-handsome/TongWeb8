# 原创TongWeb7-绿色版安装及启动停止和控制台访问

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/134146320

---

比如安装tongweb到/opt/tongtech目录，操作如下
新建/opt/tongtech目录
拷贝tongweb绿色版安装包到/opt/tongtech目录
执行tar -xvf TongWeb7.0.4.9_M1_Enterprise_Linux.tar.gz 解压
执行 mv  TongWeb7.0.4.9_M1_Enterprise_Linux.tar.gz  tongweb7049m1  修改tongweb根目录的名称
拷贝授权文件license.dat到/opt/tongtech/tongweb7049m1目录
安装jdk并配置统环境变量JAVA_HOME和PATH到/etc/profile,譬如jdk的目录为/opt/tongtech/jdk1.8.0.144
export JAVA_HOME=/opt/tongtech/jdk1.8.0.144
export PATH=JAVAHOME/bin:JAVA_HOME/bin:JAVAH​OME/bin:PATH
配置完保存后，执行source /etc/profile生效。
如果已经安装并配置过，这一步可以忽略。
配置TongWeb自启动
```bash
cd /opt/tongtech/tongweb7049m1/bin
./installservice.sh
# 启动tongweb
cd /opt/tongtech/tongweb7049m1/bin
sh startservernohup.sh
# 查看启动日志
cd /opt/tongtech/tongweb7049m1/logs
tail -f server.log
# 出现如下截图日志，说明tongweb已经启动成功：
# 停止tongweb
# 方案1：
cd /opt/tongtech/tongweb7049m1/bin./stopserver.sh quick
# 方案2：
cd ./forcestopserver.sh
```

访问tongweb控制台
链接：http://tongweb所在服务器ip:9060/console
账号：thanos
密码: thanos123.com
初次登录需要修改密码