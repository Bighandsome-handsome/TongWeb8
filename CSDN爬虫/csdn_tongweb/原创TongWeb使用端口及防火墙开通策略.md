# 原创TongWeb使用端口及防火墙开通策略

> 原文地址: https://blog.csdn.net/realwangpu/article/details/116693658

---

前言
项目部署过程中需要规划TongWeb的使用端口及防火墙策略，否则会因端口不通导致各类问题。
一、TongWeb所使用端口说明
# TongWeb 系列产品端口与配置文件汇总表

| 服务程序 | 功能描述 | 默认端口/协议 | 端口作用 | 所在配置文件 |
| :--- | :--- | :--- | :--- | :--- |
| **TongWeb** | 提供服务的核心进程 | **8088** | 默认应用访问端口 | `conf/tongweb.xml` |
| | | **9060** | 默认控制台端口 | |
| | | **7200** | JMX 端口（另随机启动两个） | |
| | | **5100** | EJB 远程调用端口 | |
| | | **8005** | 默认服务停止端口 | |
| **Agent** | 节点代理，用于集中管理通信 | **7070** | 与 Master 通信端口 | `Agent/config/agent.xml` |
| | | **19090** | 与 Master 默认文件传输端口 | |
| **TongDataGrid** | 内存会话服务器 | **5701** | 默认 Session 复制端口 | `bin/tongdatagrid.xml` |
| **TongHttpServer**| 负载均衡器 | **443** | 默认负载对外访问端口 | `bin/https.conf` |
| | | **vrrp 协议** | 配 HA（高可用）时使用 | `conf/httpserverHA.conf` |

二、端口开启访问规则
基本原则：对外用户访问只暴露应用访问端口，其它端口为内部进程通信端口，只需对内放开，不需对外暴露。
场景1. TongWeb单机情况下
1. 对外用户访问需要开启8088应用端口或自定义的应用端口。
2. 内部局域网访问的情况下要开通9060控制台端口，要能访问控制台。
场景2：JMX监控的情况下
需要开启7200及固定两个相关端口，开启防火墙，具体见：https://blog.csdn.net/realwangpu/article/details/109506744
场景3：THS集群场景下
1. 对外用户访问需要开启THS默认443应用端口或自定义的应用端口。
2.对内要开启TongWeb的http 8088应用端口，使THS能够访问TongWeb。
3. THS开启HA的情况下，THS服务器要开启vrrp协议。
场景4：集群+session复制场景下
1. 对外用户访问需要开启负载的应用端口。
2.对内要开启TongWeb的http 8088应用端口，使负载能够访问TongWeb。
3.TongDataGrid的5701端口内部开放，使TongWeb能够访问，各个TongDataGrid节点之间也需要通过该端口互备数据。
场景5：heimdall集中管理场景下
1.heimdall节点要开放9060端口，使各个agent能够访问。
2. agent节点要开放7070、19090端口，使heimdall能够访问。
3. 各个agent节点管理的TongWeb 域控制台，如：9061要开放，使heimdall能够访问。