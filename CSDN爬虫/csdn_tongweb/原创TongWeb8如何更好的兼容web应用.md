# 原创TongWeb8如何更好的兼容web应用

> 原文地址: https://blog.csdn.net/realwangpu/article/details/128494577

---

当web应用向TongWeb8移植时，为了更好的兼容可以开启“轻量模式” 或“web兼容模式”。
方式一：开启“轻量模式”对整个TongWeb生效。
此模式会关闭EJB、JCA等服务，并尝试从应用自身加载 JSF、JavaMail、WebSocket、WebService、Xml 等技术实现。如果应用是基于 Tomcat 或其它 Servlet 容器开发的，则通常可以获得更好的兼容性。
方式二：部署应用时开启“web兼容模式”
以 Web 兼容模式加载该应用，如果该应用是基于 Tomcat 等 Web 容器开发，则可以尝试打开此开关以获得更好的兼容性。开启此模式后，EJB 等企业级技术实现将不再支持，同时尝试从应用自身加载JSF、JavaMail、WebSocket、WebService、Xml 等企业级技术实现。