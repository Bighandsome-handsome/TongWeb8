# 原创TongWeb SSL安全相关配置

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109527473

---

SSL相关漏洞如下：
CVE-2015-2808 SSL/TLS 受诫礼(BAR-MITZVAH)攻击漏洞。
CVE-2014-3566 SSLv3在降级的旧版加密漏洞（POODLE）。
CVE-2011-1473 服务器支持 TLS Client-initiated 重协商攻击。
CVE-2016-0800 SSL DROWN攻击漏洞。
SSL证书非正式可信证书。
等等
解决以上漏洞问题的办法：
第一步：制作证书由用户方提供
用户需购买正式证书，TongWeb自带测试证书非正式证书，
需购买制作正式证书配SSL。如：
数字认证官网 | 电子认证、电子签名、电子合同知名厂商
制作证书时需使用OpenSSL最新版本，老版本OpenSSL有安全漏洞。
制作的证书密码位数要符合安全要求。
如果是Apache,nginx集群，则在其上配SSL解决漏洞。
Java类证书要求JKS格式，查看证书命令：keytool -list  -v -keystore server.keystore
第二步：在TongWeb
上配置SSL
证书
。
1. https通道改用NIO/NIO2模式，解决漏洞 CVE-2011-1473。
2. 不勾选SSLv3协议，只勾选TLS协议。
3. 在Ciphers中配置安全的算法，通常如下，注意有些JDK算动法不支持可以适当修改。
TLS_ECDHE_RSA_WITAES_128_CBC_SHA256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA,TLS_RSA_WITH_AES_128_CBC_SHA256,TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA256,TLS_RSA_WITH_AES_256_CBC_SHA
4. 在TongWeb使用的JDK中jre\lib\security\java.security配置禁用不安全的SSL协议和算法，如下：
#JDK8默认配置如下：
jdk.tls.disabledAlgorithms=SSLv3, TLSv1, TLSv1.1, RC4, DES, MD5withRSA, \
DH keySize < 1024, EC keySize < 224, 3DES_EDE_CBC, anon, NULL, \
include jdk.disabled.namedCurves
另外：很多项目中有人问，为什么东方通不提供SSL正式证书？ 答复：正式证书不是任意一个公司可以发布的， 见：
数字证书原理_zxh2075的专栏-CSDN博客_github数字证书的实验原理 、实验所涉及知识
cer、crt与JKS格式证书互转格式转化，具体参数含义 -help
第一步，从key和crt/cer生成pkcs12格式的keystore
openssl pkcs12 -export -in
server.crt
-inkey server.key  -out
mycert.p12
-name tongweb
第二步 生成TongWeb需要的keystore, 两个密码123456要一样
keytool -importkeystore -alias tongweb -v  -srckeystore
mycert.p12
-srcstoretype pkcs12 -srcstorepass
123456
-destkeystore
tw.keystore
-deststoretype
jks
-deststorepass
123456