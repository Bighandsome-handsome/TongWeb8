# 原创tongweb7049m1升级到tongweb7049m3，启动 报错：realm can not be null（by jjz+yjm+lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/139408482

---

原因：该版本的tongweb7049m1是由旧版本的tongweb升级到7049m1版本，升级包在升级的时候，没有把对应的tongweb.xml里的默认配置同步到tongweb.xml，导致tongweb.xml 的配置有缺失。
解决思路：
备份好要升级的tongweb目录，然后自行解压一个新的tongweb7049m3，用工具分析m3的tongweb.xml和要升级的m1的tongweb.xml，是不是有缺失的部分，有的话添加到对应的tongweb.xml，然后重新升级，再去启动