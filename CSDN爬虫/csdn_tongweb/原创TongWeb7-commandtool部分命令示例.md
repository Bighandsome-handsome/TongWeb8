# 原创TongWeb7-commandtool部分命令示例

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/133808904

---

commandtool部分命令示例，具体参数相关解释，请查看TongWeb7手册
非交互模式
替换授权：
./commandstool.sh update-license --user=cli --passwordfile=passwordfil --host=localhost --port=9060 --interactive=false
修改cli用户密码：
./commandstool.sh change-admin-password --user=cli --passwordfile=passwordfil --host=localhost --port=8099
输入以下新旧密码(老版本)
Please enter the old admin password>cli123.com
Please enter the new admin password>Cli456.com
Please enter the new admin password again>Cli456.com
Command change-admin-password executed successfully.
或者(新版本，当前测试跑在7049M2)
Please enter the new admin password>cl45@EN.com
Please enter the new admin password again>cl45@EN.com
修改TongWeb控制台密码：
./commandstool.sh config-password --adminuser=thanos --adminoldpassword=thanos123.com --adminnewpassword=Thanos123.com --user=cli --passwordfile=passwordfil --host=localhost --port=9060 --interactive=true
Command config-password executed successfully.
修改jvm参数：
./commandstool.sh set-jvm-arg --user=cli --passwordfile=passwordfile --host=localhost --port=9060 --interactive=true --arg=-Xmx1024m --arg=-Xms1024m
Command set-jvm-arg executed successfully.
应用部署：
./commandstool.sh deploy --user=cli --passwordfile=passwordfile --host=localhost --port=9060 --interactive=true --contextroot=/beanValida --defaultvs=server --applocation=…/samples/bean-validation/beanValidate.war beanValida
Command app executed successfully.
应用解部署：
./commandstool.sh undeploy --user=cli --passwordfile=passwordfile --host=localhost --port=9060 --interactive=true beanValida
Command undeploy executed successfully.
重部署应用：
./commandstool.sh redeploy --user=cli --passwordfile=passwordfile --port=9061  --interactive=false  --applocation=/home/vmjoec/samples/bean-validation/beanValidate.war beanValidate
交互：
./commandstool.sh redeploy --user=cli --passwordfile=passwordfile --port=9061   --applocation=/home/vmjoec/samples/bean-validation/beanValidate.war beanValidate
更新http通道：
./commandstool.sh update-http-listener --interactive=true --listeneraddress=localhost --securitabled=false --listenerport=9061 --user=cli --passwordfile=./passwordfil --defaultvs=server tong-http-listener
停止应用：
./commandstool.sh disable-app --user=cli --passwordfile=passwordfile --port=9060 --interactive=true beanValidate
Command disable-app executed successfully.
启动应用：
./commandstool.sh enable-app --user=cli --passwordfile=passwordfile --port=9060 --interactive=true beanValidate
Command enable-app executed successfully.
获取应用状态：
./commandstool.sh list-apps --user=cli --passwordfile=passwordfile --port=9060 --interactive=true
name=block type=war context-root=/block vNames=server status=started
name=beanValidate type=war context-root=/beanValidate vNames=server status=started
Command list-apps executed successfully.
设置启动脚本参数：
./commandstool.sh set-server-arg --user=cli --passwordfile=passwordfile --port=9060 --interactive=true  --arg=-DWebModuleOnly=true
Command set-server-arg executed successfully.
删除启动脚本参数：
./commandstool.sh delete-server-arg --user=cli --passwordfile=passwordfile --port=9060 --interactive=true  WebModuleOnly
Command delete-server-arg executed successfully.
查看TongWeb版本号：
./commandstool.sh version --user=cli --passwordfile=passwordfile --port=9060 --interactive=true
TongWeb7.0.4.7
Command version executed successfully.
passwordfile文件内容：
AS_ADMIN_password=AjLAlFlxbAed3VLKrpDZ4g==   注：AjLAlFlxbAed3VLKrpDZ4g==为调用 tongweb目录/bin/password.sh  cli123.com 后加密得来。