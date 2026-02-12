# 原创TongWeb7-版本升级说明及常见问题

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/133807677

---

涉及版本：
TongWeb 嵌入版==》不涉及
TongWeb 容器云==》不涉及
TongWeb 轻量版==》不涉及
TongWeb 企业版==》TongWeb5.0.X/6.0.X 涉及(只能关闭 TongWeb 控制台和 jmx 端口或联系东方通  销售升级 TongWeb 版本)
TongWeb7.0.4.1 涉及
TongWeb7.0.4.2–P1 涉及
TongWeb7.0.4.3 涉及
TongWeb7.0.4.4–P1–P3 涉及
TongWeb7.0.4.5–M1–M3 涉及
TongWeb7.0.4.6–M3–M4 涉及
TongWeb7.0.4.7 涉及
TongWeb7.0.4.8–M1 涉及
TongWeb7.0.4.9 涉及
TongWeb7.0.4.9M1 不涉及
**注意事项：
升级前需要需要手动备份当前正在使用的 TongWeb 整个目录。
升级前需要将整个 TongWeb 目录赋 root 用户和组，升级完成后切回原用户和组。**
补丁获取：
链接：https://pan.baidu.com/s/1WxCtEqrd80zI2roU0v9dHw 提取码：ammk
补丁包含两部分：
patchtool.zip=======>补丁升级脚本
tongweb-patchs.zip===>待升级补丁
注意：该补丁为一个复合补丁包，可升级到比当前待升级版本高的任意一个版本。
升级步骤：
譬如：TongWeb 安装路径为/opt/weaver/TongWeb7046
上传 patchtool.zip 到/opt/weaver/TongWeb7046
unzip patchtool.zip 解压升级脚本压缩包
上传 tongweb-patchs.zip 到/opt/weaver
unzip tongweb-patchs.zip 解压升级补丁压缩包
chown -R root:root /opt/weaver/TongWeb7046 对整个 TongWeb 目录赋 root 用户和组
chmod -R 777 /opt/weaver/TongWeb7046/patchtool
cd /opt/weaver/TongWeb7046/patchtool
./install.sh /opt/weaver/tongweb-patchs 7049_M1
出现以下截图标注的提示，说明 TongWeb 升级成功
mv /opt/weaver/TongWeb7046 /opt/weaver/TongWeb7049M1 修改升级之后文件名11. chown -R tongweb:tongweb /opt/weaver/TongWeb7046 切回 TongWeb 原用户和组
cd /opt/weaver/TongWeb7049M1/bin
./forcestopserver 停止 tongweb 服务
./startservernohup.sh 后台启动 tongweb 服务
临时解决方案(不推荐):
如因特殊原因暂时无法升级, 那么采用临时关闭 TongWeb 控制台的方法，
使用限制：关闭 TongWeb 控制台期间无法使用 TongWeb 控制台。
TongWeb6/7 关闭控制台，修改如下完毕后重启 tongweb 生效
a. 关闭 TongWeb 控制台将 TongWeb.xml 中的 system-http-listener 通道的对应端口状态设置为 stopped，如下:
b. 将 TongWeb.xml 中的 jmx 端口 7200 暂时关闭或仅允许可信的 IP 地址访问 jmx。
具体标签中增加 enable=“false”，如下：
TongWeb5 关闭控制台，将 config/twns.xml 中的 twns、gm 两个控制台 access-enabled值设为 false，重启生效：
<web-app access-enabled=“false” context-root=“twns” … <web-app access-enabled=“false” context-root=“gm” …
常见问题：
问题 1：升级过程中如发现 TongWeb 目录/bin 下有应用程序相关的文件夹导致报错。
解决 1：请先将应用文件夹从 TongWeb 目录/bin 下移出，待升级完毕后再移回。
问题 2：使用了 open jdk11 缺少 jdk 相关依赖报错,如下。
解决 2：JAVA_HOME 和 PATH 环境变量修改为 JDK1.8，升级完成后，再切回 JDK11。
问题 3：会话复制功能 tongdatagrid-group-password 密码解码失败，截图如下
解决 3：将如下截图中,tongdatagrid-group-password 的 value 修改为密文
QABvp6bmC/a9zfqW2XJvSg==后保存，继续升级即可，如果未使用
tongweb 的会话复制功能，也可删除该文件后继续升级。
问题 4：成功升级后遇到页面 frame 相关报错，如下截图。
解决 4：删除 TongWeb 目录/bin/external.vmopitons 中删除
-Dtongweb.X_Frame_Options=SAMEORIGIN 后重启 tongweb 即可。
问题 5：如果 TongWeb 自动部署目录 autodeploy 和控制台部署目录 deployment 含有应用中文
命名的目录或文件，导致报错。
解决 5：请在执行升级脚本前，先移出 TongWeb 目录，升级完成后再移回。
问题 6：如果升级后 TongWeb 控制台和集中管理控制台报账号密码错误，无法登录。
解决 6：
a. 升级后, TongWeb 目录/bin 配置文件 external.vmoptions 中追加参数-Dnever.expire=on，如下截图：
b. 重置 TongWeb 密码：
将 tongweb 目录/domain_template/conf/security 目录覆盖 tongweb 目录
/conf/security 目录后，重启 tongweb
c. 可使用默认账号密码登录 tongweb 控制台(thanos/thanos123.com)
可使用默认账号密码登录 tongweb 集中管理控制台(rig/rig123.com)
d. 进入 TongWeb 控制台修改密码，步骤如下截图：
问题 7：通过命令行部署应用报 com.tongweb.tongejb.OpenEJBRuntimeException:
javax.crypto.IllegalBlockSizeException: last block incomplete in decryption。
解决 7：该问题为命令行部署指定的密码文件中密码为明文导致，升级版本后需要需要重置
密码并重新设置命令行密码，使用 TongWeb 自带的 password.sh 对新密码进行加密
后写入密码文件即可，步骤如下：
a. 升级后, TongWeb 目录/bin 配置文件 external.vmoptions 中追加参数-Dnever.expire=on，
如下截图：
b. 重置 TongWeb 密码：将 TongWeb 目录/domain_template/conf/security 目录覆盖 tongweb
目录/conf/security 目录后，重启 TongWeb。
c. 通过命令行修改 cli 用户密码,执行以下命令
注： 9060 为当前 TongWeb 的控制台访问端口。passwordfil 文件位于 TongWeb 目录/bin 下，也可自行放置，但命令中需要写全路径。
passwordfil 文件内容为: AS_ADMIN_password=AjLAlFlxbAed3VLKrpDZ4g==
AjLAlFlxbAed3VLKrpDZ4g==为 cli 用户默认密码 cli123.com，通过 TongWeb 目录/bin
下的 password.sh 加密而来，如下图：
d. 修改 cli 密码成功后，使用 password.sh 对新密码进行加密处理,并将加密串复制到
passwordfil 文件中，如下图：
e. 通过命令行部署测试应用测试成功，如下图：
f. tongweb7047升级到7048，7049，7049M1,7049M2，7049M3任意版本，如果tongweb.xml配置了 <web-app seesion-manager=“” …/>中会报错如下图：错误原是因为7048，7049，7049M1,7049M2，7049M3任意版本中tongweb.xml需要配置了 <web-app session-manager=“” …/>  解决方案 ，把seesion-manager 改为session-manager即可。