# 原创如何正确的查看TongWeb日志？

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109735179

---

当使用TongWeb时出现问题，
第一处理方式为查看TongWeb logs目录下的server.log。
注意：千万不要在控制台查看日志，排序不规则，浏览行数少，不如直接看server.log。
在出现问题时，首先要收集TongWeb日志server.log，收集规则：
1.  若是必然出现的问题则清理一下 TongWeb 日志， 重新启动 TongWeb， 运行应用后收集从 TongWeb 启动后整个server.log日志。
2.  若是偶然问题的出现， 则保留 TongWeb 从开始运行后的所有日志，
且需要注明问题出现的时间点或异常日志行数。
3.  禁止只收集一、 两句的报错信息， 要保证日志的完整性， 应该收集 TongWeb 从启动开始到出现问题时的整个日志。
4.  通常应用采用 log4j 日志输出， 保证应用的 log4j 配置正确， 让应用日志输出在TongWeb 日志中。
```bash
# log4j示例
log4j.rootLogger=INFO, CONSOLE, ROLLINGFILE
# 该控制台输出，会将应用日志输出在TongWeb的server.log中
log4j.appender
.CONSOLE=org.apache.log4j.ConsoleAppender
log4j.appender.CONSOLE.Threshold=INFO
log4j.appender.CONSOLE.layout=org.apache.log4j.PatternLayout
log4j.appender.CONSOLE.layout.ConversionPattern=%d{ISO8601} - %-5p [%t:%C{1}@%L] - %m%n
# 应用自身日志文件输出
log4j.appender.ROLLINGFILE=org.apache.log4j.RollingFileAppender
log4j.appender.ROLLINGFILE.Threshold=DEBUG
log4j.appender.ROLLINGFILE.File=app.log
```
5. 日志以文本方式查看最为方便。若条件不允许，用电脑截图要截全，用手机拍照要注意提高拍摄水平、拍正、拍清。
6. 要区分哪些是TongWeb输出的日志、哪些是应用输出的日志，server.log中systemout行表示是应用输出。
```bash
[2021-01-13 13:31:51 101] [WARNING] [http-nio2-8088-exec-4] [
systemout
] [javax.xml.soap.SOAPException: Unknown Protocol:   specified for creating MessageFactory]
```
要点：部署、运行异常看server.log日志、乱码问题分析编码，日志作用不大。
查看server.log日志主要查看应用的报错的根本原因，学会找到异常的根本原因，例如如下内容。
```bash
Caused by: javax.naming.NameNotFoundException: Name "JDBC/DPORTAL" not found.
at com.tongweb.tongejb.core.ivm.naming.IvmContext.federate(IvmContext.java:199)
at com.tongweb.tongejb.core.ivm.naming.IvmContext.lookup(IvmContext.java:151)
at com.tongweb.tongejb.core.ivm.naming.OpenejbDelegateContext.lookup(OpenejbDelegateContext.java:48)
at com.tongweb.tongejb.core.ivm.naming.ContextWrapper.lookup(ContextWrapper.java:137)
at com.tongweb.tongejb.core.OpenEJBInitialContextFactory$LocalFallbackContextWrapper.lookup(OpenEJBInitialContextFactory.java:53)
at com.tongweb.naming.SelectorContext.lookup(SelectorContext.java:163)
at com.tongweb.naming.ThanosSelectorContext.lookup(ThanosSelectorContext.java:54)
at javax.naming.InitialContext.lookup(InitialContext.java:417)
at org.springframework.jndi.JndiTemplate$1.doInContext(JndiTemplate.java:155)
at org.springframework.jndi.JndiTemplate.execute(JndiTemplate.java:88)
at org.springframework.jndi.JndiTemplate.lookup(JndiTemplate.java:153)
at org.springframework.jndi.JndiTemplate.lookup(JndiTemplate.java:178)
at org.springframework.jndi.JndiLocatorSupport.lookup(JndiLocatorSupport.java:95)
at org.springframework.jndi.JndiObjectLocator.lookup(JndiObjectLocator.java:105)
at org.springframework.jndi.JndiObjectFactoryBean.lookupWithFallback(JndiObjectFactoryBean.java:200)
at org.springframework.jndi.JndiObjectFactoryBean.afterPropertiesSet(JndiObjectFactoryBean.java:186)
at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1369)
at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1335)
... 145 more
[2020-11-16 14:41:11] [SEVERE] [core] [One or more listeners failed to start. Full details will be found in the appropriate container log file]
这里是已经失败在解部署，再看下面无意义。
[2020-11-16 14:41:11] [SEVERE] [core] [Context [dportal] startup failed due to previous errors]
[2020-11-16 14:41:11] [INFO] [core] [Closing Spring root WebApplicationContext]
[2020-11-16 14:41:11] [INFO] [deployment] [Undeploying app: /opt/TongWeb7.0/deployment/dportal]
[2020-11-16 14:41:12] [SEVERE] [web-container] [Error deploying web application directory /opt/TongWeb7.0/deployment/dportal]
java.lang.RuntimeException: Start context failed.
at com.tongweb.web.thanos.startup.ThanosHostConfig.deployWar(ThanosHostConfig.java:231)
at com.tongweb.tw.thanos.ThanosWebtierWebAppBuilder.fireTomcatProcess(ThanosWebtierWebAppBuilder.java:416)
at com.tongweb.tw.thanos.ThanosWebtierWebAppBuilder.deployApplication(ThanosWebtierWebAppBuilder.java:363)
at com.tongweb.deploy.TongWebDeployer.deploy0(TongWebDeployer.java:204)
at com.tongweb.deploy.TongWebDeployer.deploy(TongWebDeployer.java:164)
at com.tongweb.deploy.commands.DeployCommand.deploy(DeployCommand.java:269)
at com.tongweb.console.deployer.service.DeployerService.deploy(DeployerService.java:587)
at com.tongweb.console.deployer.controller.DeployerController.deploy(DeployerController.java:361)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
at java.lang.reflect.Method.invoke(Method.java:498)
at org.jboss.resteasy.core.MethodInjectorImpl.invoke(MethodInjectorImpl.java:137)
at org.jboss.resteasy.core.ResourceMethodInvoker.invokeOnTarget(ResourceMethodInvoker.java:296)
at org.jboss.resteasy.core.ResourceMethodInvoker.invoke(ResourceMethodInvoker.java:250)
at org.jboss.resteasy.core.ResourceMethodInvoker.invoke(ResourceMethodInvoker.java:237)
at org.jboss.resteasy.springmvc.ResteasyHandlerAdapter.createModelAndView(ResteasyHandlerAdapter.java:96)
at org.jboss.resteasy.springmvc.ResteasyHandlerAdapter.handle(ResteasyHandlerAdapter.java:82)
at org.jboss.resteasy.springmvc.ResteasyHandlerAdapter.handle(ResteasyHandlerAdapter.java:26)
```
如下典型的案例，应用连接nacos失败，主动关闭应用卸载。
```bash
[com.alibaba.nacos.naming.push.receiver] [systemout] [2021-01-22 17:23:07.286 ERROR 75320 --- [g.push.receiver
] com.alibaba.nacos.client.naming
: [NA] error while receiving push data
java.net.SocketException: Socket closed
at java.net.PlainDatagramSocketImpl.receive0(Native Method)
at java.net.AbstractPlainDatagramSocketImpl.receive(AbstractPlainDatagramSocketImpl.java:143)
at java.net.DatagramSocket.receive(DatagramSocket.java:812)
at com.alibaba.nacos.client.naming.core.PushReceiver.run(PushReceiver.java:83)
at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
at java.util.concurrent.FutureTask.run(FutureTask.java:266)
at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$201(ScheduledThreadPoolExecutor.java:180)
at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624)
at java.lang.Thread.run(Thread.java:748)
[2021-01-22 17:23:07.286  INFO 75320 --- [o2-9060-exec-19] com.alibaba.nacos.client.naming          : com.alibaba.nacos.client.naming.backups.FailoverReactor do shutdown stop]
[2021-01-22 17:23:07.286  INFO 75320 --- [o2-9060-exec-19] com.alibaba.nacos.client.naming          : com.alibaba.nacos.client.naming.core.HostReactor do
shutdown stop
]
[2021-01-22 17:23:07.287  INFO 75320 --- [o2-9060-exec-19] com.alibaba.nacos.client.naming          : com.alibaba.nacos.client.naming.net.NamingProxy do
shutdown begin
]
[2021-01-22 17:23:07.287  WARN 75320 --- [o2-9060-exec-19] com.alibaba.nacos.client.naming          : [NamingHttpClientManager] Start destroying NacosRestTemplate]
[2021-01-22 17:23:07.287  WARN 75320 --- [o2-9060-exec-19] com.alibaba.nacos.client.naming          : [NamingHttpClientManager] Destruction of the end]
[2021-01-22 17:23:07.321  INFO 75320 --- [o2-9060-exec-19] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence unit 'default']
[2021-01-22 17:23:07.324  INFO 75320 --- [o2-9060-exec-19] com.alibaba.druid.pool.DruidDataSource   : {dataSource-1} closing ...]
[2021-01-22 17:23:07.353  INFO 75320 --- [o2-9060-exec-19] o.s.s.concurrent.ThreadPoolTaskExecutor  : Shutting down ExecutorService 'scopedTarget.asyncExecutor']
[2021-01-22 17:23:07.394  INFO 75320 --- [o2-9060-exec-19] org.mongodb.driver.connection            : Closed connection [connectionId{localValue:2, serverValue:321}] to 192.168.0.101:27017 because the pool has been closed.]
[2021-01-22 17:23:07.396  INFO 75320 --- [o2-9060-exec-19] o.s.s.concurrent.ThreadPoolTaskExecutor  :
Shutting down ExecutorService 'scopedTarget.springSessionRedisTaskExecutor
']
[2021-01-22 17:23:07.396  INFO 75320 --- [o2-9060-exec-19] o.s.s.concurrent.ThreadPoolTaskExecutor  :
Shutting down ExecutorService 'scopedTarget.commonAsyncExecutor'
]
[2021-01-22 17:23:07.401 ERROR 75320 --- [o2-9060-exec-19] o.s.boot.SpringApplication               :
Application run failed
```
最忌讳的日志提供方式：
1. 只发一大堆日志，什么问题也不描述（产品版本，现象，影响等），也不描述出现问题时日志的行数和错误，让别人使劲猜。
2. 只发别人的聊天记录，不做总结描述，让别人看聊天记录分析问题。
3. 只发一句个人认为有问题的日志，上下不连贯，让别人无法分析。
[2020-11-30 13:27:11] [SEVERE] [data-source] [Unable to create initial connections of pool.]
4. 只截取堆栈的中间，看不到开头和结尾的caused  by， 让别人无法分析。
5. 拍照模糊不清、歪歪扭扭。在本可电脑截屏的情况下，依然用手机对着电脑拍屏。
6. 把日志粘贴到word里, 只有文本日志才最好查看。