# 原创Tongweb8命令行使用收集（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/143963162

---

文章目录
声明
对应版本
修改thanos用户密码
部署应用到默认实例
节点相关操作
新增节点(一般一个服务器ip只能装一个节点)
启动节点（需确认节点没有运行）
停止节点
删除节点
节点新增应用
节点查看应用
节点启动应用
节点停止应用
节点卸载应用（谨慎操作，卸载后应用就没有了,建议备份后操作）
实例相关操作
新增实例（需确认在哪个节点上新建）
启动实例（需确认实例没有在运行）
停止实例
删除实例
实例新增应用
实例启动应用
实例停止应用
实例卸载应用（谨慎操作，卸载后应用就没有了，建议备份后操作）
集群相关操作
创建集群（前提：创建节点且节点正常运行，节点间能正常通信，节点没有加入其他集群）
启动集群
停止集群
查看集群信息（包括集群里的节点和实例）
集群中部署应用（需保证应用都在同一个目录且集群是正常运行状态）
集群查看应用
集群启动应用
集群停止应用
集群卸载应用（谨慎操作，卸载后应用就没有了,建议备份后操作）
声明
1.命令行工具在哪里：
一般在tw8安装目录的bin目录下：commandstool.sh
备注：
1.使用该工具的时候，例如使用thanos用户的时候，会把正在登录了thanos的控制台给挤掉，导致控制台需要重新登录。（同理，jmx监控也是如此，所以不建议一起使用）
2.在tw8 里，有以下三个重要的概念：实例，节点和集群
其中一个服务器ip只能有一个节点，集群>节点>实例。
根据业务的需求不同，应用可以部署在实例里，也可以部署在节点和集群里，所以我们要弄清楚，操作的对象是哪一个，是实例，节点，还是集群，这个是在命令行工具里用到的非常重要的参数：
3.关于脚本录制
命令行页面的很多指令都可以通过脚本录制获取：
如有遇到一些本文没有记录的操作，需要使用命令行操作的，建议可以先开启脚本录制，录制相关操作后点击完成，之后下载到本地。
4. Tongweb8中的应用启动和停止，还有卸载，不建议反复执行，容易导致资源没有回收，具体参考这个：
TongWeb上反复重部署应用后异常：application instance has been stopped already 或OutOfMemoryError：Metaspace
5. 本次操作仅供参考，最终以命令行工具使用手册为准。
对应版本
Tongweb8081。
修改thanos用户密码
./commandstool.sh --host
=
192.168
.10.113 --port
=
9061
--model
=
password --username
=
thanos --password
=
Yeyehuo163.com --acceptAgreement
=
true  --action
=
update
originalPassword
=
Yeyehuo163.com
newPassword
=
Yeyehuo163.com2
confirmPassword
=
Yeyehuo163.com2
# tw8所在服务器ip
--host
=
192.168
.10.113：指定管理服务所在的服务器 IP 地址。
# 控制台端口
--port
=
9061
：用于连接管理服务的端口。
--model
=
password：操作类型指定为密码操作。
--username
=
thanos：需要更新密码的用户名。
# 当前thanos使用的密码
--password
=
Yeyehuo163.com：当前用于身份验证的用户密码。
--acceptAgreement
=
true：表示您已接受相关协议。
--action
=
update：您正在执行的是更新操作。
originalPassword
=
Yeyehuo163.com：当前有效的原始密码。
newPassword
=
Yeyehuo163.com2：新密码。
confirmPassword
=
Yeyehuo163.com2：确认新密码。
部署应用到默认实例
./commandstool.sh --host
=
192.168
.10.113 --port
=
9061
--model
=
app --action
=
add --username
=
thanos --password
=
Yeyehuo163.com2 --acceptAgreement
=
true
appFrom
=
fromServer
filename
=
/opt/Tongweb/TongWeb8.0.8.0/version8.0.8.0/examples/jmsExample.war
./commandstool.sh

这是一个脚本文件，通常用于执行一系列预定义的命令，以便与服务器进行交互。
--host
=
192.168
.10.113

指定目标服务器的 IP 地址，在这里是
192.168
.10.113。
--port
=
9061
指定服务器监听的端口号为
9061
。通常用于指定与服务交互的端口。
--model
=
app

模式设置为 app，表示这是一个应用相关的操作。
--action
=
add

指定动作为 add，表明这是一个添加或部署新的应用程序到服务器的操作。
--username
=
thanos

用于认证的用户名是 thanos。
--password
=
Yeyehuo163.com2

指定用户 thanos 用于认证的密码。
--acceptAgreement
=
true

明确同意某些相关的协议，这可能是部署或使用软件时必要的同意条款。
appFrom
=
fromServer

表示应用的来源是服务器，通常指示应用部署的来源或资源位置。
filename
=
/opt/Tongweb/TongWeb8.0.8.0/version8.0.8.0/examples/jmsExample.war

