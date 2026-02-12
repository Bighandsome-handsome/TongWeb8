# 原创TongWeb主配置文件tongweb.xml概要说明

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109510066

---

TongWeb主配置文件tongweb.xml概要说明， 大部分控制台配置参数是保存在该文件中，必要时可直接修改，重启生效。
常用配置：
1. 修改默认的8005,9060,8088,8443,7200,5100等端口。
2. 删除应用配置。
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<tongweb>
<!-- 热部署，自动部署 -->
<auto-deploy enabled="true" jsp-compile="false" dir="${tongweb.root}/autodeploy" check-interval="3000"/>
<hot-deploy enabled="false" watched-resource="WEB-INF/web.xml,MATA-INF/application.xml"/>
<!-- 应用部署信息,  将对应的应用<web-app删除，即卸载应用。 -->
<apps>
<web-app name="console" original-location="${tongweb.upload}/console" location="${tongweb.sysapp}/console" context-root="/console" vs-names="admin" is-directory="true" enabled="true" description="console" deploy-order="1" object-type="sys" jsp-compile="false" dtd-validate="false" is-autodeploy="false" delegate="false"/>
<web-app name="heimdall" original-location="${tongweb.upload}/heimdall" location="${tongweb.sysapp}/heimdall" context-root="/heimdall" vs-names="admin" is-directory="true" enabled="true" description="heimdall" deploy-order="1" object-type="sys" jsp-compile="false" dtd-validate="false" is-autodeploy="false" delegate="false"/>
<web-app name="sysweb" original-location="${tongweb.upload}/sysweb" location="${tongweb.sysapp}/sysweb" context-root="/sysweb" vs-names="admin" is-directory="true" enabled="true" description="sysweb" deploy-order="1" object-type="sys" jsp-compile="false" dtd-validate="false" is-autodeploy="false" delegate="false"/>
<web-app name="dbpool" original-location="D:/dbpool" location="D:/dbpool" context-root="/dbpool" vs-names="server" is-directory="true" enabled="true" deploy-order="100" object-type="user" jsp-compile="false" dtd-validate="false" is-autodeploy="false" version="" retire-state="none" retire-strategy="nature" retire-timeout="0" version-serial-number="1" delegate="false" cache-max-size="10240"/>
<connector-app name="genericra" original-location="D:/TongWeb7041/tw7e/bin/../temp/upload/genericra" location="D:/TongWeb7041/tw7e/bin/../applications/genericra" is-directory="true" enabled="true" thread-pool="default-thread-pool" deploy-order="1" object-type="user" dtd-validate="false" is-autodeploy="false" version="" retire-state="none" retire-strategy="nature" retire-timeout="0" version-serial-number="1">
<property name="JndiProperties" value="java.naming.factory.initial=com.sun.jndi.fscontext.RefFSContextFactory,java.naming.provider.url=file:${tongweb.root}/apache-activemq/conf"/>
<property name="LogLevel" value="INFO"/>
<property name="SupportsXA" value="true"/>
<property name="ProviderIntegrationMode" value="jndi"/>
<property name="RMPolicy" value="OnePerPhysicalConnection"/>
</connector-app>
</apps>
<!-- 停止端口8005，若无此配置默认8005.   -->
<server
shutdown-port="8005"
jsf="false">
<!--  web容器编码配置 -->
<web-container jsp-development="true" parameter-encoding="GBK" response-encoding="GBK" hung-thread-threshold="0" hostnameVerifier="NullHostnameVerifier">
<!--  访问日志 -->
<access-log pattern="%{yyyyMMddHHmmssSSS}t %U %m %a %D" suffix=".txt" log-extend="false" file-date-format="yy.MM.dd.HH"/>
<!--  虚拟主机配置 -->
<virtual-host name="admin" listeners="system-http-listener" accesslog-enabled="false" accesslog-dir="logs/access" sso-enabled="false" remote-filter-enabled="false">
<sso/>
<remote-filter/>
</virtual-host>
<virtual-host name="server" listeners="tong-http-listener" accesslog-enabled="false" accesslog-dir="logs/access" sso-enabled="false" remote-filter-enabled="false">
<sso/>
<remote-filter/>
</virtual-host>
<!--  http端口配置 -->
<http-listener name="system-http-listener"
port="9060"
io-mode="nio2" redirect-port="8443" uri-encoding="GBK" parse-body-methods="POST,DELETE,PUT" default-virtual-host="admin" create-time="2019-10-29 10:54:11">
<ssl/>
<protocol max-threads="5" min-spare-threads="1"/>
<http-options/>
<advance/>
</http-listener>
<http-listener name="tong-http-listener"
port="8088"
status="started" address="0.0.0.0" io-mode="nio2" http2-enabled="false" ssl-enabled="false" redirect-port="8443" uri-encoding="GBK" use-body-encoding-for-uri="false" max-parameter-count="10000" max-post-size="3097152" parse-body-methods="POST" default-virtual-host="server" create-time="2019-10-29 10:54:11">
<ssl/>
<protocol not-allow-HTTP-methods="TRACE,OPTIONS,HEAD,CONNECT,DELETE" async-timeout="10000" enable-lookups="false" max-header-count="100" use-ipv-hosts="false" xpowered-by="false" backlog="100" accept-thread-count="1" connection-timeout="60000" keep-alive-timeout="60000" max-threads="5" min-spare-threads="1" processor-cache="200" tcp-no-delay="true" max-connections="10000" self-tuned="false">
<property name="threadPriority" value="5"/>
</protocol>
<http-options compression="on" compressable-mime-type="text/html,text/plain,text/xml" compression-min-size="2048" no-compression-user-agents="" disable-upload-timeout="true" max-http-header-size="8192" max-keep-alive-requests="100"/>
<advance disable-keep-alive-percentage="75" selector-timeout="1000" usecomet="true" use-sendfile="true" oom-parachute="1048576"/>
<property name="server" value="webserver"/>
</http-listener>
<http-listener name="ejb-server-listener"
port="5100"
uri-encoding="GBK" parse-body-methods="POST" default-virtual-host="server" create-time="2019-10-29 10:54:12">
<ssl/>
<protocol max-threads="5" min-spare-threads="1"/>
<http-options/>
<advance/>
</http-listener>
<!--  防SDOS攻击配置 -->
<property name="complete.message.timeout.seconds" value="0"/>
<property name="max.attack.times" value="3"/>
<property name="blacklist.expired.hours" value="12"/>
<property name="interrupt.current.connect" value="true"/>
</web-container>
<ejb-container>
<stateful/>
<singleton/>
<stateless/>
<mdb/>
</ejb-container>
<!-- 安全域配置 -->
<security-service>
<auth-realm name="defaultRealm" type="File">
<property name="UsersFile" value="twusers.properties"/>
<property name="GroupsFile" value="twgroups.properties"/>
</auth-realm>
</security-service>
<!-- 事务配置 -->
<transaction-service transaction-timeout-in-seconds="3600"/>
<!-- 数据源配置 -->
<jdbc-connection-pool name="testdb" is-multi="false" is-xa="false" dataSourceCreator="lite" jdbc-driver="com.mysql.jdbc.Driver" jdbc-url="jdbc:mysql://localhost:3316/platform?serverTimezone=UTC&amp;useSSL=false" user-name="platform" password="XdIDxiNaOk8nCiArVqmuZw==" jta-managed="true" default-auto-commit="true" commit-on-return="true" rollback-on-return="false" initial-size="10" max-active="20" min-idle="10" max-wait-time="30000" validation-query="SELECT 1" validation-query-timeout="5" test-on-borrow="true" test-on-connect="true" test-on-return="false" test-while-idle="false" time-between-eviction-runs="60000" min-evictable-idle-time="60000" remove-abandoned="false" propagate-interrupt-state="false" ignore-exception-on-pre-load="true" remove-abandoned-timeout="2" abandon-when-percentage-full="0" log-abandoned="false" jdbc-interceptors="StatusMonitor;QueryTimeoutInterceptor(queryTimeout=0)" validation-interval="30000" max-age="1800000" log-validation-errors="false" fair-queue="false" assoc-with-thread="false" leakCheck="false"/>
<monitor-service monitoring-enabled="false" flush-interval="60" flush-time-threshold="1800" persist-enabled="false" rotation-limit-val="10" rotation-limit-unit="MB">
<monitor-config name="Memory" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="JVMMemoryPool" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="GarbageCollector" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="JVMThread" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="Compilation" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="ClassLoading" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="Runtime" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="OperatingSystem" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="TWServer" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="ConnectorAndThreadPool" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="DataSource" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="DataSourceLite" monitoring-enabled="true" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="TransactionManager" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="JCA" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="WebModule" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="SessionManager" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="Loader" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
<monitor-config name="ResourceCache" monitoring-enabled="false" produce-interval="10" persistent-enabled="false"/>
</monitor-service>
<!-- JMX配置 -->
<jmx-service
port="7200"
address="127.0.0.1"
protocol="rmi"/>
<jms-service>
</jms-service>
<!-- 日志配置 -->
<log-service file="${tongweb.root}\logs\server.log" rotation-limit="50 MB" rotation-timelimit="0" rotation-file-count="20" rotation-by-day="false" log-format="[%d{yyyy-MM-dd HH:mm:ss SSS}] [%p] [%t] [%c] [%m]%n" rotation="true" verbose="true">
<module-log-levels ejb-container="INFO" web-container="INFO" cdi="INFO" jpa="INFO" jsf-impl="INFO" jsf-api="INFO" jta="INFO" jca="INFO" data-source="INFO" jms-resource="INFO" beanvalidation="INFO" naming="INFO" admin="INFO" configuration="INFO" deployment="INFO" monitor-service="INFO" core="INFO" security="FINEST" rmi-service="INFO" systemout="INFO" other="INFO" javamail="INFO"/>
<async-logger-config asynclogger-waitstrategy="Sleep" asynclogger-ringbuffersize="1024"/>
</log-service>
<log-save-path sql-log-path="logs" audit-log-path="logs/audit-log" persistence-log-path="persistence"/>
<compress-log-service compress-enabled="false,false,false" log-dir="${tongweb.root}/logs,${tongweb.root}/logs/access,${tongweb.root}/persistence" compress-obj="1,2,3" rotation-time="1,1,1" execution-time="1,1,1"/>
<snmp-service enabled="false" port="161" address="0.0.0.0" version="3" transportType="udp" engineID="62:a0:c1:81:11:c3:17:33" securityName="public" authKey="nmsAuthKey" privKey="myDesPriviateKey"/>
<jca-thread-pool name="default-thread-pool" min-threads="10" max-threads="200" queue="100" keep-alive-time="3600"/>
</server>
<!-- 快照配置 -->
<snapshot>
<auto-snapshot interval-second="5" relation="or">
<contents jstack="true" jmap="true" config="true" monitor="true" system-log="true" access-log="true" gc-log="true"/>
<cpu-condition times="10" times-unit="time" judgment="above" judgmentvalue="90%"/>
<memory-condition times="10" times-unit="time" judgment="above" judgmentvalue="90%"/>
<gc-condition judgment="above" judgmentvalue="60"/>
<halthttp-condition httpname="tong-http-listener" judgment="above" judgmentvalue="10"/>
</auto-snapshot>
<size-clear disk-remain-percent="20%" clear-percent="60%"/>
<time-clear timeout-day="30"/>
</snapshot>
</tongweb>