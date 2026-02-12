# 原创Tongweb7049M4有关SSL/TLS 服务器瞬时 Diffie-Hellman 公共密钥过弱的处理方案（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/144365065

---

前提条件：Tongweb7049M4已在http通道里配置了https（如何配置https可以参考这个帖子：
东方通TongWEB添加Https证书，开启SSL
）
遇到客户在配置了https后，扫描漏洞提示：
有关SSL/TLS 服务器瞬时 Diffie-Hellman 公共密钥过弱。
当时尝试在jdk.security里配置了相关参数并让客户重启，还是没有解决这个漏洞：
后来参考
SpringBoot项目：SSL/TLS 服务器瞬时 Diffie-Hellman 公共密钥过弱
看到以下配置：
Tongweb的控制台上有类似的配置，就在http通道里：
勾选TLSv1,TLSv1.3,TLSv1.2,TLSv1.1这几个协议，然后在下方的
ciphers里配置下面的内容：
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA256,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA
配置成功，可重启Tongweb，再进行漏洞扫描。