指定要添加或部署的应用程序文件的完整路径。
节点相关操作
新增节点(一般一个服务器ip只能装一个节点)
./commandstool.sh  --host
=
192.168
.10.113 --port
=
9061
--model
=
node --action
=
add --password
=
Yeyehuo163.com2 --acceptAgreement
=
true --username
=
thanos
sshPort
=
22
sshUserName
=
root
nodeCreationType
=
SSH
ip
=
192.168
.10.115
sshPassword
=
yeyehuo163
autostart
=
false
keyPairType
=
ssh-rsa
javaHome
=
/opt/bisheng-jdk-11.0.24
port
=
9061
name
=
node115
passwordType
=
PASSWORD
maxretrycount
=
0
installationPath
=
/opt/tongweb8node115
# tw8所在服务器ip
--host
=
192.168
.10.113：远程管理服务的服务器 IP。
# 控制台端口
--port
=
9061
：连接到管理服务的端口。
--model
=
node：操作的对象类型是一个节点。
--action
=
add：指定对节点执行添加操作。
--password
=
Yeyehuo163.com2：用于身份验证的密码。
--acceptAgreement
=
true：您已同意相关协议。
--username
=
thanos：执行操作的用户名。
sshPort
=
22
：SSH 连接使用的端口。
sshUserName
=
root：用于 SSH 连接的用户名。
nodeCreationType
=
SSH：节点创建类型，通过 SSH。
ip
=
192.168
.10.115：新节点的 IP 地址。
sshPassword
=
yeyehuo163：用于 SSH 的密码。
autostart
=
false：配置节点在启动时是否自动开始。
keyPairType
=
ssh-rsa：使用的密钥对类型。
javaHome
=
/opt/bisheng-jdk-11.0.24：Java 环境的安装路径。
port
=
9061
：新节点将使用的端口。
name
=
node115：节点名称。
passwordType
=
PASSWORD：密码类型指定为普通密码。
maxretrycount
=
0
：最大重试次数配置。
installationPath
=
/opt/tongweb8node115：节点的安装路径。
启动节点（需确认节点没有运行）
./commandstool.sh --host
=
192.168
.10.113 --port
=
9061
--model
=
node --action
=
start --password
=
Yeyehuo163.com2 --acceptAgreement
=
true --username
=
thanos
name
=
node115
--host
=
192.168
.10.113：目标管理服务的服务器 IP 地址。
--port
=
9061
：连接到管理服务的端口。
--model
=
node：操作的对象类型是一个节点。
--action
=
start：指定对节点执行启动操作。
--password
=
Yeyehuo163.com2：用于身份验证的密码。
--acceptAgreement
=
true：表明您已同意相关协议。
--username
=
thanos：执行操作的用户名。
name
=
node115：要启动的节点名称。
备注：如果节点已经是运行中，会有这种提示
停止节点
./commandstool.sh --host
=
192.168
.10.113 --port
=
9061
--model
=
node --action
=
stop  --password
=
Yeyehuo163.com2 --acceptAgreement
=
true --username
=
thanos
name
=
node115
# tw8所在服务器
--host
=
192.168
.10.113：目标管理服务的 IP 地址。
# 控制台端口
--port
=
9061
：连接到管理服务的端口。
--model
=
node：操作的对象类型是一个节点。
--action
=
stop：指定对节点执行停止操作。
--password
=
Yeyehuo163.com2：用于身份验证的密码。
--acceptAgreement
=
true：表示您已同意相关协议。
--username
=
thanos本停止节点 node115。以下是对命：执行操作的用户名。
name
=
node115：指定停止的节点名称是 node115。
删除节点
./commandstool.sh --host
=
192.168
.10.113 --port
=
9060
--model
=
node --action
=
delete --password
=
thanos123.com --acceptAgreement
=
true --username
=
thanos
name
=
node115
# tongweb8服务器ip
--host
=
192.168
.10.113：指定目标主机的IP地址为192.168.10.113。
#tw8控制台端口
--port
=
9060
：指定连接到目标主机的端口为9060。
--model
=
node：指定操作的模型或类型为node（节点）。
--action
=
delete：指定要执行的动作是删除（delete）。
# 改成登录控制台thanos的密码
--password
=
Yeyehuo163.com：指定连接的密码为Yeyehuo163.com。
--acceptAgreement
=
true：表示接受相关的协议或条款。
--username
=
thanos：指定用于连接的用户名为thanos。
name
=
node115：指定要操作的节点名称为node115。
节点新增应用
./commandstool.sh --host
=
192.168
.10.113 --port
=
9061
--model
=
app --action
=
add --username
=
thanos --password
=
Yeyehuo163.com2 --acceptAgreement
=
true
targetType
=
node
targetName
=
node113
appFrom
=
fromServer
filename
=
/opt/Tongweb/TongWeb8.0.8.0/version8.0.8.0/examples/examples.war
cacheMaxSize
=
1024000
--host
=
192.168
.10.113

指定目标服务器的 IP 地址，即运行应用服务器的机器。

--port
=
9061
指定服务器监听的端口，用于与服务通信。

--model
=
app

表示操作的模式为 app，即与应用程序相关。

--action
=
add

指定执行的动作为 add，这意味着当前的任务是部署新的应用程序。

--username
=
thanos 和 --password
=
Yeyehuo163.com2

提供的用户名和密码用于认证，以确保命令拥有必要的权限来操作服务器。

--acceptAgreement
=
true

表示同意相关协议或条款，这是许多工具中为操作合法性设计的参数。
targetType
=
node 和
targetName
=
node113
targetType
=
node：部署目标类型为单个节点。
targetName
=
node113：指定目标节点的名称为 node113，即部署的服务器具体节点。
appFrom
=
fromServer

