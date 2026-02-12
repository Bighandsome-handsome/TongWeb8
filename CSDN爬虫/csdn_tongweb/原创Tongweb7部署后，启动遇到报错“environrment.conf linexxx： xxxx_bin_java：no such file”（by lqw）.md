# 原创Tongweb7部署后，启动遇到报错“environrment.conf linexxx： xxxx/bin/java：no such file”（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/134880963

---

在麒麟v10部署tongweb的时候，想要使用自带jdk，于是通过以下指令，查了下jdk安装目录：
which java
#输出：
#/usr/bin/java
#2. 终端输入：
ls
-
lr
/
usr/bin/java
#输出：
#/usr/bin/java ->
#3. 终端输入
ls
-
lrt
/
etc/alternatives/java
#输出：
#/etc/alternatives/java -> /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.xx.x86_64
当时按照以往的经验，直接在/etc/profile 里面加了下面几行：
export JAVA_HOME=
/
usr/lib/jvm/java-1
.
8
.
0-openjdk-1
.
8
.
0
.
xx
.
x86_64
export JRE_HOME=
$JAVA_HOME
/
jre
export CLASSPATH=
$JAVA_HOME
/
lib:
$JRE_HOME
/
lib:
$CLASSPATH
export PATH=
$JAVA_HOME
/
bin:
$JRE_HOME
/
bin:
$PATH
然后source /etc/profile，启动tongweb，结果报错了：
根据报错信息，问题出在设置的javahome的目录下找到对应的文件，于是我cd 到对应的文件夹目录，才发现“echo $JAVA_HOME”指令所示的文件夹确实没有该文件，该文件在/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.xx.x86_64/jre/bin下面：
于是我在/etc/profile里面修改了javahome的路径，然后source之后又重启Tongweb，还是同样的报错。
我一度怀疑是不是没修改成功，重启之后输入echo $JAVA_HOME，甚至还使用了指令：java_home=xxxxxx，结果还是报错。正当我灰心的时候，我想起了用来检查tongweb状态的一个指令：
sudo systemctl status tongweb
上图是正常启动tongwebservice的提示，但是我输入同样指令后，也是提示：xxxx/bin/java no such file。
我对比了以下报错信息的目录跟已经设置好的javahome目录，发现不一致，于是vi进去这个文件，看到了以下内容
原来是这里的java_home跟正确的javahome路径设置的不一致，修改后重启服务，访问ok了！
整理一下思路，在部署tongweb之前，tongweb会读取当前环境的javahome设置，然后写入到tongweb.service文件里面，所以在部署tongweb前，一定要检查好javahome的路径！