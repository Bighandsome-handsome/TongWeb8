# 1. 安装简介
应用服务器 TongWeb 以二十多年的行业经验为基础，充分考虑企业客户的核心商业需求，提供与时俱进、轻量易于使用、性能强大而又具有极高可靠性安全性的开发、运行、维护平台，从而提高开发、维护效率，尽可能的为企业客户减少投入成本的同时保证应用稳定高效的运行。
本文档主要介绍如何安装 TongWeb 应用服务器。

## 约定说明：
为了方便后续描述，对相关产品的安装路径和实例运行路径做如下约定。
<table><tr><td>路径</td><td>约定说明</td></tr><tr><td>${tongweb.home}</td><td>TongWeb 安装路径。</td></tr><tr><td>${tongweb.base}</td><td>TongWeb 实例运行路径。例如，默认实例运行路径为“${tongweb.home}/domains/domain1”。</td></tr></table>

# 2. 环境准备

## 2.1. 平台环境
<table><tr><td>环境</td><td>版本</td></tr><tr><td>操作系统</td><td>·Windows
Microsoft Windows 系列。
·Linux
RedHat 系列、Suse Linux 系列、麒麟操作系统、统信 uos 操作系统、中科方德操作系统等。
·Mac OS
Mac OS 系列</td></tr><tr><td>芯片</td><td>支持国内主流的 ARM、X86、MIPS、LoongArch 芯片架构。例如：华为鲲鹏(ARM)、飞腾(ARM)、海光(X86)、兆芯(X86)、龙芯(MIPS/LoongArch)等。</td></tr><tr><td>数据库</td><td>主流数据库：Oracle、MySQL5、MySQL8、Sybase
15、dameng、Kingbase、Kingbase8、Oscar、HSQL、Sybase type 4 for Sybase 11.x、jtds sybase、postgres、SQLServer、Derby Client、Derby Embedded、IBM Type
4、gbase8t、gbase8s、sr、db2、highgo、uxdb、GaussDB 100、InspurK-DB、linkoopdb、oceanbase、MogDB 等。</td></tr></table>

# 2.2. 系统要求
<table><tr><td>系统组件</td><td>系统要求</td></tr><tr><td>Java 环境</td><td>JDK8-JDK24
·支持 Oracle JDK,但部分 Oracle JDK 版本商用收费,在生产使用时请注意商业授权,或采用 Open JDK、Tong JDK。
·启用国密认证,JDK 要求 JDK8-JDK11。
·使用虚拟线程,JDK 要求 JDK21。
·需要安装 JDK,不能仅安装 JRE。仅安装 JRE 会导致 TongWeb 部分功能不能使用。
·Linux 下若使用 IBM JDK,则需要手动放置如下 jar 包到“${tongweb.home}/lib/compatible”目录,否则启动 TongWeb 失败。
    ·JDK 8.0
        bcprov-jdk15on-1.70.jar
    ·JDK 8.0+
        bcprov-jdk18on-1.78.1.jar</td></tr><tr><td>内存</td><td>不低于80MB</td></tr><tr><td>硬件空间</td><td>不低于1024MB
推荐最低配置:4核CPU、4G内存、20G硬盘</td></tr><tr><td>浏览器</td><td>Microsoft IE 9/11、Mozilla Firefox 66.0-102.0、Google Chrome 75.0-105.0</td></tr></table>

# 3. 资料准备

# 3.1. 获取安装包
已购买 TongWeb 产品，在 TongWeb 产品光盘中提供 TongWeb 安装包。

# 3.2. 获取 license
安装 license 后，才能启动 TongWeb，可选择 “本地授权” 或者 “服务授权”。
• 本地授权：通过提供的 license.dat 文件进行本地授权。
• 服务授权：通过 License Server 服务进行远程服务授权。
<table><tr><td>类型</td><td>获取 license</td><td>描述</td></tr><tr><td>本地授权</td><td>license.dat</td><td>购买 TongWeb 产品后，TongWeb 产品光盘中提供了 license.dat 授权认证文件。</td></tr><tr><td>服务授权</td><td>License Server 安装包</td><td>购买 TongWeb 产品后，发货的同时发 License Server 安装包。
关于如何搭建 License Server 服务，详见《License Server_V4.5安装部署手册》。</td></tr></table>

# 说明：
TongWeb 支持轻量版、标准版、企业版、教学版及容器云版。
版本功能差异通过 license 进行控制，请获取指定版本的 license。

# 4. 安装指南

# 4.1. 安装 TongWeb
完成安装包解压即完成 TongWeb 产品的安装。
获取的安装包以 “TongWebx.x.x.x.tar.gz” 为例说明。
注意：
支持在 Kubernetes（k8s）平台上通过 Operator 部署 TongWeb，详情请咨询东方通相关人员。

# 4.1.1. Windows 平台
将安装包拷贝到待安装 TongWeb 的目录，解压到的目录即为产品的安装目录。

# 4.1.2. Linux 平台
1. 将安装包拷贝到待安装 TongWeb 的目录。
2. 执行如下命令，解压安装包，解压后的目录即为产品的安装目录。
```batch
tar -zxfv TongWebx.x.x.x.tar.gz 
```

# 4.2. License 授权认证
您需要安装 license 后，才能启动 TongWeb，可选择 “本地授权” 或者 “服务授权”。
• 本地授权：通过提供的 license.dat 文件进行本地授权。
• 服务授权：通过 License Server 服务，进行远程服务授权。

# 4.2.1. 方式1：本地授权
通过读取本地的 “license.dat” 文件的方式进行授权认证。
购买 TongWeb 产品后，在 TongWeb 产品光盘中提供有 license 文件。
将获取的 license.dat 文件复制到安装完成的 TongWeb 根目录下：${tongweb.home}，如下图所示。
```ini
[root@nemstertongweb]#ll   
总用量79532   
drwxr-xr-x 3 root root 186 11月 18 02:05 bin   
drwxr-xr-x 3 root root 21 11月 18 02:04 domains   
drwxr-xr-x 3 root root 17 11月 18 02:04 lib   
-rwxr-xr-x 1 root root 1410 11月 18 02:04 license.dat   
drwxr-xr-x 12 root root 263 11月 18 13:54 version.1.3.1-6xP   
-rw-r--r-- 1 root root 81435448 11月 18 02:05 version.1.5.1-6xPoot.zip
```
注意：
• License 将根据授权产品名称、授权版本、版本类型以及授权 IP 来判断与产品是否匹配。
• 对于永久 license，用户在启动 TongWeb 后，系统会自动激活该 license，并且与 127.0.0.1 对应的 mac地址进行绑定。
◦ 若永久 license 的创建时间（create_time）处于 90 天以内，用户可自由拷贝，且拷贝后的 license均能正常完成激活与绑定操作。
◦ 若永久 license 的创建时间已超过 90 天，则该 license 将自动失效，无法再进行激活与绑定，进而导致 TongWeb 无法正常启动。

