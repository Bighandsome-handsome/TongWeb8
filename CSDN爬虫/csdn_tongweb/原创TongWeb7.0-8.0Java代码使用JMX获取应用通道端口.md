# 原创TongWeb7.0-8.0Java代码使用JMX获取应用通道端口

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/137153861

---

以下通过java代码实现获取TongWeb7.0/8.0应用通道端口使用到的JMX均为TongWeb自带的JMX功能。
一、TongWeb7.0
1、使用本地JMX获取应用通道端口
public
String getTw7PortByLocalJmx() {
try
{
MBeanServer
beanServer
= ManagementFactory.
getPlatformMBeanServer
();
Set<ObjectName>
objectNames
=
beanServer
.queryNames(
new
ObjectName(
"*:type=Connector,*"
),
Query.
match
(Query.
attr
(
"name"
), Query.
value
(
"tong-http-listener"
)));
String
port
=((ObjectName)
objectNames
.iterator().next()).getKeyProperty(
"port"
);
return
"getTw7PortByLocalJmx channel tong-http-listener port = "
+
port
;
}
catch
(Exception
e
) {
e
.printStackTrace();
return
"error : "
+
e
.getMessage();
}
}
2、使用远程JMX获取应用通道端口
public
String getTw7PortByRemoteJmx() {
try
{
String
ipAndPort
=
"192.168.5.26:7200"
;
String
serviceUrl
= String.
format
(
"service:jmx:rmi://%s/jndi/rmi://%s/jmxrmi"
,
ipAndPort
,
ipAndPort
);
JMXServiceURL
jmxUrl
=
new
JMXServiceURL(
serviceUrl
);
Map<String, String[]>
env
=
new
HashMap<String, String[]>();
env
.put(JMXConnector.
CREDENTIALS
,
new
String[] {
"thanos"
,
"thanos123.com"
});
JMXConnector
jmxConnector
= JMXConnectorFactory.
connect
(
jmxUrl
,
env
);
MBeanServerConnection
mbsc
=
jmxConnector
.getMBeanServerConnection();
Set<ObjectName>
objectNames
=
mbsc
.queryNames(
new
ObjectName(
"*:type=Connector,*"
),
Query.
match
(Query.
attr
(
"name"
), Query.
value
(
"tong-http-listener"
)));
String
port
=((ObjectName)
objectNames
.iterator().next()).getKeyProperty(
"port"
);
return
"getTw7PortByRemoteJmx channel tong-http-listener port = "
+
port
;
}
catch
(Exception
e
) {
e
.printStackTrace();
return
"error : "
+
e
.getMessage();
}
}
二、TongWeb8.0
1、使用本地JMX获取应用通道端口
（1）使用本地JMX时需要先在对应的tongweb实例中开启注册本地Mbean的功能。入口：对应tongweb实例==》基础配置==》全局配置==》JMX
（2）相关代码
public
String getTw8PortByLocalJmx() {
try
{
MBeanServer
beanServer
= ManagementFactory.
getPlatformMBeanServer
();
Object[]
params
= {
"Connector"
,
"server"
};
String[]
signature
= { String.
class
.getName(), String.
class
.getName() };
Object
result
=
beanServer
.invoke(
new
ObjectName(
"TongWeb:name=server"
),
"show"
,
params
,
signature
);
ObjectMapper
mapper
=
new
ObjectMapper();
String
jsonString
=
mapper
.writeValueAsString(
result
);
JSONObject
jsonObject
= JSONObject.
parseObject
(
jsonString
);
String
port
=
jsonObject
.getString(
"port"
);
return
"getTw8PortByLocalJmx channel server port = "
+
port
;
}
catch
(Exception
e
) {
e
.printStackTrace();
return
"error : "
+
e
.getMessage();
}
}
2、使用远程JMX获取应用通道端口
（1）使用远程JMX时需要先在对应的tongweb实例中开启JMX接口功能。入口：集中管理==》系统管理==》JMX接口==》启用
（2）创建新的系统管理员用户专门用于远程JMX连接。
原因：为了保证用户的登录安全，当使用某用户通过浏览器登录控制台后，若再使用相同的用户通过 REST\JMX\命令行等接口接入，该用户在浏览器上的会话会被强制终止（即被踢出，需要重新登录）。
入口：集中管理==》安全配置==》管理员==》创建
（3）使用新用户登录并修改新用户的初始密码
（4）使用security用户登录tongweb给新用户赋予管理员角色
（5）相关代码
public
String getTw8PortByRemoteJmx() {
try
{
String
ipAndPort
=
"192.168.5.28:7200"
;
String
serviceUrl
= String.
format
(
"service:jmx:rmi://%s/jndi/rmi://%s/server"
,
ipAndPort
,
ipAndPort
);
JMXServiceURL
jmxUrl
=
new
JMXServiceURL(
serviceUrl
);
Map<String, Object>
environment
=
new
HashMap<>();
environment
.put(JMXConnector.
CREDENTIALS
,
new
String[] {
"jmxuser"
,
"Tongweb135.."
,
null
,
"true"
});
JMXConnector
connector
= JMXConnectorFactory.
connect
(
jmxUrl
,
environment
);
connector
.connect();
MBeanServerConnection
connection
=
connector
.getMBeanServerConnection();
Object[]
params
= {
"Connector"
,
"server"
};
String[]
signature
= { String.
class
.getName(), String.
class
.getName() };
Object
result
=
connection
.invoke(
new
ObjectName(
"TongWeb:name=server"
),
"show"
,
params
,
signature
);
ObjectMapper
mapper
=
new
ObjectMapper();
String
jsonString
=
mapper
.writeValueAsString(
result
);
JSONObject
jsonObject
= JSONObject.
parseObject
(
jsonString
);
String
port
=
jsonObject
.getString(
"port"
);
return
"getTw8PortByRemoteJmx channel server port = "
+
port
;
}
catch
(Exception
e
) {
e
.printStackTrace();
return
"error : "
+
e
.getMessage();
}
}
建议使用上面的代码方式，下面的方式需要删除字符串首尾的“[]”，代码写死，如果服务器返回数据结构发生变化会报错。
public
String getTw8PortByRemoteJmx() {
try
{
String
ipAndPort
=
"192.168.5.28:7200"
;
String
serviceUrl
= String.
format
(
"service:jmx:rmi://%s/jndi/rmi://%s/server"
,
ipAndPort
,
ipAndPort
);
JMXServiceURL
jmxUrl
=
new
JMXServiceURL(
serviceUrl
);
Map<String, Object>
environment
=
new
HashMap<>();
environment
.put(JMXConnector.
CREDENTIALS
,
new
String[] {
"jmxuser"
,
"Tongweb135.."
,
null
,
"true"
});
JMXConnector
connector
= JMXConnectorFactory.
connect
(
jmxUrl
,
environment
);
connector
.connect();
MBeanServerConnection
connection
=
connector
.getMBeanServerConnection();
Properties
properties
=
new
Properties();
properties
.setProperty(
"name"
,
"server"
);
Object
result
=
connection
.invoke(
new
ObjectName(
"TongWeb:name=console"
),
"callServerMethod"
,
// modelName action
参数
new
Object[] {
"connector"
,
"show"
,
properties
},
new
String[] { String.
class
.getName(), String.
class
.getName(), Properties.
class
.getName() });
JSONObject
jsonObject
= JSONObject.
parseObject
(String.
valueOf
(
result
));
String
models
=
jsonObject
.getString(
"models"
);
models
=
models
.substring(1,
models
.length() - 1);
jsonObject
= JSONObject.
parseObject
(
models
);
String
port
=
jsonObject
.getString(
"port"
);
return
"getTw8PortByRemoteJmx channel server port = "
+
port
;
}
catch
(Exception
e
) {
e
.printStackTrace();
return
"error : "
+
e
.getMessage();
}
}