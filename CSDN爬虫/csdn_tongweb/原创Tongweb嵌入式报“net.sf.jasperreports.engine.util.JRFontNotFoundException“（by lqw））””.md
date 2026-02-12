# 原创Tongweb嵌入式报“net.sf.jasperreports.engine.util.JRFontNotFoundException“（by lqw））””

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/146481804

---

问题描述
用户使用tongweb嵌入式p11版本，已确认linux下有黑体的字体，应用里也配置了黑体，但是直接报错：
解决方案
在应用的resource下新建一个jasperreports.properties，内容如下：
net.sf.jasperreports.awt.ignore.missing.font
=
true