# 4.2.2. 方式2：服务授权
通过远程搭建的 License Server 服务进行远程授权。

# 4.2.2.1 支持 License Server 版本
4.5.0.0 及以上版本。

# 4.2.2.2 前置条件
• 已搭建 License Server 服务。
关于如何搭建 License Server 服务，请参见《License Server_V4.5安装部署指南》。
• 已获取 License Server 服务的 IP 地址和端口（默认端口 $" 8 8 8 8 "$ ）。
• 已联系东方通相关人员获取 “TongWebx.x.x.x-license-server-client.jar” 文件，并存放到“${tongweb.home}/lib/system” 目录或者 “${tongweb.base}/lib/system” 目录。

# 4.2.2.3 注意事项
在服务授权过程中，系统会优先使用 License Server 进行授权。若在调用 License Server 服务过程中出现调用失败的情况，则自动切换至本地证书进行授权；与此同时，系统会定期进行远程激活，以确保授权有效性。
工作流程，如下所示。
1. 当本地无证书时，进行远程校验并下载证书。
2. 当本地有证书时，先校验本地证书，然后定期尝试远程激活；未激活状态最多存活 180 天。
3. 当远程校验通过，后续周期校验均走远程校验，并同时更新本地证书。
4. 当网络不通时，则使用本地证书。重启时进行本地校验，遵循未激活 180 天规则。

# 4.2.2.4 操作步骤
• 方式1：添加 Java 启动系统属性
1. 进入 “${tongweb.home}/bin” 目录。
2. 打开 admin.[bat|sh] 脚本。
3. 在文件中，添加 Java 启动时的系统属性，如下所示。
4. License Server IP地址和端口，配置格式为 [ip]:[port]
多个IP地址使用英文逗号分隔，如 192.168.1.1:8888,192.168.1.2:8888
5. 当使用https时，请务必配置为 “https://[ip]:[port]”
```txt
-Dserver.tongweb license license-ips=License Server IP地址和端口
```

# 4.2.2.5 License Server 公钥信息，需要从 License Server 控制台获取
-Dserver.tongweb.license.publicKey=License Server 公钥信息
• 方式2：添加 license.properties 文件
1. 进入 “${tongweb.home}” 目录。
2. 新建 “license.properties” 文件，并在文件中，添加如下配置信息。
3. License Server IP地址和端口，配置格式为 [ip]:[port]
多个IP地址使用英文逗号分隔，如 192.168.1.1:8888,192.168.1.2:8888
4. 当使用https时，请务必配置为 “https://[ip]:[port]”
server.tongweb.license.license-ips=License Server IP地址和端口
#License Server 公钥信息，需要从 License Server 控制台获取
server.tongweb.license.publicKey=License Server 公钥信息

# 4.2.3.方式3：在 tongweb.xml 中添加启动参数
若在默认实例 “domain1” 中配置，对当前节点有效，在其他实例配置则只对自己生效。
1. 进入 “${tongweb.base}/conf” 目录。
2. 打开 “tongweb.xml” 文件。
3. 在 <start-args> 标签下，添加如下启动参数。
```xml
<arg name="-Dserver.tongweb license license-ips= License Server IP 地址和端口"/>
```
```txt
<arg name="-Dserver.tongweb LicensePublicKey=LicenseServer 公钥信息（需要从 LicenseServer 控制台获取）"/>
```

# 4.3. 验证 JDK 环境
启动 TongWeb 前，要求在 PATH 中已设置 JDK 环境变量。本章节介绍如何验证 JDK 环境。

# 4.3.1. 前置条件
• 已从官网下载并安装JDK。
• JDK 版本要求：JDK8-JDK24。

# 4.3.1.1 注意：
◦ 支持 Oracle JDK，但部分 Oracle JDK 版本商用收费，在生产使用时请注意商业授权，或采用 OpenJDK、Tong JDK。
◦ 启用国密认证，JDK 要求 JDK8-JDK11。
◦ 使用虚拟线程，JDK 要求 JDK21。
◦ 需要安装 JDK，不能仅安装 JRE。仅安装 JRE 会导致 TongWeb 部分功能不能使用。
◦ Linux 下若使用 IBM JDK，则需要手动放置如下 jar 包到 “${tongweb.home}/lib/compatible” 目录，否则启动 TongWeb 失败。
▪ JDK 8.0 
```batch
bcprov-jdk15on-1.70.jar 
```
▪ JDK 8.0+ 
```batch
bcprov-jdk18on-1.78.1.jar 
```

# 4.3.2. 操作步骤
在命令行界面，输入 “java -version”；若回显信息为 Java 版本，说明安装成功。
以 Windows 系统为例，如下图所示。
```batch
C:\Windows\system32\cmd.exe   
Microsoft Windows [版本10.0.22000.1219] (c) Microsoft Corporation。保留所有权利。   
C:\Users>java -version java version "1.8.0_281" Java(TM)SE Runtime Environment (build 1.8.0_281-b09) Java HotSpot(TM)64-Bit Server VM (build 25.281-b09, mixed mode)
```

# 4.3.3. 系统查找 PATH 顺序
1. 首次安装 TongWeb 后，启动 TongWeb 时，优先查找系统环境变量里的 PATH。
2. 当 TongWeb 在用户的系统环境变量 PATH 没查找到 java 命令时，TongWeb 将无法启动。
Linux 环境下，支持在 “${tongweb.home}/bin” 目录中手动创建 “JAVA_HOME.txt” 文件，并配置 java的安装路径。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/b5301f077b880ac9e81ebf9032525a5c791571c4c10bacf4dc1a63584f37cb4d.jpg)
Windows 环境不支持。
```txt
[root@master bin]#vim JAVA_HOME.txt   
[root@master bin]#ll   
总用量40   
-rwxr-xr-x1 root root 772 11月 29 02:04 admin.sh   
-rwxr-xr-x1 root root 57 11月 29 02:04 commandstool.sh   
-rwxr-xr-x1 root root 63 11月 29 02:04 forcestop.sh   
-rw-r--r--1 root root 4 11月 29 17:17 JAVA_HOME.txt   
-rwxr-xr-x1 root root 60 11月 29 02:04 startd.sh   
-rwxr-xr-x1 root root 59 11月 29 02:04 startserver.sh   
-rwxr-xr-x1 root root 58 11月 29 02:04 stopserver.sh   
-rw-r--r--1 root root 5815 11月 29 02:04 tongweb-launcher.jar   
-rwxr-xr-x1 root root 54 11月 29 02:04 version.sh   
drwxr-xr-x2 root root 150 11月 29 02:04 windows
```
◦ 当 TongWeb 可以正常启动后，您也可以在
"${tongweb.home}/domains/domain1/conf/tongweb.xml" 中设置 TongWeb 实例的JAVA_HOME。
或者进入管理控制台 > “基础配置” > “JVM 配置” > “环境变量”，添加 java 路径及环境变量。此处设
置的 JAVA_HOME 为当前 TongWeb 实例缺省使用的 java。
▪ 不同的 TongWeb 实例可通过 “tongweb.xml” 自定义为不同的 java。
▪ 若不设置 TongWeb 实例的 JAVA_HOME，则 TongWeb 实例使用 PATH 或者 JAVA_HOME.txt配置的 java。
▪ 当设置了系统环境变量 PATH 或者 JAVA_HOME.txt 时，又设置了 TongWeb 实例的JAVA_HOME，TongWeb 实例使用自身配置的 JAVA_HOME。

