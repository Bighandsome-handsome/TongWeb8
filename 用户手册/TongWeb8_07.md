# 1. TongWeb 自身安全配置项
# 1.1. 以普通用户安装 TongWeb
在 Linux 操作系统以普通用户安装并运行 TongWeb，避免采用 root 用户导致 TongWeb 权限过大。
 若项目需要使用 80 端口，仍需 root 用户。

# 1.2. TongWeb 使用端口及防火墙开通策略
防火墙设置基本原则：对外用户访问只暴露应用访问端口，其它端口为 TongWeb 内部进程通信端口，只需对内放开，切勿对外暴露。
禁止在互联网暴露 9060/console 控制台，会被当做攻击对象。
<table><tr><td>服务程序</td><td>功能</td><td>默认端口</td><td>端口作用</td></tr><tr><td rowspan="4">TongWeb</td><td rowspan="4">提供服务的核心进程</td><td>8088</td><td>默认应用访问端口</td></tr><tr><td>9060</td><td>默认控制台端口</td></tr><tr><td>7200</td><td>JMX端口，默认关闭</td></tr><tr><td>5200</td><td>EJB w3 远程端口，默认关闭</td></tr><tr><td>TongWeb-MQ</td><td>消息服务器</td><td>7676</td><td>JMS 服务端口</td></tr><tr><td>TongDataGrid</td><td>内存会话服务器</td><td>5701</td><td>session 复制端口</td></tr></table>

# 1.3. 可选择性的关闭 TongWeb 控制台
TongWeb 控制台为常被攻击的对象，在不常使用 TongWeb 控制台维护的情况下，可删除
“${tongweb.base}/conf/tongweb.xml” 中的 <connector> 关闭控制台.
影响范围：这期间无法使用 TongWeb 控制台。

# 1.4. 开启动态密码
因 TongWeb 一般安装在内网，邮件认证不便，可通过动态密码方式开启动态密码，该扫码方式无需TongWeb 联网，具体操作见《TongWeb_V8.0控制台使用手册》。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/071289ab6d8e4767d3d833cabbc013746f148d08d7fad5a4489ebc6884b148a7.jpg)
影响范围：登录 TongWeb 控制台需要手机扫码登录。

# 1.5. 修改 TongWeb 默认密码
首次登录 TongWeb 控制台需修改密码。
 除修改 thanos 密码外，另外三个用户 security、auditor、monitor 也需要修改默认密码。
影响范围：因修改控制台密码后可能会忘记密码造成不便，所以请妥善保管密码。

# 1.6. 设置信任 IP
限制访问控制的客户端 IP 可进行如下设置，切忌设置为 * 。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/0706f0698fdf5394b7067ead2be7baa07d36bb7e73bfa166ba87cbf414dd42d3.jpg)
影响范围：TongWeb 控制台只允许指定的客户端 IP 访问。

# 1.7. 开启访问日志
访问日志默认没有开启，开启访问日志需登录控制台，在日志管理中开启访问日志配置。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/efd159045e460debe8a4d63f8061b2032778d24092aa7210f708642bc3bd381f.jpg)
影响范围：无，在遭受客户端攻击时，可通过访问日志分析客户端来源。

# 1.8. 控制台禁止远程文件上传
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/beda92ffa2afe7c819dc1110781bcda2b1c440bac33503166d47fd5c4de20deb.jpg)
影响范围：无法通过控制台上传应用包。

# 2. 应用相关安全配置项
以下为应用相关安全配置项，从安全角度需要开启，但开启后可能会影响到应用正常使用，请酌情考虑。

