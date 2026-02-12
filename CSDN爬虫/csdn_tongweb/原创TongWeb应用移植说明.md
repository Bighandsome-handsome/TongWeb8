# 原创TongWeb应用移植说明

> 原文地址: https://blog.csdn.net/realwangpu/article/details/151955350

---

本文主要指导用户如何将应用移植到TongWeb上，替代Weblogic 、WebSphere 、tomcat、JBoss、Jetty等产品。主要针对有移植需求的用户，前期了解移植过程，对移植要求、步骤有一个初步的认知。
一、TongWeb可移植的应用
TongWeb为JavaEE/JakartaEE应用服务器，移植的应用主要是采用JavaEE/JakartaEE规范标准开发的java应用。不适合移植到TongWeb上的应用：
1.  NET应用为Microsoft 的开发平台，支持ARM、X86等Linux平台，某些国产操作系统也声明支持，但其本身不需要TongWeb来运行。
2.  PHP应用TongHttpServer产品支持。
二、梳理应用基本架构
多数情况下用户并不了解应用开发实际采用的JavaEE/JakartaEE规范，对版本规范之间的差异也并不清楚，所以用户可以从以下几个其它方面来判断应用采用的JavaEE/JakartaEE规范标准，然后根据应用的规范来规划移植的步骤。
1. 通过应用采用的JDK版本来判断。若应用可以在JDK1.7上运行，则说明不可能采用JavaEE8规范。但反之并不成立，采用了JDK1.8，并不代表采用了JavaEE8规范。
2. 通过应用采用的开源框架来判断采用的规范，开源框架网站通常有对容器的规范要求，通过官方说明即可判断。比如：用Spring Boot2.x，Spring Framework6.x、Spring Boot3.x。
而有些应用采用的组件是绑定某种应用服务器的，无法直接移植，如: Kettle是免费的开源轻量级ETL工具，是基于Java语言开发的，其内嵌的jetty是采用API方式，这种方式必然涉及到代码的修改。
3. 应用包结构检查
主要检查应用包的结构，以判断需要采用的TongWeb版本，以及是否需要对应用包进行改造：
(1) 根据采用的应用服务器来检查，若是tomcat则可以判断为web应用，若是Weblogic等，则重点检查有没有EJB。
(2)  若应用包含有ejb jar则特别注意，不同应用服务器ejb jar的JNDI命名规则不同，
EJB2.x的配置文件不同应用服务器不同， 如：Weblogic的weblogic-ejb-jar.xml和WebSphere的ibm-ejb-jar-bnd.xml对应TongWeb的tongweb-ejb-jar.xml文件。
(3) 若应用为嵌入式jar/war包，则重点检查是以Spring Boot方式使用的，还是直接以API方式直接启动容器的，并采用TongWeb嵌入版。
4. 更加深入的了解则需要查看应用代码，重点查看使用的JavaEE  API，有没有采用绑定某一应用服务器的代码。但此方式仅适合移植出现问题时参考应用代码，并不适合移植前查看应用所有代码。
5. 了解其在其它应用服务器上的配置
通过了解应用在其它应用服务器上的配置，以了解应用用了哪些功能，如：数据源、安全域、JMS配置等等。这些配置将来也需要配置在TongWeb上。以最常见的数据源为例：若在tomcat上配置了数据源，则相应用需要在TongWeb上配置数据源。若应用采用第三方开源数据源，则无需在TongWeb上配置。