# 4.4. 启停 TongWeb

# 4.4.1. Windows 平台
• 启动 TongWeb
运行 startd.bat ，以后台模式启动 TongWeb 应用服务器默认实例。
•说明：
◦ 若用户仅调试或临时运行实例，可通过执行 startserver.bat 脚本，以前台模式启动。
◦ “startserver.bat” 和 “startd.bat” 启动方式支持使用 JAVA_OPTS 环境变量设置 JVM 启动参数。
• 停止 TongWeb
◦ 方式1：使用 $\mathsf { C t r } | + \mathsf { C }$ 停止
在 TongWeb 的运行窗口直接按下 $\mathsf { C t r } | + \mathsf { C }$ ，即可终止 TongWeb 的运行。
◦ 方式2：通过停止脚本（stopserver.bat）停止
在“${tongweb.home}/bin/windows”目录下运行“stopserver.bat”，即可停止 TongWeb 的运行。
◦ 方式3：通过强停脚本（forcestop.bat）停止
在 “${tongweb.home}/bin/windows” 目录下运行 “forcestop.bat”，即可停止 TongWeb 的运行。
• 说明：
当 TongWeb 服务器难以成功停止，或者停止过程出现意外阻塞的情况时，您可以执行强停脚本，停止 TongWeb 服务器。
强制停止通常是以强制杀进程的方式实现。

# 4.4.2. Linux 平台

# 4.4.2.1 启动 TongWeb
1. 执行如下命令，查看 Openfiles 值为默认 $\yen 1024$ (该值偏小)，建议设置为 “65535”。
ulimit -a 
2. 修改 “/etc/security/limits.conf”，增加如下两行配置。
* soft nofile 65535 
* hard nofile 65535 
3. 执行如下命令，进入到 “${tongweb.home}/bin” 目录。
```txt
cd ${tongweb.home}/bin 
```
4. 若没有执行权限，则执行如下命令，将 bin 目录下的文件权限变更为可执行权限。
```batch
chmod -R 755 * 
```
5. 执行如下命令，以后台模式启动 TongWeb 服务器实例。
```txt
./startd.sh 
```
若回显信息出现 “Server startup in xx seconds”，则说明启动 TongWeb 成功。

# 4.4.2.2 注意：
▪ “./startd.sh” 表示以后台模式启动服务器，在 Linux 下建议以后台模式启动，可防止 SSH 断开后，TongWeb 进程停止。
▪ 若用户仅调试或临时运行服务，则可以运行 “startserver.sh” 脚本，在当前终端可以直接看到服务器输出的日志信息等。
▪ “startserver.sh” 和 “startd.sh” 启动方式支持使用 JAVA_OPTS 环境变量设置 JVM 启动参数。

# 4.4.2.3 停止 TongWeb
◦ 方式1：使用 $\mathsf { C t r } | + \mathsf { C }$ 停止
在 TongWeb 的运行窗口直接按下 $\mathsf { C t r } \mathsf { I } { + } \mathsf { C }$ ，即可终止 TongWeb 的运行。
◦ 方式2：通过停止脚本（stopserver.sh）停止
在 “${tongweb.home}/bin” 目录下运行 “stopserver.sh”，即可停止 TongWeb 的运行。
◦ 方式3：通过强停脚本（forcestop.sh）停止
在 “${tongweb.home}/bin” 目录下运行 “forcestop.sh”，即可停止 TongWeb 的运行。
说明：
▪ 当 TongWeb 服务器难以成功停止或者停止过程出现意外阻塞的情况时，您可以通过执行强停脚本的方式停止 TongWeb 服务器。
▪ 强制停止通常是以强制杀进程的方式实现。

# 4.5. 查看 TongWeb 进程
• 使用 jps 命令，可查看的运行的 TongWeb 进程，例如 “TongWebMain”、“tongweb-launcher.jar”等。
• Linux 下，使用 ps -ef|grep tongweb 命令查看进程时，可以看到 TongWeb 进程参数末尾包含如下所示字样。
```csv
java ...TongWebMainSERVER_TYPE=console,SERVER_NAME=domain1  
java ...TongWebMainSERVER_TYPE node,SERVER_NAME(node01  
java ...TongWebMainSERVER_TYPE=instance,SERVER_NAME=aaa 
```
通过如上字样，可区分 console、node、instance。
参数说明，如下所示。
◦ SERVER_TYPE 表示角色类型，对应三种角色，分别为：console、node、instance。
◦ SERVER_NAME 表示业务上的名称，默认为 domain 域的名称，支持通过 “全局配置” $>$ “集中管理”中的 “别名” 来修改。
“别名” 修改的约束：
▪ 通过集中管理创建的节点，别名默认为节点的 id；
▪ 通过集中管理创建的实例，别名默认为实例的别名；
▪ 自动或手动注册节点的别名由节点进程自行独立维护，不与集中管理有关联；
▪ 自动注册的实例，集中管理上显示的别名和实例自身全局配置里的别名，自动双向关联。
若是后台启动，如 ./startd.sh 启动或通过集中控制台启动，则位于结尾的 "&" 符号之前。

# 4.6. 卸载 TongWeb
TongWeb 为免安装版本。
若需要卸载 TongWeb，请先将 TongWeb 服务器停止。然后，直接删除安装目录即可完成 TongWeb 的卸载。

# 5. 关键文件说明
安装包解压后文件说明。

