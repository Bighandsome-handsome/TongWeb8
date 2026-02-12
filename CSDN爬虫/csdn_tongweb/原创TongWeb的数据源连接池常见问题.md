# 原创TongWeb的数据源连接池常见问题

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109525749

---

TongWeb的数据源连接池占满时的日志
[2019-05-13 11:15:56] [WARNING] [other] [Failed to obtain/create connection from connection pool [ test ]. Reason : The connection could not be allocated:[http-nio-8080-exec-1] Timeout: Pool empty.
Unable to fetch a connection in 30 seconds, none available[size:10; busy:10; idle:0; lastwait:30000
].]
红色标记内容的意思是：当前使用的数据源连接数已经等于数据源的最大连接数，不能分配更多的连接。
造成数据源问题的原因通常有如下四种：
1. 数据库JDBC驱动包与数据库版本不对应。
2. 数据源最大连接设置过小，并发访问量大的时候数据源连接数不足。或是把最大连接数设的比数据库允许的连接数还大，
数据源配的最大连接数肯定得小于等于数据库允许的连接数
。
3. 应用存在连接泄漏的地方，打开数据库连接后没有正确的关闭，长时间运行后TongWeb的连接池被逐渐占光。
4. 应用存在SQL执行时间过长，长时间执行SQL,占用连接不释放。
TongWeb数据源泄露分析方式：
1. 最低级的错误是连接池配置过小，导致并发时连接不够用。若无论增大连接为多少，连接还不够用，就需要继续分析了。
2.在数据源配置中设置“泄漏超时”为30秒，跟踪连接池中的连接泄漏，并将获取连接的调用栈（堆栈）记录下来， 只记录不关闭连接。
当超时后，以WARNING级别将该堆栈信息输出到日志。从日志中可以分析到哪里存在未关闭的连接。日志示例如下：
[2019-05-13 11:05:55] [WARNING] [data-source] [
A potential connection leak detected for connection pool test. The stack trace of the thread is provided below
: java.lang.Exception
at com.tongweb.web.webutil.jdbc.pool.ConnectionPool.getThreadDump(ConnectionPool.java:1117)
at com.tongweb.web.webutil.jdbc.ThorTomEEDataSourceCreator$ThorTomEEConnectionPool.borrowConnection(ThorTomEEDataSourceCreator.java:1065)
at com.tongweb.web.webutil.jdbc.ThorTomEEDataSourceCreator$ThorTomEEConnectionPool.borrowConnection0(ThorTomEEDataSourceCreator.java:942)
at com.tongweb.web.webutil.jdbc.ThorTomEEDataSourceCreator$ThorTomEEConnectionPool.borrowConnection(ThorTomEEDataSourceCreator.java:921)
at com.tongweb.web.webutil.jdbc.pool.ConnectionPool.getConnection(ConnectionPool.java:219)
at com.tongweb.web.webutil.jdbc.ThorTomEEDataSourceCreator$ThorTomEEConnectionPool.getConnection(ThorTomEEDataSourceCreator.java:729)
at com.tongweb.web.webutil.jdbc.ThorTomEEDataSourceCreator$ThorTomEEDataSource.superGetConnection(ThorTomEEDataSourceCreator.java:241)
at com.tongweb.web.webutil.jdbc.ThorTomEEDataSourceCreator$ThorTomEEDataSource.getConnection(ThorTomEEDataSourceCreator.java:264)
at com.tongweb.tongejb.resource.jdbc.managed.local.ManagedDataSource.getConnection(ManagedDataSource.java:50)
at com.tongweb.tongejb.resource.jdbc.managed.local.ThorManagedDataSource.getConnection(ThorManagedDataSource.java:77)
at com.tongweb.web.webutil.jdbc.ThorTomEEDataSourceCreator$ThorTomEEDataSourceProxy.getConnection(ThorTomEEDataSourceCreator.java:488)
at org.apache.jsp.
DBPoolTest_jsp
._jspService(DBPoolTest_jsp.java:105)
at com.tongweb.web.jasper.runtime.HttpJspBase.service(HttpJspBase.java:70)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:722)
at com.tongweb.web.jasper.servlet.ThorJspServletWrapper.service(ThorJspServletWrapper.java:264)
at com.tongweb.web.jasper.servlet.ThorJspServlet.serviceJspFile(ThorJspServlet.java:270)
at com.tongweb.web.jasper.servlet.ThorJspServlet.service(ThorJspServlet.java:232)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:722)
at com.tongweb.web.thor.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:305)
at com.tongweb.web.thor.core.ApplicationFilterChain.doFilter(ApplicationFilterChain.java:210)
3. 找到应用代码泄露的地方, 确认代码是否会执行
connection.close()。
4. 若100%确认应用代码执行了
connection.close()，
则可能是SQL的执行时间过长，长时间占用连接。这时可以打开“SQL执行时间过滤”记录下执行时间长的SQL，针对SQL进行优化。若确认某些SQL执行时间过长，且数据库无法优化，可设置"语句超时"本质为设置java.sql.Statement.setQueryTimeout(int timeout)。
但要注意某些国产数据库的JDBC驱动不支持该方法
。
同时若应用忘记关游标statement.close()导致 maximum open cursors exceeded，可以勾上“语句跟踪”自动关闭statement。
SQL日志：  2020-11-06 13:18:26 [SQL execute 17 ms : select FILE_ID,FILE_NAME,DIS_NAME,FILE_SORT,DATA_TYPE,SERV_ID,FILE_CAT,FILE_HIST_COUNT,FILE_CHECKSUM,ORIG_FILE_ID,BELONG_DEPT,BELONG_DEPT_NAME,ITEM_CODE,FILE_PATH,FILE_SIZE,FILE_MTYPE,S_FLAG,S_CMPY,S_MTIME,FILE_MEMO,DATA_ID,WF_NI_ID,S_USER,S_UNAME,S_DEPT,S_DNAME,IESS_PROCESS_ID from SY_COMM_FILE where 1=1 and data_id = '09G2NPWVZ7TUJrJ4UKkzpr' order by FILE_SORT Thread[http-nio2-0.0.0.0-8088-exec-14]#3 Connection[2115205428]]
5. 若SQL超时不起作用，应用又不能修改代码执行connection.close()。只能用最终解决办法“
泄露回收
”。勾上后会在泄露超时后强制关闭连接，
会导致正在执行的SQL中断，一定要考虑清楚再配上。