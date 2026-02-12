# 原创TongWeb上设置应用 cookie 属性

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109711846

---

功能需求：
需要更改应用默认的 cookie 中 JSESSIONID 名称、域名、路径等配置。
解决办法：
在 JavaEE6 规范中对 web.xml 的 schema 定义中增加了 cookie 属性设置，应用的web.xml中可配置如下：
<session-config>
   <session-timeout>30</session-timeout>
   <cookie-config>
     <name>MYJSESSIONID</name>
     <domain>tong.com</domain>
     <path>/tong</path>
     <comment>no zuo no die</comment>
     <http-only>true</http-only>
     <secure>false</secure>
     <max-age>1800</max-age>
   </cookie-config>
</session-config>
说明：
<name>可以自定义会话 cookie 的名字。
<domain>和<path>对应着 cookie 的 Domain 和 Path 特性。
<comment>通常用于解释 cookie 的目的。
<http-only>和<secure>对应着 cookie 的 HttpOnly 和 Secure 特性。
<max-age>指定了 cookie 的 Max-Age 特性。
HTTP 头响应结果如下：
Set-Cookie: MYJSESSIONID=97973D55AEE06399BAC16C890F121649;Version=1; Comment="no zuo no die"; Domain=tong.com; Max-Age=1800;Path=/tong/; HttpOnly
注：虽然TongWeb中有说明可在tongweb-web.xml配置如上信息，但多数用户对tongweb-web.xml写法不熟悉，翻手册又困难，所以用标准的web.xml比较方便。