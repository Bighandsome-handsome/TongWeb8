# 原创TongWeb+TongDataGrid+TongHttpServer实现Session复制

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/156774484

---

TongWeb+TongDataGrid+TongHttpServer实现Session复制
一、环境准备：
1、服务器两台192.168.43.8和192.168.43.10
2、分别安装TongWeb7049M5和TongHttpServer6013
二、搭建TongWeb7049M5集群，集群部署应用。
1、修改两台服务器TongWeb7049M5/Agent/config/agent.xml
2、启动192.168.43.8的TongWeb7049M5,并登录集中管理台。分别启动两台服务器的Agent管理器（TongWeb7049M5/Agent/bin sh startbg.sh）。启动成功后集中管理台-节点管理-节点代理可以查看到带上的节点信息。
3、创建集群，选择开启session复制。
4、负载均衡器，可选项。我这里直接选择添加了负载均衡器，在192.168.43.8：/opt/THS6013/THS
5、静态服务器跳过，直接到服务器设置。添加所需要的节点。
6、集群创建成功，TongWeb和会话服务器会创建至/opt/TongWeb7049M5/Agent/nodes/tongweb-1和/opt/TongWeb7049M5/Agent/nodes/tongdatagrid-1
7、分别启动集群下的TongWeb和会话服务器
会话服务器打印出此日志为正常
8、集中管理台应用管理-部署应用至集群下面。
三、配置TongHttpServer6013,负载模式选择sticky。
1、启动192.168.43.8下面的TongHttpServer管理台，并登录，文本编辑菜单修改THS配置并启动THS。
2、通过负载访问集群部署的应用。通过查看日志，确定应用被分发到192.168.43.8节点上。
可以通过浏览器F12查看请求头的JSESSIONID和响应头中的一样。
3、通过集中管理台强制停止集群内192.168.43.8上面的TongWeb-1。
4、再次刷新浏览器上面应用请求，此时192.168.43.10上面tongweb-1已经接管，且session未发生改变。