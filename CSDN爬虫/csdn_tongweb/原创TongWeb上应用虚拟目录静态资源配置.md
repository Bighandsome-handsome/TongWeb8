# 原创TongWeb上应用虚拟目录静态资源配置

> 原文地址: https://blog.csdn.net/realwangpu/article/details/121599397

---

配置虚拟目录，静态资源最主要的是理清相对路径问题，如下为例。
静态资源目录如下：
在应用WEB-INF目录下建tongweb-web.xml格式示例：
<?xml version="1.0" encoding="UTF-8"?>
<tongweb-web-app>
<property name="aliases"  value="/
static01
=
/home/webappstatic01
" />
</tongweb-web-app>
#static01为访问路径
#/home/webappstatic01为静态资源绝对路径