指定应用的来源，这里是 fromServer，表明应用包可能已经存在于目标服务器上，而不是通过本地上传。
filename
=
/opt/Tongweb/TongWeb8.0.8.0/version8.0.8.0/examples/examples.war
cacheMaxSize
=
1024000
设置应用程序缓存的最大大小，为
1024000
（通常以字节为单位）。
这是一个可选参数，用于优化应用程序的缓存行为
节点查看应用
./commandstool.sh -host
=
192.168
.10.113 --port
=
9061
--model
=
app  --username
=
thanos --password
=
Yeyehuo163.com2  --acceptAgreement
=
true  --action
=
list
targetType
=
node
targetName
=
node113
[
root@localhost bin
]
# ./commandstool.sh -host=192.168.10.113 --port=9061 --model=app  --username=thanos --password=Yeyehuo163.com2  --acceptAgreement=true  --action=list targetType=node targetName=node1132024-11-22 16:24:14 >>> Execute the command: commandstool
{
"models"
:
[
{
"name"
:
"examples"
,
"autoDeploy"
:
"false"
,
"appFrom"
:
"fromServer"
,
"filename"
:
"\/opt\/Tongweb\/TongWeb8.0.8.0\/version8.0.8.0\/examples\/examples"
,
"appTemplate"
:
""
,
"springBootCompatible"
:
"true"
,
"contextRoot"
:
"examples"
,
"host"
:
"localhost"
,
"startupPriority"
:
"99"
,
"refRealm"
:
""
,
"dependentApp"
:
""
,
"delegateFirst"
:
"false"
,
"useEjbStandaloneLoader"
:
"false"
,
"forcedLoad"
:
"javax.ws"
,
"forcedSkip"
:
""
,
"webSocketEnabled"
:
"false"
,
"webModuleOnly"
:
"false"
,
"appImplModules"
:
""
,
"disableCDI"
:
"false"
,
"refLib"
:
""
,
"priorityJars"
:
""
,
"reloadable"
:
"false"
,
"addWebinfClassesResources"
:
"false"
,
"loadManifestClassPath"
:
"false"
,
"manifestClassPathBase"
:
""
,
"absoluteOrdering"
:
"false"
,
"customClassLoader"
:
""
,
"customClass"
:
""
,
"docBases"
:
""
,
"archiveIndexStrategy"
:
"BLOOM"
,
"sessionCookieName"
:
""
,
"useLegacyCookieProcessor"
:
"false"
,
"allowEqualsInValue"
:
"false"
,
"allowHttpSepsInV0"
:
"false"
,
"useHttpOnly"
:
"true"
,
"sameSiteCookies"
:
"Unset"
,
"maxActiveSessions"
:
"100000"
,
"sessionTimeout"
:
"30"
,
"refSessionHa"
:
""
,
"jspDevelopment"
:
"false"
,
"mappedFile"
:
"false"
,
"quoteAttributeEL"
:
"true"
,
"strictQuoteEscaping"
:
"true"
,
"strictWhiteSpace"
:
"true"
,
"enablePooling"
:
"true"
,
"jspPrecompile"
:
"false"
,
"jspPrecompileThreadCount"
:
"4"
,
"requestCharacterEncoding"
:
"UTF-8"
,
"responseCharacterEncoding"
:
"UTF-8"
,
"javaEncoding"
:
"UTF-8"
,
"fileEncoding"
:
"UTF-8"
,
"slowThreadEnabled"
:
"false"
,
"threshold"
:
"60"
,
"interruptThreadThreshold"
:
"0"
,
"cachingAllowed"
:
"true"
,
"cacheMaxSize"
:
"1024000"
,
"cacheObjectMaxSize"
:
"1024"
,
"cacheTtl"
:
"60"
,
"forceCache"
:
"false"
,
"preloadResource"
:
"false"
,
"preCompress"
:
"false"
,
"forcedContainerHandling"
:
"false"
,
"staticUrlPatterns"
:
""
,
"brEnabled"
:
"false"
,
"enableCORSAccess"
:
"false"
,
"corsAllowedOrigins"
:
""
,
"corsAllowedMethods"
:
"GET,POST,HEAD,OPTIONS"
,
"corsAllowedHeaders"
:
"Origin,Accept,X-Requested-With,Content-Type,Access-Control-Request-Method,Access-Control-Request-Headers"
,
"corsExposedHeaders"
:
""
,
"corsSupportCredentials"
:
"false"
,
"corsPreflightMaxAge"
:
"1800"
,
"requestParametersLostValidation"
:
"false"
,
"XSSFilterEnabled"
:
"false"
,
"csrfPrevention"
:
"false"
,
"csrfCacheSize"
:
"20"
,
"tokenValidTimes"
:
"1"
,
"csrfEntryPoints"
:
"\/login"
,
"httpHeaderToken"
:
"false"
,
"secretLevel"
:
""
,
"threadPoolPolicy"
:
"1"
,
"threadPool"
:
""
,
"threadPoolTimeout"
:
"30000"
,
"taskRule"
:
""
,
"exclusionRule"
:
""
,
"otherThreadPool"
:
""
,
"otherThreadPoolTimeout"
:
"30000"
,
"semaphoreEnabled"
:
"false"
,
"concurrency"
:
"10"
,
"block"
:
"true"
,
"interruptible"
:
"true"
,
"restrictedPorts"
:
""
,
"crossContext"
:
"false"
,
"unloadDelay"
:
"20"
,
"allowLinking"
:
"false"
,
"clearReferences"
:
"false"
,
"shtmlEnabled"
:
"false"
,
"virtualWebappRelative"
:
"false"
,
"allowExec"
:
"false"
,
"expires"
:
"0"
,
"urlPatterns"
:
"*.shtml"
,
"webAppVersion"
:
""
,
"useRelativeRedirects"
:
"true"
,
"allowCasualMultipartParsing"
:
"false"
,
"allowOverrideContentType"
:
"false"
,
"enableStatelessPoolMonitor"
:
"false"
,
"type"
:
"war"
,
"state"
:
"STARTED"
,
"jarScannerImpl"
:
""
,
"raPros"
:
""
,
"pkgCompatible"
:
"false"
}
]
,
"attachments"
:
{
"totalSize"
:
"1"
,
"pageNum"
:
"1"
,
"pageSize"
:
"10"
}
,
"success"
:
"true"
,
"msg"
:
"应用列表成功"
,
"redirectURL"
:
""
,
"dataTime"
:
""
}
--host
=
192.168
.10.113

