# 原创TongWeb支持Spring Boot、Spring Cloud说明

> 原文地址: https://blog.csdn.net/realwangpu/article/details/110219850

---

### TongWeb 版本兼容性矩阵

| TongWeb 版本 | JDK 17 | Spring Framework 6.x | Spring Boot 3.x | Spring Cloud Gateway | 支持最高规范 |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **7.0.4** | 支持 | 不支持 | 不支持 | 不支持 | JavaEE 8 |
| **8.0 / 7.0.8** | 支持 | 支持 | 支持 | 不支持 | JakartaEE 10 |
| **嵌入版 (Embedded)** | 支持 | 支持 | 支持 | 支持 | JakartaEE10仅web容器 |


TongWeb支持Spring Boot，Spring  Cloud吗？
说明：
主要看Spring Boot各个版本需要的JavaEE的web容器规范是多少，另外了解应用的运行方式。遵从以下规则：
1. 以web应用传部署方式，则Spring Boot2.x可用
2. TongWeb7、TongWeb8企业版，Spring Boot3.x只能用TongWeb8.0/7.0.8企业版。
3. 以嵌入式方式java  -jar方式运行的，则只能采用TongWeb7/8嵌入式版本。
4. Spring Cloud Gateway的运行不需要web容器， 所以仅可用TongWeb嵌入版的reactor。

注意：Spring Boot的嵌入式运行方式与web运行方式虽然可以互转，但要考虑项目后期维护的便利性， TongWeb企业版与嵌入版也是经常卖错的版本。

常见的使用问题：
问题一：
有人问TongWeb是否支持JDK17?
TongWeb7.0、8.0都支持JDK17，但问该问题的本质是想知道哪个版本支持Spring Boot3.x、Spring Framework6.x 框架。 TongWeb7.0.4版本支持JDK17，但不支持Spring Boot3.x、Spring Framework6.x框架，需要TongWeb8.0。

问题二：
有些应用框架采用Spring Cloud Gateway，运行在非servlet容器上，所以仅可用TongWeb嵌入版的reactor，无法运行在TongWeb企业版上。见Spring官网说明。

问题三：
不能单纯以应用包为jar包或war包来判断采用TongWeb嵌入版或企业版，个别情况下有的应用为war包，但仍以 java  -jar  app.war的嵌入式方式来运行。

问题四：
Spring Boot3.x，Spring Framework6.x为什么不能在TongWeb7.0.4.x版本上运行？
因为从Jakarta EE9规范开始  javax命名空间变为 jakarta命名空间，API发生了本质变化。
1. TongWeb7.0.4.x及以下版本不支持Jakarta EE9规范,也就是不支持Spring Boot3.x版本。
2. TongWeb7.0.8/8.0企业版需要切换为Jakarta命名空间版本来支持Spring Boot3.x应用。
3. TongWeb7/8嵌入版需要引入支持Spring Boot3.x的jar来运行。

问题五：
替换了嵌入版的tomcat，如何判断替换成功？
当嵌入版启动时，看到TongWeb图标时表示采用TongWeb嵌入版的Spring Boot启动。
附：TongWeb7.0.E.x嵌入版打包示例。
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>1.0.0</groupId>
  <artifactId>springboot-tw</artifactId>
  <version>1</version>
  <packaging>jar</packaging>
  <name>springboot-tw</name>
  <url>http://maven.apache.org</url>
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <java.version>1.8</java.version>
  </properties>
   <parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.3.8.RELEASE</version>
		<relativePath/> 
	</parent>
  <dependencies> 
      <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
			<!-- 不用tomcat -->
			<exclusions>
              <exclusion>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-starter-tomcat</artifactId>
              </exclusion>
			</exclusions>
      </dependency>
	  <!--引入tongweb包 -->
	  <dependency>
           <groupId>com.tongweb.springboot</groupId>
           <artifactId>tongweb-spring-boot-starter</artifactId>
           <version>2.x.0.RELEASE</version>
      </dependency>
      <dependency>
           <groupId>com.tongweb</groupId>
           <artifactId>tongweb-embed</artifactId>
           <version>7.0.E.1</version>
      </dependency>     
      <dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
	</dependency>  
  </dependencies>
  <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <mainClass>com.tong.App</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>