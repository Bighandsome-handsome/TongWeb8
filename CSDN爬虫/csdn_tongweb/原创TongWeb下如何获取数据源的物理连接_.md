# 原创TongWeb下如何获取数据源的物理连接?

> 原文地址: https://blog.csdn.net/realwangpu/article/details/152126080

---

在某些场景下需要获取数据源的物理连接，以针对特定数据库进行处理，如下：

```java
import oracle.sql.BLOB;
import oracle.jdbc.OracleConnection;

......

(OracleConnection)con
......
oracle.sql.BLOB  blob=(oracle.sql.BLOB)rs.getBlob(1).;
// 像DBCP数据源可以通过如下方式获取
Connection conn = ds.getConnection();
Connection dconn = ((DelegatingConnection) conn).getInnermostDelegate();
...
conn.close()
```
在TongWeb下获取数据源物理连接的方法如下：
1. 将数据源驱动包放在TongWeb的lib目录下，不在应用的lib下放驱动包，也不在配置数据源时指定驱动包路径，否则多份类加载会引起类冲突。类似如下：
```java
java.lang.ClassCastException: oracle.sql.BLOB cannot be cast to oracle.sql.BLOB]
  at com.tong.Test.testDB(Test.java:81)]
  at com.tong.Test.doGet(Test.java:45)]
  at javax.servlet.http.HttpServlet.service(HttpServlet.java:622)]
  at javax.servlet.http.HttpServlet.service(HttpServlet.java:729)]
  at com.tongweb.catalina.core.ApplicationFilterChain.internalDoFilter(ApplicationFilterChain.java:230)]
```
2. TongWeb7,8 获取数据源物理连接代码如下. 该类TongWeb7.0在tongweb.jar中，TongWeb8.0在
modules/ejb/tongweb-ejb.jar中。
```java
import com.tongweb.tongejb.resource.jdbc.managed.util.NativeJdbcExtractor

try {
 DataSource dataSource = (DataSource) new InitialContext().lookup("jdbc/test");
 Connection con = dataSource.getConnection();
 System.out.println("逻辑连接：" + con);
 Connection physicalconnection = 
 NativeJdbcExtractor.extractNativeConnection(con);
 System.out.println("物理连接：" + physicalconnection);
 con.close();
} catch (Exception e) {
 e.printStackTrace();
}
```