指定目标服务器的 IP 地址，命令将作用于此服务器上。

--port
=
9061
服务器监听的端口号, 用于工具与服务器之间的通信。

--model
=
app

操作对象为应用程序，表明该命令属于应用程序管理任务。

--username
=
thanos 和 --password
=
Yeyehuo163.com2

登录信息，用以验证用户权限的合法性。

--acceptAgreement
=
true

确认接受协议条款，这是运行命令前的必要条件。

--action
=
list

指定操作为列出当前节点上的应用程序，而非删除或其他管理操作。
targetType
=
node 和
targetName
=
node113
targetType
=
node：目标为某个特定节点，兴趣集中在节点级部署的应用程序。
targetName
=
node113：该节点的名称为 node113，这是正在查询哪个节点的具体说明。
节点启动应用
./commandstool.sh  --host
=
192.168
.10.113 --port
=
9060
--model
=
app --action
=
start --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
targetName
=
node10
name
=
examples
targetType
=
node
--host
=
192.168
.10.113:

目标服务器的 IP 地址，用于连接操作。
--port
=
9060
:

目标服务器的端口，指定应用管理接口。
--model
=
app:

指定操作的模块为 app，表示对应用进行管理操作。
--action
=
start:

操作类型为 start，表示要启动应用或服务。
--password
=
Yeyehuo163.com:

用于身份验证的密码。应注意这类信息的安全管理，避免硬编码。
--acceptAgreement
=
true:

指定已同意相关使用协议，通常用于许可条款。
--username
=
thanos:

执行操作的用户名，确保具有相应权限。
targetName
=
node10:

要操作的具体节点名称。此处为 node10。
name
=
examples:

需要启动的应用或服务名称。此处为 examples。
targetType
=
node:

指定目标类型为 node，即该操作针对具体的节点。
节点停止应用
./commandstool.sh  --host
=
192.168
.10.113 --port
=
9060
--model
=
app --action
=
stop --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
targetName
=
node10
name
=
examples
targetType
=
node
--host
=
192.168
.10.113:

目标服务器的 IP 地址，用于连接操作。
--port
=
9060
:

目标服务器的端口，指定应用管理接口。
--model
=
app:

指定操作的模块为 app，表示对应用进行管理操作。
--action
=
stop:

操作类型为 stop，表示要停止的应用或服务。
--password
=
Yeyehuo163.com:

用于身份验证的密码。应注意这类信息的安全管理，避免硬编码。
--acceptAgreement
=
true:

指定已同意相关使用协议，通常用于许可条款。
--username
=
thanos:

执行操作的用户名，确保具有相应权限。
targetName
=
node10:

要操作的具体节点名称。此处为 node10。
name
=
examples:

需要启动的应用或服务名称。此处为 examples。
targetType
=
node:

指定目标类型为 node，即该操作针对具体的节点。
节点卸载应用（谨慎操作，卸载后应用就没有了,建议备份后操作）
./commandstool.sh -host
=
192.168
.10.113 --port
=
9061
--model
=
app --username
=
thanos --password
=
Yeyehuo163.com2 --acceptAgreement
=
true  --action
=
delete
targetType
=
node
targetName
=
node113
name
=
examples
--host
=
192.168
.10.113

指定目标服务器的 IP 地址，表示运行应用服务器的机器。

--port
=
9061
服务器用于接收工具请求的监听端口。

--model
=
app

操作的对象为应用程序，强调这次操作的中心是应用管理。

--username
=
thanos 和 --password
=
Yeyehuo163.com2

提供合法的认证凭据，以确保有权限在服务器上执行这些操作。

--acceptAgreement
=
true

确认接受了与操作相关的协议或条款，为合规性而设。

--action
=
delete

指定执行的操作是删除一个应用程序。
targetType
=
node 和
targetName
=
node113
targetType
=
node：表明目标是一个节点级别的操作。
targetName
=
node113：指定目标节点，即从 node113 节点上删除应用程序。
name
=
examples