# 2.1. 会话与Cookie
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/79e8c12795001b240a12709e44b56eaf2cb3308e0aa0c56273a281674b73aaad.jpg)
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>applications>app
Table 1. 应用的【会话与Cookie】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>sessionCookieName</td><td>会话的Cookie名</td><td>指定应用会话的Cookie名称。注：若应用的web.xml中同样设置了该属性，则优先使用web.xml中的值。若以上两处都没有设置，则使用默认的JSESSIONID作为名称。</td></tr><tr><td>useLegacyCookieProcessor</td><td>使用老版Cookie处理器</td><td>使用老版Cookie处理器，是基于RFC6265、RFC2109、RFC2616的，开启后可兼容基于Tomcat 8以前版本开发的应用。</td></tr><tr><td>allowEqualsInValue</td><td>Cookie Equal Signs</td><td>如果是true，则在解析未加引号的Cookie值时允许使用等号字符。如果是false，当遇到等号时，包含等号的Cookie值将被终止，并且剩余的Cookie值将被删除。</td></tr><tr><td>allowHttpSepsInV0</td><td>HTTP分隔符</td><td>如果是true，则允许在Cookie名称和值中使用HTTP分隔符。</td></tr><tr><td>useHttpOnly</td><td>Cookie HttpOnly</td><td>会话Cookie是否使用 HttpOnly标志。</td></tr><tr><td>sameSiteCookies</td><td>Cookie SameSite</td><td>设置Cookie的SameSite属性。Unset:不要设置SameSiteCookie属性;None:Cookie始终在跨站点请求中发送;Lax:Cookie仅在同站点请求和跨站点顶级导航GET请求上发送;Strict:防止浏览器在所有跨站点请求中发送cookie。</td></tr><tr><td>maxActiveSessions</td><td>最大会话数</td><td>限制该应用同时在线的最大会话数,以防止会话过大导致系统瘫痪。设置为“-1”表示不限制。</td></tr><tr><td>sessionTimeout</td><td>会话超时时间</td><td>设置应用会话(Session)的超时时间(单位:分钟)。</td></tr><tr><td>localPersistence</td><td>本地持久化</td><td>开启后,应用在停止时会将当前内存中的会话持久化存储到本地,如文件系统,并在启动后重新载入内存。本地持久化为异步进行,受“全局配置”中“定时任务周期”影响,若TongWeb进程被强杀(如执行了forcestop脚本)则最多会丢失最近一个“定时任务周期”内写入的会话数据。</td></tr><tr><td>refSessionHa</td><td>会话服务器</td><td>选择应用要连接的会话服务器,将应用的Session存储到会话服务器。其优先级高于虚拟主机设置的会话服务器;但若虚拟主机同时开启了“Session共享”则优先级低于虚拟主机的会话服务器。注:当由于网络等原因导致会话服务器不可用时,应用的Session仍会在本地内存中存取,不会中断应用的业务处理。</td></tr><tr><td>disableSessionInvalid date</td><td>禁用会话注销</td><td>开启后,应用调用session invalidate时会话不再销毁,后续依靠自动过期机制销毁会话。</td></tr></table>