# 5.1. 根目录文件
TongWeb 根目录文件如下图所示。
<table><tr><td colspan="7">[redic#-n#t#r tongweb]# ll</td></tr><tr><td colspan="7">总用量 79532</td></tr><tr><td>drwxr-xr-x</td><td>3</td><td>root</td><td>root</td><td>186</td><td>02:05</td><td>bin</td></tr><tr><td>drwxr-xr-x</td><td>3</td><td>root</td><td>root</td><td>21</td><td>02:04</td><td>domains</td></tr><tr><td>drwxr-xr-x</td><td>3</td><td>root</td><td>root</td><td>17</td><td>02:04</td><td>lib</td></tr><tr><td>-rwxr-xr-x</td><td>1</td><td>root</td><td>root</td><td>1410</td><td>02:04</td><td>license.dat</td></tr><tr><td>drwxr-xr-x</td><td>12</td><td>root</td><td>root</td><td>263</td><td>13:54</td><td>version.a.s.t.sh#h#t</td></tr><tr><td>-rw-r--r--</td><td>1</td><td>root</td><td>root</td><td>81435448</td><td>02:05</td><td>version.a.s.t.sh#h#t.zip</td></tr></table>
TongWeb 根目录文件说明，如下表所示。
<table><tr><td>文件名称</td><td>文件说明</td></tr><tr><td>bin</td><td>可执行文件。</td></tr><tr><td>domains</td><td>该目录下为TongWeb实例存放的位置。
domains/domain1为TongWeb提供的默认实例。
说明：
支持将domain1重命名为特定业务名称（如console、master等），以便于定制运维。</td></tr><tr><td>lib</td><td>全域共享的jar包。
lib/app目录下为应用共享的jar包。</td></tr><tr><td>version*.zip</td><td>对应产品版本的库文件。</td></tr><tr><td>license.dat</td><td>安装的TongWeb license文件。</td></tr></table>

# 5.2. 实例目录文件
TongWeb 默认实例存放于 “${tongweb.home}/domains/domain1”目录。
创建的新实例目录位于 “${tongweb.base}/domains”，以实例名进行命名，实例下的目录结构相同，如下图所示。
<table><tr><td colspan="7">domain1]# ll</td></tr><tr><td colspan="7">总用量0</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>root</td><td>root</td><td>6 7月</td><td>19</td><td>00:24 autodeploy</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>root</td><td>root</td><td>127 7月</td><td>19</td><td>00:24 conf</td></tr><tr><td>drwxr-xr-x</td><td>3</td><td>root</td><td>root</td><td>17 7月</td><td>19</td><td>00:24 data</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>root</td><td>root</td><td>6 7月</td><td>19</td><td>00:24 deployment</td></tr><tr><td>drwxr-xr-x</td><td>3</td><td>root</td><td>root</td><td>17 7月</td><td>19</td><td>00:24 lib</td></tr><tr><td>drwxr-xr-x</td><td>4</td><td>root</td><td>root</td><td>27 7月</td><td>19</td><td>00:24 logs</td></tr><tr><td>drwxr-xr-x</td><td>3</td><td>root</td><td>root</td><td>19 7月</td><td>19</td><td>00:24 temp</td></tr></table>
TongWeb 实例目录文件说明，如下表所示。
<table><tr><td>文件名称</td><td>说明</td></tr><tr><td>autodeploy</td><td>TongWeb 提供的默认自动部署目录。</td></tr><tr><td>conf</td><td>配置文件所在目录。
·console.xml: 集中管理和用户登录配置文件。
·tongweb.xml: 主配置文件。
·default-web.xml: 默认的 Web 描述文件。</td></tr><tr><td>data</td><td>用于存放应用备份文件。
·/app/backup: 备份部署应用存放路径。
·/app/recycle: 解部署应用存放路径。
·/app/update: 创建应用增量存放路径。
·/conf: 存放自动备份的 console.xml 和 tongweb.xml 文件目录。
·/secure: 存放受管的可信文件列表的文件目录。
·tongweb.pid: 用于记录进程的 PID, 在做开机自启动 systemd 服务时, 指明进程 PID 文件。
注意:
·删除该文件后会宕机。
·如果是老版本升级, 本地实例在重启并完成升级后, 会提示启动失败, 此时可忽略该提示; 当重启集中管理后状态将会恢复正常。</td></tr><tr><td>deployment</td><td>已部署应用的应用程序目录。</td></tr><tr><td>lib</td><td>实例的库文件。例如: 数据源的驱动包, 可提前存放在 “/lib” 目录下。</td></tr><tr><td>logs</td><td>存放日志文件的目录。
·access: 访问日志存放路径。开启访问日志后, 可查看, 默认关闭。
·audit: 审计日志存放路径。
·gc: gc垃圾回收日志存放路径。
·jvm: 进程jvm相关日志存放路径。
·server: 系统日志存放路径。</td></tr><tr><td>temp</td><td>TongWeb 启动后，生成的目录。用于存放 TongWeb 运行过程中产生的临时文件。</td></tr></table>

# 5.3. 主配置文件
TongWeb 提供了可视化界面和主配置文件两种方式供用户配置和管理应用。
主配置文件的路径，如下所示。
• 主配置文件： $\$ 1$ {tongweb.base}\conf\tongweb.xml
• 集中管理和用户登录配置文件：${tongweb.base}\conf\console.xml
• 默认的 web 描述文件： $\$ 1$ {tongweb.base}\conf\default-web.xml

# 5.3.1. 双重备份
主配置文件（tongweb.xml 和 console.xml）在运行期间支持双重备份，防止被手动篡改。

# 5.3.1.1 双重备份
指内存和实例路径 “${tongweb.base}\conf” 下，分别进行实时备份。

# 5.3.1.2 实例路径下实时备份文件
• 文件：tongweb.xml.lastUpdated 和 console.xml.lastUpdated
• 路径：${tongweb.base}\conf

# 5.3.2. 系统自动恢复
为了确保主配置文件的安全性，在 TongWeb 运行期间采取了防篡改措施。若主配置文件被意外篡改，系统会自动恢复并不会应用这些修改。
• 启动 TongWeb 时，若检测到主配置文件被意外删除或者篡改，而导致启动失败，则会使用实例路径下实时备份文件 “.lastUpdated” 恢复主配置文件。
• 若 “主配置文件” 和 “实例路径下实时备份文件” 在运行期间被删除或篡改，TongWeb 会自动使用内存里的实时备份文件进行恢复。

# 5.3.3. 如何修改
当用户在预置自动部署相关配置、配置启动参数、自定义控制台前缀、设置信任 IP 等情况下时，需要修改主配置文件并使其生效。
可参照如下任意一种方式修改主配置文件。
• 方式1：
停止 TongWeb 服务器，然后再进行修改。
• 方式2：
在确保安全的情况下，在控制台关闭 “服务器主配置文件防篡改” 开关，默认 “开启”。
该开关用于禁止在 TongWeb 运行期间对主配置文件进行修改。
1. 登录 TongWeb 控制台。
2. 切换到目标实例。
3. 在左侧菜单栏中，选择 “安全管理” $>$ “安全策略”，进入安全策略页面。
4. 在 “文件防篡改” 页签，关闭 “服务器主配置文件防篡改” 开关。
5. 关闭后，重启 TongWeb 服务器使配置生效。
6. 该开关关闭后，用户即可在 TongWeb 运行期间修改主配置文件。
修改完成后，请及时开启该开关，防止主配置文件在运行期间被篡改。