指定要删除的应用程序名称为 examples
实例相关操作
新增实例（需确认在哪个节点上新建）
./commandstool.sh --host
=
192.168
.10.113 --port
=
9061
--model
=
instance --action
=
add --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
node
=
default
needConsolePort
=
true
name
=
testexamples002
startwithnode
=
false
appPort
=
8091
maxretrycount
=
0
installationPath
=
/opt/testexamples002
autostart
=
false
#这里我指定的是tongweb8控制台所在的服务器ip
--host
=
192.168
.10.113：指定目标主机的 IP 地址为
192.168
.10.113。
#这里的9061是我的tongweb8控制台的端口
--port
=
9061
：指定与目标服务交互的端口为
9061
。
--model
=
instance：指明操作的对象为一个实例。
--action
=
add：执行的操作是添加一个新的实例。
#这个password是我修改的thanos账户的密码
--password
=
Yeyehuo163.com：设置实例的相关密码为 Yeyehuo163.com。
--acceptAgreement
=
true：表示接受协议条款。
--username
=
thanos：指定使用的用户名为 thanos。
#这里使用的是tw自带的节点
node
=
default：使用的节点是 default。
needConsolePort
=
true：明确表示需要一个控制台端口。
name
=
testexamples002：设置实例名称为 testexamples002。
startwithnode
=
false：实例不会随节点一起启动。
appPort
=
8091
：应用程序使用端口
8091
。
maxretrycount
=
0
：设置最大重试次数为
0
。
installationPath
=
/opt/testexamples002：指定实例的安装路径为 /opt/testexamples002。
autostart
=
false：实例不会自动启动。
启动实例（需确认实例没有在运行）
./commandstool.sh  --host
=
192.168
.10.113 --port
=
9061
--model
=
instance --action
=
start --password
=
Yeyehuo163.com2 --acceptAgreement
=
true --username
=
thanos
name
=
testexamples001
# tw8所在服务器ip
--host
=
192.168
.10.113：目标管理服务的服务器 IP 地址。
# 控制台端口
--port
=
9061
：连接到管理服务的端口。
--model
=
instance：操作的对象类型是一个实例。
--action
=
start：指定对实例执行启动操作。
--password
=
Yeyehuo163.com2：用于身份验证的密码。
--acceptAgreement
=
true：表示您已同意相关协议。
--username
=
thanos：执行操作的用户名。
name
=
testexamples001：要启动的实例的名称。
停止实例
./commandstool.sh  --host
=
192.168
.10.113 --port
=
9061
--model
=
instance --action
=
stop --password
=
Yeyehuo163.com2 --acceptAgreement
=
true --username
=
thanos
name
=
testexamples001
--host
=
192.168
.10.113：目标管理服务的 IP 地址。
--port
=
9061
：用于连接管理服务的端口号。
--model
=
instance：表明操作的目标类型是实例（instance）。
--action
=
stop：指定对实例执行停止操作。
--password
=
Yeyehuo163.com2：身份验证使用的密码。
--acceptAgreement
=
true：表明已同意相关协议，允许操作继续。
--username
=
thanos：执行操作的用户名。
name
=
testexamples001：需要停止的实例名称。
备注：如果已停止的时候执行，会有以下提示
删除实例
./commandstool.sh --host
=
192.168
.10.113 --port
=
9060
--model
=
instance --action
=
delete --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
name
=
testinstance001
实例新增应用
./commandstool.sh --host
=
192.168
.10.113 --port
=
9061
--model
=
app --action
=
add --username
=
thanos --password
=
Yeyehuo163.com2 --acceptAgreement
=
true
targetType
=
instance
targetName
=
testexamples002
appFrom
=
fromServer
filename
=
/opt/Tongweb/TongWeb8.0.8.0/version8.0.8.0/examples/webServiceExample.war
contextRoot
=
/
--host
=
192.168
.10.113

目标服务器的 IP 地址，用于指定部署目标的机器。

--port
=
9061
服务器的监听端口，负责接收该工具的请求。

--model
=
app

操作对象为应用程序，强调此次操作是与应用有关。

--action
=
add

执行的动作是添加一个新应用，意味着会将指定的 WAR 包部署到服务器上。

--username
=
thanos 和 --password
=
Yeyehuo163.com2

提供访问服务器所需的认证信息，以确保具有进行此操作的权限。

--acceptAgreement
=
true

确认接受了与这些操作相关的协议或条款，这通常是必要的法律合规措施。
targetType
=
instance 和
targetName
=
testexamples002
targetType
=
instance：目标类型为实例级别的部署。
targetName
=
testexamples002：指定目标实例的名称为 testexamples002，表明应用部署的具体实例。
appFrom
=
fromServer

指定应用源为 fromServer，这通常表示应用程序包已经存在于目标服务器上，而不需要从本地上传。
filename
=
/opt/Tongweb/TongWeb8.0.8.0/version8.0.8.0/examples/webServiceExample.war

指定要部署的应用程序文件，此处为 webServiceExample.war
contextRoot
=
/
指定应用程序的上下文根为 /，意味着该应用将会成为默认应用程序，直接通过根路径访问
实例启动应用
./commandstool.sh  --host
=
192.168
.10.113 --port
=
9060
--model
=
app --action
=
start --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
targetName
=
testinstance10
name
=
examples
targetType
=
instance
--host
=
192.168
.10.113:

目标服务器的 IP 地址，用于连接操作。
--port
=
9060
:

目标服务器的端口，指定应用管理接口。
--model
=
app:

指定操作的模块为 app，表示对应用进行管理操作。
--action
=
start:

操作类型为 start，表示要启动应用或服务。
--password
=
Yeyehuo163.com:

用于身份验证的密码。应注意这类信息的安全管理，避免硬编码。
--acceptAgreement
=
true:

指定已同意相关使用协议，通常用于许可条款。
--username
=
thanos:

