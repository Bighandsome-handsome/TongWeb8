# 原创TongWeb的license安装与替换

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109611636

---

一、TongWeb企业版简单安装与替换步骤说明
:
1. 登录TongWeb服务器，进入TongWeb目录停止TongWeb。
2. 通过FTP工具将license.dat文件覆盖原有TongWeb根目录下的license.dat。
3. 启动TongWeb即完成替换。
注意：只能叫license.dat，不能改名。
二、TongWeb嵌入版安装:
TongWeb嵌入版license可以放在jar文件类路径上，也可以配置加载路径。
方式一：
将license.dat放在tongweb-embed-7.0.E.x.jar中。
方式二：
在应用spring boot application.properties 或 者application.yaml 文件中指明license的路径。如：
server.tongweb.license.path=D:/springboot/license.dat
这样一台服务起多个TongWeb嵌入版的spring boot实例读取一份license文件即可。更新license无需像方式一重新打包。
三、TongWeb详细安装与替换步骤说明：
1. 确认TongWeb安装的目录、版本类型、二级版本号，
注意: 安全版、企业版、标准版、轻量版、嵌入版、容器云版license不通用，TongWeb6.1与TongWeb7.0的license不通用。
轻量版
标准版
企业/专用机版
安全版
嵌入版
容器云版
license的TW_Edition值
Light
Standard
Enterprise
ASDP
Embed
Cloud
license的TW_Version_Number值
7.0
7.0
7.0
7.0
7.0.E
7.0.C
2. 查看当前license到期时间及版本的三种方法。
（1）执行bin下startserver命令启动TongWeb, 通过日志查看license到期时间。
[2020-01-15 14:47:51] [INFO] [System.out] [
License expires 2020-03-18
]
[2020-01-15 14:47:54] [INFO] [core] [Starting TongWeb Server...]
（2）若bin下有version命令，可执行该命令查看。
./version.sh
服务器：
TongWeb 7.0.2.4
，构建于：2019-10-29 10:09:06
-----------------------------------------
-----------License 信息-------------------
consumer_name=test
project_name=test
license_type=release
create_date=2019-05-13
end_date=2020-05-13   #
到期时间, -1为永不过期
TW_Product_Name=TongWeb
TW_Version_Number=7.0  #
二级版本号
TW_IpAddress=127.0.0.1
TW_CPU_COUNT=1
TW_Edition=Enterprise    #企业版
(3)  登录TongWeb的管理控制台首页查看具体版本和到期时间。
3. 确认版本和到期时间后，联系东方通商务获取TongWeb产品license.dat文件。
4. 在确认重启TongWeb不影响系统的情况下，停止TongWeb。
5. 通过FTP工具将license.dat文件覆盖原有TongWeb根目录下的license.dat。
6. 启动TongWeb，按步骤2检查license是否替换成功。
说明：
license到期注意向东方通商务
申请、临时license到期后凌晨6点会停止TongWeb。
7. 替换不对导致TongWeb无法启动，具体看TongWeb的logs下server.log日志。
[System.out] [Lisence file not found!]   #
没把
license.dat
放
TongWeb
的根目录下
[System.out] [License will never expire.]   #
这是永不过期
[System.out] [License expired.]     #
这是已过期
[System.out] [License expires 2018-11-28]  #
这是过期时间
[System.out] [License is not for this version of product.]   #这是license与产品版本不对应
[System.out] [Invaild license.]    #license不合法
8. 若 license 项目名称为 test，则 http 通道最大线程数为 5，生产环境与性能测试时注意。启动TongWeb时日志有提示。
[core] [License 信息:客户名称=test;项目名称=
test
;到期时间=2020-11-17]
[Starting ProtocolHandler [http-nio2-8088]
License limits the connector to a maximum of 5 threads.
]