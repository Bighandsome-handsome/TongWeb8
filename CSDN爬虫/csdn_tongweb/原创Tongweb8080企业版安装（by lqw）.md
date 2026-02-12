# 原创Tongweb8080企业版安装（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/143113491

---

文章目录
安装准备
配置jdk
安装Tongweb8080企业版
关闭Tongweb
密码修改
忘记密码
安装准备
1.已配置jdk环境变量（最低jdk1.8也就是jdk8）。
2.将Tongweb8080企业版安装包和授权上传到服务器（授权联系商务获取）
3.防火墙已经关闭，或者放行8088和9060端口。
配置jdk
Tongweb8080企业版启动需要用到jdk，jdk一般有系统自带和自行解压新的jdk安装包两种形式。
系统自带的话，使用which is java 查看jdk安装目录
[
root@localhost opt
]
# which is java
/usr/bin/which: no is
in
(
/opt/bisheng-jdk-11.0.24/bin::/opt/bisheng-jdk-11.0.24/bin::/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
)
/opt/bisheng-jdk-11.0.24/bin/java
记下这个路径，待会配置要用。
輸入 java -verison 看看是否有jdk信息，沒有的話説明沒有配置jdk环境变量。
如果没有的话，推荐可以根据自己应用所需jdk版本来进行下载和解压安装（最低要求jdk1.8，也就是jdk8）。
下载推荐使用bishengjdk，链接如下：
bishengjdk下载链接
例如本文示范的時候,使用的是bisheng-jdk-11.0.24-linux-x64.tar.gz（本地测试的应用需要用到jdk11），下载好后放上去服务器，直接解压。
备注：
1.bishengjdk有分arrch和x86的安装包，可以输入lscpu查看自己的cpu架构进行选择。
无论是解压的jdk还是系统自带的jdk，都要去检查/etc/profile这个文件里是否已经配置了jdk环境变量。
没有的话，可以vi /etc/profile
#这里的jdk路径换成你的jdk路径
JAVA_HOME
=
/opt/bisheng-jdk-11.0.24
JAVA_BIN
=
$JAVA_HOME
/bin
JRE_HOME
=
$JAVA_HOME
/jre
PATH
=
$JAVA_BIN
:
$JRE_BIN
:
$PATH
export
JAVA_HOME JRE_HOME
PATH
vi后esc输入：wq保存，然后source /etc/profile,输入java -version 查看是否生效：
[
root@localhost opt
]
# source /etc/profile
[
root@localhost opt
]
# java -version
openjdk version
"11.0.24"
2024
-07-16
OpenJDK Runtime Environment BiSheng
(
build
11.0
.24+11
)
OpenJDK
64
-Bit Server VM BiSheng
(
build
11.0
.24+11, mixed mode
)
[
root@localhost opt
]
#
如果遇到系统存在多个jdk版本，且默认版本的jdk不兼容的情况下，可以在安装目录的bin目录下，新建一个JAVA_HOME的txt，里面写一下jdk的路径，如下图：
安装Tongweb8080企业版
确认jdk已经配置，且网络层面已经确保能访问9060后，解压Tongweb8080的安装包：
tar
-zvxf TongWeb8.0.8.0.tar.gz
解压后会得到一个目录(記得把license.dat也就是授权文件放进去)：
放进去后先cd 到解压目录的bin目录，执行./version.sh,看看授权是否有效：
之后先到解压目录的domains/domain1/conf目录下，找到console.xml，配置信任ip（也就是允许访问Tongweb控制台的ip）：
打个比方，部署完Tongweb8080企业版后，我想用我本地的window 的ip 进行访问，那就配这个window 的ip ：
如果是同一个网段的，则最后一位改成*：
如果是不限制的话，则直接改成*：
改完后，cd到解压目录的bin目录，执行以下指令：
./startd.sh
启动后可以使用jps 或者ps -ef |grep tongweb 看看是否存在对应进程：
如果需要查看日志，可cd 到解压目录的/domains/domain1/logs/server下，查看server.log.
之後本地win+r 輸入cmd ，輸入telnet 服务器ip 9060 进行测试（沒改的話，控制台訪問端口默認為9060）：
一般telent 成功的話，如下圖所示：
然後訪問https://服務器ip:9060/console
初次登陸，初始賬號：thanos，初始密碼：thanos123.com
相关使用手册可以在解压目录的version8.0.8.0.zip里，解压后找到docs目录：
关闭Tongweb
直接在解压目录的bin目录执行：
./forcestop.sh
或者ps -ef |grep tongweb 然后kill进程。
密码修改
忘记密码
关闭Tongweb服务（最好直接kill 进程），然后找到Tongweb安装目录domains/domain1/conf/console.xml,备份好console.xml
将丢失账户（如 “thanos” ）对应的 “changeInitPwd” 字段修改为 “true”，要求该账户登录时，必须修改初始密码，同时替换掉password的部分。
thanos初始密码为：
44D3
$2
$0B8AA118786066B2A9DF05A44B342AE2FC147F2164B5A9F232259E50DE5D9F1C
$SHA
-256
替换后重启Tongweb。