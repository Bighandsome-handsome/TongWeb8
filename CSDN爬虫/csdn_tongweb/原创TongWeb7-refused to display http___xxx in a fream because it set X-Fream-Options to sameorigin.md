# 原创TongWeb7-refused to display http://xxx in a fream because it set X-Fream-Options to sameorigin

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/133808867

---

应用适配如遇到页面frame相关报错
删除TongWeb目录/bin/external.vmopitons中删除
-Dtongweb.X_Frame_Options=SAMEORIGIN，或者设置为NONE，后重启tongweb即可