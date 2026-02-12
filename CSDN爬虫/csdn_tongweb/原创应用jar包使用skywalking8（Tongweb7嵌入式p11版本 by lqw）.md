# 原创应用jar包使用skywalking8（Tongweb7嵌入式p11版本 by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/143706049

---

文章目录
声明
linux使用skywalking
安装包下载
Elasticsearch安装
Skywalking 安装
Skywalking 如何使用Agent探针
window本地使用skywalking
声明
1.安装参考：
SkyWalking 部署（包含ES
2.首先安装一定要根据本帖所建议的版本进行安装和测试，不然会有各种莫名的报错（帖主已经踩了好几个不同版本的坑了，尤其是skywalking跟es之间的版本，有哪个没适配上，报错在网上还不好搜解决方案）。
另外，agent探针部分，示范版本不要用skywalking APM下自带的agent目录的agent.jar，会识别不到的！！！！会识别不到的！！！会识别不到的！！！重要的事情说三次！！！
其次，建议安装高版本一点的jdk，本次示范用的jdk为jdk11(如何安装和配置jdk，自行百度吧)。
3.应用使用了Tongweb7嵌入式p11版本的依赖。
如何使用Tongweb7嵌入式p11，参考这个帖子：
TongWeb7.0.E.6_P11嵌入式版本使用指引（by lqw）
linux使用skywalking
安装包下载
本次示范，使用版本：
1.apache-skywalking-apm-9.5.0.tar.gz（可以理解为web页面+数据收集监控部分）
下载链接：
Skywalking APM
2.apache-skywalking-java-agent-8.16.0.tgz（agent探针，可以理解为缺少这部分的话，无法把应用的监控数据传到apm上）。
下载链接：
Skywalking java agent
3.elasticsearch-8.5.3-linux-x86_64.tar.gz（es作为skywalking的数据源，这个根据自己的系统架构来选，本次示范的是x86的）。
Elasticsearch下载
如果上面的资源失效，可试试点这里：
skywalking下载链接
elasticsearch下载链接
Elasticsearch安装
elasticsearch需要自建普通用户来运行：
adduser elasticsearch
passwd
elasticsearch
新建一个目录用来放elasticsearch的安装包，例如本次示范
```bash 
mkdir -p  /opt/elasticsearch
cd /opt/elasticsearch
tar -zvxf elasticsearch-8.5.3-linux-x86_64.tar.gz
chown -R elasticsearch:elasticsearch  /opt/elasticsearch/elasticsearch-8.5.3
```
按照上述解压并修改用户组后，编译一下/opt/elasticsearch/elasticsearch-8.5.3/config/elasticsearch.yml，添加这一行：`xpack.security.enabled: false`
这里相当于是配置了不用密码，如果需要密码的话，则配置成true。
如果配成true，需自行百度一下如何配置elasticsearch的密码（有很多个用户的，例如elasticsearch用户，这里为了方便测试，所以没用配置密码的形式，因为配置后，后面的skywalking的apm上也要配置，很麻烦）
其他都不用动。
然后切换用户，启动elasticsearch，测试是否正常运行：
```bash
su elasticsearch
cd /opt/elasticsearch/elasticsearch-8.5.3/bin./elasticsearch -d
curl http://localhost:9200
```
如果有以下提示，说明elasticsearch已成功安装并运行：
没有的话，最好去看看/opt/elasticsearch/elasticsearch-8.5.3/logs下的日志文件，例如elasticsearch.log有啥报错信息。
Skywalking 安装
skywalking直接用root装就可以了。
请将skywalking下载好的两个包都丢到对应目录，例如本次示范的/opt/skywalking 下：
```bash
mkdir -p /opt/skywalking
tar -xvf apache-skywalking-apm-9.5.0.tar.gz
tar -xvf apache-skywalking-java-agent-8.16.0.tgz
```
解压完后得到这两个包：
需要配置的是apache-skywalking-apm-bin，另一个先别动。
本次示范跟参考的帖子有一些不同，没有配elasticsearch的账号密码，需要改动的地方在/opt/skywalking/apache-skywalking-apm-bin/config/application.yml里，如下图所示：
大概135行左右，配数据源为elasticsearch：
下面大概137行，配一个自定义的命名空间，例如本次示范的skywalking-index（注意默认为"",要填写在“”里面）：
如需配elasticsearch的账号密码，如下所示：
由于elasticsearch跟skywalking配在同一个虚拟机上，所以这里没改：
修改/opt/skywalking/apache-skywalking-apm-bin/webapp下的application.yml，避免端口冲突（默认端口8080）,这里改成8096。保存后启动脚本：
```bash
cd
```/opt/skywalking/apache-skywalking-apm-bin/bin
./startup.sh
```
看到如下提示后：
看看安装目录logs目录的skywalking-oap-server.log和skywalking-webapp.log里是否有报错，防火墙是否已经关闭
systemctl stop firewalld
关闭防火墙后，用http://服务器ip:8096 访问
Skywalking 如何使用Agent探针
到这一步，skywalking只是安装了大部分功能，我们还需要使用agent探针，把应用的信息传到skwalking apm上。
使用了Tongweb7嵌入式版本p11的应用，本质上就是一个打成jar包的java程序，可以使用java -jar来启动，那么在启动的时候，可以利用skwalking的agent包，实现Agent探针。
本地测试，可以使用以下两种方式来监控springboot的应用（前提是已经达成jar包，并且能用java -jar来运行，运行测试没有任何问题）。
执行如下指令：
`java -javaagent:/opt/skywalking/skywalking-agent/skywalking-agent.jar -DSW_AGENT_NAME = skywalkingtestspringboot -DSW_AGENT_COLLECTOR_BACKEND_SERVICES=192.168.10.115:11800 -jar /opt/skywalkingtestjar/skywalking_springboot.jar`
备注：
1.请根据自身的情况进行修改，尤其是修改最后的指定的springboot的应用jar包。
2.如果skywalking apm 跟skywalkingagent.jar同在一个服务器，可以用127.0.0.1，否则用skywalking apm所属服务器或者虚拟机。
3.skywalkingtestsprintboot是我自己起的名字，各位请根据自身需要进行修改和配置。
执行完这个指令后，访问你的应用(不然没法刷新数据同步到skywalking那边)
到skywalking apm的页面看看，是否已经识别到（可多次刷新）。
另外可以在/opt/skywalking/skywalking-agent/plugins下，放入tongweb的jar包（如果是springboot1.x跟2.x，直接放tongweb-plugin.jar,springboot3.x的则放tongweb-plugin-3.x.jar）
这两个包在tongweb-embed-7.0.E.6_P11.zip里
放进去后，执行以下参考指令：
java -javaagent:/opt/skywalking/skywalking-agent/skywalking-agent.jar -Dskywalking.agent.service_name
=
ruoyi-admin -Dskywalking.collector.backend_service
=
192.168
.10.115:11800 -Dserver.port
=
8997
/opt/skywalkingtestjar/ruoyi-admin.jar
备注：
请根据自身需求来配，例如agent.jar的路径，代理服务名称等。
同样也是刷新应用页面后，到skywalking的ui页面看看是否识别：
window本地使用skywalking
这个部分主要是针对开发阶段的，另外没有配置elasticsearch作为数据源，单纯是为了测试window下skywalking是否能识别到idea上部署和运行的springboot应用。
确认本地已配置了jdk：
下载apache-skywalking-apm-8.5.0.tar.gz (linux部分已经贴了下载链接，自行下载吧)，然后解压。
解压后，改一下webapp下的webapp.yml,不要用8080端口，很容易冲突。
idea上，在这里配一下启动参数：
`-javaagent:E:\skywalking\apache-skywalking-apm-8.5.0\apache-skywalking-apm-bin\agent\skywalking-agent.jar -DSW_AGENT_NAME=tongweb_getway_p11 -DWING_INSTANCE_NAME=tongwebgetway_p11_instance  -DSW_AGENT_COLLECTOR_BACKEND_SERVICES=127.0.0.1:11800`

其中skywalking-agent.jar直接用apache-skywalking-apm-8.5.0下的agent下的skywalking-agent.jar就好了，其余的根据自身需求调整。
直接用管理者身份运行apache-skywalking-apm-8.5.0这两个脚本（这样做容易看出是否有啥报错）
运行后访问localhost:你修改过的端口，看看是否有skywalking的页面：
然后运行idea上的应用（这两个键都可以，左边是启动，右边是debugger启动）：
多次刷新应用页面，然后刷新skywalking的页面，看看是否识别(没有的话看运行的skywalking的窗口里是否有报错)：