三、通过应用服务器做初步的分析
某些场景下用户并不清应用采用了哪些JavaEE规范、组件，只能说明采购的应用服务器及版本，这种情况下只能通过用户采购的应用服务器及版本来做初步的判断：通过应用服务器及版本，来判断应用的大概架构。
JavaEE规范常用应用服务器版本
Java EE6
TongWeb6.1、Weblogic12.1.x、WebSphere8.x、tomcat7(web容器)
Java EE7
TongWeb7.0、Weblogic12.2.x、WebSphere9.x、tomcat8.x(web容器)
Java EE8
TongWeb7.0/8.0、tomcat9.x 、Weblogic14.x、WebSphere Liberty18.x
Jakarta EE9
TongWeb8.0、tomcat10.x、WebSphere Liberty21.x
例如：
1. 若应用采用tomcat10版本，则一定是采用了Jakarta EE9规范，jakarta命名空间的应用。则一定要用TongWeb8.0 jakarta命名空间方式来移植。
2. 若应用采用了Jetty、undertow，则大概率采用的是嵌入式方式，嵌入式方式也分为Spring Boot方式和
直接以API方式直接启动容器的方式。
3. 若应用采用了Weblogic、WebSphere等商用中间件，则有可能采用了EJB，这是在后期移植时需要通过迁移工具移植的，还有检查应用是否采用了Oracle、IBM公司一些相关产品。
注意：用户用Weblogic、WebSphere、JBoss时不用过份强调EJB移植，只有在一些老旧应用移植时才有可能会遇到EJB2.x的移植。 近年即使采用Weblogic、WebSphere、JBoss的应用也很少采用EJB技术。
仅仅知道应用服务器及版本只能做大概的移植判断，归根结底还是要以分析应用架构为准。原因是应用服务器的使用方式是多样的，并不能从应用服务器本身判断应用的情况，
某些人存在严重的理解误区：总以为根据原来用的JavaEE应用服务器是什么就能写出移植方案。
例如：
1. 某一用户用的tomcat9.0版本，则有可能是嵌入式方式，也有可能是通常的web应用方式。
2. 某一用户采够了weblogic8.1-weblogic12c等各个版本分散在各个项目上使用，有的项目应用可能采用了老规范的EJB 2.x版本，涉及EJB  xml文件的移植；有的项目应用则是纯web应用；有的项目应用还用了IBM MQ。这种情况就不能仅仅通过应用服务器及版本来判断了。
3. 有的说undertow很少用过，不知怎么移植。这可以判断是嵌入式方式，本质还是看应用的JavaEE/JakartaEE规范，引入的Spring Boot版本。
四、国产平台迁移环境
迁移应用前还要考察是否适配国产平台，主要从几方面考虑：
1. 国产平台多以龙芯、飞腾、鲲鹏、申威、海光、兆芯等CPU的国产操作Linux环境为主，涉及到CPU指令集不同、windows到Linux的转变。
2. 国产平台Open JDK由操作系统自带，多以Open JDK1.8/11/17/21为主，老版本JDK不提供。
3. 数据库的迁移，由Oracle等数据库迁移到国产数据库，同样涉及应用的改造。
4. 判断采购的东方通产品是否合适？ 有的PHP应用，却采购的TongWeb； 有的嵌入式应用，却采购的TongWeb企业版;  有的一听说是云平台，不去了解应用，直接推荐TongWeb容器云版本, 实际有可能是嵌入版。
5. 针对采用本地库的应用，原应用在x86平台下，迁移到国产环境时要对源码重新编译。
6. 其它相关软件是否支持购买的国产平台。

五、举例说明
通过以上说明对应用移植的分析过程有一个初步的了解，下面举几个实例来说明一下移植过程中所涉及的常见修改。
1. Spring3.x版本不支持JDK1.8，报错如下：
Caused by: java.lang.IllegalArgumentException
    at org.springframework.asm.ClassReader.<init>(Unknown Source)
    at org.springframework.asm.ClassReader.<init>(Unknown Source)
    at org.springframework.asm.ClassReader.<init>(Unknown Source)
    at org.springframework.core.type.classreading.SimpleMetadataReader.<init>(SimpleMetadataReader.java:52)
    at org.springframework.core.type.classreading.SimpleMetadataReaderFactory.getMetadataReader(SimpleMetadataReaderFactory.java:80)
原因：spring使用的 asm 类库版本太低，而JDK1.8之后Java class格式有变化，老版本的asm类库不能支持处理 Jdk8 的class文件导致报错抛异常。
解决办法：升级spring到spring4以上版本。
2.  不同应用服务器之间的JNDI上下文和JNDI命名规则不同，所以也需要修改应用调用EJB2.x、数据源的部分。
#weblogic  JNDI上下文
java.naming.provider.url=t3://192.168.1.10:7001
java.naming.factory.initial=weblogic.jndi.WLInitialContextFactory
#websphere  JNDI上下文
java.naming.provider.url=iiop://localhost:2811
java.naming.factory.initial=com.ibm.websphere.naming.WsnInitialContextFactory
#jboss  JNDI上下文
java.naming.factory.initial=org.jnp.interfaces.NamingContextFactory
java.naming.factory.url.pkgs=org.jboss.naming:org.jnp.interfaces
java.naming.provider.url=localhost:1099
#TongWeb  JNDI上下文
java.naming.provider.url=http://192.168.1.10:5100/ejbserver/ejb
java.naming.factory.initial=com.tongweb.naming.java.javaURLContextFactory
EJB2.x在不同应用服务器下xml的不同。
只有在一些老旧应用移植时才有可能会遇到EJB2.x的移植。 近年即使采用Weblogic、WebSphere、JBoss的应用也很少采用EJB技术。
<!-- tongweb-ejb-jar.xml   -->
<?xml version="1.0" encoding="UTF-8"?>
<tongweb-ejb-jar>
	<ejb-deployment ejb-name="helloEJB">
		<jndi name="helloEJBLocal1"
			interface="com.tongweb.ejb2.HelloWorldLocalHome"></jndi>
		<jndi name="helloEJBRemote1"
			interface="com.tongweb.ejb2.HelloWorldRemoteHome"></jndi>
	</ejb-deployment>
