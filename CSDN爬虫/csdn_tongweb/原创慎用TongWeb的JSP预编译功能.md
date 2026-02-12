# 原创慎用TongWeb的JSP预编译功能

> 原文地址: https://blog.csdn.net/realwangpu/article/details/115263876

---

第一次访问JSP时会有一个JSP编译成class的过程，所以第一次访问JSP会慢，于是应用服务器通常有JSP预编译功能。但是这个功能会影响部署速度，所以尽量少用。如下图在部署应用时有一个"JSP预编译"选项，针对JSP较多的应用该项不要选，否则部署过程会把所有JSP编译一遍，造成部署时间过长，且每次重新启动TongWeb也会重新编译应用的JSP，造成TongWeb启动时间过长。
可以从server.log日志看到，一旦配了"JSP预编译"则每次TongWeb启动都会把所有JSP编译一遍，造成启动时间过长。
```bash
[2021-03-27 13:47:45 367] [INFO] [main] [core] [Built File: \jsp\jsp2\el\functions.jsp]
[2021-03-27 13:47:45 436] [INFO] [main] [core] [Built File: \jsp\jsp2\el\implicit-objects.jsp]
[2021-03-27 13:47:45 488] [INFO] [main] [core] [Built File: \jsp\include\foo.jsp]
[2021-03-27 13:47:45 547] [INFO] [main] [core] [Built File: \jsp\include\include.jsp]
[2021-03-27 13:47:45 596] [INFO] [main] [core] [Built File: \jsp\forward\forward.jsp]
[2021-03-27 13:47:45 662] [INFO] [main] [core] [Built File: \jsp\forward\one.jsp]
[2021-03-27 13:47:45 739] [INFO] [main] [core] [Built File: \jsp\error\err.jsp]
[2021-03-27 13:47:45 795] [INFO] [main] [core] [Built File: \jsp\error\errorpge.jsp]
[2021-03-27 13:47:45 870] [INFO] [main] [core] [Built File: \jsp\dates\date.jsp]
[2021-03-27 13:47:45 935] [INFO] [main] [core] [Built File: \jsp\colors\colrs.jsp]
[2021-03-27 13:47:46 008] [INFO] [main] [core] [Built File: \jsp\checkbox\checkresult.jsp]
[2021-03-27 13:47:46 090] [INFO] [main] [core] [Built File: \jsp\cal\cal1.jsp]
[2021-03-27 13:47:46 168] [INFO] [main] [core] [Built File: \jsp\cal\cal2.jsp]
[2021-03-27 13:47:46 245] [INFO] [main] [core] [Built File: \jsp\async\async1.jsp]
[2021-03-27 13:47:46 300] [INFO] [main] [core] [Built File: \jsp\async\async3.jsp]
[2021-03-27 13:47:46 361] [INFO] [main] [core] [Built File: \jsp\async\index.jsp]
[2021-03-27 13:47:46 697] [INFO] [main] [core] [TongWeb server startup complete in 33487 ms.]
```