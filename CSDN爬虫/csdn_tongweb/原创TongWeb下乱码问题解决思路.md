# 原创TongWeb下乱码问题解决思路

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109540781

---

解决乱码问题主要看以下几项配置，重点要了解这些编码设置所起的作用。
注：乱码问题看TongWeb的server.log日志基本没用，重点是看应用采用的编码以及操作系统、TongWeb的编码设置。
1. Linux下先通过local -a查看操作系统是否有相应的中文字符集。
2. Linux下再看环境变量LANG值，通常为zh_CN.GBK或zh_CN.UTF-8。通过echo $LANG查看，通过
export LANG=zh_CN.GBK
来设置。
3. JDK参数-Dfile.encoding=GBK，加在TongWeb启动脚本中。
以上两项是JDK的默认编码，-Dfile.encoding优先于LANG环境变量。
file.encoding 这个属性的英文解释：
This property is used for the default encoding in Java， all readers and writers would default to use this property. “file.encoding” is set to the default locale of Windows operationg system since Java 1.4.2. System.getProperty(“file.encoding”) can be used to access this property. Code such as System.setProperty(“file.encoding”， “UTF-8”) can be used to change this property. However， the default encoding can not be changed dynamically even this property can be changed. So the conclusion is that the default encoding can’t be changed after JVM starts. “java -Dfile.encoding=UTF-8” can be used to set the default encoding when starting a JVM. I havesearched for this option Java official documentation. But I can’t find it.
同时还有一参数
-Dsun.jnu.encoding=UTF-8
,
sun.jnu.encoding 影响文件名的创建，而 file.encoding 则影响到文件内容。在我们使用 Java 处理中文文件的时候，如果发现文件的中文内容没有乱码，而文件的中文名发生乱码，就应当多考虑一下 sun.jnu.encoding。
4. TongWeb 的Web容器 request 、response
默认编码GBK。
5.  对于URL的编码，在TongWeb的 http通道中设置，默认GBK。
“URL编码格式”相当于tomcat的URIEncoding。“ uri处理”相当于tomcat的useBodyEncodingForURI。
若tomcat下不乱码，而在TongWeb下乱码，则可参考tomcat配置来配置TongWeb。
URIEncoding：This specifies the character encoding used to decode the URI bytes, after %xx decoding the URL. If not specified, GBK will be used.
useBodyEncodingForURI：This specifies if the encoding specified in contentType should be used for URI query parameters, instead of using the URIEncoding. This setting is present for compatibility with Tomcat 4.1.x, where the encoding specified in the contentType, or explicitly set using Request.setCharacterEncoding method was also used for the parameters from the URL. The default value is false.
6. 数据库存入数据乱码，还要看数据本身的编码设置。另外不同数据的JDBC  url也有编码设置，如:MySQL的jdbc:mysql://localhost:3306/test?
useUnicode=true&characterEncoding=utf-8   。
7.重点查看应用编码规则，一定要了解应用的编码用法。
主要看应用filter中设置的编码：request.setCharacterEncoding("UTF-8")
应用代码中有没有做转码，如： new String(test.getBytes("iso-8859-1"),"utf-8");
8.日志乱码主要原因:
(1)telnet终端编码与日志输出的编码不一致导致，把日志下载到windows下用Notepad++等工具查看，并进行UTF-8与GBK转码试试。
(2) log4j编码设置不对，注意参数中的log4j.appender.file.encoding=UTF-8。