</tongweb-ejb-jar>

<!-- weblogic-ejb-jar.xml  TongWeb可以兼容 -->
<?xml version="1.0" encoding="UTF-8"?>
<weblogic-ejb-jar>
	<weblogic-enterprise-bean>
		<ejb-name>helloEJB</ejb-name>
		<jndi-name>helloEJBRemote1</jndi-name>
		<local-jndi-name>helloEJBLocal1</local-jndi-name>
	</weblogic-enterprise-bean>
</weblogic-ejb-jar>

<!-- jboss.xml --> 
<?xml version="1.0" encoding="UTF-8"?>
<jboss>
	<enterprise-beans>
		<session>
			<ejb-name>helloEJB</ejb-name>
			<jndi-name>helloEJBRemote1</jndi-name>
		</session>
	</enterprise-beans>
</jboss>

<!-- ibm-ejb-jar-bnd.xml  TongWeb可以兼容--> 
<?xml version="1.0" encoding="UTF-8"?>
<ejbbnd:EJBJarBinding xmi:version="2.0"
	xmlns:xmi="http://www.omg.org/XMI" xmlns:ejb="ejb.xmi" xmlns:ejbbnd="ejbbnd.xmi"
	xmi:id="EJBJarBinding_1393691689296">
	<ejbJar href="META-INF/ejb-jar.xml#ejb-jar_ID" />
	<ejbBindings xmi:id="EnterpriseBeanBinding_1393691689296"
		jndiName="ejb/helloEJBRemote1">
		<enterpriseBean xmi:type="ejb:Session"
			href="META-INF/ejb-jar.xml#helloEJB" />
	</ejbBindings>
</ejbbnd:EJBJarBinding>
3. Hibernate配置
(1) 大部分应用采用Hibernate JPA或Eclipselink来实现，所以TongWeb的JPA功能可以关闭。
(2) Hibernate JPA采用JTA容器事务时，不同应用服务器提供不同的事务实现，在TongWeb8.0下接口类如下设置，注意不同hibernate版本事务接口类不同。
<!-- hibernate4如下 -->
<property name="hibernate.transaction.jta.platform" value="com.tongweb.tongejb.jpa.integration.hibernate.h4.TongWebJtaPlatform" />
<!-- hibernate4.3及之后版本如下 -->
<property name="hibernate.transaction.jta.platform" value="com.tongweb.tongejb.jpa.integration.hibernate.h5.TongWebJtaPlatform" />

错误移植方式：
问题：TongWeb不同产品版本是否向下兼容技术规范？
错误方式：通常建议应用采用的JavaEE版本与TongWeb版本对应，应用是JavaEE5规范只能用TongWeb5.0、JavaEE6规范只能用TongWeb6.1、JavaEE7规范只能用TongWeb7.0。
正确方式：
1. Jakarta EE8及以前规范大部分是可以向下兼容的，不存在规范对应唯一版本的说法。
2. 到了Jakarta EE9规范，由于开发API由javax.servlet变为jakarta.servlet，所以从这个规范开始与之前不兼容。
3. TongWeb8.0提供了对应用 javax.*与jakarta.*  API互转的功能 与 javax/jakarta命名空间转化功能，可以兼容新老规范。

问题：我们应用系统大量采用的是WebSphere, 请问如何移植？
错误方式：提供TongWeb与WebSphre一对一配置参数说明。
正确方式：应用系统各有不同，采用的开发框架也不同，本质还是要从应用本身入手进行分析。

问题：你们在移植方面有什么经验和方案？
错误方式：我们有移植工具，可进行应用移植。随即把移植工具和手册给用户，完毕。
正确方式：移植工具只能解决部分配置类移植，且应用多不提供源码，无法做到代码级的检查。所以还需要人工移植。

六、移植案例过程
案例一：某项目用户有jetty替换需求，公司安排技术人员进行移植技术交流。于是得到的交流结果如下：
(1) 需求：用户需要我们提供jetty的移植方案、需要我们介绍移植过程中的经验，请销售安排人处理。
(2) 提出问题：跟用户交流没有了解用户采用的jetty版本、没有了解用户jetty的使用方式、没有了解应用的情况(采用什么规范、哪些开源框架等等)。 同时对于无法处理的技术问题不找领导协调安排，让销售在售前、售后、开发之间转达，项目无负责人牵头。
(3) 得到答复：用户也不清楚jetty版本、该查看jetty哪些配置、应用情况，只需要我们提供一个通用的测试方案，能按照方案一步步移植即可，移植tomcat这块我们很熟悉了，知道如何移植。jetty遇到的少，所以需要协调他人写jetty移植方案。用户很着急，马上要。

