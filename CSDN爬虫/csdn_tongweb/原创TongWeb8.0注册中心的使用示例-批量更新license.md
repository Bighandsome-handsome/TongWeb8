# 原创TongWeb8.0注册中心的使用示例-批量更新license

> 原文地址: https://blog.csdn.net/realwangpu/article/details/136316638

---

简介：
TongWeb8.0
注册中
心
可用于注册和发
现
TongWeb
实例
服务，
也
可用于
存储
和
共
享 TongWeb 实例配置。
应用场景：
项目上安装多套TongWeb经常更改配置，传统方式下需要逐套更改配置，而通过注册中心管理变更其中任何一个实例，都将自动同步到其它实例。
以批量更新license为例进行说明:
1.  搭建注册中心环境如: TongNCS、Nacos、Etcd、 Zookeeper其一，本文以Nacos为例。
2.  安装TongWeb8.0, 并将Nacos的jar放入TongWeb的lib目录下。如下以Nacos 2.2.3 版本 jar 包清单为例说明：
• commons-codec-1.15.jar
• commons-logging-1.2.jar
• httpasyncclient-4.1.3.jar
• httpclient-4.5.3.jar
• httpcore-4.4.6.jar
• httpcore-nio-4.4.6.jar
• jackson-annotations-2.12.7.jar
• jackson-core-2.12.6.jar
• jackson-databind-2.12.7.1.jar
• nacos-auth-plugin-2.2.3.jar
• nacos-client-2.2.3.jar
• nacos-encryption-plugin-2.2.3.jar
• simpleclient_tracer_common-0.12.0.jar
• simpleclient_tracer_otel_agent-0.12.0.jar
• simpleclient_tracer_otel-0.12.0.jar
• simpleclient-0.12.0.jar
• slf4j-api-2.0.7.jar
• snakeyaml-2.jar
3. 每个TongWeb8.0配置注册中心地址、用户名、密码、标识符。
4. 每个TongWeb开启授权中心。
5. 以上配置完成后，测试更新效果。
(1) 准备新的license.dat文件。
(2) 进入某一 TongWeb 的 “集中管理” > “系统管理” > “产品授权” > “更新”，进入更新页面，在更新license时，开启“推送到授权中心”。
（3）检查其它TongWeb 节点license已更新。