# 5.4. 脚本文件说明
• ${tongweb.home}/bin：包含了 Linux 平台上产品启动、停止等所需要的可执行脚本文件。
• ${tongweb.home}/bin/windows：包含了 Windows 平台上产品启动、停止等所需要的可执行脚本文件。
<table><tr><td>文件名称</td><td>说明</td></tr><tr><td>admin.[bat|sh]</td><td>服务器主脚本。可用于管理服务器内部资源、服务器启停、版本信息、安装TongWeb自启动服务,生成轻量版、嵌入版等。关于脚本的使用说明,请参见《TongWeb_V8.0控制台使用手册》“进阶使用”中的“admin.[bat|sh]脚本使用说明”章节。</td></tr><tr><td>cli.[bat|sh]</td><td>命令行工具。交互式执行命令且可通过“Tab”键提示或者自动补全参数。关于命令行工具的使用说明,请参见《TongWeb_V8.0命令行工具手册》。</td></tr><tr><td>commandstool.[bat|sh]</td><td>命令行工具。关于命令行工具的使用说明,请参见《TongWeb_V8.0命令行工具手册》。</td></tr><tr><td>forcestop.[bat|sh]</td><td>强停服务器实例脚本。支持 stopserver.[bat|sh]:all 和 forcestop.[bat|sh]:all 命令停止 domains 下所有实例。</td></tr><tr><td>set_home.sh</td><td>设置 TongWeb 安装目录环境变量的公共脚本。</td></tr><tr><td>standalone.sh</td><td>以单个进程的模式来运行TongWeb服务器实例。此模式通常更节省系统资源，但基于tongweb.xml配置的自动化重启（如宕机重启、定时重启）和自定义环境变量等功能将不可用。
容器环境推荐使用standalone脚本（如果无需控制台输出日志，可以前往页面的“系统日志”模块，将“启用控制台日志”开关关闭）。</td></tr><tr><td>startd.[bat|sh]</td><td>以后台模式启动服务器实例。
支持 startd.[bat|sh]:all 后台启动 domains 下所有实例。
注意：
•物理机或虚拟机环境下，推荐时使用 startd.[bat|sh] 脚本。
•Linux环境下建议以后台模式启动服务器实例，执行 startd.sh 脚本，可防止 SSH 断开后，TongWeb 进程停止。</td></tr><tr><td>startserver.[bat|sh]</td><td>启动服务器实例。</td></tr><tr><td>stopserver.[bat|sh]</td><td>停止服务器实例。
支持 stopserver.[bat|sh]:all 和 forcestop.[bat|sh]:all 命令停止 domains 下所有实例。</td></tr><tr><td>tongweb-launcher.jar</td><td>启动引导程序。</td></tr><tr><td>version.[bat|sh]</td><td>运行脚本后，可查看TongWeb版本信息（产品版本、构建时间、命名空间、运行模式、OS、JVM等）和License信息。</td></tr></table>

# 5.5. 临时目录说明
临时文件目录 “${tongweb.base}/temp/cache”，如下图所示。
```txt
[root@root temp]# cd cache/ cache]#ll   
总用量0   
drwxr-xr-x2 root root 61月 17 10:57 ejb   
drwxr-xr-x2 root root 61月 17 10:56 sign   
drwxr-xr-x3 root root 191月 17 10:56 work
```
TongWeb 临时文件目录说明如下表所示。
<table><tr><td>文件名称</td><td>说明</td></tr><tr><td>work</td><td>用于存放 TongWeb 在运行时的编译文件，即“.class”文件。例如：JSP 编译后的文件。清空 work 目录，然后重启 TongWeb，即可达到清除缓存的作用。修改 console 访问前缀、停止应用、卸载应用后均会自动清理 work 目录。</td></tr></table>

# 5.6. 日志文件说明
日志文件目录如下图所示。
```txt
[root@centos tongweb]# ll domains/domain1/logs/ total 0   
drwxr-xr-x 2 root root 53 Aug 20 14:37 audit   
drwxr-xr-x 2 root root 6 Aug 20 14:26 gc   
drwxr-xr-x 2 root root 21 Aug 20 14:27 jvm   
drwxr-xr-x 2 root root 55 Aug 20 14:37 server   
drwxr-xr-x 2 root root 61 Aug 20 14:37 sessionha   
drwxr-xr-x 2 root root 49 Aug 20 14:41 subprocess 
```
日志路径：${tongweb.base}/logs
TongWeb 日志文件说明，如下表所示。
<table><tr><td>文件名称</td><td>文件说明</td></tr><tr><td>access</td><td>访问日志。启用访问日志后,即可生成访问日志文件。默认为“关闭”。进入TongWeb管理控制台&gt;“日志管理”&gt;“访问日志配置”页面,启用访问日志。</td></tr><tr><td>audit</td><td>审计日志。用于跟踪记录用户对服务器进行的操作。仅安全审计员可查看和配置审计日志。</td></tr><tr><td>gc</td><td>gc垃圾回收日志。默认为“关闭”。若需要GC垃圾回收日志,可通过如下方式进行配置。1.进入TongWeb管理控制台&gt;“基础配置”&gt;“JVM配置”&gt;“GC策略”页面。2.开启“记录GC日志”,并设置“GC日志文件”路径即可。默认路径为“logs/gc/gc.log”。</td></tr><tr><td>jvm</td><td>进程 JVM 相关的日志。启用记录 JVM 日志后，系统才会传给 JVM 加载，生成 JVM 日志文件。默认为“开启”。若需要关闭，可通过如下方式进行配置。1. 进入 TongWeb 管理控制台 &gt; “基础配置” &gt; “JVM 配置” &gt; “JVM 日志”页面。2. 关闭“记录 JVM 日志”即可。关闭“记录 JVM 日志”后，日志将不记录到日志文件中。</td></tr><tr><td>server</td><td>服务器运行期间产生的系统日志。</td></tr><tr><td>sessionha</td><td>部署应用时，在“会话与Cookie”页签中，选择会话服务器后，即开启会话高可用。会话相关日志输出到独立的“${tongweb.base}/logs/sessionha”日志目录。</td></tr></table>

# 6. 快速使用指引

# 6.1. 访问 TongWeb 控制台

# 6.1.1. Windows 平台

# 6.1.1.1. 步骤1：启动 TongWeb
1. 进入 “${tongweb.home}/bin/windows” 目录。
2. 运行 startd.bat ，以后台模式启动 TongWeb 应用服务器默认实例。
关于启停 TongWeb 的更多信息，详见《TongWeb_V8.0安装与使用指引》的 “启停 TongWeb” 章节。