# 2.2. 应用安全配置项
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/544c39eaa696e3ec2fb493d8967b9499e00108535708072731a9780181a89673.jpg)
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>applications>app
Table 2. 应用的【安全】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>enableCORSAccess</td><td>允许跨域访问</td><td>通过为资源实现W3C的CORS（跨域资源共享）规范来启用客户端跨域请求。</td></tr><tr><td>corsAllowedOrigins</td><td>允许的源</td><td>设置允许跨域访问的源，配置多个源使用英文逗号分隔，例如http://www.xxx.com, http://www.zzz.com。注：设置为“*”表示所有源都允许。</td></tr><tr><td>corsAllowedMethods</td><td>允许的方法</td><td>允许跨域访问的方法，默认支持GET, POST, HEAD, OPTIONS。配置多个方法以英文逗号分隔，例如GET, POST, HEAD, OPTIONS。</td></tr><tr><td>corsAllowedHeaders</td><td>允许的 HTTP 头</td><td>允许的 HTTP 头,XMLHttpRequest 对象的getResponseHeader(   ) 方法拿到的基本字段,默认支持Origin,Accept,X-Requested-With,Content-Type,Access-Control-Request-Method,Access-Control-Request-Headers,配置多个 HTTP 头以英文逗号分隔。</td></tr><tr><td>corsExposedHeaders</td><td>暴露 HTTP 头</td><td>通过 Access-Control-Expose-Headers 暴露指定的HTTP 头,Access-Control-Expose-Headers 标头指示哪些标头可以安全地公开给 CORS API 规范的 API。注:配置多个 HTTP 头以英文逗号分隔。</td></tr><tr><td>corsSupportCredentials</td><td>支持凭证</td><td>CORS 请求默认不发送 Cookie 和 HTTP 认证信息。若需要把Cookie 发到服务器,则设置为 “true”,默认为“false”。</td></tr><tr><td>corsPreflightMaxAge</td><td>预检请求的有效期</td><td>用来指定本次预检请求的有效期(单位:秒)。在此期间,不用发出另一条预检请求,默认值 1800 秒。</td></tr><tr><td>requestParametersLostValidation</td><td>参数防丢失</td><td>开启该功能后,若请求参数解析期间出现故障(如请求参数个数超过了设置的阈值或 POST 数据的大小超过了设置的阈值等),系统将拒绝请求,以确保客户端提交的参数值不会丢失。</td></tr><tr><td>XSSFilterEnabled</td><td>XSS 攻击拦截</td><td>拦截可疑的 XSS 攻击请求,通常是含有 script、&lt;、&gt;等特殊标记的请求,以 403 响应码返回到客户端。</td></tr><tr><td>csrFPrevention</td><td>CSRF 防护</td><td>注意:请谨慎打开此功能,否则可能导致应用无法访问!! 为 Web 应用提供基本的 CSRF 防护支持,该功能需要应用自身予以配合:调用HttpServletResponse#encodeRedirectURL(String)和HttpServletResponse#encodeURL(String)方法(每执行一次则产生一个新的令牌,当 CSRF 令牌缓存数设置为0时,一个会话只产生一个令牌)编码 URL 后发送到客户端,其目的是要发送回服务器的URL都带有csrf_token参数以认证身份。编码后的 URL 示例:/myservlet/myres?param=val&amp;csrftoken=...。TongWeb 的 CSRF 防护同时可以阻挡重放攻击,只要不将 CSRF 令牌缓存数设置为0即可。</td></tr><tr><td>csrFCacheSize</td><td>CSRF令牌缓存数</td><td>CSRF令牌会随着客户端请求而更新,CSRF令牌缓存数表示保留最新的令牌个数,这同时也表示允许的客户端并发数。0表示不限制。</td></tr><tr><td>tokenValidTimes</td><td>CSRF令牌有效次</td><td>提供CSRF令牌循环使用支持,使用次数超出有效次后会自动失效,可用于资源需要重复访问而不支持及时更新CSRF令牌等场景。注意:1. CSRF令牌允许循环使用时,将无法阻挡重放攻击;2.该功能仅在“CSRF令牌缓存数”不为0时有效。</td></tr><tr><td>csrFEntryPoints</td><td>CSRF免防入口</td><td>开启CSRF防护后,可选设置一些免防入口(应用URL),如登录资源,以跳过防护检查。设置多个入口时,使用英文逗号分隔。</td></tr><tr><td>httpHeaderToken</td><td>REST支持</td><td>开启了CSRF防护的应用,将无法使用REST接口,原因是REST接口无法通过URL传递令牌,开启“REST支持”可解决该问题。开启“REST支持”需要应用自身予以配合:1. 客户端须首先请求免防资源,服务器通过响应头返回令牌;2. 客户端请求其它资源须通过请求头(名为:csrF_token)回传服务器令牌,以通过服务器的安全认证。</td></tr><tr><td>secretLevel</td><td>应用密级</td><td>设置本应用的保密等级,此保密等级将用于应用数据网络传输、主体数据存取、客体请求访问等过程的加密处理。</td></tr><tr><td>threadPoolPolicy</td><td>业务安全规则</td><td>1(单线程池):使用通道内置的线程池处理所有业务;2(双线程池):符合规则的业务由线程池处理,其它业务由通道内置的线程池处理;3(三线程池):符合规则的业务由线程池处理,其它业务由其它线程池处理。线程池不会作用的范围:由服务器处理的静态资源、支持异步Servlet处理的业务。注意:对于使用了异步Filter的业务,请谨慎或不要使用线程池功能。注意:若业务处理时间过长(如超过30秒),则建议增大线程超时阈值,否则可能导致请求失败!</td></tr><tr><td>threadPool</td><td>线程池</td><td>线程池功能可将指定的业务交给指定的线程池来处理,可支持应用根据业务的重要性、优先级等方面约束系统资源的使用。该功能一般适用于并且只建议应用于比较耗时的业务操作,例如长事务、远程服务调用等。</td></tr><tr><td>threadPoolTimeout</td><td>线程超时阈值</td><td>业务处理时长达到该阈值后,响应结果将即刻发送回客户端,而不再等待线程处理结束,这会提高整体的响应效率,但可能导致客户端没有获取到最终的处理结果。单位是毫秒,0表示使用通道的异步请求的默认超时。</td></tr><tr><td>taskRule</td><td>匹配规则</td><td>指定需要线程池执行的业务的匹配规则,其格式须是匹配URL的正则表达式。不指定则表示可接受所有业务。注:业务的匹配规则是基于请求的Servlet路径,而不包含应用的访问名。</td></tr><tr><td>exclusionRule</td><td>排除规则</td><td>指定需要线程池从匹配规则中要排除的业务规则,其格式须是匹配URL的正则表达式。不指定则表示不排除。注:业务的匹配规则是基于请求的Servlet路径,而不包含应用的访问名。</td></tr><tr><td>otherThreadPool</td><td>其它线程池</td><td>当使用三线程池策略时,符合规则的业务由线程池处理,其它业务由其它线程池处理。</td></tr><tr><td>otherThreadPoolTimeout</td><td>其它线程超时阈值</td><td>其它业务处理时长达到该阈值后,响应结果将即刻发送回客户端,而不再等待线程处理结束,这会提高整体的响应效率,但可能导致客户端没有获取到最终的处理结果。单位是毫秒,0表示使用通道的异步请求的默认超时。</td></tr><tr><td>semaphoreEnabled</td><td>并发安全控制</td><td>出于安全等考虑,控制访问应用的并发量。</td></tr><tr><td>concurrency</td><td>限制最大并发</td><td>允许的最大并发访问量。</td></tr><tr><td>block</td><td>阻塞等待</td><td>当应用达到最大并发访问量时,是否阻塞等待访问应用。若不等待,请求会被终止,并记录一条日志。</td></tr><tr><td>interruptible</td><td>允许中断阻塞</td><td>当请求线程在阻塞等待访问应用时,是否允许被中断,若被中断则请求会被终止,并记录一条日志。</td></tr><tr><td>restrictedPorts</td><td>限定访问端口</td><td>限定访问端口后,只有指定的端口可以访问本应用,其它端口的访问会被拒绝,不指定则表示不限制。可用于支持系统应用、重要应用、普通应用的端口隔离式的安全访问,并可通过设置不同端口的资源大小来约束不同应用的业务处理效率。注意:该功能只适用于Web应用,对于远程访问的EJB应用无效,如需限制远程EJB的访问,则可在"EJB http协议"模块进行相关设置。</td></tr><tr><td>crossContext</td><td>允许跨应用访问</td><td>指定是否允许调用 ServletContext Context("/appName") 方法访问此服务器中其他Web 应用程序的上下文。</td></tr><tr><td>unloadDelay</td><td>卸载等待</td><td>卸载应用时，若存在请求未处理完毕，则等待一段时间（单位：秒），超时后会强制卸载，此时会给出线程泄漏的警告日志。</td></tr><tr><td>allowLinking</td><td>允许链接文件</td><td>是否允许使用软链接访问应用的资源文件。</td></tr><tr><td>clearReferences</td><td>内存泄漏检测</td><td>在应用停止时，检查并尝试回收与应用相关联的可能导致内存泄漏的JDBC驱动、线程、线程局部变量（ThreadLocal）、Java 序列化对象缓存、RMI 目标对象等资源。</td></tr><tr><td>enableRecycling</td><td>应用回收</td><td>启用后，应用卸载时将备份到回收站，可在应用回收列表查看。</td></tr></table>

