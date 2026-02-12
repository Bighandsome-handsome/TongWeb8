# 原创TongWeb上反复重部署应用后异常：application instance has been stopped already 或OutOfMemoryError：Metaspace

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109510297

---

问题现象：
在不重启TongWeb的情况下，在TongWeb控制台反复部署应用。会导致TongWeb日志报错如下：
java.lang.IllegalStateException: Illegal access:
this web application instance has been stopped already
. Could not load [redis.clients.util.Pool]. The following stack trace is thrown for debugging purposes as well as to attempt to terminate the thread which caused the illegal access.
或：
OutOfMemoryError
：Metaspace,
OutOfMemoryError:PermGen space
或：The web application [testdb] registered the JDBC driver [com.mysql.cj.jdbc.Driver] but failed to unregister it when the web application was stopped. To prevent a memory leak, the JDBC Driver has been forcibly unregistered.
问题原因：
应用经常会启动一些端口或线程，在应用服务器上卸载、反复部应用时，若应用代码写的不规范，就不能正常停止应用建的线程，导致应用卸载不干净。 老应用未停止线程加载类报此异常:this web application instance has been stopped already。  同时会导致不能卸载class，反复加载class导致元数据区不足报
OutOfMemoryError
：Metaspace。
正确的解决方法：
TongWeb的重部署reload实际操作就是对应用重新stop又start了一下，而这个过程除了class的重新加载以外，对于web.xml中定义的一些资源，如listener，filter，servlet等也重新stop又start了。 所以这时需要在listener或servlet的destory中停止应用启动的端口或线程，这样应用服务器在stop应用时，会调用
listener
或
servlet
的
destory
方法，从而可以销毁应用创建的资源。而很多应用却忽略了这一点。
如：重写
listener   contextDestroyed
方法，该卸载的卸载。实际应用常用spring初始化，注意将spring资源关闭。
#重写listener contextDestroyed()方法
public void contextDestroyed(ServletContextEvent arg0) {
   // 停止应用的端口
   //停止应用的线程
}
#重写servlet destroy()方法
public void destroy() {  
   // 停止应用的端口
   //停止应用的线程
}
#典型的场景就是启动了quartz线程池。无关闭quartz线程池步骤，则重部署一次应用，线程池就多增加一份。
<bean id="SpringQtzJobMethod"  class="org.springframework.scheduling.quartz.MethodInvokingJobDetailFactoryBean">


#通过annotation关闭实例
import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import org.springframework.stereotype.Component;
 
@Component
public class Test{
	public Test(){
		System.out.println("test constructor...");
	}
	
	//对象创建并赋值之后调用
	@PostConstruct
	public void init(){
		System.out.println("test....@PostConstruct...");
	}
	
	//容器移除对象之前
	@PreDestroy
	public void detory(){
		System.out.println("test....@PreDestroy...");
	}
 
}
临时解决办法：
在修改不了应用的前提下，只要重部署了应用，就需要重启TongWeb释放无用的线程和Metaspace区内存，否则多次重部署后还会报该异常。 增大-XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=512m参数只能缓解 OutOfMemoryError
：
Metaspace出现的频率。
同时引申出另外一个问题：在不重启TongWeb的情况下，能否动态更新应用、在线升级应用版本？
答：实际场景下往往不能这样用，原因同上，很多应用不在卸载时执行应用资源关闭操作。这样导致TongWeb的热部署功能、应用版本在线更新功能基本不可用。
若重部署应用不重启TongWeb通常会引发以下三类问题：
(1)
容易导致内存溢出，报错如下：
#JDK7及以下
OutOfMemoryError:PermGen space
#JDK8及以上
OutOfMemoryError
：
Metaspace
(2) 应用启动的
端口占用报错：
address has been used。
(3) 线程不断增加，而不释放报错：this web application instance has been stopped already。
(4)  反复加载动态库，报错：UnsatisfiedLinkError Native Library xxx.so already loaded。
https://blog.csdn.net/realwangpu/article/details/109554060