# 6.1.1.2. 步骤2：登录管理控制台
首次登录 TongWeb 管理控制台，请通过安装 TongWeb 的本机浏览器进行登录。
1. 在浏览器地址中，输入如下地址，按 Enter，进入 TongWeb 管理控制台登录页面。
https://localhost:9060/console 
# 6.1.1.2.1 说明：
◦ 请使用 “https” 协议访问 TongWeb 管理控制台。
◦ 9060：为 TongWeb 管理控制台默认监听端口。
2. 在输入登录地址后，会弹出安全提示页面。
3. 直接单击 “高级” > “继续访问”，即可访问 TongWeb 管理控制台登录页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/b77b33a7d4e2f9e1ccb18ddc39d59e5c59787b7679839fd7cf58207f9477b556.jpg)
4. 输入 “账户名称” 和 “账户密码”，进入 TongWeb 管理控制台。
系统管理员默认账户，如下所示。
◦ 账户名称：thanos
◦ 账户密码：thanos123.com
◦ 动态密码：若未开启 “动态密码”，则可不填写，默认未开启。
关于如何开启 “动态密码”，请参见 《TongWeb_V8.0控制台使用手册》中 “开启动态密码”。
# 6.1.1.2.2 注意：
◦ 当用户首次登录失败后，需要输入登录验证码。
◦ 默认情况下，用户连续认证失败 5 次后，账户将被锁定。
◦ 默认情况下，当控制台会话持续超时达 15 分钟，账号将自动退出登录。
◦ 用户也可使用 OAuth2 协议登录控制台，详见 《TongWeb_V8.0控制台使用手册》中的 “OAuth2 协议登录控制台”。
关于控制台安全相关策略，请进入控制台 “集中管理” > “安全配置” $>$ “控制台安全”，设置控制台相关安全策略。
5. 阅读《许可协议》，并勾选 “已阅读并同意《许可协议》”。
注：当用户勾选 “已阅读并同意《许可协议》” 选项时，页面会弹出 “下次自动勾选” 选项。若用户勾选此选项，系统将自动记录该勾选状态。
6. 单击 “登录”，即可进入 TongWeb 控制台 “默认实例” 的 “首页” 页面。
注意：
默认情况下，控制台会话超时时间为 15 分钟。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/0fc70a417677b4516b284e1250afedacb2fd90d1fb2a776c45623e885311f11f.jpg)


# 6.1.1.3. 步骤3：修改初始密码
为了保障系统的安全性，成功登录 TongWeb 管理控制台后，系统强制要求修改“初始密码”。
修改初始密码，要求在安装 TongWeb 的本机 IP 上进行修改。
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击“集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择“安全配置”>“修改密码”，进入修改密码页面。
4. 修改初始密码，参数说明如下表所示。
<table><tr><td>参数</td><td>参数说明</td></tr><tr><td>原始密码</td><td>登录系统的原始密码。</td></tr><tr><td>新密码</td><td>用于登录系统的新密码。
密码长度介于10-20个字符之间，新密码不能和原始密码相同。</td></tr><tr><td>确认密码</td><td>确认用于登录系统的新密码。</td></tr><tr><td>动态密码</td><td>默认“不开启”。
若需要开启“动态密码”，请参见《TongWeb_V8.0控制台使用手册》中的“开启动态密码”。</td></tr></table>
5. 密码修改完成后，单击“更新”，更新密码信息。
若界面弹出 “修改密码成功” 提示信息，则说明修改密码成功。

# 6.1.1.4. 步骤4：设置信任 IP
若仅使用安装 TongWeb 的本机访问 TongWeb 控制台，则可跳过此步骤。
若需要使用远程浏览器访问 TongWeb 管理控制台，需要将远程浏览器所在的主机 IP 设置为“信任 IP”。
设置为 “*” 表示信任所有机器（不建议）。
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击“集中管理”，进入集中管理页面。
3. 选择 “安全配置” $>$ “控制台安全”，进入控制台页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/8ca04c9688624c68ddb48786319d52249eb7dbf3882385f39d2289079140142e.jpg)
4. 设置 “信任 IP” 即可。
信任 IP 设置完成后，您即可通过信任 IP 所在浏览器客户端访问 TongWeb 管理控制台。

# 6.1.2. Linux 平台

# 6.1.2.1. 步骤1：设置信任 IP
首次登录 TongWeb 管理控制台前，请在安装 TongWeb 的本机将远程浏览器访问 TongWeb 的主机 IP 设置为 “信任 IP”。
设置为 “*” 表示信任所有机器（不建议）。
本示例采用修改主配置文件 “console.xml” 的方式，设置信任 IP。

# 6.1.2.1.1 注意事项
• 主配置文件 “console.xml” 具备防篡改限制，在运行期间禁止对其进行修改。若需要修改并使其生效，请确保 TongWeb 服务器处于停止状态，然后再进行修改。
• 若已启动 TongWeb 且不希望停止 TongWeb，可使用命令行方式来设置信任 IP。详细信息请参见《TongWeb_V8.0控制台使用手册》的 “控制台安全” $>$ “设置信任 IP” 章节。

# 6.1.2.1.2 前置条件
已获取远程浏览器客户端所在的 IP 地址。

# 6.1.2.1.3 操作步骤
1. 进入 “${tongweb.base}/conf” 目录。
2. 打开 “console.xml” 文件。
3. 将 “trustedIP” 设置为远程浏览器客户端所在的主机 IP。
注：请根据实际情况替换为您远程浏览器客户端的主机 IP。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/641d4b5525fe4e4c574a432e0feac8c56c69d9d0f0a8bd655efec33e6aeef3d7.jpg)


# 6.1.2.2. 步骤2：启动 TongWeb
1. 进入 “${tongweb.home}/bin” 目录。
2. 运行 ./startd.sh ，以后台模式启动 TongWeb 服务器默认实例。
若回显信息出现 “Server startup in xx seconds”，则说明启动 TongWeb 成功。
关于启停 TongWeb 的更多信息，详见《TongWeb_V8.0安装与使用指引》的 “启停 TongWeb” 章节。

