# 原创TongWeb7企业版巡检脚本

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/134830242

---

#!/bin/bash
# 设置输出编码为 UTF-8
export LANG=en_US
.
UTF-8
export LC_ALL=en_US
.
UTF-8
# 检查是否已安装 sysstat 包
if
!
command
-
v pidstat &>
/
dev/null
;
then
echo
"sysstat 包未安装，正在安装..."
# 检查操作系统类型并执行相应的安装命令
if
[
-
f
/
etc/redhat-release
]
;
then
# CentOS/RHEL/Fedora
sudo yum install
-
y sysstat
  elif
[
-
f
/
etc/debian_version
]
;
then
# Debian/Ubuntu
sudo apt-get update
    sudo apt-get install
-
y sysstat
  elif
[
-
f
/
etc/kylin-release
]
;
then
# Kylin
sudo apt-get update
    sudo apt-get install
-
y sysstat
else
echo
"未知的操作系统类型，无法安装 sysstat 包！"
exit
1
  fi
# 检查安装是否成功
if
!
command
-
v pidstat &>
/
dev/null
;
then
echo
"sysstat 包安装失败，请手动安装后再运行脚本！"
exit
1
  fi
echo
"sysstat 包安装成功！"
fi
if
[
-
z
"
$1
"
]
;
then
echo
"请指定输出文件名！"
exit
1
fi
# 检查是否指定输出文件名和安装目录
if
[
-
z
"
$1
"
]
|
|
[
-
z
"
$2
"
]
;
then
echo
"请指定输出文件名和TongWeb安装目录"
exit
1
fi

output_file=
$1
tongweb_dir=
$2
#PROCESS_NAME="$TONGWEB/tongweb"  # 进程名
pid=$
(
cat
$tongweb_dir
/
tongweb
.
pid
)
# 获取进程ID
if
[
-
z
"
$pid
"
]
;
then
echo
"进程未启动"
exit
0
fi
echo
"检测到进程：
$pid
"
>>
$1
echo
"=========================================================================="
>>
$1
echo
"查看进程状态："
>>
$1
if
ps
-
p
$pid
>
/
dev/null
then
ps
-
fp
$pid
>>
$1
else
echo
"进程
$pid
不存在"
>>
$1
fi
echo
"=========================================================================="
>>
$1
echo
"查看授权信息版本号："
>>
$1
$tongweb_dir
/
bin/version
.
sh >>
$1
echo
"=========================================================================="
>>
$1
echo
"查看jvm配置："
>>
$1
cat
$tongweb_dir
/
bin/external
.
vmoptions >>
$1
echo
"=========================================================================="
>>
$1
echo
"根据进程号查看CPU使用率："
>>
$1
pidstat
-
p
$pid
>>
$1
echo
"=========================================================================="
>>
$1
echo
"查看内存使用情况："
>>
$1
free
-
h >>
$1
echo
"=========================================================================="
>>
$1
echo
"查看磁盘空间使用情况："
>>
$1
df
-
h >>
$1
echo
"=========================================================================="
>>
$1
echo
"系统核心参数设置情况："
>>
$1
sysctl
-
a
|
grep shm >>
$1
sysctl
-
a
|
grep sem >>
$1
echo
"=========================================================================="
>>
$1
echo
"查看JDK版本："
>>
$1
java
-
version 2>&1
echo
"=========================================================================="
|
tee
-
a
$1
java
-
version 2>&1
|
tee
-
a
$1
echo
"=========================================================================="
|
tee
-
a
$1
使用说明：
如脚本名为inspection.sh，赋执行权限
chmod +x inspection.sh
执行脚本需指定输出文件名和TongWeb安装目录
./inspection.sh test.log /test/TongWeb7.0.4.9_M1_Enterprise_Linux
查看生成的输出文件-巡检内容