执行操作的用户名，确保具有相应权限。
targetName
=
testinstance10:

要操作的具体实例名称。此处为 testinstance10。
name
=
examples:

需要启动的应用或服务名称。此处为 examples。
targetType
=
instance:

指定目标类型为 instance，即该操作针对具体的实例。
实例停止应用
./commandstool.sh  --host
=
192.168
.10.113 --port
=
9060
--model
=
app --action
=
stop --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
targetName
=
testinstance10
name
=
examples
targetType
=
instance
--host
=
192.168
.10.113:

目标服务器的 IP 地址，用于连接操作。
--port
=
9060
:

目标服务器的端口，指定应用管理接口。
--model
=
app:

指定操作的模块为 app，表示对应用进行管理操作。
--action
=
stop:

操作类型为 stop，表示要停止应用或服务。
--password
=
Yeyehuo163.com:

用于身份验证的密码。应注意这类信息的安全管理，避免硬编码。
--acceptAgreement
=
true:

指定已同意相关使用协议，通常用于许可条款。
--username
=
thanos:

执行操作的用户名，确保具有相应权限。
targetName
=
testinstance10:

要操作的具体实例名称。此处为 testinstance10。
name
=
examples:

需要启动的应用或服务名称。此处为 examples。
targetType
=
instance:

指定目标类型为 instance，即该操作针对具体的实例。
实例卸载应用（谨慎操作，卸载后应用就没有了，建议备份后操作）
./commandstool.sh -host
=
192.168
.10.113 --port
=
9061
--model
=
app --username
=
thanos --password
=
Yeyehuo163.com2 --acceptAgreement
=
true  --action
=
delete
targetType
=
instance
targetName
=
testexamples002
name
=
examples
-host
=
192.168
.10.113

目标服务器的 IP 地址，表示运行应用服务器的机器。

--port
=
9061
工具请求所连接的服务器端口，用于接收并处理命令。

--model
=
app

操作的对象是应用程序，表明此次操作是针对某个应用进行管理。

--username
=
thanos 和 --password
=
Yeyehuo163.com2

提供认证信息，以确保用户拥有执行该操作的权限。

--acceptAgreement
=
true

表示接受与操作相关的条款或协议，这通常是为了遵守软件使用规定。

--action
=
delete

执行的操作是删除用于移除指定的应用程序。
targetType
=
instance 和
targetName
=
testexamples002
targetType
=
instance：表明目标为一个具体的应用程序实例。
targetName
=
testexamples002：指定应用程序从哪个实例中删除，这里是 testexamples002。
name
=
examples

要删除的应用程序的名称为 examples
集群相关操作
创建集群（前提：创建节点且节点正常运行，节点间能正常通信，节点没有加入其他集群）
./commandstool.sh --host
=
192.168
.10.113 --port
=
9061
--model
=
cluster --action
=
add --password
=
Yeyehuo163.com2  --acceptAgreement
=
true --username
=
thanos
node
=
node113,node114,node115
autoUpdateLbConf
=
true
name
=
clustertest01
startwithnode
=
false
maxretrycount
=
0
autostart
=
false
rollingUpdate
=
false
--host
=
192.168
.10.113 和 --port
=
9061
指定目标服务器的 IP 和端口，用于连接到管理服务器。

--model
=
cluster

表明操作是基于集群的管理任务。

--action
=
add

指定操作为添加，意味着将节点加入到指定的集群中。

--username
=
thanos 和 --password
=
Yeyehuo163.com2

提供用于身份验证的用户名和密码，确保权限符合要求。

--acceptAgreement
=
true
node
=
node113,node114,node115

列出要添加到集群的节点列表，这里包括 node113、node114 和 node115。
name
=
clustertest01

指定目标集群的名称为 clustertest01，将这些节点加入此集群。
autoUpdateLbConf
=
true

指定在操作后自动更新负载均衡配置，这有助于确保集群的流量分发功能立即反映新增节点。
startwithnode
=
false

指定新增节点是否自动启动服务：
false
表示不自动启动，可能需要后续手动操作启动。
maxretrycount
=
0
表明对失败的操作不重试，0 意味着没有最大重试次数。
autostart
=
false

新增节点加入集群后是否自动启动集群：
false
表示不会自动启动。
rollingUpdate
=
false

是否进行滚动更新：
false
表示不会逐个节点滚动更新，可能用于一次性添加多个节点。
备注：
1.不要把已经加入到其他集群的节点加入到新建的集群，一般推荐最好一个节点加入一个集群即可，否则很容易出现各种问题。
2.本次示范新建的集群并没有负载均衡功能，需要负载均衡功能的，建议使用Tonghttpserver。
启动集群
./commandstool.sh --host
=
192.168
.10.113 --port
=
9060
--model
=
cluster --action
=
start  --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
name
=
clustertest01
--host
=
192.168
.10.113：目标主机的 IP 地址为
192.168
.10.113。
--port
=
9060
：指定连接到目标主机的端口为
9060
。
--model
=
cluster：指定操作的模型或类型为 cluster（集群）。
--action
=
start：表示要执行的动作是启动（start）。
--password
=
Yeyehuo163.com：指定连接的密码为 Yeyehuo163.com。
--acceptAgreement
=
true：表示接受相关协议或条款。
--username
=
thanos：指定用于连接的用户名为 thanos。
name
=
clustertest01：指定要操作的集群名称为 clustertest01
停止集群
./commandstool.sh --host
=
192.168
.10.113 --port
=
9060
--model
=
cluster --action
=
stop  --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
name
=
clustertest01
--host
=
192.168
.10.113：目标主机的 IP 地址是
192.168
.10.113。
--port
=
9060
：连接到目标主机所用的端口为
9060
。
--model
=
cluster：表示操作对象的类型为 cluster（集群）。
--action
=
stop：指要执行的动作是停止（stop）。
--password
=
Yeyehuo163.com：用于连接的凭证密码为 Yeyehuo163.com。
--acceptAgreement
=
true：表示用户已接受必要的协议或条款。
--username
=
thanos：用于连接的用户名为 thanos。
name
=
clustertest01：指定要操作的集群名称为 clustertest01。
查看集群信息（包括集群里的节点和实例）
./commandstool.sh -host
=
192.168
.10.113 --port
=
9061
--model
=
cluster  --username
=
thanos --password
=
Yeyehuo163.com2  --acceptAgreement
=
true  --action
=
list
targetType
=
cluster
targetName
=
cluster
--host
=
192.168
.10.113