# 2.3. 全局安全策略

# 2.3.1. 文件防篡改
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/f089d06742fd0b33f3eb43c439995cf3331f4928686aa8dcbfe8865b77a32245.jpg)
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>security
Table 3. 安全策略的【文件防篡改】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>configProtection</td><td>服务器主配置文件防篡改</td><td>开启后，禁止在TongWeb运行期间对主配置文件tongweb.xml、console.xml、default-web.xml等进行修改。若被意外篡改，则自动进行恢复。</td></tr><tr><td>fileProtectionPattern</td><td>应用防篡改文件后缀</td><td>指定应用的防止篡改的文件的后缀。在应用部署后，对应用的所有原始文件进行周期性（由服务器“全局配置”&gt;“定时任务周期”指定）的检测。当发现文件被篡改后，尝试恢复到原文件。配置防篡改文件后缀，表示开启该功能；不配置，则不开启。防篡改文件后缀格式为 .html, .png, .jpg 等，多个后缀以英文逗号分隔。注意：同时开启热加载和防篡改功能，可能存在冲突，建议不要同时开启。</td></tr></table>

# 2.3.2. 客户端拦截
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/617676486872563dd0e463322600bd58e9a63438459a3f76de5575b810ee6076.jpg)
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>security
Table 4. 安全策略的【客户端拦截】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>filterRemoteHost</td><td>客户端主机名拦截</td><td>出于安全等考虑，拦截特定主机名的客户端请求，请求被拦截后将得到403响应码。注：本机访问不受限制。</td></tr><tr><td>allowHost</td><td>允许的主机名</td><td>指定允许的主机名，其值可为具体的主机名称或匹配主机名称的正则表达式。注：需要通道允许DNS反向查找。</td></tr><tr><td>denyHost</td><td>拒绝的主机名</td><td>指定拒绝的主机名，其值可为具体的主机名称或匹配主机名称的正则表达式。注：需要通道允许DNS反向查找，拒绝的主机名拦截优先于允许的主机名。</td></tr><tr><td>filterRemoteAddr</td><td>客户端IP拦截</td><td>出于安全等考虑，拦截特定IP的客户端请求，请求被拦截后将得到403响应码。注：本机访问不受限制。</td></tr><tr><td>allowAddr</td><td>允许的IP</td><td>指定允许的IP,其值可为具体的IP、匹配IP的正则表达式或通配符IP(如:168.1.2.*,168.1.4.5-168.1.4.99)。</td></tr><tr><td>denyAddr</td><td>拒绝的IP</td><td>指定拒绝的IP,其值可为具体的IP、匹配IP的正则表达式或通配符IP(如:168.1.2.*,168.1.4.5-168.1.4.99)。注:拒绝的IP拦截优先于允许的IP。</td></tr><tr><td>denySdos</td><td>SDOS攻击拦截</td><td>检测并拦截SDOS攻击。</td></tr><tr><td>sdosTimeThreshold</td><td>SDOS探测阈值(秒)</td><td>当一个请求的处理时间超过此SDOS探测阈值时,则将该请求判定为SDOS攻击。</td></tr><tr><td>sdosCountThreshold</td><td>SDOS次数阈值</td><td>当一个客户端(通常是浏览器)发出的请求被判定为SDOS攻击的次数超过此SDOS次数阈值,则阻止该客户端IP地址的一切请求。</td></tr><tr><td>sdosUnblockPeriod</td><td>解除阻止周期(小时)</td><td>被阻止的客户端IP将在一个周期后自动解除。</td></tr></table>

