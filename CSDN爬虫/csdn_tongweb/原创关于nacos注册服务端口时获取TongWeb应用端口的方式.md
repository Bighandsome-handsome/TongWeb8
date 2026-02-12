# 原创关于nacos注册服务端口时获取TongWeb应用端口的方式

> 原文地址: https://blog.csdn.net/realwangpu/article/details/153312817

---

应用场景：
在使用Spring Boot、Spring Cloud向nacos注册服务端口时，在TongWeb嵌入版、tomcat嵌入版的使用方式如下，通过server.port注册端口。
```java
@Component
public class NacosConfig implements ApplicationRunner {

@Autowired(required = false)
private NacosAutoServiceRegistration registration;

@Value("${server.port}")
Integer port;

@Override
public void run(ApplicationArguments args) {
    if (registration != null && port != null) {
        registration.setPort(port);
        registration.start();
    }
 }
}
```
面临问题：
而由于种种原因将嵌入式应用改造成war应用部署在TongWeb、tomcat上，这里就需要改造注册端口方式。 大部分参考tomcat方式通过JMX Mbean获取http端口，而在TongWeb7.0下此代码虽然也可以通过该方式获取端口，但由于TongWeb7.0默认启动9060、8088、5100三个端口，所以如下代码方式通过Mbean获取的端口不一定为应用端口， 从而导致注册的端口不对。
```java
/**
 * 让外部tomcat中的程序也能向nacos注册
 */
@Configuration
public class NacosConfig implements ApplicationRunner {

    @Autowired(required = false)
    private NacosAutoServiceRegistration registration;

    @Value("${server.port}")
    Integer port;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        if (registration != null && port != null) {
            Integer apport = port;
            try {
                apport = new Integer(getTomcatPort());
                //TongWeb修改方式
                //apport = new Integer(TongWebPort().getPort());
            } catch (Exception e) {
                e.printStackTrace();
            }

            registration.setPort(apport);
            registration.start();
        }
    }
    /**
     * 获取外部tomcat端口
     */
    public String getTomcatPort() throws Exception {
        MBeanServer beanServer = ManagementFactory.getPlatformMBeanServer();
        Set<ObjectName> objectNames = beanServer.queryNames(new ObjectName("*:type=Connector,*"), Query.match(Query.attr("protocol"), Query.value("HTTP/1.1")));
        String port = objectNames.iterator().next().getKeyProperty("port");
        return port;
    }

}
```
解决办法：
TongWeb7.0.4版本可以通过JMX Mbean获取端口号，将getTomcatPort()代码稍微改造如下：
```java
public static String getTongWebPort(){
    MBeanServer beanServer = ManagementFactory.getPlatformMBeanServer();
	        Set<ObjectName> objectNames = beanServer.queryNames(new ObjectName("*:type=Connector,*"), Query.match(Query.attr("name"), Query.value("tong-http-listener")));
	String port = objectNames.iterator().next().getKeyProperty("port");
	return port;
}
```
TongWeb7,8版本可以通过如下方式从配置文件获取应用端口来进行注册。
```java
package com.tong;

import com.tongweb.server.util.ServerUtil;
import com.tongweb.server.util.XmlUtils;
import java.util.List;
import com.tongweb.config.ConfigTool;
import com.tongweb.config.bean.HttpListener;

public class TongWebPort {

	public static String getPort() {

		String log = System.getProperty("java.util.logging.manager");
		if (log != null & log.equals("com.tongweb.log.TongwebLogManager"))
			return TW7port();
		else if (log != null & log.equals("com.tongweb.logger.JulLogManager"))
			return TW8port();
		else
			return "8088";
	}

   /*
    *获取TongWeb7应用端口
    */

	private static String TW7port() {
		String port = null;
		List<HttpListener> httpListeners = ConfigTool.getRoot().getServer().getWebContainer().getHttpListener();
		for (HttpListener httpListener : httpListeners) {
			if (httpListener.getName().equals("tong-http-listener"))
				port = String.valueOf(httpListener.getPort());
		}
		return port;
	}

   /*
    *获取TongWeb8应用端口
    */

	private static String TW8port() {
		String port = null;
		port = XmlUtils.getProperty(ServerUtil.getTwXmlFile(), "//connector[@name='server']").getProperty("port");
		return port;
	}

}
```