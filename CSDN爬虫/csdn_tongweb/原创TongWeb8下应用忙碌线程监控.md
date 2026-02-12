# 原创TongWeb8下应用忙碌线程监控

> 原文地址: https://blog.csdn.net/realwangpu/article/details/133127843

---

问题 ：
在系统运行过程中发现TongWeb进程占用CPU过高，需要分析是应用哪里引起的问题。
分析过程(仅限Linux环境)：
1.  通过top命令查看TongWeb的java进程占用的CPU情况。
查看误区：不要以为java进程CPU占到398%就是高，若服务器为8核，则CPU占用满显示为800%。
[root@localhost bin]# top
top - 10:45:58 up  1:19,  1 user,  load average: 3.65, 1.56, 0.68
Tasks: 171 total,   2 running, 169 sleeping,   0 stopped,   0 zombie
%Cpu(s): 38.7 us,  1.0 sy,  0.0 ni,  60.0 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st
KiB Mem :  1863220 total,    73452 free,  1352208 used,   437560 buff/cache
KiB Swap:  2097148 total,  2095604 free,     1544 used.   214164 avail Mem

   PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND
 13382 root      20   0 4235564 834012  17716 S 398.0 44.8   2:52.53 java
 14871 root      39  19  108036   1032    744 R  1.3  0.1   0:00.92 updatedb
  7153 root      20   0  483536  34056   7660 S  0.3  1.8   0:12.50 containerd
 14491 root      20   0  162036   2356   1604 R  0.3  0.1   0:00.11 top
     1 root      20   0  133892   3892   2344 S  0.0  0.2   0:01.70 systemd
     2 root      20   0       0      0      0 S  0.0  0.0   0:00.00 kthreadd
     3 root      20   0       0      0      0 S  0.0  0.0   0:00.15 ksoftirqd/0
     5 root       0 -20       0      0      0 S  0.0  0.0   0:00.00 kworker/0:0H
     7 root      rt   0       0      0      0 S  0.0  0.0   0:00.00 migration/0
2. 进入TongWeb8控制台查看忙碌线程，查看占用CPU高的线程栈所执行的操作。
3. 若服务器CPU很忙，已经无法打开TongWeb控制台，则可以用./admin.sh busy-thread  [pid]  [线程数]  命令查看。
[root@localhost bin]# ./admin.sh busy-thread  13382  200
Execute the command: busy-thread
[1] Busy(48.3%) thread(14214/0x3786) stack of java process(13382):
"TW-0.0.0.0-8088-16" #200 daemon prio=5 os_prio=0 tid=0x00007ff508459800 nid=0x3786 runnable [0x00007ff5148e6000]
   java.lang.Thread.State: RUNNABLE
        at com.tong.TestServlet.doGet(TestServlet.java:52)
        at javax.servlet.http.HttpServlet.service(HttpServlet.java:503)
        at javax.servlet.http.HttpServlet.service(HttpServlet.java:590)
        at com.tongweb.server.core.ApplicationFilterChain.enterApp(ApplicationFilterChain.java:366)
        at com.tongweb.server.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:236)
        at com.tongweb.server.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
        at com.tongweb.web.websocket.server.WsFilter.doFilter(WsFilter.java:32)
        at com.tongweb.server.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:197)
        at com.tongweb.server.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:162)
        at com.tongweb.server.core.StandardWrapperValve.invoke(StandardWrapperValve.java:146)
        at com.tongweb.server.core.StandardContextValve.invoke(StandardContextValve.java:78)
        at com.tongweb.ee.server.OpenEJBValve.invoke(OpenEJBValve.java:29)