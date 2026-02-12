# 原创TongWeb的cacheMaxSize设置

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109509870

---

在TongWeb7上部署应用经常报警告如下, TongWeb7上设这个cacheMaxSize 值一般要比应用所有静态资源总合要大，才不报如下警告：
[WARNING] [other] [Unable to add the resource at [/WEB-INF/lib/lucene-analyzers-common-4.7.2.jar] to the cache because there was insufficient free space available after evicting expired cache entries - consider increasing the maximum size of the cache]
在
默认虚拟主机server中
，增加其它属性：(或应用所在的虚拟主机)
cacheMaxSize：为部署在此虚拟机下的应用设置静态资源缓存的最大值，单位为 K。
cachingAllowed：为部署在此虚拟机下的应用设置是否允许启用静态资源(HTML、图片、声音等)的缓存。默认值为 true。
cacheObjectMaxSize: 为部署在此虚拟机下的应用设置允许缓存的最大文件容量，大小此容量的文件将不被 Cache。 cacheObjectMaxSize 会被限定在cacheMaxSize/20 以下。
如何判断缓存设置是否够用，打开TongWeb应用监控可以看到缓存使用情况。