提出问题：
用户不清楚的原因：一是跟沟通交流安排的人不对，二是不能引导用户移植时要关注哪些移植点。 移植方案没有通用的，从jetty1.x到jetty12.x 版本差异就很大，连用户用的版本都无法调查清楚，就无法写移植方案。 移植应用有方法论，但无法做到一步步移植操作说明。 同时也不用说对jetty不熟悉所以写不出来，tomcat移植多，谁能写出一步步移植操作说明。 最后说用户很着急，这个一是拿用户着急催别人干活，二是把事情拖延了。
类似这类事件的本质是安排了不懂移植的人员跟用户沟通移植方案，无法深入了解用户需求，且在无法反馈用户有效信息的情况下，又把工作抛给其他人完成，着急要移植文档也只是为交差而已，属于无效工作。
正常的移植过程应该是这样：
1.  先了解用户在所有项目上用的jetty版本范围，如：主要用jetty8、9版本。这时即使对jetty不熟悉，从jetty官网
https://jetty.org/download.html
也可以看到其jetty8、9支持的规范情况。从而可以判断应用肯定为web应用，在规范Servlet3.1、JSP2.3及以下。
2. 再分别了解每个项目上jetty的使用方式，大概有三种：
方式一：web应用部署在jetty上的方式
了解到这种方式则可以确认需要采用TongWeb企业版/轻量版/容器版，同时再检查其在jetty上的配置，如最常见的数据源配置（不同jetty版本配置不同），再对应TongWeb的数据源配置进行移植。
<!-- 在工程的WEB-INF目录下新建名字为jetty-env.xml的文件   -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Configure PUBLIC "-//Mort Bay Consulting//DTD Configure//EN" "http://jetty.mortbay.org/configure.dtd">
<Configure class="org.eclipse.jetty.webapp.WebAppContext">
	<New id="DSTest" class="org.eclipse.jetty.plus.jndi.Resource">
		<Arg></Arg>
		<Arg>jdbc/DSTest</Arg>
		<Arg>
			<New class="oracle.jdbc.pool.OracleDataSource">
				<Set name="DriverType">thin</Set>
				<Set name="URL">jdbc:oracle:thin:@fmsswdb1:10017:otcd</Set>
				<Set name="User">xxxx</Set>
				<Set name="Password">xxxx</Set>
				<Set name="connectionCachingEnabled">true</Set>
				<Set name="connectionCacheProperties">
					<New class="java.util.Properties">
						<Call name="setProperty">
							<Arg>MinLimit</Arg>
							<Arg>5</Arg>
						</Call>
						<!-- put the other properties in here too -->
					</New>
				</Set>
			</New>
		</Arg>
	</New>
</Configure>
方式二：Spring Boot 嵌入式jetty的方式
了解到这种方式则可以确定给用户推荐TongWeb嵌入版，这也是最常用的方式。

方式三：非Spring Boot嵌入式的jetty开发方式。
这种方式引用jetty类进行Java开发，同样是推荐采用TongWeb嵌入版，但需要改应用代码。
```java
package start;
import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.webapp.WebAppContext;
 
public class Start {
	public static void main(String[] args){
		Server server = new Server(8080);
		
		WebAppContext context = new WebAppContext();
		context.setContextPath("/jettyWebApp");
		context.setDescriptor("webRoot/WEB-INF/web.xml");		
		server.setHandler(context);
		
		try {
			server.join();
			server.start();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
	}
}
```
初步了解到用户采用的jetty版本范围，各个项目上jetty的使用方式后，才能确定需要采用的TongWeb版本，才能针对性能写移植方案。
案例二：

某项目用户有tomcat移植替换需求, 通过交流从用户处得到信息，应用采用tomcat10版本，有非spring框架的web应用，也有Spring Boot嵌入式的应用，采用了hibernate持久化框架，并要将Oracle数据库会替换为达梦国产数据库。
通过以上大概信息就可以做出如下判断：
1. 采用tomcat10版本则肯定是Jakarta EE9的Web容器规范，也无需考虑存在EJB的可能性。且需要TongWeb8.0转为Jakarta命名空间来移植。
2. tomcat下为web应用，则TongWeb8.0开启轻量模式移植最简单。
3. 有Spring Boot嵌入式的应用，则还应该加上TongWeb8.0嵌入版移植。
4. 采用hibernate框架要将Oracle数据库替换为达梦数据库，则能想到需要将org.hibernate.dialect.OracleDialect方言类改为org.hibernate.dialect.DMDialect方言类。
5. 熟悉tomcat的，会再检查server.xml是否采用了tomcat数据源，将应用中lookup("java:comp/env/jdbc/test")方式改为lookup("jdbc/test")方式。
6. 检查应用包下用的开源组件版本，比如：CXF4.0版本，则可以判断必须用JDK17及以上版本，且不要开启TongWeb本身的Web Service功能。
如此细致方可写出移植方案。