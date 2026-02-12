# 原创因易用性导致的TongWeb使用误区

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109713734

---

误区一：
使用TongWeb企业版本，即按照《TongWeb7企业版用户手册.pdf》手册操作。
安装好TongWeb后doc目录下有手册
，TongWeb手册的正确观看顺序：
1. 最先看《TongWeb7快速使用手册.pdf》了解基本的安装、使用。
2.再看《TongWeb7用户使用手册.pdf》手册介绍的是单机console控制台。
3.TongWeb企业版本提供console和heimdall两个管理控制台，在试用、移植测试阶段采用console单机控制台即可。在配置集群、统一管理各个TongWeb节点时可用heimdall控制台。
4.《TongWeb7企业版用户手册.pdf》手册介绍的是heimdall控制台。
5. 配TongHttpServer（THS）集群请参看《TongHttpServer用户手册.pdf》。 集群在heimdall控制台配可以，纯手工配置也可以。
误区二：
在Linux下用./startserver.sh启动TongWeb，这样造成当ssh工具断开与Linux的连接后，TongWeb的进程退出。
正确使用方法：通过TongWeb  bin目录下的
./startservernohup.sh或  nohup  ./startserver.sh &
启动TongWeb，这样为后台启动。
误区三：
以nohup启动TongWeb后，bin下的nohup.out文件越来越大。
正确使用方法：在控制台关闭nohup日志输出。
误区四：
问TongWeb内存是如何管理、释放的？
正解：TongWeb是不管理JVM内存的，所有的内存控制是由JVM来管理。TongWeb所能做的是依靠 -Xms 、 -Xmx 、 -Xmn 、 -XX:MaxPermSize 、-XX:+UseConcMarkSweepGC等JVM本身参数，调整其内存大小及垃圾回收策略。JVM 虽然可自动回收内存，但并不代表程序就不用关心内存问题了。如果对象已经无用，但又一直被引用， JVM 是无法将其回收的。 垃圾回收无法清理出内存，导致内存占光，于是 OutOfMemoryError问题产生了。
注意：JVM内存并非越大越好
，很多运维人员在一出现内存问题时就拼命把内存设大，这是解决不了根本问题的，
重要的是看GC，Full GC越少性能越好。
误区五：
TongWeb怎样配置集群、负载均衡？
正解：TongWeb自身不提供负载均衡功能，是由其自带的TongHttpServer(THS)软件来实现的。另外还可以采用东方通硬件负载设备TongADC、开源的 Apache、 nginx、 Haproxy 等配置TongWeb集群。session复制是通过TongDataGrid来完成的，而不是像tomcat+redis方式。
误区六：
把应用包放在deployment下是不是就可以像tomcat 一样自动部署？
正确使用方法：TongWeb是将应用包放在autodeploy目录下，自动解压在deployment目录下的。而不像tomcat是在当前webapps目录下解压。
误区七：
更新应用文件后，在TongWeb控制台点击停止、启动后应用不更新。
正确使用方法：老版本启动、停止只是允不允许访问应用，并不会更新应用，这与weblogic功能不同，TongWeb并不会执行应用卸载，加载的流程。若要更新应用需要点击“重部署”。  自TongWeb7.0.4.5之后版本启动、停止才会真正执行卸载，加载的流程。
误区八：
专用机版本不要修改startserver.sh、stopserver.sh、conf下environment等shell文件，一旦修改就不允许执行了，只能重装TongWeb。若修改启动参数，
只能改bin下external.vmoptions文件。
在专用机下新建的domain的bin目录下启动脚本是没有可执行权限的，需要以TongWeb根目录bin下的
./startdomain.sh 域名
方式启动。
误区九：
TongWeb 的8005端口找不到，控制台找不到，tongweb.xml里也找不到。
正确使用方法：只能直接在tongweb.xml 的<server标签里增加红色信息 <server
shutdown-port="8015"
jsf="false"> ， 默认没有为8005，一般都不知道，是不是一个缺乏人性化的设计？
误区十：
安装时请把TongWeb性能调到最、最、最优 ； TongWeb能支持多大并发、需要几台服务器才能满足需求？
正解：初次安装TongWeb通常调整系统open files值、JVM内存值、线程数、数据源连接配置，做一个基础调优。这些值没有一个固定的最优值，每个应用系统软、硬件环境不同，访问量不同，优化方式就不同。任何软件都不会直接提供一个最优值，但都会提供相应的优化方法，重要的是掌握优化方法。
应用系统的性能取决于软/硬件的配置，硬件如：CPU、内存、网络带宽。软件如：操作系统、中间件、数据库、更重要的是应用系统的架构设计。评估一个应用系统的性能指标取决于软/硬件的综合能力，并不能在无任何前提条件的情况下，评估出TongWeb的需要几台服务器以及并发能力。  TongWeb可以提供一些项目上性能处理能力供参考。
这好比要去买一辆车，不能仅看发动机就判断车速的快、慢。新车也不是一开始就是最好开的，要经过一段时间的磨合期，才能达到最佳性能。
误区十一：
我们够买的TongWeb嵌入版，需要现场安装。
答复： TongWeb嵌入版为jar 文件，不需要安装。 将来是放在Spring Boot的类路径上，跟应用一起打成jar文件以java -jar的形式运行的，所以无需安装，也无需制作专用机安装包。将来也不会知道TongWeb用在了哪里。
误区十二：
应用系统慢、有异常，重启TongWeb就好了，所以是TongWeb的问题。
答复：TongWeb与应用同在一个JVM进程中共享资源，所以出问题重启TongWeb后，TongWeb与应用的资源都会清理掉并重建。 这种方式可以恢复应用，但并不表明为TongWeb问题。 正如当电脑、手机不好用时，可重启机器来解决问题，但并不能确定是哪方软、硬件造成的。
正如下日志： 应用采用开源数据源，数据源连接占满导致应用访问慢，只要重启TongWeb，应用的开源数据源就会清零，系统自然会恢复。还有诸如内存溢出等问题，只要重启TongWeb都可以解决，但并不表示内存溢出是TongWeb造成的。
```java
java.sql.SQLTransientConnectionException: DatebookHikariCP -
Connection is not available, request timed out after 30000ms.
at com.zaxxer.
hikari
.pool.HikariPool.createTimeoutException(HikariPool.java:548)
at com.zaxxer.hikari.pool.HikariPool.getConnection(HikariPool.java:186)
at com.zaxxer.hikari.pool.HikariPool.getConnection(HikariPool.java:145)
at com.zaxxer.hikari.HikariDataSource.getConnection(HikariDataSource.java:99)
at org.springframework.jdbc.datasource.DataSourceUtils.doGetConnection(DataSourceUtils.java:111)
```
误区十三：
TongWeb7数据源配置里没有我们需要的数据库类型。
答复：数据库类型只是方便后面的“数据库驱动类名”和"连接url"填写，若没有相应的数据库类型，任选一个再改动“数据库驱动类名”和"连接url"即可。 也可在applications\console\WEB-INF\classes\jdbc\data-type-config.xml中手工添加数据库类型。 以前TongWeb5版本是可以在控制台增加数据库类型的。
误区十四：
生产系统出现性能问题需要用TongAPM进行分析
答复：TongAPM只适合在测试环境下使用，因没有持久化功能，所以不能长时间跟踪记录性能日志，重启TongWeb后日志会消失。推荐一个小巧的工具：TProfiler。
误区十五：
TongWeb的共享库路径配置优先级如何？
答复：TongWeb的共享库路径配置有以下几个：
1. ${TongWeb_Base}\lib\endorsed 目录为最高优先级(优先JDK自身类)， 依赖参数：-Djava.endorsed.dirs=${JAVA_ENDORSED_DIRS}
2. ${TongWeb_Base}\lib目录，常用于存放JDBC驱动类，其它共享jar不建议放。
3. ${TongWeb_Base}\lib\classes、${TongWeb_Base}\lib\common、assets.xml对应的控制台共享库，这三处配置的优先级，以及跟war应用，ear应用/APP-INF目录的优先级、父子加载下的优先级，天知道，试试看吧。
误区十六：
TongWeb要配国密证书
答复：1.TongWeb企业版、标准版、轻量版本身不能配置国密，要通过TongHttpServer(THS)来配置国密证书。 2.   TongWeb嵌入版、容器云版可以直接配置国密证书。  国密制作工具：
GMSSL - 国密SSL实验室