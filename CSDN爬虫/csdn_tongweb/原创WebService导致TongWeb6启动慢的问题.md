# 原创WebService导致TongWeb6启动慢的问题

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109554166

---

问题描述：
启动TongWeb慢，通过jstack分析主线程在执行WebService扫描部署， 如下：com.tongweb.tongejb.config.WsDeployer可看出来。
解决办法：
多数情况下应用自带开源WebService组件，无需TongWeb的WebService功能，可以在启动脚本中增加-Dopenejb.webservices.enabled=false参数，不扫WebService以加快启动速度。
"main" prio=10 tid=0x00007f043c00b000 nid=0x231f runnable [0x00007f0443a63000]
java.lang.Thread.State: RUNNABLE

```java
at java.net.PlainSocketImpl.socketConnect(Native Method)
at java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:339)
- locked <0x00000007d738fc90> (a java.net.SocksSocketImpl)
at java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:200)
at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:182)
at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:392)
at java.net.Socket.connect(Socket.java:579)
at java.net.Socket.connect(Socket.java:528)
at sun.net.NetworkClient.doConnect(NetworkClient.java:180)
at sun.net.www.http.HttpClient.openServer(HttpClient.java:432)
at sun.net.www.http.HttpClient.openServer(HttpClient.java:527)
- locked <0x00000007d738fc08> (a sun.net.www.http.HttpClient)
at sun.net.www.http.HttpClient.<init>(HttpClient.java:211)
at sun.net.www.http.HttpClient.New(HttpClient.java:308)
at sun.net.www.http.HttpClient.New(HttpClient.java:326)
at sun.net.www.protocol.http.HttpURLConnection.getNewHttpClient(HttpURLConnection.java:997)
at sun.net.www.protocol.http.HttpURLConnection.plainConnect(HttpURLConnection.java:933)
at sun.net.www.protocol.http.HttpURLConnection.connect(HttpURLConnection.java:851)
at sun.net.www.protocol.http.HttpURLConnection.getInputStream(HttpURLConnection.java:1301)
- locked <0x00000007d738f220> (a sun.net.www.protocol.http.HttpURLConnection)
at java.net.URL.openStream(URL.java:1037)
at com.tongweb.tongejb.loader.IO.read(IO.java:355)
at com.tongweb.tongejb.config.ReadDescriptors.readWsdl(ReadDescriptors.java:676)
at com.tongweb.tongejb.config.WsDeployer.getWsdl(WsDeployer.java:387)
at com.tongweb.tongejb.config.WsDeployer.processPorts(WsDeployer.java:200)
at com.tongweb.tongejb.config.WsDeployer.deploy(WsDeployer.java:65)
at com.tongweb.tongejb.config.ConfigurationFactory$Chain.deploy(ConfigurationFactory.java:366)
at com.tongweb.tongejb.config.ThorConfigurationFactory.configureApplication(ThorConfigurationFactory.java:887)
at com.tongweb.twnt.thor.ThorTomcatWebAppBuilder.startInternal(ThorTomcatWebAppBuilder.java:1205)
at com.tongweb.twnt.thor.ThorTomcatWebAppBuilder.configureStart(ThorTomcatWebAppBuilder.java:1000)
at com.tongweb.twnt.thor.GlobalListenerSupport.lifecycleEvent(GlobalListenerSupport.java:118)
at com.tongweb.web.thor.util.LifecycleSupport.fireLifecycleEvent(LifecycleSupport.java:119)
at com.tongweb.web.thor.util.LifecycleBase.fireLifecycleEvent(LifecycleBase.java:90)
at com.tongweb.web.thor.core.ThorStandardContext.startInternal(ThorStandardContext.java:239)
- locked <0x00000007ee025bc0> (a com.tongweb.web.thor.core.ThorStandardContext)
at com.tongweb.web.thor.util.LifecycleBase.start(LifecycleBase.java:150)
- locked <0x00000007ee025bc0> (a com.tongweb.web.thor.core.ThorStandardContext)
at com.tongweb.web.thor.core.ContainerBase.addChildInternal(ContainerBase.java:913)
at com.tongweb.web.thor.core.ContainerBase.addChild(ContainerBase.java:889)
at com.tongweb.web.thor.core.StandardHost.addChild(StandardHost.java:618)
at com.tongweb.web.thor.core.ThorStandardHost.addChild(ThorStandardHost.java:462)
at com.tongweb.web.thor.startup.ThorHostConfig.deployWar(ThorHostConfig.java:701)
at com.tongweb.twnt.thor.ThorTomcatWebAppBuilder.fireTomcatProcess(ThorTomcatWebAppBuilder.java:2438)
at com.tongweb.twnt.thor.ThorTomcatWebAppBuilder.deployApplication(ThorTomcatWebAppBuilder.java:2378)
at com.tongweb.deploy.TongWebDeployer.deploy(TongWebDeployer.java:216)
at com.tongweb.twnt.thor.TongwebLoader.initDeploy(TongwebLoader.java:414)
at com.tongweb.twnt.thor.TongwebLoader.event(TongwebLoader.java:263)
at com.tongweb.web.thor.startup.Tomee.laststep(Tomee.java:891)
at com.tongweb.web.thor.startup.Tomee.start(Tomee.java:752)
at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
at java.lang.reflect.Method.invoke(Method.java:606)
at com.tongweb.web.thor.startup.ThorBootstrap.start(ThorBootstrap.java:352)
at com.tongweb.web.thor.startup.ThorBootstrap.main(ThorBootstrap.java:495)
```