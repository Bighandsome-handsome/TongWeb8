# 原创tongweb7049上传报：Caused by: com.tongweb.web.util.http.fileupload.FileCountLimitExceededException（lqw

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/155054835

---

问题描述
客户使用tongweb7049部署应用后，应用上传文件 formData 参数超过10 个, 会报错,：Caused by: com.tongweb.web.util.http.fileupload.FileCountLimitExceededException
问题分析
经查看，tongweb的lib下的jar有以下代码：
也就是说maxPartCount，默认限制就是10个。
解决方案
虽然代码里默认限制是10个，但可以通过控制台的http通道里添加配置maxPartCount，将maxPartCount改大，如下图所示：