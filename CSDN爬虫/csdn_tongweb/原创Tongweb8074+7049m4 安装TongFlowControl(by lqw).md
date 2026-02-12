# 原创Tongweb8074+7049m4 安装TongFlowControl(by lqw)

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/141596326

---

文章目录
介绍
安裝包和説明
Tongweb8074 安装TongFlowControl
Tongweb7049m4 安装TongFlowControl
介绍
TongFlowControl是面向分布式服务架构的流量监控工具，是TongWeb基于QPS/并发数和调用关系的流量
控制功能，可在TongFlowControl控制台进行实时监控和流量策略配置。
安裝包和説明
备注：flowcontrol-console.jar的启动需要用到tongweb嵌入式的授权，相关授权请跟商务联系获取。
Tongweb8074 安装TongFlowControl
前提条件：
1.Tongweb8074已安装并能够通过页面访问控制台。
2.安装请安装步骤来，别跳步，很容易出问题。
3.生产环境建议备份好tw8的安装目录，再做操作。
首先在本地将flowcontrol-console.jar里的licese.dat 替换为有效授权。
在tw8安装目录的domains/domain1/lib下，新建/flowcontrol/client 和 /flowcontrol/service 目录并在其目录中添加所需要的jar。
将如下jar包放在“/flowcontrol/service”目录:
▪ flowcontrol-console.jar
将如下jar包放在“/flowcontrol/client”目录:
▪ flowcontrol-core.jar
▪ flowcontrol-datasource-extension.jar
▪ flowcontrol-json.jar
▪ flowcontrol-parameter-flow-control.jar
▪ flowcontrol-transport-common.jar
▪ flowcontrol-transport-simple-http.jar
▪ flowcontrol-web-servlet.jar
放入后记得检查权限。
将TongFlowControl启动脚本放入Tongweb8074安装目录的bin目录下，放入后检查一下权限：
在Tongweb8074控制台配置启动参数登录控制台 > 基础配置 > 启动参数。
配置的參數如下：
-DenableFlowcontrol
=
true
-Dcsp.flowcontrol.api.port
=
8060
-Dcsp.flowcontrol.dashboard.server
=
127.0
.0.1:8060
其中127.0.0.1可替换为服务器ip，8060端口需检查是否被其他服务占用。
配置后重启Tongweb8074然後在Tongweb8074的控制台部署 flowcontrol.war。
输入自己的flowcontrol.war的路径进行部署。
部署成功后可以点击检查是否能正常访问：
之后cd到tw8的bin目录，执行脚本：
./startflowcontrol.sh
执行后cd到Tongweb8074安装目录的/domains/domain1/logs下看看是否有这个文件：
有的説明已經有日志输出了，可以直接tail -100f nohup_flowcontrol.out 看看日志输出内容
如果有类似这种提示，说明授权过期了，需要更换授权（授权用的是嵌入式版本tongweb授权，需联系商务获取）：
有类似这种则说明启动成功
启动成功后，使用服务器ip:8060访问flowcontrol的控制台页面：
◦ 默认用户名：flowcontrol
◦ 初始密码：flowcontrol
刚进去的时候只有这些内容
登录后回到tw8的控制台，点击这里访问一下
访问后点点这两个
之后回到flowcontrol的控制台，会发现多了这些：
同理，在Tongweb8074控制台部署完其他应用后，记得点击一下相关应用的访问连接，以便flowcontrol识别到。
flowcontrol的控制台的使用，请参考002_TongWeb V8.0 用户指南_8070A01.pdf，5.2.20. TongFlowControl这一章节。
Tongweb7049m4 安装TongFlowControl
前提条件：
1.Tongweb7049m4已安装并能够通过页面访问控制台。
2.安装请安装步骤来，别跳步，很容易出问题。
3.生产环境建议备份好tw8的安装目录，再做操作。
首先在本地将flowcontrol-console.jar里的licese.dat 替换为有效授权。
由于Tongweb7049m4的目录结构跟Tongweb8074的有点不一样，所以我们需要在Tongweb7049m4的安装目录下，创建以下目录（安装目录为/opt/TongWeb7.0.4.9_M4_Enterprise_Linux/domains/作为例子）：
1./opt/TongWeb7.0.4.9_M4_Enterprise_Linux/domains/domain1/logs
2./opt/TongWeb7.0.4.9_M4_Enterprise_Linux/domains/domain1/lib/flowcontrol/client
3./opt/TongWeb7.0.4.9_M4_Enterprise_Linux/domains/domain1/lib/flowcontrol/service
将如下jar包放在“/opt/TongWeb7.0.4.9_M4_Enterprise_Linux/domains/domain1/lib/flowcontrol/service”目录:
▪ flowcontrol-console.jar
将如下jar包放在“/opt/TongWeb7.0.4.9_M4_Enterprise_Linux/domains/domain1/lib/flowcontrol/client目录:
▪ flowcontrol-core.jar
▪ flowcontrol-datasource-extension.jar
▪ flowcontrol-json.jar
▪ flowcontrol-parameter-flow-control.jar
▪ flowcontrol-transport-common.jar
▪ flowcontrol-transport-simple-http.jar
▪ flowcontrol-web-servlet.jar
放入后记得检查权限。
将TongFlowControl启动脚本放入Tongweb7049m4安装目录的bin目录下，放入后检查一下权限：
登录Tongweb7049m4的控制台，添加一下启动参数：
以下是添加的启动参数
-DenableFlowcontrol
=
true
-Dcsp.flowcontrol.api.port
=
8060
-Dcsp.flowcontrol.dashboard.server
=
127.0
.0.1:8060
其中127.0.0.1可替换为服务器ip，8060端口需检查是否被其他服务占用。
配置后重启Tongweb7049m4然後在Tongweb7049m4的控制台部署 flowcontrol.war。
部署完毕后，可以点一下http访问看看是否成功：
cd到Tongweb7049m4的bin目录，执行以下指令启动flowcontrol：
./startflowcontrol.sh
启动后看看/opt/TongWeb7.0.4.9_M4_Enterprise_Linux/domains/domain1/logs/nohup_flowcontrol.out 输出的日志
tail
-100f
nohup_flowcontrol.out
如果有类似这种提示，说明授权过期了，需要更换授权（授权用的是嵌入式版本tongweb授权，需联系商务获取）：
有类似这种则说明启动成功
启动成功后，使用服务器ip:8060访问flowcontrol的控制台页面：
◦ 默认用户名：flowcontrol
◦ 初始密码：flowcontrol
刚进去的时候只有这些内容：
点一下这两个让flowcontrol识别到
之后回到flowcontrol的控制台，会发现多了这些：
同理，在Tongweb7049m4控制台部署完其他应用后，记得点击一下相关应用的访问连接，以便flowcontrol识别到。
flowcontrol的控制台的使用，请参考002_TongWeb V8.0 用户指南_8070A01.pdf，5.2.20. TongFlowControl这一章节。