# 2.3.3. 协议头安全
<table><tr><td colspan="8">安全策略 ② / 编辑 ⑧</td></tr><tr><td>文件防篡改</td><td>客户端拦截</td><td>协议头安全</td><td>支持XFF</td><td>反爬虫</td><td>禁用时间段</td><td>启停安全</td><td>其它</td></tr><tr><td colspan="8">Host Header拦截 ①</td></tr><tr><td colspan="8">referer拦截 ②</td></tr><tr><td colspan="8">响应头防护 ③</td></tr></table>
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>security
Table 5. 安全策略的【协议头安全】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>hostHeaderFilter</td><td>Host Header拦截</td><td>开启 Host Header拦截后，将会从请求头“Host”中解析主机名和IP地址，只有符合规则的请求才可以访问本主机。注：本机访问不受限制。</td></tr><tr><td>allowHostHeader</td><td>允许的 Host</td><td>支持正则表达式，依照此规则对 Host 中的主机进行校验，如192.168.1.[0-9]*:9060|www.tw.com；未设置此规则，表示不进行该校验。注：“允许的 Host”校验的优先级低于“拒绝的 Host”。</td></tr><tr><td>denyHostHeader</td><td>拒绝的 Host</td><td>支持正则表达式，依照此规则对 Host 中的主机进行校验，如192.168.1.[0-9]*:9060；未设置此规则，表示不进行该校验。注：“允许的 Host”校验的优先级低于“拒绝的 Host”。</td></tr><tr><td>refererFilter</td><td>referer拦截</td><td>开启 referer拦截后，将会从请求头“referer”中解析主机名和IP地址。只有符合规则的请求才可以访问本主机。注：本机访问不受限制。</td></tr><tr><td>allowReferer</td><td>允许的 referer</td><td>指定允许访问本主机的域名或者 IP，支持正则表达式。依照此规则对 referer 中的主机进行校验。未设置此规则，表示不进行该校验。注：“允许的 referer”校验的优先级低于“拒绝的 referer”。</td></tr><tr><td>denyReferer</td><td>拒绝的 referer</td><td>指定不允许访问本主机的域名或者 IP，支持正则表达式。依照此规则对 referer 中的主机进行校验。未设置此规则，表示不进行该校验。注：“允许的 referer”校验的优先级低于“拒绝的 referer”。</td></tr><tr><td>responseHeader</td><td>响应头防护</td><td>可对响应头添加特定的消息，以通知浏览器进行必要的安全操作。</td></tr><tr><td>antiClickJackingEnabled</td><td>X-Frame-Options</td><td>站点可以通过确保网站没有被嵌入到别人的站点里面，从而避免点击劫持攻击。</td></tr><tr><td>antiClickJackingOption</td><td>X-Frame策略</td><td>DENY：页面不允许在frame中展示；SAMEORLGIN：页面可以在相同域名页面的frame中展示；ALLOW-FROM：页面可以在指定来源的 frame 中展示。</td></tr><tr><td>antiClickJackingUri</td><td>指定来源</td><td>页面可以在指定来源的 frame 中展示，示例：http://ip:port 或者 http://ip:*。注：若是多个地址，需要使用空格隔开。</td></tr><tr><td>hstsEnabled</td><td>Strict-Transport-Security</td><td>通知浏览器，网站禁止使用 HTTP 方式加载，浏览器应该自动把所有尝试使用 HTTP 的请求自动替换为 HTTPS 请求。</td></tr><tr><td>blockContentTypeSn iffingEnabled</td><td>X-content-Type- Options</td><td>禁止浏览器的类型猜测行为。</td></tr><tr><td>xssProtectionEnable d</td><td>X-XSS-Protection</td><td>当检测到跨站脚本攻击(XSS)时，浏览器将停止加载页面。</td></tr></table>

