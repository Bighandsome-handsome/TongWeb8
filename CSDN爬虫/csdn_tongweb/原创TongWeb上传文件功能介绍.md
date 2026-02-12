# 原创TongWeb上传文件功能介绍

> 原文地址: https://blog.csdn.net/realwangpu/article/details/129797831

---

Servlet3.0之前通常借助commons-fileupload-x.jar和commons-io-x.jar等开源jar包实现文件上传。而在Servlet3.0时可以通过@MultipartConfig注解以及相关的方法比较方便的进行文件上传。
@MultipartConfig的常用属性
| 属性名 | 类型 | 是否可选 | 描述 |
|--------|------|----------|------|
| fileSizeThreshold | int | 是 | 当数据量大于该值时，内容将被写入文件。 |
| location | String | 是 | 存放生成的文件地址。 |
| maxFileSize | long | 是 | 允许上传的文件最大值。默认值为 -1，表示没有限制。 |
| maxRequestSize | long | 是 | 针对该 multipart/form-data 请求的最大数量，默认值为 -1，表示没有限制。 |

示例如下：
```java
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Part;

// form 设置ectype属性为multipart/form-data才可上传文件
// 使用MultipartConfig注解标注改servlet能够接受文件上传的请求
@WebServlet("/UploadServlet")
@MultipartConfig(location = "/tmp", fileSizeThreshold = 1024 * 1024, maxFileSize = 1024 * 1024
		* 5, maxRequestSize = 1024 * 1024 * 5 * 5) 
public class UploadServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	public UploadServlet() {
		super();
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		//获取用户选择的长传文件
		Part part = request.getPart("myfile");
		String disposition = part.getHeader("Content-Disposition");
		String suffix = disposition.substring(disposition.lastIndexOf("."), disposition.length() - 1);
        // 随机的生存一个32的字符串
		String filename = UUID.randomUUID() + suffix;
         // 获取上传的文件名
		InputStream is = part.getInputStream();
        // 动态获取服务器的路径
		String serverpath = request.getServletContext().getRealPath("upload");
		FileOutputStream fos = new FileOutputStream(serverpath + "/" + filename);
		byte[] bty = new byte[1024];
		int length = 0;
		while ((length = is.read(bty)) != -1) {
			fos.write(bty, 0, length);
		}
		fos.close();
		is.close();
	}
}
```
常见问题一：
若maxFileSize, maxRequestSize 设置过小，则会报异常如下：
```bash
Caused by: com.tongweb.web.util.http.fileupload.impl.SizeLimitExceededException:
the request was rejected because its size (1722) exceeds the configured maximum (25)at com.tongweb.web.util.http.fileupload.impl.FileItemIteratorImpl.init(FileItemIteratorImpl.java:116)
at com.tongweb.web.util.http.fileupload.impl.FileItemIteratorImpl.getMultiPartStream(FileItemIteratorImpl.java:160)
at com.tongweb.web.util.http.fileupload.impl.FileItemIteratorImpl.findNextItem(FileItemIteratorImpl.java:179)
at com.tongweb.web.util.http.fileupload.impl.FileItemIteratorImpl.<init>(FileItemIteratorImpl.java:77)
at com.tongweb.web.util.http.fileupload.FileUploadBase.getItemIterator(FileUploadBase.java:218)
at com.tongweb.web.util.http.fileupload.FileUploadBase.parseRequest(FileUploadBase.java:240)
at com.tongweb.server.connector.Request.parseParts(Request.java:2738)
... 31 more
```
从堆栈看往往误以为是TongWeb对上传文件大小有限制，默认TongWeb不限制大小。除annotation外，还可以在web.xml中设置。
<multipart-config>
	<location>/tmp</location>
	<max-file-size>20848820</max-file-size>
	<max-request-size>418018841</max-request-size>
	<file-size-threshold>1048576</file-size-threshold>
</multipart-config>
若是spring boot应用，则可进行如下配置，参数说明及默认值如下。
Spring Boot 1.3.x或者之前
multipart.maxFileSize=100Mb
multipart.maxRequestSize=1000Mb
Spring Boot 1.4.x:
spring.http.multipart.maxFileSize=100Mb
spring.http.multipart.maxRequestSize=1000Mb
Spring Boot 2.0之后:
spring.servlet.multipart.max-file-size=100MB
spring.servlet.multipart.max-request-size=1000MB
Name
Description
Default Value
spring.servlet.multipart.enabled
Whether to enable support of multipart uploads.
true
spring.servlet.multipart.file-size-threshold
Threshold after which files are written to disk.
0
spring.servlet.multipart.location
Intermediate location of uploaded files.
spring.servlet.multipart.max-file-size
Max file size.
1MB
spring.servlet.multipart.max-request-size
Max request size.
10MB
spring.servlet.multipart.resolve-lazily
Whether to resolve the multipart request lazily at the time of file or parameter access.
false
常见问题二：
上传路径
默认 @MultipartConfig 上传路径与commons-fileupload-x.jar默认上传路径相同，均为： \domains\domain1\temp\cache\work\server\localhost\webapp下 。
因为两者都是通过getServletContext().getAttribute("javax.servlet.context.tempdir") 设置的临时目录，所以有时分不清应用是@MultipartConfig 上传的，还是开源commons-fileupload-x.jar上传的。若想修改上传路径：
1. @MultipartConfig方式是通过指定location的值或 spring.servlet.multipart.location。
2. commons-fileupload通过如下方式，不同版本可能不同。
DiskFileItemFactory factory = new DiskFileItemFactory();
factory.setSizeThreshold(1024 * 1024);// 缓冲区大小为1M
factory.setRepository(file);// 临时目录的保存目录,需要一个file