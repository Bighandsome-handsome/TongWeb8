# 原创Tongweb7启动的时候显示要输入java参数（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/142252116

---

问题描述：
启动tongweb7的时候，提示要输入java参数，如下图所示：
原因：
tongweb安装目录bin目录下的external.vmoptions文件改动，在# 符号后加多了一个空格。
external.vmoptions记录的是启动参数，在external.vmoptions文件里，#并非是注释符号，而是作为标签栏进行读取和识别的，所以在改动external.vmoptions的时候，默认的#部分请不要动，如有不需要的启动参数，也请直接删除。
总而言之：
编辑external.vmoptions的时候，最好做个备份，除了默认的#号，不要有多余的符号，包括空格，不需要的启动参数请直接删除。