# 6.1.2.3. 步骤3：登录管理控制台
通过远程浏览器客户端访问 TongWeb 管理控制台。
1. 在浏览器地址中，输入如下地址，按 Enter，进入 TongWeb 管理控制台登录页面。
```txt
https://<TongWebIP>:9060/console 
```
说明：
◦ <TongWebIP>：表示 TongWeb 主机 IP 地址。
◦ 9060：TongWeb 管理控制台默认监听端口。
用户可根据需要打开 “${tongweb.base}/conf/tongweb.xml” 文件，进行修改。
注：tongweb.xml 为 TongWeb 主配置文件，具有防篡改限制。若需要修改并使其生效，请先停止TongWeb 服务器，然后再进行修改。
2. 在输入登录地址后，会弹出安全提示页面。
3. 直接单击 “高级” $>$ “继续访问”，即可访问 TongWeb 管理控制台登录页面。
4. 输入 “账户名称” 和 “账户密码”，进入 TongWeb 管理控制台。
系统管理员默认账户，如下所示。
◦ 账户名称：thanos
◦ 账户密码：thanos123.com
◦ 动态密码：若未开启 “动态密码”，则可不填写，默认未开启。
关于如何开启 “动态密码”，请参见 《TongWeb_V8.0控制台使用手册》中 “开启动态密码”。
5. 注意：
◦ 当用户首次登录失败后，需要输入登录验证码。
◦ 默认情况下，用户连续认证失败 5 次后，账户将被锁定。
◦ 默认情况下，当控制台会话持续超时达 15 分钟，账号将自动退出登录。
◦ 用户也可使用 OAuth2 协议登录控制台，详见 《TongWeb_V8.0控制台使用手册》中的 “OAuth2 协议登录控制台”。
关于控制台安全相关策略，请进入控制台 “集中管理” > “安全配置” $>$ “控制台安全”，设置控制台相关安全策略。
6. 阅读《许可协议》，并勾选 “已阅读并同意《许可协议》”。
注：当用户勾选 “已阅读并同意《许可协议》” 选项时，页面会弹出 “下次自动勾选” 选项。若用户勾选此选项，系统将自动记录该勾选状态。
7. 单击 “登录”，即可进入 TongWeb 控制台 “默认实例” 的 “首页” 页面。

# 6.1.2.3.1 注意：
默认情况下，控制台会话超时时间为 15 分钟。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/6358d902ad097777ff6c0a7627e2e99c1a99d544ae2dc26ebbda95b060a52fe9.jpg)


# 6.1.2.4. 步骤4：修改初始密码
为了保障系统的安全性，成功登录 TongWeb 管理控制台后，系统强制要求修改 “初始密码”。
修改初始密码后，才允许用户执行相关操作。
(1) 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击“集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择“安全配置”>“修改密码”，进入修改密码页面。
4. 修改初始密码，参数说明如下表所示。
<table><tr><td>参数</td><td>参数说明</td></tr><tr><td>原始密码</td><td>登录系统的原始密码。</td></tr><tr><td>新密码</td><td>用于登录系统的新密码。
密码长度介于10-20个字符之间，新密码不能和原始密码相同。</td></tr><tr><td>确认密码</td><td>确认用于登录系统的新密码。</td></tr><tr><td>动态密码</td><td>默认“不开启”。
若需要开启“动态密码”，请参见《TongWeb_V8.0控制台使用手册》中的“开启动态密码”。</td></tr></table>
5. 密码修改完成后，单击“更新”，更新密码信息。
若界面弹出 “修改密码成功” 提示信息，则说明修改密码成功。

# 6.2. 部署应用
在登录 TongWeb 控制台后，默认进入 “默认实例” 页签，本地路径为
“${tongweb.home}/domains/domain1/”。 
本章节以自带用例 “${tongweb.home}/version*/examples/examples.war” 为例介绍如何在 “默认实例” 页面部署一个应用，并通过部署的应用来调用数据源。
“examples.war” 中包含多个示例，如下以 “jdbc $>$ noXaDsWeb” 为例说明。

# 6.2.1 注意事项
• 用户可以根据需要前往 “集中管理” $>$ “服务管理” $>$ “实例” 页面自行创建本地实例（存放在
“${tongweb.home}/domains/” 目录），并在创建的本地实例上部署应用。
• 用户也可以根据需要前往 “集中管理” $>$ “服务管理” 页面，通过添加节点并搭建集群的方式，实现对多个实例的统一管理，进而在搭建的集群上部署应用。
• 在多实例场景下，建议默认实例 domain1 只做管理，不部署应用。
• 在不同节点搭建集群的场景下，为了避免普通运维人员对默认实例 domain1 进行操作，系统支持用户采用权限分配的方式，将默认实例 domain1 隐藏，详见《TongWeb_V8.0控制台使用手册》。

# 6.2.2. 前置条件
• 开通 TongWeb 所在机器和数据库服务器之间的端口，确保能够连接成功。
• 确保浏览器客户端所在的 IP 为信任 IP。
• 由于示例需要调用数据源，因此需要提前准备好数据库源相关信息。
比如：连接 URL、驱动类、用户名、密码、相应版本对应的 JDBC 的 jar 包。
数据源示例以如下信息为例说明。
◦ 连接URL：jdbc:mysql://168.1.1.1:3316/zmm2
◦ 驱动类：com.mysql.cj.jdbc.Driver
◦ 用户名：root
◦ 密码：123456
◦ 驱动包：mysql-connector-java-8.0.11.jar
若已将驱动包存放在 “${tongweb.base}/lib/” 目录下，则在部署应用时，“驱动包位置” 参数不填写。

# 6.2.3. 创建数据源
当应用需要调用数据源时，需要首先在控制台创建数据源。
由于 “examples.war” 的 “jdbc $>$ noXaDsWeb” 示例中已配置好数据源名称 “testdb”，因此创建的数据源名称必须为 “testdb”。
说明：
用户可解压 “examples.war”，并打开 “examples/jdbc/noXaDsWeb/initdb.jsp” 文件，查看数据源名称。
```javascript
DataSource dataSource = (DataSource) context.lookup("testdb"); 
```
操作步骤，如下所示。
1. 登录 TongWeb 管理控制台。
2. 进入 “默认实例” 页面。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源页面。
4. 单击 “创建”，进入创建数据源页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/e7b9d3b284ee5b5e1980afa51bf306dfc7a7c34bcffa453252c9f8ec3162395b.jpg)
5. 配置数据源的相关参数，如下表所示。
<table><tr><td>参数</td><td>说明</td><td>示例</td></tr><tr><td>数据源名</td><td>数据源名称</td><td>testdb</td></tr><tr><td>绑定 JNDI 名</td><td>数据源的别名被用作绑定到 JNDI 资源树上的名称。</td><td>不填写</td></tr><tr><td>数据库连接方式</td><td>使用 TongWeb 预置的 Jdbc 模板连接数据库。</td><td>使用 JDBC 标准方式</td></tr><tr><td>连接URL</td><td>数据库连接URL。请根据实际环境填写。</td><td>jdbc:mysql://168.1.13.108:3316/zmm2</td></tr><tr><td>驱动类</td><td>数据库驱动类的全名称。</td><td>com.mysql.cj.jpeg.Driver</td></tr><tr><td>用户名</td><td>登录数据库的用户名。</td><td>root</td></tr><tr><td>密码</td><td>登录数据库用户名对应的密码。</td><td>****(请根据实际环境填写)</td></tr><tr><td>驱动包位置</td><td>设置数据库驱动类Jar文件在服务器上的绝对路径。多个路径以“,”分隔。
·若在TongWeb启动前，已经将驱动包文件放置到“${tongweb.base}/lib”，则可不设置驱动Jar的位置。
例如存放在默认实例下：
“${tongweb.home}/domains/domain1/lib/mysql-connector-java-8.0.11.jar”。
·若在TongWeb启动后再放置，则需要重启TongWeb服务器才能生效。</td><td>不填写</td></tr></table>
6. 其他参数采用默认值，您也可以根据需要进行配置。
7. 配置完成后，单击 “添加”，完成数据源的创建操作。
8. 在数据源列表中，单击已创建数据源所在行的 “测试”，测试连接是否成功。
若界面弹出 “数据源测试成功” 提示信息，则说明数据源连接成功。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/69c8d3cc5becd8ab285737e79112fec9ce9fbf8696f90f74381602c3ade65eb8.jpg)


