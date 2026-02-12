# 原创手册不全，如何手工刨出TongWeb的监控信息？

> 原文地址: https://blog.csdn.net/realwangpu/article/details/115485214

---

前言
TongWeb提供几类监控接口，如何通过这些接口获取信息?   我们通过TongWeb7.0.4.2版本讲解下获取方式。
注：换个版本就不一定对了。
一、通过JMX接口获取Mbean信息
TongWeb的JMX默认开启，通过server.log获取JMX  url，更多见：
https://blog.csdn.net/realwangpu/article/details/109506744
```bash
[INFO] [main] [systemout] [tuserport:0;jcport:0]
[INFO] [main] [admin] [URL for the Standard JMXConnectorServer : (
service:jmx:rmi:///jndi/rmi://192.168.163.1:7200/jmxrmi
)]
[INFO] [main] [core] [Starting service TONGWEB]
[INFO] [main] [core] [Starting Servlet Engine: TongWeb]
```
编写JMX程序，主要获取的信息能常有：JVM内存、线程池、数据源连接池、应用session数、应用请求数等，demo如下：
```java
package com.tong;
import java.util.HashMap;
import java.util.Map;
import javax.management.MBeanServerConnection;
import javax.management.ObjectName;
import javax.management.remote.JMXConnector;
import javax.management.remote.JMXConnectorFactory;
import javax.management.remote.JMXServiceURL;

public class TestJMX {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			// 创建JMX 的URL
			JMXServiceURL url = new JMXServiceURL("service:jmx:rmi:///jndi/rmi://127.0.0.1:7200/jmxrmi");
			// 构造获取连接所使用的认证信息,使用安全域的用户。
			Map env = new HashMap();
			env.put("jmx.remote.credentials", new String[] { "thanos", "thanos123.com" });
			JMXConnector connector = JMXConnectorFactory.connect(url, env);
			MBeanServerConnection mbsc = connector.getMBeanServerConnection();
			//指定ObjectName 
			ObjectName mbeanName = new ObjectName("TONGWEB:type=ThreadPool,name=\"http-nio2-0.0.0.0-8088\"");
			Object obj = mbsc.getAttribute(mbeanName, "maxThreads");
			System.out.println("8088 maxThreads Attribute is " + obj.toString());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
```
想获取相关的监控值，主要问题是ObjectName的获取。因为TongWeb手册上不全、不同TongWeb小版本号的ObjectName也不一样，所以想获取真正的ObjectName只有一条路：通过打开 jconsole手工查找相应的监控值，一字诀：刨。
注意：一定要注意TongWeb的小版本号，比如：有的TongWeb版本8088端口的ObjectName为:
`TONGWEB:type=ThreadPool,name="http-nio2-0.0.0.0-8088"`，而有的TongWeb版本8088端口的ObjectName为:`TONGWEB:type=ThreadPool,name="http-nio2-8088"`；换为无敌浩克Hulk数据源后，监控值更不同了。

二、通过rest接口获取TongWeb信息
在应用程序中导入 HttpClient4 所需 jar 包 httpclient-4.x.jar、 httpcore-4.x.jar、commons-logging.jar，${TW_HOME}/lib/agent 目录下的 common-7.0.jar 文件。demo如下：
```java
package com.tong;
import com.tongweb.httpclient.utils.HttpClient4Util;
public class TestRest {

	public static void main(String[] args) {
		String result = null;
		try {
            //注意改用一个thanos外的用户，否则会踢出已登录控制台的thanos用户
			result = HttpClient4Util.execute("/rest/api/listener_detail", "GET", "thanos", "thanos123.com", "127.0.0.1",
					"9060", null);
			System.out.println(result);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
```
注意：这个rest 接口只有手册提供的部分接口，手册提供就提供了，没提供的就不知道了，不能像jconsole一样去刨。
三、通过集中管理获取所有节点监控值
采用集中管理方式，通过heimdall管理TongWeb各个节点，然后访问
http://127.0.0.1:9060/heimdall/notinrealm/rest/monitor/ibm/view
即可得到各个TongWeb节点的运行状态、内存、JDBC数据源、线程池、应用的监控信息的json数据。
```json
{
    "nodes": [
        {
            "monitorList": [
                {
                    "appname": "", 
                    "dbname": "", 
                    "monitorName": "nodestatus", 
                    "monitorType": "warn", 
                    "monitorValue": "stopped", 
                    "servletName": "", 
                    "threadPoolName": ""
                }, 
                {
                    "appname": "", 
                    "dbname": "", 
                    "monitorName": "OOM", 
                    "monitorType": "warn", 
                    "monitorValue": "", 
                    "servletName": "", 
                    "threadPoolName": ""
                }
            ], 
            "nodeHome": "D:\\TongWeb7042\\TW7E\\domains\\aa", 
            "nodeIp": "192.168.163.1", 
            "nodeStatus": "stopped"
        }
    ]
}