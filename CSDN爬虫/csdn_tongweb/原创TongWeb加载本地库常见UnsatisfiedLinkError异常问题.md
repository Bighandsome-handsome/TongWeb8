# 原创TongWeb加载本地库常见UnsatisfiedLinkError异常问题

> 原文地址: https://blog.csdn.net/realwangpu/article/details/109554060

---

开发的 Java 应用，有部分采用本地库开发，需要采用 JNI 方式调用。如何加载本地库?
重点要记住：
1. 32位JDK用32位本地库，64位JDK用64位本地库，注意通过linux的file命令查看本地库属性。
2. 本地库不能跨平台，不同window、linux版本不能混用，要在当前平台编译。
3. Java加载本地库通常是通过环境变量 Linux为LD_LIBRARY_PATH，windows为PATH加载，或是JDK的参数 -Djava.library.path指向so目录。 若设置 -Djava.library.path, 则系统环境变量的不生效。
4. TongWeb的bin目录通常为进程启始目录，也是加载本地库的目录。 若在其它目录启动TongWeb，则启始目录发生改变。
5.System.loadLibrary("hello"); 加载同一本地库只能加载一次，再加载就会报已加载的异常。
6.常见java.lang.UnsatisfiedLinkError异常就是本地库没做好，没有配好引起的。
举例说明linux下加载动态库的方式：
1. 本地库libhello.so放在/home/usr 下。Java代码调用： System.loadLibrary("hello");
2. 需设置环境变量： export LD_LIBRARY_PATH=/home/usr:$LD_LIBRARY_PATH。
3. 若不会设置环境变量，则修改TongWeb的startserver.sh或external.vmoptions启动脚本，增加或修改
-Djava.library.path=/home/usr:$LD_LIBRARY_PATH
4. 以上都不会设置的话，把so放在TongWeb 的bin目录，在bin目录下启动TongWeb即可。
常见问题： UnsatisfiedLinkError Native Library xxx.so already loaded  异常解决办法：
Web应用里引入so文件通过JNI调用，一旦应用重新部署而不重启java进程，so库又重新加载则会报该异常。建议java接口按如下方式改造一下。
static{ 
   //增加一个全局变量，只要加载过这个so就不再执行，除非进程重启才会清掉该变量。 
   if(System.getProperty("myapplibrary")==null){ 
     System.setProperty("myapplibrary", "test.so"); 
     System.loadLibrary("test"); 
   } 
}