# 6.2.4. 部署应用
您可以通过指定应用文件在服务器上位置的方式部署应用。
1. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
2. 单击 “部署”，进入应用/部署页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/7cc08f19acd599183895222a148cb0772945b3af69712d23f8e17c244ddee82f.jpg)
3. 配置应用的相关参数，如下表所示。
<table><tr><td>参数</td><td>说明</td><td>示例</td></tr><tr><td>应用名</td><td>非必填，若不填写，则系统自动获取应用包的名称作为应用名。</td><td>example</td></tr><tr><td>应用来源</td><td>·上传文件：通过上传文件的方式，上传应用文件。
    控制台默认关闭上传文件功能。
    若需要开启，需要单击控制台左上角的“集中管理”，并选择“安全配置”&gt;“控制台安全”，进入控制台安全页面。
    在控制台安全页面，关闭“禁用文件上传”，并重启TongWeb服务器即可。
·服务器文件：从服务器端指定的位置读取应用文件。</td><td>服务器文件</td></tr><tr><td>部署路径</td><td>指定应用文件在服务器的位置。应用文件必须是“.war”、“.jar”、“.ear”、“.rar”等标准类型，否则将会导致部署失败。</td><td>应用所在路径：
: ${tongweb.home}/version*/examples/examples WAR</td></tr><tr><td>虚拟主机</td><td>应用所部署到的虚拟主机，可共用虚拟主机提供的资源和管理控制。</td><td>localhost</td></tr><tr><td>启动优先级</td><td>必填项，用以约束应用的启动顺序。该值越小越优先启动。</td><td>99</td></tr><tr><td>其他参数</td><td>应用的其他属性</td><td>采用默认值</td></tr></table>
4. 应用属性配置完成后，单击 “添加”，完成应用部署操作。
若界面弹出 “应用添加成功” 提示信息，则说明应用部署成功。
在应用/列表页面，可查看已部署的应用。

# 6.2.5. 访问应用
应用部署成功后，您可以访问部署的应用，并测试通过访问应用的方式调用数据源。
1. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用/列表页面。
2. 在已部署应用所在行的操作列，单击 “链接”，进入应用/链接页面。
应用 链接
状态: true
消息: 应用链接成功
http://192.168.22.185:8088/examples 
3. 单击生成的 URL 链接，即可访问您部署的应用。
说明：
TongWeb 默认为应用分配的访问端口为8088。
4. 测试调用数据源。
访问部署的应用，并依次单击 "Jdbc NoXaDataSource" $>$ "create" $>$ "GlobalDataSource"，若页面显示如下信息，则说明调用数据源成功。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/a64bb24192856f0bf5d249dbffd479870e934fc9bc659587b8dcbc596810e6c4.jpg)
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/d99c2a065348d9ffef5b9b497bffe25e0af03fbfa286dca7f6fce5896210d8be.jpg)
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/41617c5ad935ec912bc04a1200bec3835e87611a966f0927e5783e900bdcf756.jpg)
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/93c6b90401cadafdfec799afae7619eb616389dcb74146e0081eafef9da30239.jpg)
192.168.22.185:8088/examples/jdbc/noXaDsWeb/GlobalDataSource 
GET DATASOURCE 
$= = = = = = = = = = = = = = =$ GET DATASOURCE SUCCEESSFULLY: == = =: 
Result is: 
----accno:20 balance:9 customer:user1 

# 6.3. 安全加固

# 6.3.1. 安全启动
您可以根据需要在管理控制台中，选择 “安全管理” > “安全策略”，进入 “启停安全” 页签，开启 “启动限制”。
开启 “启动限制” 后，对 TongWeb 的启动进行权限验证，验证通过后才能正常启动 TongWeb，否则启动将会终止。

# 6.3.2. 安全停止
您可以根据需要在管理控制台中，选择 “安全管理” > “安全策略”，进入 “启停安全” 页签，开启 “安全停止”。
开启“安全停止后”，当使用 TongWeb 的停止脚本（ stopserver.[bat|sh] 或者 forcestop.[bat|sh] ）停止TongWeb 服务时，需要输入正确的系统管理员密码，才能停止。

# 7. “标准版/企业版/教学版” 生成轻量版

# 7.1. 方式一：通过控制台切换为轻量模式
通过标准版、企业版或教学版控制台切换为 “轻量模式”，以轻量模式运行的 TongWeb 与 License 控制台的轻量版相同。
1. 登录 TongWeb 管理控制台。
2. 切换至目标实例。
3. 在左侧导航栏中，选择 “基础配置” $>$ “全局配置”，进入全局配置页面。
4. 打开 “轻量模式” 开关。
5. 单击 “更新”，并重启 TongWeb 服务器使配置生效。

# 7.2. 方式二：通过控制台生成轻量版
通过标准版、企业版或教学版控制台生成的轻量版，主要用于云平台、微服务环境。
功能上等同于轻量版，但不包含控制台、国密算法、本地节点实例管理、本地节点的会话服务器管理、命令行、JMX、REST接口。
1. 登录 TongWeb 管理控制台。
2. 单击控制台左上角的 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “扩展支持” $>$ “版本生成”，进入版本生成页面。
4. 单击 “创建”，进入版本生成/创建页面。
5. “版本类型” 选择为 “轻量版”。
6. 根据需要选择是否需要控制台，并勾选命名空间。
7. 其他参数请根据需要配置。
8. 单击 “生成”，即可生成轻量版。
在版本生成列表中，可查看已构建的产品版本，包含产品版本名称、版本类型、含控制台、命名空间、版本号等信息。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-05/6255f9b8-bf08-4706-a66b-93b9357c1e94/f9c15abcd11068f14df5c4350513d3f3958fdc023e0d73cec74e7c3712d9daaf.jpg)