# 2.3.4. 支持 XFF
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/f9123f8075ac98eb13f9c4ffbdbc62fa87e23c9b84b384d2fd265140d86046c4.jpg)
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>security
Table 6. 安全策略的【支持 XFF】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>XForwardedFor</td><td>解析 XFF 头</td><td>X-Forwarded-For (XFF) 是用来识别通过 HTTP 代理或负载均衡方式连接到 Web 服务器的客户端最原始的 IP 地址的 HTTP 请求头字段。开启该功能后，将基于代理或负载均衡器的请求头 X-Forwarded-For 来获得连接的原始 IP 地址。</td></tr><tr><td>internalProxies</td><td>内部代理</td><td>匹配内部代理的IP地址的正则表达式。若它们出现在remotelpHeader标头中,则它们将被信任并且不会出现在proxiesHeader标头中。</td></tr><tr><td>trustedProxies</td><td>信任的代理</td><td>匹配受信任代理的IP地址的正则表达式。若它们出现在remotelpHeader标头中,则它们将被信任并出现在proxiesHeader标头中。</td></tr><tr><td>protocolHeader</td><td>协议信息请求头</td><td>包含协议信息的HTTP标头,通常命名为X-Forwarded-Proto。若为空,则不会替换Request的scheme、secure、主机名和端口。</td></tr><tr><td>hostHeader</td><td>获取主机的请求头</td><td>从这个请求头取值,用以覆盖Request.getServerName()的返回值。若开启了“替换本地主机”,则同时覆盖Request.getLocalName()的返回值。</td></tr><tr><td>changeLocalName</td><td>替换本地主机</td><td>若开启,则从“获取主机的请求头”中取值,用以覆盖Request.getLocalName()的返回值。</td></tr><tr><td>portHeader</td><td>获取端口的请求头</td><td>从这个请求头取值,用以覆盖Request.getServerPort()的返回值。若开启了“替换本地端口”,则同时覆盖Request.getLocalPort()的返回值。对于http协议,若没有从“获取端口的请求头”中获取到值,则使用“缺省http端口”。</td></tr><tr><td>changeLocalPort</td><td>替换本地端口</td><td>若开启,则从“获取端口的请求头”中取值,用以覆盖Request.getLocalPort()的返回值。对于http协议,若没有从“获取端口的请求头”中获取到值,则使用“缺省http端口”。</td></tr><tr><td>httpServerPort</td><td>缺省http端口</td><td>对于http协议,若没有从“获取端口的请求头”中获取到值,则使用该缺省值。</td></tr><tr><td>httpsServerPort</td><td>缺省https端口</td><td>对于https协议,若没有从“获取端口的请求头”中获取到值,则使用该缺省值。</td></tr></table>

# 2.3.5. 反爬虫
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/c030fb7d9c54b48626c4c2df8a45c9f8cd829a4a83f675ca832bf767004ad765.jpg)
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>security
Table 7. 安全策略的【反爬虫】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>enableCrawlerSessionManager</td><td>反爬虫管理</td><td>Web爬虫在爬取站点时会触发数千个会话的创建，这可能会导致大量内存消耗。此功能确保爬虫与单个会话相关联 - 就像普通用户一样 - 无论他们是否在请求中提供会话令牌。</td></tr><tr><td>sessionInactiveInterval</td><td>爬虫会话超时时间</td><td>指定爬虫会话的会话超时（单位：秒），通常应小于用户会话时间。</td></tr><tr><td>crawlerlps</td><td>识别爬虫IP</td><td>设置匹配IP的正则表达式或通配符IP（如：168.1.2*，168.1.4.5-168.1.4.99）来识别爬虫会话。</td></tr><tr><td>singleSession</td><td>启用单会话</td><td>启用单会话功能，开启后，每个IP只会创建一个会话。</td></tr><tr><td>crawlerUserAgents</td><td>识别爬虫User-Agent</td><td>设置匹配User-Agent的正则表达式来识别爬虫。</td></tr></table>

# 2.3.6. 禁用时间段
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/8e892c45706b9998bb14f9466075184c9f0dd8ccbfbe7d8c8358debc9fb977e6.jpg)
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>security
Table 8. 安全策略的【禁用时间段】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>filterTime</td><td>禁用时间段</td><td>设置禁止外部访问本服务器的时间段。注：本机访问不受限制。</td></tr><tr><td>filterTimeBegin</td><td>开始时间</td><td>指定的拦截规则在每日的该时间点（小时，24小时制）开始生效。</td></tr><tr><td>filterTimeEnd</td><td>结束时间</td><td>指定的拦截规则在每日的该时间点（小时，24小时制）结束生效。</td></tr><tr><td>repeat</td><td>重复规则</td><td>设置此拦截规则重复生效的规则。</td></tr></table>