指定目标服务器的 IP 地址，这里是与哪台服务器进行通信的具体 IP。

--port
=
9061
服务器监听的端口号，工具通过该端口与服务器通讯。

--model
=
cluster

表示当前操作涉及的对象是集群。

--username
=
thanos 和 --password
=
Yeyehuo163.com2

用于用户身份验证的信息，确保具备执行此操作的权限。

--acceptAgreement
=
true

需要明确接受使用协议才能执行此命令。
--action
=
list

指定的操作为列出，即查询集群信息的操作。
targetType
=
cluster

目标类型为集群，表明要列出与集群相关的内容。
targetName
=
cluster

这是要查询的具体集群名称（或全局标识符），用于指定在哪个集群上执行操作。
集群中部署应用（需保证应用都在同一个目录且集群是正常运行状态）
需保证应用都在不同服务器的同一个目录之下，不然很容易出各种问题。
./commandstool.sh --host
=
192.168
.10.113 --port
=
9060
--model
=
app --action
=
add --username
=
thanos --password
=
Yeyehuo163.com --acceptAgreement
=
true
targetType
=
cluster
targetName
=
clustertest01
appFrom
=
fromServer
filename
=
/opt/examples.war
cacheMaxSize
=
1024000
contextRoot
=
/
# tw8服务器ip
--host
=
192.168
.10.113：目标主机的 IP 地址是
192.168
.10.113。
# 控制台端口
--port
=
9060
：连接目标主机使用的端口号为
9060
。
--model
=
app：操作的模型为 app，即应用。
--action
=
add：执行的动作是添加（add）。
--username
=
thanos：用于连接的用户名为 thanos。
--password
=
Yeyehuo163.com：用于连接的密码为 Yeyehuo163.com。
--acceptAgreement
=
true：表示用户已接受必要的协议或条款。
targetType
=
cluster：目标类型为集群。
targetName
=
clustertest01：目标集群的名称为 clustertest01。
appFrom
=
fromServer：表示应用来源是服务器（fromServer）。
filename
=
/opt/examples.war：应用的文件路径为 /opt/examples.war。
cacheMaxSize
=
1024000
：指定缓存的最大大小为
1,024
,000（单位可能是字节，需根据系统文档确认）。
contextRoot
=
/：应用的部署路径为根路径 /
集群查看应用
./commandstool.sh -host
=
192.168
.10.113 --port
=
9060
--model
=
app  --username
=
thanos --password
=
Yeyehuo163.com  --acceptAgreement
=
true  --action
=
list
targetType
=
cluster
targetName
=
clustertest01
-host
=
192.168
.10.113：指定目标服务器的 IP地址为
192.168
.10.113。
--port
=
9060
：指定连接到目标服务器的端口号为
9060
。
--model
=
app：操作的对象类型是应用程序。
--username
=
thanos：用于认证的用户名为 thanos。
--password
=
Yeyehuo163.com：用于认证的密码。
--acceptAgreement
=
true：确认接受协议或条款。
--action
=
list：指定动作为列出当前已经部署的应用程序。
targetType
=
cluster：指定目标的类型是集群。
targetName
=
clustertest01：指定目标集群的名称为 clustertest01。
输出信息解析：
应用信息：
"name"
:
"examples"
：应用名称是 examples。
"autoDeploy"
:
"false"
：自动部署选项被禁用。
"appFrom"
:
"fromServer"
：应用来自服务器。
"filename"
:
"\/opt\/examples"
：应用文件的路径。
"springBootCompatible"
:
"true"
：应用与Spring Boot兼容。
"contextRoot"
:
"\/"
：应用部署在根路径（即 /）。
部署与启动：
"host"
:
"localhost"
：运行应用的主机为 localhost。
"startupPriority"
:
"99"
：启动优先级为99。
缓存配置：
"cacheMaxSize"
:
"1024000"
：缓存的最大大小为
1,024
,000。
"cacheObjectMaxSize"
:
"1024"
：单个缓存对象的最大大小为
1,024
。
"cacheTtl"
:
"60"
：缓存存活时间为
60
秒。
CORS设置：
"enableCORSAccess"
:
"false"
：CORS访问未启用。
"corsAllowedMethods"
:
"GET,POST,HEAD,OPTIONS"
：允许的HTTP方法。
状态信息：
"type"
:
"war"
：应用的类型是 WAR 文件。
"state"
:
"STARTED"
：应用当前的状态为已启动。
输出元数据：
"success"
:
"true"
：操作成功。
"msg"
:
"应用列表成功"
：操作成功的信息提示。
"attachments"
：分页相关信息，这表示当前返回的应用列表的大小与分页情况
集群启动应用
./commandstool.sh  --host
=
192.168
.10.113 --port
=
9060
--model
=
app --action
=
start --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
targetName
=
clustertest01
name
=
examples
targetType
=
cluster
--host
=
192.168
.10.113:

指定目标服务器的 IP 地址，工具将连接到此主机。
IP 地址
192.168
.10.113 是本地网络中的服务器。
--port
=
9060
:

指定目标服务器的端口号，工具将在此端口上与服务器通信。
--model
=
app:

模块名称，表示此次操作针对的模块为 app。
app 可能是某种服务、应用或组件的逻辑名称。
--action
=
start:

操作名称，此处表示执行“启动”操作。
start 可能是启动应用或服务的指令。
--password
=
Yeyehuo163.com:

用户的密码，通常用于身份验证。
注意：在实际场景中，建议避免直接在命令行中明文写密码，以免泄露。可以改用配置文件或环境变量。
--acceptAgreement
=
true:

表示接受某种协议或条款，一般用于软件许可协议的确认。
--username
=
thanos:

用户名，表示执行此次操作的用户是 thanos。
targetName
=
clustertest01:

目标名称，此处为集群的名称 clustertest01。
可能表示操作的对象是一个特定的集群实例。
name
=
examples:

应用或服务的名称，此处为 examples。
具体可能是部署的某个应用程序名称或服务实例的标识。
targetType
=
cluster:

目标类型，此处指定目标为 cluster（集群）。
表示这次操作针对的是集群类型的目标，而非单独的节点。
输出内容分析：
Application Model Details

name: examples
应用程序的名称。
autoDeploy:
"false"
是否允许自动部署。
appFrom:
"fromServer"
应用程序的来源，也许是从服务器获取的。
filename:
"/opt/examples"
部署的应用程序文件路径。
springBootCompatible:
"true"
该应用是否兼容Spring Boot。
contextRoot:
"/"
应用的上下文根，通常在Web服务器中用于定义应用的访问路径。
host:
"localhost"
主机，这里指应用服务运行的主机。
startupPriority:
"99"
启动优先级。
其余字段大多数是应用程序的特性配置，涉及类加载、缓存、编码、CORS 配置、线程池等与应用服务部署相关的细节。
Configuration Options

虽然其中许多选项是布尔值（true或false）和数值配置，但这些都用于控制应用程序的各个方面，如是否启用Web Socket，HTTP cookie的相关配置，是否启用CORS访问等。
archiveIndexStrategy, cacheMaxSize, sessionTimeout,等参数决定了如何处理应用内部的资源管理和计算。
Operational Result

success:
"true"
表明操作执行成功。
msg:
"应用启动成功"
具体的操作结果信息，这里表示应用程序成功启动。
Unused Fields

attachments, redirectURL, dataTime 在此JSON响应中是空或未被使用变量，可能在其他上下文中有用。
集群停止应用
./commandstool.sh  --host
=
192.168
.10.113 --port
=
9060
--model
=
app --action
=
stop --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
targetName
=
clustertest01
name
=
examples
targetType
=
cluster
--host
=
192.168
.10.113:

目标服务器的 IP 地址。
用于指示在哪里连接进行操作。
--port
=
9060
:

目标服务器的端口号。
--model
=
app:

指明所涉及的模块是 app，可能是对此模块的管理操作。
--action
=
stop:

这次执行“停止”操作，表示要停止运行的应用或服务。
--password
=
Yeyehuo163.com:

用于身份验证的密码。
实际应用中推荐使用更安全的方式管理密码。
--acceptAgreement
=
true:

是否接受协议，一般是许可协议确认。
--username
=
thanos:

用于操作的用户名。
targetName
=
clustertest01:

目标对象的名称，这里是一个叫 clustertest01 的集群。
name
=
examples:

要进行操作的应用或服务的名称。
targetType
=
cluster:

指定目标类型为 cluster（集群）。
集群卸载应用（谨慎操作，卸载后应用就没有了,建议备份后操作）
./commandstool.sh  --host
=
192.168
.10.113 --port
=
9060
--model
=
app --action
=
delete --password
=
Yeyehuo163.com --acceptAgreement
=
true --username
=
thanos
targetName
=
clustertest01
name
=
examples
targetType
=
cluster
--host
=
192.168
.10.113:

目标主机的 IP 地址，表示操作的目标服务器。
--port
=
9060
:

目标服务器的端口号。
--model
=
app:

指定操作的模型是 app，即对应用进行管理操作。
--action
=
delete:

操作类型是 delete，表示删除应用或服务。
--password
=
Yeyehuo163.com:

用于身份验证的密码。需要确保密码管理的安全性。
--acceptAgreement
=
true:

表示已经接受了操作协议，通常这是一个许可协议。
--username
=
thanos:

用于执行操作的用户名。
targetName
=
clustertest01:

目标对象名称，这里是 clustertest01，可能是一个集群的名称。
name
=
examples:

要删除的应用或服务名称，examples 是该应用的名称。
targetType
=
cluster:

指定目标类型为 cluster，即该操作是对集群进行管理