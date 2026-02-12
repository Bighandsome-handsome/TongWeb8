# 原创ClassNotFoundException:com.tongweb.geronimo.osgi.locator.ProviderLocator

> 原文地址: https://blog.csdn.net/realwangpu/article/details/121599209

---

问题:
在TongWeb7上部署应用报错：
ClassNotFoundException:com.tongweb.geronimo.osgi.locator.ProviderLocator
原因：
当-DWebModuleOnly=true后，不加载javamail_1.4_mail.jar，而com.tongweb.geronimo.osgi.locator.ProviderLocator则在这个jar中。
解决办法：
将javamail_1.4_mail.jar改名为不以javamail开头的jar即可，如:  aamail.jar。