# 2.3.7. 启停安全
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/9c640822785c1d0be97bfae0342f10afd57de87f53711f06921ae2170e7811bc.jpg)
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>security
Table 9. 安全策略的【启停安全】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>enabledRejectSystemExit</td><td>System退出检测</td><td>探测通过 System.exit()、Runtime.exit()、Runtime.halt()以及 Ctrl+C等方式停止 TongWeb 服务的行为，并记录相关的调用堆栈。</td></tr><tr><td>rejectSystemExit</td><td>禁止 System 退出</td><td>当 System 退出被检测到时，是否阻止该行为。注：使用停止脚本停止 TongWeb 的行为不受影响。</td></tr><tr><td>rejectStart</td><td>启动限制</td><td>对 TongWeb 的启动进行权限验证，验证通过后可正常启动 TongWeb，否则启动将会终止。</td></tr><tr><td>checkedOsUsers</td><td>禁止用户</td><td>指定不允许启动 TongWeb 的操作系统用户列表，多个用户以英文逗号分隔。</td></tr><tr><td>minimumUmask</td><td>最小 Umask</td><td>指定须为运行 TongWeb 的操作系统用户配置的最小 umask。若配置了该参数，则 TongWeb 会在启动之前去环境变量（参数名为&quot;tongweb.umASK&quot;）或 -D 参数（参数名为&quot;tongweb.umASK&quot;）里检查操作系统用户的 umask（若两处都设置则以 -D 参数为准），只有当其值与最小 umask 值作按位与操作得出的值仍为最小 umask 值时才允许启动。注：该配置格式为八进制，须是一个合法的 umask 值。</td></tr><tr><td>secureStop</td><td>安全停止</td><td>在调用 TongWeb 的停止脚本时进行密码验证，输入正确的系统管理员密码才可以停止 TongWeb 服务。</td></tr><tr><td>startdTimeout</td><td>后台启动超时</td><td>在使用 startd 脚本启动 TongWeb 时，若 startd 脚本的执行超过此时长后仍未结束，则会主动终止并立即退出，此后 TongWeb 进程可能仍在后台继续启动，请注意检查日志以获悉最终启动结果。</td></tr><tr><td>startdDiscardTimeout</td><td>后台启动放弃超时</td><td>在使用 startd 脚本启动 TongWeb 时，若因为端口冲突等原因最终不可能启动成功，通过设置此超时阈值，可及早终止等待。</td></tr></table>

# 2.3.8. 序列化安全
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/17f34d74e4f536592eb434cfc1bce739c3def18e8daa0f1a51346a27ace3db11.jpg)
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>security
Table 10. 安全策略的【其它】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>useJavaSerializer</td><td>Java原生序列化</td><td>是否使用 Java 原生的序列化工具，即 ObjectOutputStream/ObjectInputStream API。在遇到序列化相关问题时，可尝试打开该功能，打开后可能会影响集中管理、远程 EJB 等场景的性能。注：使用集中管理时，所有实例应该一起设置，或都打开，或都保持关闭。</td></tr><tr><td>whitelist</td><td>白名单</td><td>设置允许使用序列化和反序列化的 Java 类，其格式为 Java 类的全名称（包名加类名）或全名称的前缀部分（通常是包名）加通配符“”，以英文逗号分隔可设置多个，如 java.lang.,com.tongweb.*。注：该配置会影响 ejb 或其它需要序列化处理的功能，请在设置后进行充分的测试和验证。</td></tr><tr><td>rmiServerHostname</td><td>RMI 服务主机名</td><td>设置提供 RMI 服务的主机名，该主机名将被返回给 RMI 客户端用于访问远程对象。该参数最终会设置到 JVM 参数 -Djava.rmi.server hostname 上，效果与之相同。</td></tr></table>

