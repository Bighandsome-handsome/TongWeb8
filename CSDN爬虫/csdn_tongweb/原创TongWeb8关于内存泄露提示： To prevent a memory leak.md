# 原创TongWeb8关于内存泄露提示： To prevent a memory leak

> 原文地址: https://blog.csdn.net/realwangpu/article/details/131570604

---

原因：
该问题与
https://blog.csdn.net/realwangpu/article/details/109510297
相同，TongWeb7, TongWeb8在卸载应用时，会尝试回收可能存在的内存泄露， 本质应该从应用方面解决。
解决办法：
若无法修改应用，只是不想看到这些警告信息，则TongWeb8提供关闭功能项。这样仅仅是屏蔽了警告日志输出，无法从根本上解决可能存在的内存泄露。
场景模拟用例：
import com.mysql.cj.jdbc.AbandonedConnectionCleanupThread;

@WebListener
public class DBListener implements ServletContextListener {
	
	 private Driver driver = null; 

	 public void contextInitialized(ServletContextEvent sce) { 
		 //模拟常见的数据源驱动加载
		 try {
			 Class.forName("com.mysql.cj.jdbc.Driver");
			 String url = "jdbc:mysql://localhost:3306/test?user=root&password=111";
			 driver = DriverManager.getDriver(url);
			 DriverManager.registerDriver(driver);
		} catch (Exception e) {
			e.printStackTrace();
		}
		 
	 }
	 
	 public void contextDestroyed(ServletContextEvent sce) { 
         //卸载应用，若当应用卸载时没有驱动卸载操作则报警告：To prevent a memory leak, the JDBC Driver has been forcibly unregistered.
	      try {
			DriverManager.deregisterDriver(driver);
			//不同数据库处理不同，注册mysql还会起一个名为[mysql-cj-abandoned-connection-cleanup]的线程, 需要如下方式停止下来。
			AbandonedConnectionCleanupThread.uncheckedShutdown();
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	 }
}
#完整日志如下：
2023-05-04 09:26:04 [WARN] - The web application [testdb] registered the JDBC driver [com.tong.DBDriver] but failed to unregister it when the web application was stopped. To prevent a memory leak, the JDBC Driver has been forcibly unregistered.