# 原创TongWeb配置http强制跳转https端口

> 原文地址: https://blog.csdn.net/realwangpu/article/details/122538224

---

配置步骤：
1.在TongWeb上建https端口。
2.在TongWeb建http端口，其中"重定向端口 "配置https端口
3.应用web.xml中配置如下：
<security-constraint>
<web-resource-collection >
<web-resource-name >SSL</web-resource-name>
<url-pattern>/*</url-pattern>
</web-resource-collection>
<user-data-constraint>
<transport-guarantee>CONFIDENTIAL</transport-guarantee>
</user-data-constraint>
</security-constraint>
4.部署应用，当通过http://IP:8088访问时，自动跳转到https://IP:8443上。