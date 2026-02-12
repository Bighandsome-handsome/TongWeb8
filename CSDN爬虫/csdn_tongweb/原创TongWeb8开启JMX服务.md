# 原创TongWeb8开启JMX服务

> 原文地址: https://blog.csdn.net/realwangpu/article/details/128494370

---

默认TongWeb8的JMX服务是关闭的，若需要开启JMX服务通过控制台如下完成。
通过JMX,Rest接口采集监控值具体可参考《TongWeb_V8.0REST接口参考.pdf》
采用TongWeb8的 JMX取监控值可参考examples.war中的示例，代码方式如下：
import javax.management.MBeanServerConnection;
import javax.management.ObjectName;
import javax.management.remote.JMXConnector;
import javax.management.remote.JMXConnectorFactory;
import javax.management.remote.JMXServiceURL;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

public class JmxClient {

	public static void main(String[] args) throws Exception {
		String ip = "127.0.0.1";
		String port = "7200";
		String username = "monitor";
		String password = "monitor135.COM";
		String password2fa = "null";
		String model = "connector";
		String action = "monitor";
		String name = "server";
        //集中配置加密公钥
		String transferKey = "30819F300D06092A864886F70D010101050003818D0030818902818100BE0F308AF29D14ACBF20686278CA9279BD91F8584F979D03B4CDB49387831DF719864E456E802A4EB4ABEFC554DAB46C5A8E3647C43FC5F477CF520EAC695C402C1CC3BCBEB194BF87F1B26B21794CB745791BE118E8F6327F0DEC60BD1CEC8C1486A85D0C6AFF0F4E7344F9D856E41568B0A6472FDE35444BE2BFA298F92CC90203010001";

		Properties properties = new Properties();
		properties.setProperty("lang", "zh");
        //请求参数
		properties.setProperty("name", name);
		properties.setProperty("targetType", "instance");
		properties.setProperty("targetName", "domain1");

		String ipAndPort = ip + ":" + port;
		String serviceUrl = "service:jmx:rmi://" + ipAndPort + "/jndi/rmi://" + ipAndPort + "/server";
		JMXServiceURL url = new JMXServiceURL(serviceUrl);

		Map<String, Object> environment = new HashMap<>();
		if (!transferKey.isEmpty()) {
            //加密工具包：${tongweb.home}/version*/sysapp/console/WEB-INF/lib/tongweb-web-console-framework.jar
			password = com.tongweb.sdk.util.TongWebUtils.encryptWithPubKey(password, transferKey);
		}
		environment.put(JMXConnector.CREDENTIALS, new String[] { username, password, password2fa, "true" });
		JMXConnector connector = JMXConnectorFactory.connect(url, environment);
		connector.connect();
		MBeanServerConnection connection = connector.getMBeanServerConnection();

		Object result = connection.invoke(new ObjectName("TongWeb:name=console"), "callServerMethod",
				new Object[] { model, action, properties },
				new String[] { String.class.getName(), String.class.getName(), Properties.class.getName() });
		System.out.println(result);
	}
}
推荐通过rest接口采集监控值，代码如下：
import javax.net.ssl.*;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;
import java.util.Properties;

public class RESTClient {

    public static final X509TrustManager X_509_TRUST_MANAGER = new X509TrustManager() {
        @Override
        public void checkClientTrusted(X509Certificate[] x509Certificates, String s) throws CertificateException {
        }

        @Override
        public void checkServerTrusted(X509Certificate[] x509Certificates, String s) throws CertificateException {
        }

        @Override
        public X509Certificate[] getAcceptedIssuers() {
            return new X509Certificate[0];
        }
    };

    public static void main(String[] args) throws Exception {
        String ip = "127.0.0.1";
        String port = "9060";
        String username = "monitor";
        String password = "wang135.COM";
        String password2fa = "null";
        String model = "connector";
        String action = "monitor";
        String name = "server";
        String transferKey = "30819F300D06092A864886F70D010101050003818D0030818902818100BE0F308AF29D14ACBF20686278CA9279BD91F8584F979D03B4CDB49387831DF719864E456E802A4EB4ABEFC554DAB46C5A8E3647C43FC5F477CF520EAC695C402C1CC3BCBEB194BF87F1B26B21794CB745791BE118E8F6327F0DEC60BD1CEC8C1486A85D0C6AFF0F4E7344F9D856E41568B0A6472FDE35444BE2BFA298F92CC90203010001";
        Properties properties = new Properties();
        properties.setProperty("name", name);
		properties.setProperty("targetType", "instance");
		properties.setProperty("targetName", "domain1");

        StringBuilder params = new StringBuilder();
        params.append("j_username=").append(username);
        if (!transferKey.isEmpty()) {
            password = com.tongweb.sdk.util.TongWebUtils.encryptWithPubKey(password, transferKey);
            password = java.net.URLEncoder.encode(password, "UTF-8");
        }
        params.append("&j_password=").append(password); // 需要调用 tongwebutils 工具类
        if (password2fa != null && password2fa.trim().length() != 0) {
            params.append("&password2fa=").append(password2fa);
        }
        params.append("&acceptAgreement=true");
        params.append("&lang=zh");

        for (String key : properties.stringPropertyNames()) {
            params.append("&").append(key).append("=").append(properties.getProperty(key));
        }

        SSLContext sslContext = SSLContext.getInstance("TLS");
        sslContext.init(new KeyManager[0], new TrustManager[]{X_509_TRUST_MANAGER}, new SecureRandom());

        String spec = "https://" + ip + ":" + port + "/console/rest/json/" + model + "/" + action + "/" + name;
        URL http = new URL(spec);
        HttpsURLConnection connection = (HttpsURLConnection) http.openConnection();
        connection.setSSLSocketFactory(sslContext.getSocketFactory());
        connection.setHostnameVerifier((hostname, session) -> true);
        setConnectionProperties(connection);
        String res = sendPost(connection, params.toString());
        System.out.println(res);
    }

    public static void setConnectionProperties(HttpURLConnection conn) throws Exception {
        conn.setRequestMethod("POST");
        conn.setDoInput(true);
        conn.setDoOutput(true);
        conn.setUseCaches(false);
        conn.setConnectTimeout(60000);
        conn.setRequestProperty("Connection", "close");
        conn.setRequestProperty("Charset", "UTF-8");
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        conn.setRequestProperty("accept", "*/*");
        conn.setInstanceFollowRedirects(false);
    }

    public static String sendPost(HttpURLConnection con, String body) throws IOException {
        try (OutputStream outStream = con.getOutputStream()) {
            byte[] data = body.getBytes(StandardCharsets.UTF_8);
            outStream.write(data);
        }

        try (InputStream inputStream = con.getInputStream()) {
            if (con.getHeaderField("Content-disposition") != null && con.getHeaderField("Content-disposition").contains("filename=")) {
                String filePath = System.getProperty("user.dir") + File.separator + con.getHeaderField("Content-disposition").split("filename=")[1];
                FileOutputStream out = new FileOutputStream(filePath);
                final byte[] buffer = new byte[1024 * 1024 * 10];
                int length;
                while ((length = inputStream.read(buffer)) != -1) {
                    out.write(buffer, 0, length);
                }
                out.flush();
                out.close();
                return "Download to: " + filePath;
            } else {
                StringBuilder msg = new StringBuilder();
                String readLine;
                BufferedReader responseReader = new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8));
                while ((readLine = responseReader.readLine()) != null) {
                    msg.append(readLine).append("\n");
                }
                return msg.toString();
            }
        }
    }
}