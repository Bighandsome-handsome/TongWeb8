# 原创Tongweb7 日志报错：HttpServletResponse is exceeding the 65535 bytes limit（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/140461448

---

遇到jsp访问的时候页面加载不全，看tw7日志有如下图信息：
原因： jsp的本质是servlet，编译时会先将他转换成java代码，然后再进行编译。 你的jsp编译成生成的文件太大，导致报错。（Java 编译器限制单个方法的字节大小不能超过 65535 字节。如果 JSP 页面包含大量的 HTML、JavaScript 或嵌入的 Java 代码，编译后生成的 _jspService 方法可能会非常大，超过此限制。）
查询了一下，tomcat的做法是在web.xml里配置了如下配置：
于是尝试在tongweb的conf目录下找到default-web.xml，先备份，然后找到对应的配置部分：
看着跟tomcat的很类似，于是在 development下的 下加了一段配置：
<
init-param
>
<
param-name
>
mappedfile
<
/param-name
>
<
param-value
>
false
<
/param-value
>
<
/init-param
>
配置后重启tongweb，测试一下应用的jsp页面，问题解决。