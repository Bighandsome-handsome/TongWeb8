# 原创TongWeb因sigar而崩溃

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109639529

---

问题描述：
在某些平台下启动TongWeb后JVM进程崩溃，在TongWeb的bin目录下生成hs_err_pid*.log文件，开头内容如下：
#
#  EXCEPTION_ACCESS_VIOLATION (0xc0000005) at pc=0x0000000010014ed4, pid=19512, tid=0x0000000000004fbc
#
# JRE version: Java(TM) SE Runtime Environment (8.0_261-b12) (build 1.8.0_261-b12)
# Java VM: Java HotSpot(TM) 64-Bit Server VM (25.261-b12 mixed mode windows-amd64 compressed oops)
# Problematic frame:
# C
[sigar-amd64-winnt.dll+0x14ed4]
#
# Failed to write core dump. Minidumps are not enabled by default on client versions of Windows
解决办法：
sigar用于监控机器CPU、内存，删除后不影响TongWeb使用。
1.增加启动参数-DenableSigar=false关闭sigar。
2. 将TongWeb的lib/sigar目录删除即可。