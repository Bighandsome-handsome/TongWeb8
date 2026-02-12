# 原创关于jdk17部署tongweb7047出现java.lang.NullPointerException: Cannot read field “configFactory“（by liuhui）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/136046309

---

问题现象启动报错如下图
Caused by: java.lang.NullPointerException: Cannot read field “configFactory” because “this.assembler” is null]
[2024-02-05 17:55:55 163] [WARNING] [main] [systemout] [        at com.tongweb.tongejb.config.JNDIResourceConfigListener.(JNDIResourceConfigListener.java:30)]
[2024-02-05 17:55:55 163] [WARNING] [main] [systemout] [        at com.tongweb.tongejb.config.EELoader.addJNDIResourceConfigListener(EELoader.java:227)]
问题原因
由于tongweb7047版本跟jdk17不兼容导致
解决办法
更换tongweb版本7.0.8.70版本即可