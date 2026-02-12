# 原创TongWeb8首次安装控制台限制

> 原文地址: https://blog.csdn.net/realwangpu/article/details/128493633

---

限制一：
TongWeb8安装后，默认只能本机登录控制台并在本机强制修改默认密码后方可使用，远程登录控制台无法进行任何修改操作。后台日志提示：
Client IP ( 192.168.55.94 ) was rejected because the trust mode is not satisfied: (  )
The client IP [ 192.168.55.94 ] has been intercepted, and the currently configured trusted IP policy is: [ ]
所以在完成TongWeb安装后，想通过远程访问TongWeb控制台进行修改操作，需要在TongWeb本机通过控制台或命令行修改默认密码、设置信任IP。 修改方式有两种：
方式一：通过本机登录控制台修改
强调：必须是在安装TongWeb的本机上打开浏览器，通过127.0.0.1或localhost地址登录修改。
错误方式：TongWeb装在A机，却在B机上打开浏览器输入：https://127.0.0.1:9060/console，然后说访问不了。
这种方式缺点：在IT机房服务器上安装的TongWeb，进入机房登录服务器本机是不方便的。
方式二：SSH远程登录linux服务器，通过命令修改(推荐方式)
进入TongWeb的bin目录，执行如下两条命令：
#修改密码，将红色部分改为需要的密码即可
sh commandstool.sh --model=password --action=update --username=thanos --password=thanos123.com --acceptAgreement=true originalPassword=thanos123.com newPassword=
wang135.COM
confirmPassword=
wang135.COM
#设置信任客户端IP， 将红色部分改为浏览器所在机器的IP, 或模糊匹配192.168.55.*
sh commandstool.sh --username=thanos --password=wang135.COM --acceptAgreement=true --model=consolesecurity --action=update trustedIP=
192.168.55.159
IP地址也可以直接修改默认域domain1下的domains\domain1\conf\console.xml文件中的trustedIP属性值。
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- ================================== 注意事项 ====================================== -->
<!-- 在 TongWeb 运行期间，主配置文件 tongweb.xml 和 console.xml 具有防篡改限制，禁止对其进行修改 -->
<!-- 当主配置文件遭到意外篡改时，系统会自动恢复，所做的修改将不会生效 -->
<!-- 若需要修改主配置文件并使其生效，请先停止 TongWeb 服务器，然后再进行修改 -->
<!-- ================================================================================= -->
<console disableUpload="false" failureCount="5"	lockOutTime="300" trustedIP="192.168.55.*">
	<auth verCodeEnabled="true">
限制二：
TongWeb8默认禁用了应用包远程上传功能，若需要远程上传应用包功能，请在“集中管理”->"安全配置"->"控制台安全"中关闭“禁用文件上传”。
限制三：
TongWeb8默认禁用了自动部署功能，若需要自动部署目录，则在“全局配置”中开启。
限制四：
TongWeb8默认不开启JSP自动更新功能，若需要动态更新JSP，在部署应用时，开启JSP开发模式。注：只要JSP与生成的class文件时间不相等，则会触发更新。
限制五：
TongWeb8默认不开启JMX功能，若需要JMX监控，可在“集中管理”->“系统管理”->“JMX接口”中开启。