# 2.4. 在虚拟主机中自定义错误页面
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/17f5fef3fe5353fcfd80d1d7226aac9ab37e00bc27a669606236971ef5bd7535.jpg)
属性及属性说明，如下表所示。
持久化位置：conf/tongweb.xml:tongweb>server>service>container>host
Table 11. 虚拟主机的【基本属性】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>name</td><td>主机名</td><td>虚拟主机的名称，可作为访问该虚拟主机的域名。注意：避免使用IP地址；若使用IP地址，则通过此IP地址就只能访问此虚拟主机下的应用，可能导致控制台无法访问。</td></tr><tr><td>aliases</td><td>别名</td><td>虚拟主机的别名，别名和主机名一样可作为访问该虚拟主机的域名。多个别名以英文逗号分隔。注意：避免使用IP地址，若使用IP地址，则通过此IP就只能访问此虚拟主机下的应用，可能导致控制台无法访问。</td></tr><tr><td>refRealm</td><td>默认安全域</td><td>此处设置的安全域可作用于所有部署在此虚拟主机上的应用，其优先级低于应用自身设置的安全域。若此虚拟主机同时开启了“单点登录（SSO）”，则优先级高于应用设置的安全域。</td></tr><tr><td>refSessionHa</td><td>会话服务器</td><td>选择应用要连接的会话服务器，将应用的Session存储到会话服务器。此处设置的会话服务器可作用于所有部署在此虚拟主机上的应用，其优先级低于应用自身设置的会话服务器。若此虚拟主机同时开启了“Session共享”，则优先级高于应用设置的会话服务器。</td></tr><tr><td>addValve</td><td>自定义 Valve</td><td>自定义 Valve 的全类名,自定义的 Valve 会添加到虚拟主机的 pipeline (valve 链) 里,访问应用时执行自定义的操作。自定义的 Valve 需继承com.tongweb.server.valves.ValveBase 类(所在 jar: ${tongweb.home}/version*/tongweb-web.jar);在重写 invoke 方法时,需要确保调用“getNext().invoke(request, response)”;在重写其它方法时,需要确保调用对应的 super 方法。多个自定义 Valve 需以英文逗号分隔。注:需在 TongWeb 启动之前,将包含自定义 Valve 的 jar 文件放置到${tongweb.base}/lib 下。</td></tr><tr><td>customErrorPage</td><td>自定义错误页面</td><td>自定义错误页面,数据格式为 code=path,其中 code 指定错误状态码,path 指定自定义错误页面的绝对路径,也可以是相对于 TongWeb 安装目录或域目录的相对路径,多个自定义错误页面需以英文逗号分隔。</td></tr><tr><td>useJsonReport</td><td>使用 Json 报告</td><td>开启此选项后,任何导致 HTTP 错误状态码的请求都将收到一个包含错误信息的 JSON 数据格式的响应。若未开启,服务器将继续使用默认的 HTML 数据格式的页面响应。</td></tr><tr><td>ssoEnabled</td><td>单点登录</td><td>是否开启单点登录,默认关闭。开启后,同一虚拟主机下使用相同安全域的应用可以实现多点登录,即登录一次访问多个应用。注:若要启用单点登录功能,则需要首先设置默认安全域。</td></tr><tr><td>sessionShareEnable d</td><td>Session 共享</td><td>是否开启应用间的 Session 共享功能。开启后,同一虚拟主机下的应用可以实现 Session 数据共享。</td></tr><tr><td>rewriteEnabled</td><td>启用 URL 重写</td><td>支持 URL 重写和请求转发,能够在请求到达 Servlet 容器之前对 URL 进行修改,类似于 Apache HTTP 服务器中的mod rewrite 模块。</td></tr><tr><td>rewriteConfigFile</td><td>URL 重写规则文件</td><td>指定 URL 重写功能使用的规则文件。</td></tr></table>

# 3. SSL 配置相关
SSL 通常为安全检查必配项，在进行 SSL 相关配置时，需要依据以下方案：
1. 购买正式证书，TongWeb 自带测试证书非正式证书，需购买制作正式证书配 SSL。
2. 在负载均衡条件下，证书通常配置在负载设备上，如：硬件 F5、软件 THS。
注意：
不了解证书如何申请，为什么要购买，一般厂商为什么提供不了正式证书？
对以上问题通俗的讲解可参考：https://blog.csdn.net/zxh2075/article/details/78104510

# 3.1. 关于 SSL 安全配置
SSL 相关漏洞和问题如下：
1. CVE-2015-2808： SSL/TLS 受诫礼(BAR-MITZVAH)攻击漏洞。
2. CVE-2014-3566： SSLv3 在降级的旧版加密漏洞（POODLE）。
3. CVE-2016-0800： SSL DROWN 攻击漏洞。
4. CVE-2016-0800： SSL DROWN 攻击漏洞。
5. SSL 证书非正式可信证书等。
解决以上漏洞和问题的方法：
第1步：制作证书由用户方提供
1. 用户制作证书请求时需使用 OpenSSL 最新版本，老版本 OpenSSL 有安全漏洞。
2. 制作的证书密码位数要符合安全要求。
3. 如果是在 THS、Apache、nginx 上配的 SSL，则在 THS、Apache、nginx 上解决漏洞。
第2步：在 TongWeb 上配置 SSL 证书
1. 勾选相应 TLS 协议。
2. 在 “启用密码套件” 中配置安全的算法。
例如：以下算法：
TLS_ECDHE_RSA_WITAES_128_CBC_SHA256,TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,TLS_ECDH E_RSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA,TLS_RSA_WITH_AE S_128_CBC_SHA256,TLS_RSA_WITH_AES_128_CBC_SHA 
3. 在 TongWeb 使用的 JDK 中 “jre\lib\security\java.security” 配置禁用不安全的 SSL 协议和算法。
如下所示：
#JDK8 默认配置如下：jdk.tls.disabledAlgorithms=SSLv3, TLSv1, TLSv1.1, RC4, DES, MD5withRSA, \DH keySize $<$ 1024, EC keySize $<$ 224, 3DES_EDE_CBC, anon, NULL, \
include jdk.disabled.namedCurves 

# 3.2. http 强制跳转 https 端口
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/a8808c13a1a4475cc5eefb9bccd421f3d8536b89fe5426e662553d1600d17596.jpg)
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-12/d69d2a0b-a79f-4307-adf8-f0f8448078c7/c0a2fc1ba6d00466ca2ea48303a6a5cfa0364a6d0a37f749192089836c746e98.jpg)
