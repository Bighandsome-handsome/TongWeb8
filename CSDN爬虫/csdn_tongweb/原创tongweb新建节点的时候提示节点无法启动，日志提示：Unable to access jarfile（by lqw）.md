# 原创tongweb新建节点的时候提示节点无法启动，日志提示：Unable to access jarfile（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/135203560

---

tongweb在新建节点之后，提示节点无法启动，以下是节点配置和日志信息：
后来我cd到安装目录，发现安装目录只有一个zip格式包，于是安装了unzip，安装后再重新新建节点，问题解决！
原因：linux没有安装unzip，导致新建节点的时候，无法解压zip包。