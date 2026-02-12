

# 1. 版本变更说明
本章节记录了 8.0.9.XX 版本的所有变更说明。
# 1.1 A10
<table><tr><td>序号</td><td>功能模块</td><td>功能说明</td><td>相关章节</td></tr><tr><td>1</td><td>应用管理 &gt; 应用</td><td>为保证系统稳定性,若应用被其他模块所引用,则系统将禁止对其执行编辑操作。</td><td>编辑应用</td></tr><tr><td>2</td><td>应用管理 &gt; 应用</td><td>在“会话与Cookie”页签中,新增“禁用会话注销”属性,开启后,应用调用session invalidate 时会话不再销毁,后续依靠自动过期机制销毁会话。</td><td>应用配置参数说明</td></tr><tr><td>3</td><td>资源管理 &gt; 会话服务器</td><td>开启会话服务器后,可将连接失败日志输出到“\$\{tongweb.base\}/logs/sessionha”目录。</td><td>创建会话服务器</td></tr><tr><td>4</td><td>诊断管理 &gt; 类冲突检测</td><td>优化类冲突检测报告的展示形式,并支持报告下载。</td><td>类冲突检测</td></tr><tr><td>5</td><td>安全管理 &gt; 安全策略 &gt;启停安全</td><td>新增“后台启动超时”和“后台启动放弃超时”属性,支持配置后台启动超时时间以满足启动慢的场景需求。</td><td>安全策略</td></tr><tr><td>6</td><td>基础配置 &gt; 全局配置</td><td>· 在“服务器”页签中,新增“从环境变量配置”开关。
· 在“服务器”页签中,新增“系统临时目录”属性,用于缓存上传的文件、编译的JSP等。
· 在“服务器”页签中,优雅停机机制调整为先暂停端口再停止应用,且优雅停机过程中拒绝新入请求。
· 在“应用”页签中,新增“应用共享类加载器”属性,支持设置应用共享类加载器。
· 在“集中管理”页签中,新增“别名”属性,用于标识当前TongWeb的业务身份。
· 在“集中管理”页签中,“注册到集中管理URL”中,支持填写IPv6格式。</td><td>· 更新全局配置
· 全局配置参数说明</td></tr><tr><td>7</td><td>集中管理 &gt; 服务管理 &gt; 集群</td><td>创建集群时，负载均衡器移除从节点，改为多选节点形式。</td><td>· 创建负载均衡器
· 创建集群</td></tr><tr><td>8</td><td>集中管理 &gt; 服务管理 &gt; 节点</td><td>在控制台添加节点时，节点 IP 支持输入主机名。</td><td>创建节点</td></tr><tr><td>9</td><td>集中管理 &gt; 服务管理 &gt; 节点</td><td>手动注册节点时，新增“同步集中管理配置”开关，开启后支持将原节点下已管理的实例同步注册过来。</td><td>· 手动创建节点
· 节点配置参数说明</td></tr><tr><td>10</td><td>集中管理 &gt; 服务管理 &gt; 节点</td><td>自动注册节点时，优先使用管理端口配置的 IP，其次是全局 IP，最后为自动获取。</td><td>SSH 创建节点</td></tr><tr><td>11</td><td>集中管理 &gt; 服务管理 &gt; 实例</td><td>编辑实例时，用户可根据需要重命名实例名称。</td><td>编辑实例</td></tr><tr><td>12</td><td>集中管理 &gt; 安全配置 &gt; 访问令牌</td><td>支持外部系统以访问令牌的方式管理TongWeb 资源。</td><td>访问令牌</td></tr><tr><td>13</td><td>集中管理 &gt; 安全配置 &gt; 控制台安全</td><td>新增“信任 IP 安全警示”属性，当“信任 IP”设置为“*”时，用户可根据需要打开此开关，通过控制台页面给出“小红点”提示信息。</td><td>· 设置信任 IP
· 控制台安全配置参数说明</td></tr><tr><td>14</td><td>集中管理 &gt; 系统管理 &gt; 页面定制</td><td>新增“扩展 HTTP 方法”属性，用于扩展 HTTP 方法。</td><td>扩展 HTTP 方法</td></tr></table>
#1.2  A09
<table><tr><td>序号</td><td>功能模块</td><td>功能说明</td><td>相关章节</td></tr><tr><td>1</td><td>应用管理 &gt; 应用</td><td>新增支持通过 TW_CLASSPATH 环境变量扩展系统类加载路径。</td><td>类加载策略</td></tr><tr><td>2</td><td>应用管理 &gt; 应用</td><td>监视增加每秒处理请求数（QPS）、平均响应时间、错误率指标。</td><td>监视应用</td></tr><tr><td>3</td><td>Web 容器 &gt; 通道</td><td>在 “HTTP 属性” 页签，新增 “分段表单最大段数” 和 “分段表单每段最大请求头”。</td><td>通道配置参数说明</td></tr><tr><td>4</td><td>Web 容器 &gt; 通道</td><td>监视增加错误率、平均响应时间、QPS指标。</td><td>监视通道</td></tr><tr><td>5</td><td>Web 容器 &gt; 数据源</td><td>·“语句管理”页签的“监视慢 SQL”中,记录较慢的 SQL时,支持设置记录 SQL参数。
·监视数据源新增正在建立数据库连接的连接数监视指标。</td><td>·监视数据源
·数据源配置
参数说明</td></tr><tr><td>6</td><td>Web 容器 &gt; 数据源模板</td><td>支持将连接池相关的参数做为模板方便快速建立连接池资源。</td><td>·数据源模板
·数据源模板配置参数</td></tr><tr><td>7</td><td>EJB 容器 &gt; EJB http 协议</td><td>新增支持限定远程访问 EJB 服务的端口。</td><td>EJB w3 协议</td></tr><tr><td>8</td><td>诊断管理 &gt; 类冲突检测</td><td>内置类冲突检测工具,检查已部署应用类路径下存在的类冲突信息。</td><td>类冲突检测</td></tr><tr><td>9</td><td>安全管理 &gt; 证书管理</td><td>新增 SSL 证书统一管理模块。</td><td>证书管理</td></tr><tr><td>10</td><td>安全管理 &gt; 安全策略</td><td>·安全起见,移除了“黑名单”,仅支持设置“白名单”。
·调整了“白名单”的使用说明,且在页面上的设置入口不再与“Java 原生序列化”有关联。</td><td>·配置安全策略
·安全策略配置参数说明</td></tr><tr><td>11</td><td>安全管理 &gt; 巡检基线</td><td>添加更灵活的配置选项。</td><td>巡检基线</td></tr><tr><td>12</td><td>基础配置 &gt; 全局配置</td><td>在“服务器”页签中,新增“主机名允许字符”属性,支持配置允许主机名使用下划线等特殊字符。</td><td>·更新全局配置
·全局配置参数说明</td></tr><tr><td>13</td><td>集中管理 &gt; 系统管理 &gt; 页面定制</td><td>·“功能定制”菜单更名为“页面定制”。
·“禁用功能”更名为“隐藏菜单”。</td><td>页面定制</td></tr><tr><td>14</td><td>集中管理 &gt; 系统管理 &gt; 一键巡检</td><td>增加脚本支持。</td><td>一键巡检</td></tr></table>
• A08
<table><tr><td>序号</td><td>功能模块</td><td>功能说明</td><td>相关章节</td></tr><tr><td>1</td><td>应用管理 &gt; 应用</td><td>在“会话与Cookie”页签中,新增“本地持久化”开关,默认关闭。开启后,应用在停止时会将当前内存中的会话持久化存储到本地。</td><td>应用参数配置说明</td></tr><tr><td>2</td><td>应用管理 &gt; 应用迁移</td><td>应用服务器类型新增支持 Jetty。</td><td>应用迁移</td></tr><tr><td>3</td><td>资源管理 &gt; 会话服务器</td><td>新增“启用分布式锁”开关,支持使用分布式锁保障会话并发访问安全性。</td><td>·创建会话服务器
·会话服务器配置参数说明</td></tr><tr><td>4</td><td>诊断管理 &gt; 采集模板</td><td>默认“default”配置优化为:服务器日志、jstack、top。</td><td>创建采集模板</td></tr><tr><td>5</td><td>基础配置 &gt; 全局配置</td><td>·在“服务器”页签中,新增“启用Validator”开关,默认关闭。关闭后,将不加载 TongWeb 内置的 Validator组件。
·在“服务器”页签中,新增“启用 JTA”开关,默认开启。关闭后,将不加载 TongWeb 内置的 JTA 组件。</td><td>全局配置参数说明</td></tr><tr><td>6</td><td>·应用管理 &gt; 应用 &gt; 其它
·Web 容器 &gt; 通道 &gt;
HTTP 属性
·基础配置 &gt; 全局配置 &gt;
服务器</td><td>“附加响应头”允许使用()字符。
优先级:应用的优先级高于通道,通道优先级高于全局配置。</td><td>·应用
·通道
·全局配置</td></tr><tr><td>7</td><td>集中管理 &gt; 服务管理 &gt; 集群</td><td>新增“IP 哈希”和“访问日志开启”属性。</td><td>·创建集群
·集群配置参数说明</td></tr><tr><td>8</td><td>集中管理 &gt; 扩展支持 &gt; 支持列表</td><td>新增支持 Apollo 作为配置中心。</td><td>·注册中心
·Apollo</td></tr><tr><td>9</td><td>集中管理 &gt; 扩展支持 &gt; 支持列表</td><td>新增支持 Eclipse 社区版。</td><td>Eclipse</td></tr><tr><td>10</td><td>集中管理 &gt; 扩展支持 &gt; 支持列表</td><td>新增支持 IntelliJ IDEA 社区版,并优化配置界面。</td><td>IntelliJ IDEA</td></tr></table>
• A07
<table><tr><td>序号</td><td>功能模块</td><td>功能说明</td><td>相关章节</td></tr><tr><td>1</td><td>应用管理 &gt; 应用迁移</td><td>·新增支持迁移 JBoss、Nginx 应用;
·新增支持批量迁移;
·新增支持是否迁移通道。</td><td>应用迁移</td></tr><tr><td>2</td><td>资源管理 &gt; 会话服务器</td><td>会话服务器使用 Redis 时,哨兵模式下,新增支持“哨兵密码”。</td><td>会话服务器配置参数说明</td></tr><tr><td>3</td><td>资源管理 &gt; 注册中心</td><td>Consul 的 “ACL 认证 Token” 变更为必填项。</td><td>注册中心</td></tr><tr><td>4</td><td>资源管理 &gt; 注册中心</td><td>收到“配置注册中心”变更信息后,在控制台上给出重启通知提示。</td><td>启用配置注册中心</td></tr><tr><td>5</td><td>诊断管理 &gt; 预警策略</td><td>在“处理办法”页签中,新增“发送响应码”属性。</td><td>预警策略配置参数说明</td></tr><tr><td>6</td><td>安全管理 &gt; 巡检基线</td><td>新增支持对巡检内容进行配置,丰富安全基线的巡检指标和报告等。</td><td>·巡检基线
·巡检基线配置参数说明</td></tr><tr><td>7</td><td>基础配置 &gt; 远程 JMX</td><td>所有实例支持独立开启本实例的远程 JMX 接口。</td><td>·远程 JMX
·远程 JMX 配置参数说明</td></tr><tr><td>8</td><td>服务管理 &gt; 集中配置</td><td>在“集中管理”页签中,新增“集群子任务超时”属性,设置子任务的超时时间。</td><td>集中配置</td></tr><tr><td>9</td><td>脚本启停实例</td><td>支持脚本一次性启动或停止 domain1 下所有实例。</td><td>脚本启停实例</td></tr></table>
• A06
<table><tr><td>序号</td><td>功能模块</td><td>功能说明</td><td>相关章节</td></tr><tr><td>1</td><td>Web 容器 &gt; 通道</td><td>在“线程”页签中，新增“使用自调节线程”属性，开启后，TongWeb 会根据业务请求处理的速率自主调节线程池的大小，以持续优化处理效率和系统资源的使用率。</td><td>通道配置参数说明</td></tr><tr><td>2</td><td>Web 容器 &gt; 数据源</td><td>新增支持实时启动和停止数据库连接池。</td><td>· 停止数据源
· 启动数据源</td></tr><tr><td>3</td><td>监视管理 &gt; 概览</td><td>“操作系统负荷”区域调整为:CPU使用率、内存使用率、硬盘使用率。</td><td>监视概览</td></tr><tr><td>4</td><td>监视管理 &gt; 操作系统</td><td>新增CPU使用率、内存使用率、硬盘使用率指标,移除“系统负载”指标。</td><td>操作系统</td></tr><tr><td>5</td><td>监视管理 &gt; 守护监视</td><td>新增支持对监视数据文件进行轮转、压缩等设置。</td><td>·创建守护监视
·守护监视配置参数说明</td></tr><tr><td>6</td><td>诊断管理 &gt; 数据库连接</td><td>新增“数据库连接”模块,用于汇总和管理数据库连接池中的活跃连接对象,并可对检测为泄漏的数据库连接进行手动回收。</td><td>数据库连接</td></tr><tr><td>7</td><td>基础配置 &gt; 全局配置</td><td>·在“服务器”页签中,“延迟启动通道”不再约束管理端口,管理端口总是优先启动以便于管理。
·在“应用”页签中,新增“慢线程检测”属性,探测执行超时的请求,并能够自动中断执行的线程,以提高资源的利用效率。
·在“集中配置”页签中,“滚动更新超时”移动到“集中管理”&gt;“服务管理”&gt;“集中配置”,并更名为“远程操作等待时间”。</td><td>全局配置参数说明</td></tr><tr><td>8</td><td>集中管理 &gt; 服务管理 &gt; 实例</td><td>创建实例时允许显式地指定管理端口。</td><td>·创建实例
·实例配置参数说明</td></tr><tr><td>9</td><td>集中管理 &gt; 服务管理 &gt; 集中配置</td><td>“全局配置”模块中的“滚动更新超时”移动到“集中管理”&gt;“服务管理”&gt;“集中配置”,并更名为“远程操作等待时间”。</td><td>·集中配置
·集中配置参数说明</td></tr><tr><td>10</td><td>集中管理 &gt; 系统管理 &gt; 产品升级</td><td>在产品升级列表中,新增“构建日期”列属性。</td><td>升级主TongWeb</td></tr><tr><td>11</td><td>集中管理 &gt; 系统管理 &gt;一键巡检</td><td>新增支持收集系统日志。</td><td>一键巡检</td></tr></table>
• A05
<table><tr><td>序号</td><td>功能模块</td><td>功能说明</td><td>相关章节</td></tr><tr><td>1</td><td>应用管理 &gt; 应用</td><td>·在“基本属性”页签中,“访问前缀”属性允许在不同的虚拟主机上为不同应用配置相同的访问前缀。
·在“会话与Cookie”页签中,选择会话服务器后,即开启会话高可用。会话相关日志输出到独立的“${tongweb.base}/logs/sessionha”日志目录。
·在“资源加载”页签中,新增“跟踪已加载类”属性,支持跟踪查看应用已加载的类明细。仅支持Web应用。
·在“其它”页签中,新增“使用定向扫描”属性,在指定场景下,可大幅提升应用的启动速度。</td><td>·部署应用
·应用配置参数说明</td></tr><tr><td>2</td><td>应用管理 &gt; 迁移配置</td><td>新增“迁移配置”管理模块,用于对应用服务器TongWeb7执行应用迁移操作时,允许多端口迁移。</td><td>迁移配置</td></tr><tr><td>3</td><td>Web 容器 &gt; 通道</td><td>在“其它”页签中,将“解析器缓存数”改为自调节,不再提供可视化配置参数。</td><td>通道配置参数说明</td></tr><tr><td>4</td><td>EJB 容器 &gt; JCA 连接池</td><td>新增“JNDI 名”属性,可自定义多个JNDI绑定名字。</td><td>·创建JCA连接池
·JCA连接池配置参数说明</td></tr><tr><td>5</td><td>EJB 容器 &gt; JCA 托管对象</td><td>新增“JNDI 名”属性,可自定义多个JNDI绑定名字。</td><td>·创建JCA托管对象
·JCA托管对象配置参数说明</td></tr><tr><td>6</td><td>EJB 容器 &gt; JavaMail 资源</td><td>新增“JNDI 名”属性,可自定义多个JNDI绑定名字。</td><td>·创建JavaMail资源
·JavaMail资源配置参数说明</td></tr><tr><td>7</td><td>EJB 容器 &gt; 工作管理器</td><td>新增“JNDI 名”属性，可自定义多个 JNDI 绑定名字。</td><td>·创建工作管理器
·工作管理器配置参数说明</td></tr><tr><td>8</td><td>资源管理 &gt; 会话服务器</td><td>·新增“缓存直连”属性，开启后，TongWeb 将放弃本地内存中存取Session 数据，而全部从会话服务器中存取，以利于排查相关问题。
·“同步清理”属性更名为“被动清理”。
·新增支持 RDS 无密码场景。</td><td>·创建会话服务器
·会话服务器配置参数说明</td></tr><tr><td>9</td><td>资源管理 &gt; JNDI 资源</td><td>新增“JNDI 名”属性，可自定义多个 JNDI 绑定名字。</td><td>·创建 JNDI 资源
·JNDI 资源配置参数说明</td></tr><tr><td>10</td><td>资源管理 &gt; 注册中心</td><td>新增对 Consul 的支持。</td><td>·注册中心
·Consul</td></tr><tr><td>11</td><td>诊断管理 &gt; 类加载结构</td><td>在类加载结构“信息”窗口中，新增“已加载的类”属性。用户可在应用部署时，开启“跟踪已加载类”开关，查看已加载类的明细。</td><td>类加载结构</td></tr><tr><td>12</td><td>·可信管理 &gt; 可信行为模型
·可信管理 &gt; 可信行为详情</td><td>新增可信行为模型，可借助机器学习技术，自动采集进程行为，并生成可信行为模型库。系统会将采集的行为数据模型库数据转换为可信策略，并以此为用户提供可信防护。</td><td>·可信行为模型
·可信行为详情</td></tr><tr><td>13</td><td>安全管理 &gt; 安全策略</td><td>在“反爬虫”页签中，新增“启动单会话”属性，开启后，每个 IP 只会创建一个会话，以增加易用性。</td><td>安全策略配置参数说明</td></tr><tr><td>14</td><td>安全管理 &gt; 密码安全</td><td>“全局加密算法”新增支持国密算法“SM4”。</td><td>全局加密算法</td></tr><tr><td>15</td><td>基础配置 &gt; 全局配置</td><td>· 在“服务器”页签，为提高兼容性，默认关闭了 JPA。
· 在“应用”页签，新增“应用主动备份”属性，支持在应用部署后主动进行一次备份。</td><td>· 更新全局配置
· 全局配置参数说明</td></tr><tr><td>16</td><td>基础配置 &gt; 全局配置 &gt; 应用</td><td>“服务器文件大小限制”设置为0时，表示不限制。</td><td>全局配置参数说明</td></tr><tr><td>17</td><td>集中管理 &gt; 资源配置 &gt; TongDataGrid</td><td>不再需要填写认证信息（认证名和认证密码），由系统内部自行维护。</td><td>创建 TongDataGrid</td></tr><tr><td>18</td><td>集中管理 &gt; 资源配置 &gt; 消息服务器</td><td>产品出厂默认不再附带消息服务器安装包文件，用户可联系官方获取TongWeb-MQ安装包。</td><td>获取安装包</td></tr><tr><td>19</td><td>集中管理 &gt; 安全配置 &gt; 管理员</td><td>· 新增管理员时，“摘要算法”新增支持“SM3”。
· “摘要算法”移动到“安全”tab页签。</td><td>创建管理员</td></tr><tr><td>20</td><td>集中管理 &gt; 安全配置 &gt; 权限分配</td><td>为了避免普通运维人员对“默认实例”页面进行操作，系统支持用户采用权限分配的方式，将“默认实例”页面隐藏。</td><td>分配权限</td></tr><tr><td>21</td><td>集中管理 &gt; 系统管理 &gt; 产品升级</td><td>由于通信方式发生改变，补充特殊版本升级操作说明。</td><td>特殊版本</td></tr><tr><td>22</td><td>集中管理 &gt; 系统管理 &gt; 功能定制</td><td>新增支持定制页面功能菜单的显示名称。</td><td>定制模块/字段名称</td></tr><tr><td>23</td><td>集中管理 &gt; 扩展支持 &gt; 支持列表</td><td>IntelliJ IDEA TongWeb插件仅支持“tongweb-idea-232.zip”和“tongweb-idea-242.zip”。</td><td>获取 IntelliJ IDEA TongWeb插件</td></tr><tr><td>24</td><td>集中管理 &gt; 扩展支持 &gt; 版本生成</td><td>· 去掉“版本生成”页面的“命名空间”属性。
· 生成的不含控制台的版本，默认打开“启动时部署”。</td><td>版本生成</td></tr><tr><td>25</td><td>集中管理 &gt; 扩展支持 &gt; 进阶使用</td><td>移除了“启动命令式传参”功能，以JAVA_OPTS环境变量替代。</td><td>启动命令式传参</td></tr></table>
• A04
<table><tr><td>序号</td><td>功能模块</td><td>功能说明</td><td>相关章节</td></tr><tr><td>1</td><td>Web 容器 &gt; 通道</td><td>“其它”页签下,“处理器缓存大小”属性更名为“解析器缓存数”。为资源优化考虑,出厂配置参数调整为0。</td><td>通道配置参数说明</td></tr><tr><td>2</td><td>日志管理 &gt; Syslog 推送</td><td>新增支持通过syslog的方式记录服务器日志和访问日志。</td><td>Syslog</td></tr><tr><td>3</td><td>集中管理 &gt; 扩展支持 &gt; 支持列表</td><td>为利于安全扫描和易于管理等,idea插件从产品发布包内移除。若有需要,可联系东方通相关人员获取。</td><td>下载IntelliJIDEA TongWeb插件</td></tr></table>
• A03
<table><tr><td>序号</td><td>功能模块</td><td>功能说明</td><td>相关章节</td></tr><tr><td>1</td><td>首页</td><td>“产品信息”中的“版本号”修改为“产品版本”。</td><td>查看产品信息</td></tr><tr><td>2</td><td>应用管理&gt;应用</td><td>新增“解压目录”属性,在部署位于服务器上的*.war或*.ear文件时,指定该文件的解压目录。若配置为空,则解压到文件所在目录。</td><td>应用配置参数说明</td></tr><tr><td>3</td><td>应用管理&gt;应用模板</td><td>新增“解压目录”属性,在部署位于服务器上的*.war或*.ear文件时,指定该文件的解压目录。若配置为空,则解压到文件所在目录。</td><td>应用模板配置参数说明</td></tr><tr><td>4</td><td>Web容器&gt;虚拟主机</td><td>新增“启用URL重写”属性,支持URL重写和请求转发,能够在请求到达Servlet容器之前对URL进行修改,类似于Apache HTTP服务器中的mod rewrite模块。</td><td>虚拟主机配置参数说明</td></tr><tr><td>5</td><td>EJB容器</td><td>EJB远程通信支持SSL</td><td>访问EJB</td></tr><tr><td>6</td><td>·日志管理&gt;系统日志
·日志管理&gt;系统日志&gt;
日志文件</td><td>·“服务器日志”更名为“系统日志”。
·移除了“使用系统配置”。
·新增“文件名称”属性,支持设置日志文件的名称。</td><td>·系统日志
·系统日志配置参数说明</td></tr><tr><td>7</td><td>·日志管理&gt;访问日志配置
·日志管理&gt;访问日志明细</td><td>·“访问日志”页面更名为“访问日志配置”。
·移除了“使用系统配置”。
·新增访问日志明细，用于可视化展示访问日志开启后请求处理记录。</td><td>新增“访问日志明细”页面，可查看访问日志明细。</td></tr><tr><td>8</td><td>安全管理&gt;安全策略&gt;通信</td><td>将“序列化安全”页签名称修改为“通信”。</td><td>配置安全策略</td></tr><tr><td>9</td><td>集中管理&gt;日志管理&gt;审计配置</td><td>移除了“使用系统配置”。</td><td>审计配置</td></tr><tr><td>10</td><td>集中管理&gt;实例</td><td>新增重启实例功能。</td><td>管理实例</td></tr><tr><td>11</td><td>“admin.[bat|sh)”脚本使用说明</td><td>补充创建domain时输入实例名称domainName)的注意事项。</td><td>domain</td></tr></table>
• A02
<table><tr><td>序号</td><td>功能模块</td><td>功能说明</td><td>相关章节</td></tr><tr><td>1</td><td>应用管理 &gt; 应用 &gt; 性能</td><td>·新增“客户端资源缓存”属性，支持为特定资源添加 Expires 和 Cache-Control 响应头以设置客户端缓存。
·“阻塞阈值”和“中断阈值”的单位由“秒”修改为“毫秒”。</td><td>应用</td></tr><tr><td>2</td><td>应用管理 &gt; 应用</td><td>将“SpringBoot 兼容”修改为默认关闭，以增加安全可控性。</td><td>控制台部署应用</td></tr><tr><td>3</td><td>应用管理 &gt; 应用</td><td>监视项目新增“平均请求处理时间”。</td><td>监视应用</td></tr><tr><td>4</td><td>应用管理 &gt; 应用</td><td>自动部署应用支持通过自定义描述文件配置“startupPriority”，指定启动顺序。</td><td>设置多应用启动优先级</td></tr><tr><td>5</td><td>应用管理 &gt; 应用迁移</td><td>新增“是否拷贝应用”属性，指定迁移过程中是否拷贝应用。若关闭“是否拷贝应用”开关，则仅迁移服务器的配置。</td><td>·应用迁移
·应用迁移配置参数说明</td></tr><tr><td>6</td><td>·Web 容器 &gt; 数据源 &gt; 连接参数
·EJB 容器 &gt; JCA 连接池
·EJB 容器 &gt; JCA 托管对象</td><td>连接属性/其他属性中的 password 属性加密存储。</td><td>·创建数据源
·创建 JCA 连接池
·创建 JCA 托管对象</td></tr><tr><td>7</td><td>Web 容器 &gt; 数据源</td><td>·页面参数进行了重新排布，提高易用性。
·客户端信息页面改为键值对形式。</td><td>数据源</td></tr><tr><td>8</td><td>Web 容器 &gt; 数据源 &gt; 连接参数</td><td>因功能冲突等原因，移除了“重置连接活跃时间”。</td><td>数据源配置说明</td></tr><tr><td>9</td><td>Web 容器 &gt; 数据源 &gt; 连接池</td><td>·新增“线程公平等待”属性，在连接池为空时，客户端线程会等待池中有连接可用，打开此功能后，先等待的线程会优先获得连接，否则顺序会不确定（但会有更好的性能）。
·新增“即时回收”属性，对未关闭的连接在请求结束后立即回收到连接池，以供继续复用。
·“使用LIFO队列”默认值修改为false。</td><td>数据源配置说明</td></tr><tr><td>10</td><td>Web 容器 &gt; 数据源 &gt; 健康管理</td><td>“检查后的清理策略”更名为“失效清理策略”，并在开启“空闲时验证”后有效。</td><td>数据源配置说明</td></tr><tr><td>11</td><td>Web 容器 &gt; 数据源 &gt; 语句管理</td><td>新增“SQL 错误时回收”属性，支持在执行 SQL 遇到错误时，立即回收当前连接。</td><td>数据源配置说明</td></tr><tr><td>12</td><td>Web 容器 &gt; 数据源</td><td>新增“回收器工作中”监视量，以反映空闲连接验证的线程状态。</td><td>监视数据源</td></tr><tr><td>13</td><td>其它容器 &gt; WebFlux 应用</td><td>新增支持部署和管理基于 Spring WebFlux 开发的应用程序。</td><td>WebFlux 应用</td></tr><tr><td>14</td><td>资源管理 &gt; 会话服务器</td><td>外部会话服务器新增支持 RDS 类型。</td><td>会话服务器</td></tr><tr><td>15</td><td>日志管理 &gt; 服务器日志 &gt; 基本属性</td><td>·服务器日志中的“接管系统打印”新增“应用日志仅输出到控制台”开关。
·新增“轮询间隔”属性，开启异步日志后，TongWeb会周期性检测是否有需要输出的日志，此处可设置检测的频率，即每隔多久检测一次，单位：毫秒。</td><td>·服务器日志
·服务器日志配置说明</td></tr><tr><td>16</td><td>·日志管理 &gt; 服务器日志
·日志管理 &gt; 访问日志
·集中管理 &gt; 安全配置 &gt; 审计配置</td><td>·服务器日志、访问日志、审计日志增加“追加类型目录”开关，开启后，在指定的目录下增加一个类型目录以存放日志文件。
·服务器日志、访问日志、审计日志增加“日志文件轮转”和“日志追加”控制开关。</td><td>·服务器日志配置说明
·访问日志配置说明
·审计日志配置参数说明</td></tr><tr><td>17</td><td>日志管理 &gt; 服务器日志 &gt; 日志级别</td><td>新增“Java Logger 日志级别”属性，默认和系统日志级别保持一致。</td><td>服务器日志配置说明</td></tr><tr><td>18</td><td>·日志管理 &gt; 服务器日志 &gt; 在线日志
·日志管理 &gt; 访问日志 &gt; 在线日志</td><td>优化了服务器日志和访问日志的在线检索功能。</td><td>·在线实时查看服务器日志
·在线实时查看访问日志</td></tr><tr><td>19</td><td>基础配置 &gt; 全局配置 &gt; 应用</td><td>自动部署应用增加可选“生成状态标签”和“部署到 deployment”。</td><td>·自动部署应用
·全局配置</td></tr><tr><td>20</td><td>基础配置 &gt; 全局配置 &gt; 应用</td><td>将“忽略客户端异常”从“应用管理”&gt;“应用”&gt;“其它”页签，移动到了“基础配置”&gt;“全局配置”&gt;“应用”页签。</td><td>·应用
·全局配置</td></tr><tr><td>21</td><td>基础配置 &gt; 全局配置 &gt; 应用</td><td>·新增“服务器文件大小限制”属性，当文件来源为服务器文件时，出于安全考虑，限定了读取文件的大小（单位：MB）。设置为0表示拒绝读取所有文件。
·新增“映射ROOT路径”属性，可自动将“ROOT”名字的应用访问前缀设置为“/”。</td><td>全局配置</td></tr><tr><td>22</td><td>基础配置 &gt; 全局配置 &gt; 应用</td><td>支持将“应用备份数量”配置为0，表示禁用备份。</td><td>全局配置</td></tr><tr><td>23</td><td>基础配置 &gt; JVM 配置 &gt; GC 策略</td><td>垃圾回收器新增支持 “ZGC”。</td><td>JVM 配置</td></tr><tr><td>24</td><td>集中管理 &gt; 服务管理 &gt; 节点</td><td>节点属性移除 “命名空间”。用户可根据需要在 “节点” 或 “实例” 的 “全局配置” 中切换命名空间。</td><td>· 创建节点
· 节点参数配置说明</td></tr><tr><td>25</td><td>集中管理 &gt; 日志管理 &gt; 审计配置</td><td>可设置是否启用审计日志功能。</td><td>启动审计日志</td></tr><tr><td>26</td><td>集中管理 &gt; 系统管理 &gt; 远程 JMX</td><td>新增支持 “开启 SSL” , 使用 TLS 加密网络数据。</td><td>远程 JMX</td></tr><tr><td>27</td><td>集中管理 &gt; 扩展支持 &gt; 进阶使用</td><td>standalone.sh 单进程模式不再强依赖之前的任何环境变量, 可选使用 JAVA_OPTS 环境变量设置 JVM 启动参数。</td><td>单进程启动模式</td></tr><tr><td>28</td><td>集中管理 &gt; 扩展支持 &gt; 进阶使用</td><td>安全考虑, 移除 “调试功能”。</td><td>移除 “打开调试功能” 章节。</td></tr><tr><td>29</td><td>admin 脚本 "${tongweb.home}/bin"</td><td>admin 脚本的 password 命令更名为encrypt, 并新增多种编码或加密方式。</td><td>encrypt</td></tr><tr><td>30</td><td>admin 脚本 "${tongweb.home}/bin"</td><td>新增 start-args 命令, 以单进程模式运行TongWeb 服务器实例。</td><td>start-args</td></tr></table>

# • A01
首次发版。
相对于 8.0.8.4，变更内容如下所示。
<table><tr><td>序号</td><td>功能模块</td><td>功能说明</td><td>相关章节</td></tr><tr><td>1</td><td>应用管理 &gt; 应用 &gt; 其它</td><td>·新增“忽略客户端异常”属性，支持忽略客户端异常，以避免非必要的异常处理和日志打印等。
·出于兼容性考虑，默认打开“允许覆写ContentType”。</td><td>应用</td></tr><tr><td>2</td><td>应用管理 &gt; 应用</td><td>增加并行部署对自动部署的多个应用生效。</td><td>自动部署</td></tr><tr><td>3</td><td>·应用管理&gt;应用&gt;其它
·Web容器&gt;通道&gt;
HTTP属性
·基础配置&gt;全局配置&gt;
服务器</td><td>新增“附加响应头”属性，允许服务器在 HTTP响应中附加自定义头部信息。
优先级：应用的优先级高于通道，通道优先级高于全局配置。</td><td>·应用
·通道
·全局配置</td></tr><tr><td>4</td><td>应用管理&gt;应用迁移</td><td>支持迁移WebLogic应用。</td><td>应用迁移</td></tr><tr><td>5</td><td>Web容器&gt;通道</td><td>·在“HTTP属性”页签，新增“附加原因短语”开关，开启后，在HTTP响应中添加 HTTP Reason Phrase（原因短语）。
·在“其它”页签，启用网络数据监控时，支持统计端口上处理的慢请求数量、支持周期性归零监控数据。
·在“通道/监视”页面，新增“慢请求总数”统计项。</td><td>·通道
·监视通道</td></tr><tr><td>6</td><td>Web容器&gt;虚拟主机</td><td>新增“使用 Json报告”开关，开启此选项后，任何导致HTTP错误状态码的请求都将收到一个包含错误信息的JSON数据格式的响应。</td><td>虚拟主机</td></tr><tr><td>7</td><td>Web容器&gt;数据源</td><td>·数据源配置模板“数据库连接方式”增加 “TDSQL-MySQL”。
·支持数据源的用户名加密存取。
·在“池大小”页签中，新增“单批次创建数”和“批次间隔”，连接池的数据库连接分批次创建，以减小对数据库的压力。
·在“健康检查”页签中，新增“清除策略”，检测到失效连接时如何清除连接（清除“当前检测连接”或“所有空闲连接”）。
·在“慢SQL监视”中，记录较慢SQL/记录失败SQL，慢SQL和失败SQL日志记录到独立的日志文件中“${tongweb.base}/logs/sql”。</td><td>·创建数据源
·数据源配置
参数说明</td></tr><tr><td>8</td><td>监视管理 &gt; Prometheus服务</td><td>Prometheus 的访问记录到访问日志中。</td><td>查看Prometheus 访问 TongWeb 的日志</td></tr><tr><td>9</td><td>日志管理 &gt; 服务器日志 &gt; 日志文件</td><td>新增 “开启线程日志” 开关,开启线程日志后,系统日志在原有日志的基础上,会同步地单独保存到一个独立的文件中。</td><td>服务器日志</td></tr><tr><td>10</td><td>基础配置 &gt; 全局配置 &gt; 服务器</td><td>新增 “切换命名空间” 开关,开启后,自动切换命名空间。</td><td>• 全局配置• 命名空间</td></tr><tr><td>11</td><td>基础配置 &gt; 全局配置 &gt; 服务器</td><td>• “启用 WebService” 功能新增支持 “兼容JBoss” 的 WSDL 格式。• 新增 “启用 JPA” 开关,开启后,将加载 TongWeb 内置的 JPA 组件。</td><td>全局配置</td></tr><tr><td>12</td><td>基础配置 &gt; 全局配置 &gt; 应用</td><td>新增 “启动时部署” 开关。开启后,扫描自动部署目录,执行且仅执行一次应用自动部署。</td><td>• 全局配置• 自动部署</td></tr><tr><td>13</td><td>• 集中管理 &gt; 服务管理 &gt; 实例• 集中管理 &gt; 服务管理 &gt; 集群• 集中管理 &gt; 服务管理 &gt; 节点• 集中管理 &gt; 服务管理 &gt; 负载均衡器• 集中管理 &gt; 资源配置 &gt; 消息服务器</td><td>实例、集群、节点、负载均衡器、消息服务器等资源名称不再允许使用冒号。</td><td>• 创建实例• 创建集群• 创建节点• 创建负载均衡器• 创建消息服务器</td></tr><tr><td>14</td><td>集中管理 &gt; 安全配置 &gt; 管理员 &gt; 安全</td><td>• 新增 “密码最小长度” 属性• 新增 “包含类型” 属性• 管理员可以为不同用户设置各自的密码规则(如密码最小长度和复杂度)。新用户可以根据自己的密码规则进行密码更新。• 用户可以添加启动参数,禁用密码校验。</td><td>• 创建管理员• 管理员• 可添加启动参数</td></tr><tr><td>15</td><td>集中管理 &gt; 安全配置 &gt; 控制台安全</td><td>移除关闭控制台的 “校验密码强度”。</td><td>控制台安全</td></tr><tr><td>16</td><td>集中管理 &gt; 系统管理 &gt; 一键巡检</td><td>增加基线扫描报告。</td><td>一键巡检</td></tr><tr><td>17</td><td>集中管理 &gt; 服务管理 &gt; 节点</td><td>创建节点时，用户可选择在不同的节点上创建不同命名空间（ javax 或 jakarta）的TongWeb 包。TongWeb 集群支持同时管理这两种命名空间的实例。</td><td>· TongWeb 集群
· 创建节点</td></tr><tr><td>18</td><td>集中管理 &gt; 系统管理 &gt; 产品升级</td><td>支持通过控制台回退版本。</td><td>版本回退</td></tr><tr><td>19</td><td>集中管理 &gt; 扩展支持 &gt; 支持列表</td><td>支持卫士通密码机对密钥文件进行加密。</td><td>Westone</td></tr><tr><td>20</td><td>集中管理 &gt; 扩展支持 &gt; 进阶使用 &gt; 单进程启动模式</td><td>在设置环境变量时，变量都提供了默认值，用户可以选择不设置。</td><td>单进程启动模式</td></tr><tr><td>21</td><td>集中管理 &gt; 扩展支持 &gt; 示例应用</td><td>添加 ejb 安全角色示例ejbRolesAllowedExample。</td><td>示例应用</td></tr></table>

# 前言
本文档是 TongWeb 产品的用户使用手册之一，提供管理控制台对应用进行部署、管理操作等说明。

# 阅读前注意事项
通过阅读本文档，您确认并同意自行承担因未具备必要专业背景和知识而导致的任何风险或后果。在使用本文档中提供的信息和指南时，请始终谨慎，并在必要时寻求专业人士建议和指导。
• 适用对象
本文档主要适用于使用本产品的系统管理员阅读，部分内容同样适用于基于本产品进行应用开发或应用部署的人员阅读。
• 专业背景
本文内容可能涉及到操作系统、服务器硬件、网络等相关领域的知识。请确保您具备相关背景和知识，以便更好地理解和应用本手册的内容。
• 技能要求
为了能够充分理解和应用本文档的内容，建议您具备如下技能：
◦ 基本系统管理任务
◦ 掌握 Linux 系统基本操作
◦ 在终端窗口发布命令
◦ 使用 Web 浏览器
◦ 安装软件
• 术语和概念
本文档可能使用一些专业术语和概念。请确保您熟悉这些术语和概念，或者有能力查阅相关资料以便进一步理解。
• 实践经验
为了最大程度地受益于本文档，建议您具备一定实践经验。这将帮助您更好地应用文档中的操作指南和建议。
请注意，本文档不适用于没有相关专业背景和知识的用户。如果您对本文档的内容或所需背景有任何疑问，请在使用之前咨询相关专业人士或寻求额外的支持。

# 用户手册集
TongWeb 为您提供如下用户使用手册。
<table><tr><td>用户手册</td><td>说明</td></tr><tr><td>000_TongWeb_V8.0产品对比手册</td><td>详细介绍了TongWeb的版本差异以及如何选择TongWeb的产品等。</td></tr><tr><td>001_TongWeb_V8.0产品介绍手册</td><td>详细介绍了TongWeb的概述、体系结构、版本功能对比等信息。</td></tr><tr><td>002_TongWeb_V8.0安装与使用指引</td><td>详细介绍了TongWeb各平台上的安装启动、版本切换等说明。</td></tr><tr><td>003_TongWeb_V8.0控制台使用手册</td><td>详细介绍了TongWeb管理控制台对应用进行部署、管理操作等说明。</td></tr><tr><td>004_TongWeb_V8.0命令行工具手册</td><td>详细介绍了TongWeb命令行工具的使用说明。</td></tr><tr><td>005_TongWeb_V8.0REST API手册</td><td>详细介绍了TongWeb REST接口的使用说明。</td></tr><tr><td>006_TongWeb_V8.0常见问题手册</td><td>详细介绍了使用TongWeb过程中遇到的常见问题及解决方案。</td></tr><tr><td>007_TongWeb_V8.0安全加固手册</td><td>详细介绍了TongWeb常见的安全加固配置方法说明。</td></tr><tr><td>008_TongWeb_V8.0容器化部署手册</td><td>详细介绍了TongWeb在容器上的部署说明。</td></tr></table>

# 技术支持
东方通产品将为您提供全方位的技术支持，您可以通过以下方式获得技术支持：
• 网址：www.tongtech.com
• 电话：400-650-7088
• 邮箱：support@tongtech.com
您在取得技术支持时，请提供如下信息：
• 您的姓名
• 您的公司信息
• 您的联系方式
• 操作系统及其版本
• 产品版本号
• 日志等错误的详细信息


# 1. 快速上手
# 1.1. 初级操作指引
# 1.1.1. 登录管理控制台
# 1.1.1.1. Windows 平台
# 1.1.1.1.1. 步骤1：启动 TongWeb
1. 进入 “${tongweb.home}/bin/windows” 目录。
2. 运行 startd.bat ，以后台模式启动 TongWeb 应用服务器默认实例。
关于启停 TongWeb 的更多信息，详见《TongWeb_V8.0安装与使用指引》的 “启停 TongWeb” 章节。

# 1.1.1.1.2. 步骤2：登录管理控制台
首次登录 TongWeb 管理控制台，请通过安装 TongWeb 的本机浏览器进行登录。
1. 在浏览器地址中，输入如下地址，按 Enter，进入 TongWeb 管理控制台登录页面。
```txt
https://localhost:9060/console
```
# 说明：
◦ 请使用 “https” 协议访问 TongWeb 管理控制台。
◦ 9060：为 TongWeb 管理控制台默认监听端口。
2. 在输入登录地址后，会弹出安全提示页面。
3. 直接单击 “高级” $>$ “继续访问”，即可访问 TongWeb 管理控制台登录页面。

# TongWeb
# 管理控制台
# 用户登录
D动态密码

# 登录
已阅读并同意《许可协议》
4. 输入 “账户名称” 和 “账户密码”，进入 TongWeb 管理控制台。
系统管理员默认账户，如下所示。
◦ 账户名称：thanos
◦ 账户密码：thanos123.com
◦ 动态密码：若未开启 “动态密码”，则可不填写，默认未开启。
关于如何开启 “动态密码”，请参见 《TongWeb_V8.0控制台使用手册》中 “开启动态密码”。

# 注意：
◦ 当用户首次登录失败后，需要输入登录验证码。
◦ 默认情况下，用户连续认证失败 5 次后，账户将被锁定。
◦ 默认情况下，当控制台会话持续超时达 15 分钟，账号将自动退出登录。
◦ 用户也可使用 OAuth2 协议登录控制台，详见 《TongWeb_V8.0控制台使用手册》中的 “OAuth2 协议登录控制台”。
关于控制台安全相关策略，请进入控制台 “集中管理” > “安全配置” $>$ “控制台安全”，设置控制台相关安全策略。
5. 阅读《许可协议》，并勾选 “已阅读并同意《许可协议》”。
注：当用户勾选 “已阅读并同意《许可协议》” 选项时，页面会弹出 “下次自动勾选” 选项。若用户勾选此选项，系统将自动记录该勾选状态。
6. 单击 “登录”，即可进入 TongWeb 控制台 “默认实例” 的 “首页” 页面。

# 注意：
默认情况下，控制台会话超时时间为 15 分钟。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/93600547df246da19524b10e4e6f101b92a21da1a9e6452df737e0326e32d887.jpg)

# 1.1.1.1.3. 步骤3：修改初始密码
为了保障系统的安全性，成功登录 TongWeb 管理控制台后，系统强制要求修改“初始密码”。
修改初始密码，要求在安装 TongWeb 的本机 IP 上进行修改。
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击“集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择“安全配置”>“修改密码”，进入修改密码页面。
4. 修改初始密码，参数说明如下表所示。
<table><tr><td>参数</td><td>参数说明</td></tr><tr><td>原始密码</td><td>登录系统的原始密码。</td></tr><tr><td>新密码</td><td>用于登录系统的新密码。
密码长度介于10-20个字符之间，新密码不能和原始密码相同。</td></tr><tr><td>确认密码</td><td>确认用于登录系统的新密码。</td></tr><tr><td>动态密码</td><td>默认“不开启”。
若需要开启“动态密码”，请参见《TongWeb_V8.0控制台使用手册》中的“开启动态密码”。</td></tr></table>
5. 密码修改完成后，单击“更新”，更新密码信息。
若界面弹出 “修改密码成功” 提示信息，则说明修改密码成功。

# 1.1.1.1.4. 步骤4：设置信任 IP
若仅使用安装 TongWeb 的本机访问 TongWeb 控制台，则可跳过此步骤。
若需要使用远程浏览器访问 TongWeb 管理控制台，需要将远程浏览器所在的主机 IP 设置为“信任 IP”。设置为 “*” 表示信任所有机器（不建议）。
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击“集中管理”，进入集中管理页面。
3. 选择 “安全配置” > “控制台安全”，进入控制台页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/b865b9726143035c5830251e2522a80f6ff5e170a13adf5da1439163b00c52d9.jpg)
4. 设置 “信任 IP” 即可。
信任 IP 设置完成后，您即可通过信任 IP 所在浏览器客户端访问 TongWeb 管理控制台。

# 1.1.1.2. Linux 平台
# 1.1.1.2.1. 步骤1：设置信任 IP
首次登录 TongWeb 管理控制台前，请在安装 TongWeb 的本机将远程浏览器访问 TongWeb 的主机 IP 设置为 “信任 IP”。
设置为 “*” 表示信任所有机器（不建议）。
本示例采用修改主配置文件 “console.xml” 的方式，设置信任 IP。

# 注意事项
• 主配置文件 “console.xml” 具备防篡改限制，在运行期间禁止对其进行修改。若需要修改并使其生效，请确保 TongWeb 服务器处于停止状态，然后再进行修改。
• 若已启动 TongWeb 且不希望停止 TongWeb，可使用命令行方式来设置信任 IP。详细信息请参见《TongWeb_V8.0控制台使用手册》的 “控制台安全” $>$ “设置信任 IP” 章节。
# 前置条件
已获取远程浏览器客户端所在的 IP 地址。
# 操作步骤
1. 进入 “${tongweb.base}/conf” 目录。
2. 打开 “console.xml” 文件。
3. 将 “trustedIP” 设置为远程浏览器客户端所在的主机 IP。
注：请根据实际情况替换为您远程浏览器客户端的主机 IP。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/19bb19cad6d3c33b98eee13f3cb141fc8066c5c76468c92d2d1547982dddda08.jpg)


# 1.1.1.2.2. 步骤2：启动 TongWeb
1. 进入 “${tongweb.home}/bin” 目录。
2. 运行 ./startd.sh ，以后台模式启动 TongWeb 服务器默认实例。
若回显信息出现 “Server startup in xx seconds”，则说明启动 TongWeb 成功。
关于启停 TongWeb 的更多信息，详见《TongWeb_V8.0安装与使用指引》的 “启停 TongWeb” 章节。

# 1.1.1.2.3. 步骤3：登录管理控制台
通过远程浏览器客户端访问 TongWeb 管理控制台。
1. 在浏览器地址中，输入如下地址，按 Enter，进入 TongWeb 管理控制台登录页面。
```txt
https://<TongWebIP>:9060/console
```

# 说明：
◦ <TongWebIP>：表示 TongWeb 主机 IP 地址。
◦ 9060：TongWeb 管理控制台默认监听端口。
用户可根据需要打开 “${tongweb.base}/conf/tongweb.xml” 文件，进行修改。
注：tongweb.xml 为 TongWeb 主配置文件，具有防篡改限制。若需要修改并使其生效，请先停止TongWeb 服务器，然后再进行修改。
2. 在输入登录地址后，会弹出安全提示页面。
3. 直接单击 “高级” $>$ “继续访问”，即可访问 TongWeb 管理控制台登录页面。

# TongWeb

# 管理控制台

# 用户登录
D动态密码

# 登录
已阅读并同意《许可协议》
4. 输入 “账户名称” 和 “账户密码”，进入 TongWeb 管理控制台。
系统管理员默认账户，如下所示。
◦ 账户名称：thanos
◦ 账户密码：thanos123.com
◦ 动态密码：若未开启 “动态密码”，则可不填写，默认未开启。
关于如何开启 “动态密码”，请参见 《TongWeb_V8.0控制台使用手册》中 “开启动态密码”。

# 注意：
◦ 当用户首次登录失败后，需要输入登录验证码。
◦ 默认情况下，用户连续认证失败 5 次后，账户将被锁定。
◦ 默认情况下，当控制台会话持续超时达 15 分钟，账号将自动退出登录。
◦ 用户也可使用 OAuth2 协议登录控制台，详见 《TongWeb_V8.0控制台使用手册》中的 “OAuth2 协议登录控制台”。
关于控制台安全相关策略，请进入控制台 “集中管理” > “安全配置” $>$ “控制台安全”，设置控制台相关安全策略。
5. 阅读《许可协议》，并勾选 “已阅读并同意《许可协议》”。
注：当用户勾选 “已阅读并同意《许可协议》” 选项时，页面会弹出 “下次自动勾选” 选项。若用户勾选此选项，系统将自动记录该勾选状态。
6. 单击 “登录”，即可进入 TongWeb 控制台 “默认实例” 的 “首页” 页面。

# 注意：
默认情况下，控制台会话超时时间为 15 分钟。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/83cf1cad9db7e31e9d22424cdaaabdf138d8ccdd38f39f9877e1c39b660404ec.jpg)


# 1.1.1.2.4. 步骤4：修改初始密码
为了保障系统的安全性，成功登录 TongWeb 管理控制台后，系统强制要求修改 “初始密码”。
修改初始密码后，才允许用户执行相关操作。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击“集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择“安全配置”>“修改密码”，进入修改密码页面。
4. 修改初始密码，参数说明如下表所示。
<table><tr><td>参数</td><td>参数说明</td></tr><tr><td>原始密码</td><td>登录系统的原始密码。</td></tr><tr><td>新密码</td><td>用于登录系统的新密码。
密码长度介于10-20个字符之间，新密码不能和原始密码相同。</td></tr><tr><td>确认密码</td><td>确认用于登录系统的新密码。</td></tr><tr><td>动态密码</td><td>默认“不开启”。
若需要开启“动态密码”，请参见《TongWeb_V8.0控制台使用手册》中的“开启动态密码”。</td></tr></table>
5. 密码修改完成后，单击“更新”，更新密码信息。
若界面弹出 “修改密码成功” 提示信息，则说明修改密码成功。

# 1.1.2. 查看产品信息
本章节主要介绍如何查看 TongWeb 产品信息。
1. 登录 TongWeb 管理控制台，进入 “默认实例” 页面。
2. 在左侧导航栏中，单击 “首页”，进入“首页”页面。
3. 您可以查看 TongWeb 产品的产品相关信息，如下表所示。
<table><tr><td>参数</td><td>说明</td></tr><tr><td colspan="2">产品信息</td></tr><tr><td>产品名称</td><td>产品的名称为“TongWeb”。</td></tr><tr><td>产品版本</td><td>产品的版本号。</td></tr><tr><td>运行模式</td><td>当前TongWeb 运行模式。</td></tr><tr><td>命名空间</td><td>命名空间，例如： javax、jakarta。</td></tr><tr><td>实例目录</td><td>产品的实例的目录。</td></tr><tr><td>安装目录</td><td>产品的安装目录。</td></tr><tr><td>Java 环境</td><td>服务器实例使用的java 路径信息。</td></tr><tr><td>构建日期</td><td>服务器构建的日期。</td></tr><tr><td colspan="2">授权信息</td></tr><tr><td>授权产品</td><td>授权产品为“TongWeb”。</td></tr><tr><td>授权版本</td><td>授权产品的版本类型。</td></tr><tr><td>版本类型</td><td>产品的版本类型。</td></tr><tr><td>授权客户</td><td>授权客户的名称。</td></tr><tr><td>授权类型</td><td>产品的授权类型。</td></tr><tr><td>授权期限</td><td>授权期限，授权期限内才能启动TongWeb。</td></tr><tr><td>授权节点数</td><td>授权集中管理可管理的最大节点数。</td></tr><tr><td>授权IP</td><td>授权的IP地址，只允许在授权IP段范围内的IP地址，才能启动TongWeb。注意：
·TongWeb每日06:00检查license有效期，若license到期，TongWeb将停止服务。
·用户也可以自定义授权检查时间及授权到期提醒。
  ·进入“基础配置”&gt;“全局配置”&gt;“授权”，在授权页面设置“授权检查时间”，详情请参见设置授权检查时间。
  ·进入“基础配置”&gt;“全局配置”&gt;“授权”，在授权页面设置“授权到期提醒”，详情请参见设置授权到期提醒。</td></tr><tr><td>授权绑定MAC</td><td>授权绑定的MAC地址。</td></tr></table>

# 1.1.3. 管理默认实例（domain1）
登录 TongWeb 控制台后，TongWeb 提供一个 “默认实例” 供用户使用。默认本地实例路径为
“${tongweb.home}/domains/domain1/”。
用户可以根据需要在默认实例上进行应用管理、Web 容器、EJB 容器、其他容器、资源管理、监视管理、诊断管理、、日志管理、安全管理、基础配置等操作，详见应用管理及配置管理。
默认实例操作界面，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/1a1a8ec60076d7d071fd51087747ff2ca43e4293b6c44450a09a152477dea22c.jpg)


# 1.1.4. 单机多实例管理
若 TongWeb 提供的 “默认实例” 无法满足您的需求，您可以根据自己的需要创建一个或多个自己的实例，多实例场景说明请参见多实例场景。
创建的本地 TongWeb 实例默认存放在 “${tongweb.home}/domains/” 目录。
在不同实例上您可以根据需要进行应用管理、Web 容器、EJB 容器、其它容器、资源管理、监视管理、诊断管理、日志管理、安全管理、基础配置等操作。

# 注意：
在同一个节点多个实例场景下，建议默认实例 domain1 只做管理，不部署应用。

# 1.1.4.1. 多实例场景
通常情况下一台服务器只需要安装一套 TongWeb。
若存在如下场景，则可通过创建多个实例的方式解决。
<table><tr><td>场景</td><td>场景说明</td></tr><tr><td>场景一</td><td>服务器CPU、内存比较大，可通过创建多个TongWeb实例，充分利用系统资源。</td></tr><tr><td>场景二</td><td>不同应用需要使用不同JDK版本，关于如何给不同实例配置不同的JDK版本，请参见不同实例配置不同JDK版本。</td></tr><tr><td>场景三</td><td>应用之间互相冲突，需要分别部署在不同TongWeb实例上。</td></tr><tr><td>场景四</td><td>应用有内存溢出或占用线程资源多，频繁出问题的放一个TongWeb实例上运行，不影响其它应用。</td></tr></table>

# 1.1.4.2. 创建本地实例
支持将本地 TongWeb 实例安装到一个指定的绝对目录（若目录不存在，TongWeb 将则会自动建立）。

# 注意：
Windows 下创建实例时，若需要指定安装目录，可能需要管理员启动 TongWeb。
若未指定安装目录，则默认安装到 “${tongweb.base}/domains” 目录下。
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例页面。
4. 配置实例相关信息。
5. 单击 “创建”，进入创建实例页面。
◦ 名称：必填项，输入实例名称。请使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 所在节点：选择 “default”。
◦ 其他参数：请根据需要配置。
6. 配置完成后，单击 “添加”，完成实例的添加操作。
本地实例创建完成后，默认为 “停止” 状态。

# 1.1.4.3. 启停本地实例
用户可根据需要启动、停止实例。

# 启动实例
实例创建后，默认为“停止”状态，为了能对实例进行管理，首先您需要启动实例。
启动实例可能因为超时而导致失败，您可以在一段时间后刷新状态，确认是否启动成功。
1. 进入 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例页面。
4. 单击目标实例所在行的 “启动”，弹出确认启动实例窗口。
5. 单击 “确定”，完成启动实例操作。
若界面弹出 “实例启动成功” 提示信息，且 “运行中” 更新为 “true”，则说明实例启动成功。

# 停止实例
您可以根据需要停止处于“启动”状态的实例。
1. 进入 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例页面。
4. 单击目标实例所在行的 “停止”，弹出确认停止实例窗口。
5. 单击 “确定”，完成停止实例操作。
若界面弹出“实例停止成功”提示信息，且“运行中”更新为“false”，则说明实例停止成功。

# 1.1.4.4. 切换本地实例
已创建且启动实例，才能切换实例。切换到目标实例后，您才能对目标实例进行管理。
1. 进入 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a9d67ba87ff2ac32e160a3afa46d55ee1e4549088eec86a58c070603eaaf84cf.jpg)
4. 单击 “管理”，即可切换到目标实例。
您即可在该实例上进行相关配置管理，包含应用管理、Web容器、EJB容器、资源管理等。

# 1.1.4.5. 管理本地实例
您可以根据需要对本地实例进行应用管理、Web 容器、EJB 容器、其它容器、资源管理、监视管理、诊断管理、日志管理、安全管理、基础配置等操作，详见应用管理及配置管理。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/8fe29b9baaa61f46fb96ebaee02381bbcbda5123f59c949b4a8cf9f9437a15a4.jpg)


# 1.1.5. TongWeb 集群管理
在实际应用中存在多种高并发的业务场景，需要构建 Web 应用服务器集群予以支撑。
TongWeb 集群是由多个同时运行的 JavaEE 应用服务器（TongWeb 实例）、负载均衡器、TDG 组成。集群中负载均衡器、TongWeb 实例、TongDataGrid（TDG） 可以任意增加节点，无启动顺序要求。
关于如何搭建和管理 TongWeb 集群，请参见集群管理。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a08b836ead5ade6fd4e806205943dd978e1f1479d63287d10423d605bda66a8f.jpg)


# 1.1.6. 收藏常用菜单
您可以根据需要将常用的菜单进行收藏，收藏后可在 “我的收藏” 中进行快速定位操作。
如下以将“应用”加入“我的收藏”为例进行说明。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 单击列表右侧的 “★”，即可点亮该菜单，添加到 “我的收藏”。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/955b8b0caeb150c394d5d8ae6c33e92934fa0e8307d53192bba3e22e98503e46.jpg)
5. 在左侧导航栏中，可查看到生成“我的收藏”菜单栏，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/98875eaf00029edb51296053a1d024767390763430811416b6aceee06b1e6b5b.jpg)


# 说明：
◦ 您也可以使用同样的方式，将 “★” 点灭，取消收藏的菜单。
◦ 当 “我的收藏” 里的菜单全部都取消收藏后，“我的收藏” 菜单栏将会消失。

# 1.1.7. 隐藏不常用功能
您可以使用页面定制的方式，隐藏不常用的功能。
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “系统管理” > “页面定制”，进入页面定制页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/03b9a1978d6fd8569360b17de542f1889cb95d26a90be0714ad36732e64ccbce.jpg)
4. 在 “隐藏菜单” 下拉菜单中，根据需要勾选隐藏功能。例如：应用回收全部功能。
5. 单击 “更新”，即可完成隐藏功能操作。
6. 进入 “应用管理” 页面，可查看 “应用回收” 功能已隐藏。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/57f0797288031f6bf83ee079da59f00419a2326296e42fdd23b9ff487df395dc.jpg)


# 1.1.8. 搜索指定功能
您可以通过 TongWeb 提供的搜索功能，搜索指定的功能，并跳转到指定位置。
1. 登录 TongWeb 管理控制台。
2. 在控制台右上角的搜索框中，输入待搜索的关键字。
例如：搜索会话服务器，输入 “会话”，即可弹出关键字相关的功能，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/976a2d8cbd69a7569735519c2cc1f99e0a8cb42483cd33b12ef15015e4cbebde.jpg)
3. 在弹出的关键字关联选项中，选择并单击指定功能，即可跳转到指定位置。

# 1.1.9. 其它功能

# 1.1.9.1. 中英繁切换
用户可根据将控制台界面切换为简体、繁体或英文。
1. 登录 TongWeb 管理控制台。
2. 单击切换语言按钮，在弹出的菜单中，选择目标语言，即可切换到对应的控制台界面，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/16192949a80070eb51abbd584ebfdb1333c5236355f080b790ab3bb7f6bb4d45.jpg)


# 1.1.9.2. 在线手册
用户可通过访问在线手册获取最新的产品使用指南。
1. 登录 TongWeb 管理控制台。
2. 单击手册按钮，在弹出的下拉列表中，选择指定手册，即可打开对应的在线手册，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/97b33f5c981846b5cd762d179310cc775276f9056db53b6416c9f334d0b8b4af.jpg)


# 1.2. 进阶使用指引

# 1.2.1. 单进程启动模式
以单个进程的模式来运行 TongWeb 服务器实例。此模式通常更节省系统资源，但基于 tongweb.xml 配置的自动化重启（如宕机重启、定时重启）和自定义环境变量等功能将不可用。
1. 进入安装根目录 “${tongweb.home}/bin”。
2. (可选)按需填写 JVM 启动参数，默认值从 tongweb.xml 中读取。
若配置 JAVA_OPTS 环境变量，可参考以下示例进行设置。
export JAVA_OPTIONS  $=$  "-Xms2048M-Xmx2048M"
3. 执行如下命令，启动 TongWeb 服务器实例。
```txt
./standalone.sh
```

# 1.2.2. 脚本启停实例

# 1.2.2.1. 脚本启动实例
多实例场景下，可根据需要启动默认实例，或者启动指定实例。
• Windows
进入 “${tongweb.home}/windows” 目录。
◦ 以后台模式启动当前主机的默认实例
▪ 若当前主机下存在多个实例，且多个实例均开启 “自启动”，则启动默认实例的同时，由默认实例带动其他实例同步启动。
▪ 若用户仅调试或临时运行实例，可通过执行 startserver.bat 脚本，以前台模式启动。
startd.bat
◦ 后台启动 domains 下所有实例
startd.bat :all
◦ 启动指定实例
startd.bat 实例名
• Linux
进入 “${tongweb.home}” 目录。
◦ 以后台模式启动当前主机的默认实例
▪ 若当前主机下存在多个实例，且多个实例均开启 “自启动”，则启动默认实例的同时，由默认实例带动其他实例同步启动。
▪ 若用户仅调试或临时运行实例，可通过执行 startserver.sh 脚本，以前台模式启动。
./startd.sh
◦ 后台启动 domains 下所有实例
./startd.sh :all
◦ 启动指定实例
./startd.sh 实例名

# 1.2.2.2. 脚本停止实例
多实例场景下，可根据需要停止默认实例，或者停止指定实例。
• Windows
进入“${tongweb.home}/windows”目录。
◦ 停止当前主机的默认实例
stopserver.bat
◦ 停止 domains 下所有实例
stopserver.bat :all
◦ 强停 domains 下所有实例
forcestop.bat :all
◦ 停止指定实例
stopserver.bat 实例名
◦ 强停指定实例
forcestop.bat 实例名
• Linux
进入 “${tongweb.home}” 目录。
◦ 停止当前主机的默认实例
./stopserver.sh
◦ 停止 domains 下所有实例
./stopserver.sh :all
◦ 强停 domains 下所有实例
./forcestop.sh :all
◦ 停止指定实例
./stopserver.sh 实例名
◦ 强停指定实例
./forcestop.sh 实例名

# 1.2.3. 命令行操作集群
通过命令行，操作集群下的实例。
1. 登录控制台创建名为 cluster0 的集群。
2. 单击该集群的 “管理” 即进入其管理页面，可部署应用或进行其它操作。
3. 通过命令行，查看该集群下的应用。
commandstool.bat --username=thanos --password=xxx --acceptAgreement=true --model  $\equiv$  app  
--action=list targetType  $\equiv$  cluster targetsName  $\equiv$  cluster0
操作单个实例或者节点，执行的命令跟集群类似。
◦ 查看某个节点下的应用列表。
```txt
commandstool.bat --username=thanos --password=xxx --acceptAgreement=true --model=app  
--action=list targetsType=node targetsName=要查看的节点名称
```
◦ 查看某个实例下的应用列表。
```txt
commandstool.bat --username=thanos --password=xxx --acceptAgreement=true --model=app  
--action=list targetType=instance targetsName=要查看的实例名称
```
◦ 查看服务发现的某个实例下的应用列表。
```txt
commandstool.bat --username=thanos --password=xxx --acceptAgreement=true --model=app  
--action=list targetType=servicediscovery targetsName=要查看的服务发现的名称
```
以上命令中的参数说明，如下所示。
◦ targetType：对应节点、集群、实例、注册实例的模块名，分别为
“node”、“cluster”、“instance”、“servicediscovery”。
◦ targetName：对应节点、集群、实例、注册实例的名称。

# 1.2.4. admin.[bat|sh] 脚本使用说明
admin 脚本是 TongWeb 服务器的主脚本文件，可用于管理服务器内部资源、服务器启停、版本信息、安装 TongWeb 自启动服务等。
admin 脚本脚本位于 “${tongweb.home}/bin” 目录。
• Linux
```txt
${tongweb.home}/bin/admin.sh
```
• Windows
```txt
\$\{tongweb.home\}/bin.windows/admin.bat
```

# 1.2.4.1. 注意事项
• 命令支持仅输入开头几个字母（能唯一区分于其它命令即可）。
• 命令行支持前缀带 “-” 和 “--” 的使用习惯，如 admin -v 等。
• 版本升级时，需要同时升级 “${tongweb.home}/bin/tongweb-launcher.jar”。

# 1.2.4.2. 执行方式
执行如下命令，可查看 admin 脚本的使用方式。
如下以 Linux 环境为例说明。
```txt
./admin.sh
```
可查看使用方式，如下所示。
```yaml
usage:admin<command> [args]
```
参数说明，如下所示。
• command：可以是 checksum、cli、commandstool、domain、encrypt、error-code、server、start-args、systemd、version。
• args：可根据 command 实际情况设置参数。

# 1.2.4.3. checksum
可通过 ./admin.sh checksum [filepath] 计算文件的哈希值。
以 Linux 环境为例说明，操作步骤如下所示。
1. 进入“${tongweb.home}/bin”目录。
2. 执行如下命令，计算文件的哈希值。
可执行文件以 “/home/jdk1.8.0_261/bin/java” 为例说明。
```txt
./admin.sh checksum /home/jdk1.8.0_261/bin/java
```
回显信息，显示该可执行文件的哈希值及文件路径，如下图所示。
```txt
Execute the command: checksum  
file MD5 checksum:  
4BA98972DE5B19AFB2EF93A081873F6C | /home/jdk1.8.0_261/bin/java  
Copy the above format and paste in ${tongweb.base}/data/secure/trusted-files.txt to add trusted files
```
关于获取的哈希值及文件路径的使用说明，请参见《TongWeb_V8.0控制台使用手册》中的 “可信文件”章节。

# 1.2.4.4. cli
可通过 ./admin.[bat|sh] cli 命令管理服务器内部资源。
cli 与 commandstool 工具功能相同。
cli 工具为交互式命令行工具且可通过 “Tab” 键提示或者自动补全参数。
关于 cli 命令行工具详细使用说明，请参见《TongWeb_V8.0命令行工具手册》。

# 1.2.4.5. commandstool
可通过 ./admin.[bat|sh] commandstool 命令管理服务器内部资源。
以 Linux 环境为例说明。操作步骤如下所示。
1. 进入“${tongweb.home}/bin”目录。
2. 执行如下命令，修改登录 TongWeb 的初始密码。
```batch
sh admin.sh commandstool --model=password --action=update --username=thanos --password=thanos123.com --acceptAgreement=true originalPassword=thanos123.com  
newPassword=Thanos12.com confirmPassword=Thanos12.com --offline
```
若回显信息中出现“修改密码更新成功”字样，则说明修改初始密码成功。

# 1.2.4.6. domain
可通过 ./admin.[bat|sh] domain [create domainName, delete domainName] 命令创建或删除本地 TongWeb 实例。

# 1.2.4.6.1. 注意事项
domainName：仅支持输入实例的名称，且该名称中不得包含路径分隔符）。同时，系统不支持创建具有绝对路径的实例。

# 1.2.4.6.2. 创建 TongWeb 实例
若 domain1 处于运行状态，您只能通过控制台创建实例。
以 Linux 环境为例说明。
1. 进入 “${tongweb.home}/bin” 目录。
2. 执行如下命令，创建 TongWeb 实例。
以创建 “test” 实例为例。
```shell
./admin.sh domain create test
```
回显信息中出现 “Create domain [xxxx] complete!” 字样，则说明创建 TongWeb 实例成功。
3. 进入 “${tongweb.home}/domains” 目录，可查看已创建的 test 实例。

# 1.2.4.6.3. 创建不带管理端口的实例
在创建实例命令的最后加上 “false”，即可创建不带管理端口的实例。

# 注意事项
• 若 domain1 处于运行状态，您只能通过控制台创建实例。
• 不带管理端口的实例不支持远程管理。
• 仅能对不带管理端口的实例进行启停操作。

# 操作步骤
1. 进入 “${tongweb.home}/bin” 目录。
2. 执行如下命令，创建 TongWeb 实例。
以创建 “test” 实例为例。
```txt
./admin.sh domain create test false
```
回显信息中出现 “Create domain [xxxx] complete!” 字样，则说明创建 TongWeb 实例成功。
3. 进入 “${tongweb.home}/domains” 目录，可查看已创建的 test 实例。

# 1.2.4.6.4. 删除 TongWeb 实例
默认实例 domain1 无法删除。
1. 进入 “${tongweb.home}/bin” 目录。
2. 执行如下命令，删除 TongWeb 实例。
以删除 “test” 实例为例。
```shell
./admin.sh domain delete test
```
回显信息中出现 “Delete domain [xxxx] complete!” 字样，则说明应用转换成功。
3. 进入 “${tongweb.home}/domains” 目录，可查看到 test 实例已被删除。

# 1.2.4.7. encrypt
可通过 ./admin.[bat|sh] encrypt [symmetric, digest, asymmetric, id] 命令加密密码，例如：数据库连接密码、HTTP 证书密码等。
• symmetric：表示对称算法。
对称加密适用于：数据源的数据库连接密码；通道的 AJP 协议密钥、私钥库密码、信任库密码、证书密码；节点的 SSH 密码、密钥字符串；JavaMail 资源的会话密码；安全域的连接 LDAP 服务的密码；SNMP 服务的认证密码、加密密码；以及其它需要解密获得原始密码的配置参数。
• digest：表示摘要算法。
摘要加密适用于：控制台管理员的登录密码；安全域用户的用户登录密码。
• asymmetric：表示非对称算法。
非对称加密适用于：在传输过程中需要加密的任意参数，可用于防止网络数据窥探，在使用 SSL 传输时通常不需要再进行此项加密。
• id：表示特殊字符加密。
特殊字符加密适用于：使用 REST 等接口需要传递的 #、?、&、:、%、 $^ +$ 以及空白符等参数。

# 注意事项
加密密码可用于该 TongWeb 的不同实例。

# 操作步骤
以 Linux 环境 “加密密码 thanos123.com” 为例。
1. 进入“${tongweb.home}/bin”目录。
2. 执行如下命令，加密密码 thanos123.com。
```txt
./admin.sh encrypt symmetric thanos123.com
```
若回显信息中出现加密后的密文密码，则说明加密成功。

# 1.2.4.8. error-code
可通过 ./admin.[bat|sh] error-code [Error Code] 命令查找错误码说明。
关于错误码对照表，请参见《TongWeb_V8.0命令行工具手册》中的 “错误码对照表”。
以Linux环境下查找错误码说明为例，操作步骤如下所示。
1. 进入 “${tongweb.home}/bin” 目录。
2. 执行如下命令，查找所有的错误码说明。
```txt
./admin.sh error-code
```
错误码对照说明，如下图所示。
```ini
[root@centos bin]# ./admin.sh error-code  
********** TongWebErrorCode Info ***  
0000:  
%s  
%s  
%s  
0001:  
远程服务器[%s:%s]请求错误：%s。请查看日志以获取详细信息  
远程服务器[%s:%s]请求錯誤：%s。请查看日志以獲取詳細信息  
Remote server [%s:%s] request error：%s. Please check the logs for details  
0002:  
端口[%s]已被使用  
端口[%s]已被使用  
Port [%s] is used  
0003:  
服务器正在启动中或相关服务尚未就绪，请稍后重试  
服务器正在啟動中或相關服務尚未就締，請稍後重試  
The server is starting or related services are not ready, please try again later  
0004:  
不支持  
不支持  
Not supported  
0005:  
类 %s 未找到  
類 %s 未找到  
Class %s not found  
0006:  
没有这样的方法，类型：%s，操作：%s  
沒有這樣的方法，類型：%s，操作：%s  
No such method, type：%s, operation：%s
```
3. 执行如下命令，查找指定错误码说明。
以“008”为例说明。
```txt
./admin.sh error-code 008
```
回显信息，如下所示。
```txt
[root@centos bin]# ./admin.sh error-code 0008  
********** TongWebErrorCode Info ****  
0008:  
    公钥参数错误  
    公鑰參數錯誤  
    The public key parameter is incorrect
```

# 1.2.4.9. server
可通过 ./admin.[bat|sh] server [startd, start, stop, forcestop] 命令后台启动、启动、停止、强停 TongWeb 服务器实例。
若不指定实例名，则表示启动 TongWeb 默认实例。
以 Linux 环境 “启动 TongWeb 默认实例 domain1” 为例。
操作步骤，如下所示。
1. 进入 “${tongweb.home}/bin” 目录。
2. 执行如下命令，启动 TongWeb 默认实例 domain1。
以启动 “domain1” 实例为例说明。
```txt
./admin.sh server start domain1
```
若回显信息中出现 “Server startup in xx seconds” 字样，则说明启动 domain1 实例成功。

# 1.2.4.10. start-args
可通过 ./admin.sh start-args [domain_name] ，以单进程模式运行 TongWeb 服务器实例。
若不指定实例名，则表示启动 TongWeb 默认实例。
1. 进入 “${tongweb.home}/bin” 目录。
2. 执行如下命令，以单进程模式启动 TongWeb 实例。
以启动 “domain1” 实例为例说明。
```txt
./admin.sh start-args domain1
```

# 1.2.4.11. systemd
可通过 ./admin.sh systemd [install, uninstall] 可安装或者卸载 TongWeb 实例为自启动服务。
若不指定实例名，则表示安装默认实例 domain1 为自启动服务。

# 注意事项
仅 Linux 平台支持安装自启动服务。

# 操作步骤
以“安装指定实例domain2为自启动服务”为例说明。
1. 进入 “${tongweb.home}/bin” 目录。
2. 执行如下命令，安装指定实例 domain2 为自启动服务。
```shell
./admin.sh systemd install domain2
```
若回显信息出现 “The service has been installed” 字样，则说明安装自启动服务成功。

# 1.2.4.12. version
可通过 ./admin.[bat|sh] version 显示当前版本信息。
以 Linux 环境 “显示当前 TongWeb 版本信息” 为例。操作步骤如下所示。
1. 进入 “${tongweb.home}/bin” 目录。
2. 执行如下命令，显示当前 TongWeb 版本信息。
```txt
./admin.sh version
```
若回显信息出现 TongWeb 版本信息（产品版本、构建时间、命名空间、OS、JVM 等）和 License 信息，则说明显示当前 TongWeb 版本信息成功。
[root@centos bin]# ./admin.sh version   
Server Info: TongWeb/   
Server Version:   
Server Type:   
Server Built:   
Server Package: javax   
OS Name: Linux   
OS Version: 3.10.0-1160.119.1.el7.x86_64   
OS Architecture:amd64   
JVM Version: 1.8.0_341-b10   
JVM Vendor: Oracle Corporation License   
end_date  $= 20$    
consumer_name  $= 1$    
license_id  $= 119289$    
license_type  $= \mathrm{trial}$    
TW_Product_Name  $= \mathrm{TongWeb}$    
TW_Max Node  $= 5$    
TW_Edition  $= \text{山}$    
TW_Max_Number  $= -1$    
project_name  $= 1$    
create_date  $= 20$    
TW_Version_Number  $= \text{山}$    
[root@centos bin]#

# 1.2.5. 免脚本使用说明
对于没有执行权限的脚本，或者因为改脚本导致脚本不可用时，可使用免脚本方式进行启动、停止TongWeb 实例等操作。
免脚本方式支持但不限于对 TongWeb 进行启动、停止、强杀、加密、命令行、查看产品版本、显示忙碌线程、安装/卸载自启动服务等操作。
如下以 Linux 环境为例说明免脚本使用方式。

# 1.2.5.1. 启动 TongWeb 实例
支持在 TongWeb 服务器的任何目录下或非 TongWeb 目录内执行 “java -jar /xx/../tongweb-launcher.jarserver start”，而不需要预先设置任何环境变量等参数。
domain1 为默认值，可省略。
```batch
java -jar ${tongweb_home}/bin/tongweb-launcher.jar server start domain1
```

# 1.2.5.2. 后台启动 TongWeb 实例
```batch
java -jar ${tongweb_home}/bin/tongweb-launcher.jar server startd
```

# 1.2.5.3. 停止 TongWeb 实例
domain1 为默认值，可省略。
```shell
java -jar ${tongweb_home}/bin/tongweb-launcher.jar server stop domain1
```

# 1.2.5.4. 强杀 TongWeb 实例
domain1 为默认值，可省略。
```batch
java -jar ${tongweb_home}/bin/tongweb-launcher.jar server forcestop domain1
```

# 1.2.5.5. 执行命令行
```batch
java -jar ${tongweb_home}/bin/tongweb-launcher.jar commandstool
```

# 1.2.5.6. 加密工具
```batch
java -jar ${tongweb_home}/bin/tongweb-launcher.jar password user-password
```

# 1.2.5.7. 查看产品版本
```shell
java -jar ${tongweb_home}/bin/tongweb-launcher.jar version
```

# 1.2.5.8. 安装自启服务
Windows 不支持，仅 Linux 支持。
```shell
java -jar ${tongweb_home}/bin/tongweb-launcher.jar systemd install
```

# 1.2.5.9. 卸载自启服务
Windows 不支持，仅 Linux 支持。
```batch
java -jar ${tongweb_home}/bin/tongweb-launcher.jar systemd uninstall
```

# 1.2.6. 可信管理
可信管理是一种安全管理系统，其主要功能包括对指定的工作目录、服务程序或运行脚本进行授权访问和执行以及对操作系统或组件的配置文件进行防篡改保护。此外，它还能对违反安全策略的行为进行审计，以确保信息系统和数据的安全性和可信度。

# 1.2.6.1. 安装可信管理

# 1. 获取并解压可信模块安装包
a. 联系东方通相关支持人员获取可信模块安装包 “trusted.zip”。
b. 解压 “trusted.zip” 到 “${tongweb.home}” 目录下，并保留 “trusted” 目录。

# 2. 安装可信模块
a. 进入 “${tongweb.home}/trusted” 目录。
b. 运行 install 脚本，安装可信模块。
若已经启动 TongWeb，需先停止 TongWeb，接着执行 install 脚本，然后再启动 TongWeb。
安装完成后，若提示信息出现 “success” 字样，则说明安装可信模块成功。
关于如何卸载可信模块，详见卸载可信模块。

# 3. 修改 console.xml
a. 进入 “${tongweb.base}/conf” 目录。
b. 打开 “console.xml” 文件。
注意：
主配置文件 “console.xml” 具备防篡改限制，在运行期间禁止对其进行修改。若需要修改并使其生效，请确保 TongWeb 服务器处于停止状态，然后再进行修改。
c. 在 <console> 标签下添加 “enabledTrustedManager="true"”，如下所示。
```txt
<console enabledTrustedManager="true">
```
d. 配置完成后，启动 TongWeb，并登录管理控制台，在默认实例下即可查看到可信管理模块。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/4b0a1ee6a8a6ab05413aea7421e339713663e7b219ee253fa6685a4d4b90e983.jpg)


# 其它操作-卸载可信模块
1. 执行如下命令，停止可信模块。
```txt
/etc/init.d/tiptermd stop
```
2. 执行如下命令，查看可信模块。
```txt
rpm -qa | grep tip
```
回显信息，如下图所示。
```txt
[root@10-10-55-136 ~]# rpm -qa | grep tiptipterminal-1.0.5969-29512_beta.ky10.x86_64  
multipath-tools-0.7.7-17.ky10.x86_64  
[root@10-10-55-136 ~]#
```
3. 执行如下命令，卸载可信模块。
```batch
rpm -e tipterminal-xxxxxx
```
4. 执行如下命令，删除残留文件。
```txt
rm -rf /usr/local/HTTC /var/htdocsec
```

# 1.2.6.2. 可信授权
用户可下载 “export_file_name.req” 文件，提供给可信管理人员生成授权证书，并将授权证书导入到TongWeb 控制台界面，即可形成完整的授权管理。

# 1. 下载 “export_file_name.req” 文件
a. 登录 TongWeb 管理控制台。
b. 选择 “默认实例” $>$ “可信管理” > “可信授权” $>$ “更新”，进入可信授权的更新页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/bad219831f12858ad12e344749e6612dbadd9cc275a6d1362cad5bdc1c2ad0c6.jpg)
c. 单击 “下载”，弹出选择要下载的文件窗口。
d. 选择 “export_file_name.req” 文件，并单击 “确定”，下载以 “trustedauthority-xxxx.zip” 命名的压缩包。
e. 解压压缩包即可得到 “export_file_name.req” 文件。
将下载获取的 “export_file_name.req” 文件提供给可信管理人员制作授权文件即可。

# 2. 上传授权证书
当从可信管理人员处获取到已制作完成的授权证书后，即可导入到 TongWeb 控制台。授权文件格式要求为 “.resp” 文件。
a. 登录 TongWeb 管理控制台。
b. 选择 “默认实例” $>$ “可信管理” $>$ “可信授权” $>$ “更新”，进入可信授权的更新页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/01aca521e8fbf3a7f93ba6e261df793b9a3558f86fd34256e5c07cc875454403.jpg)
c. 选择 “上传文件” 或者 “服务器文件”，上传获取的授权证书 “.resp” 文件。
d. 单击 “更新”，跳转到 “安全模块授权” 页签，可查看更新的授权信息。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/b6549100cd170a161f9aeedca842a505c3a6c5f9b8e31ffca785a49562e7ca31.jpg)


# 1.2.6.3. 静态度量
配置静态度量目录后，系统将会对该目录进行静态度量校验。
度量文件类型为标准脚本、二进制执行程序、动态库、内核文件。
当系统检测到此类型文件遭到破坏时，将会阻止篡改；若被强行篡改，系统将会阻止其运行。

# 1.2.6.3.1. 新增静态度量目录
注意：新增的静态度量目录必须已经存在。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “静态度量”，进入静态度量页面。
3. 单击 “新增”，进入新增静态度量目录页面。
静态度量／新增 ☆
*目录
度量模式
CHECK
ONOCHECK
添加
返回
4. 输入需要进行静态度量的目录，并选择度量模式。
◦ CHECK：检测。
◦ NOCHECK：不检测。
5. 配置完成后，单击 “添加”，即完成静态度量目录的添加操作。
在静态度量列表中，可查看静态度量的目录、发起方、度量模式等。

# 1.2.6.3.2. 查看静态度量目录
用户可在静态度量列表中，查看已添加的静态度量目录、发起方（发起方|值）、静态度量模式等信息。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “静态度量”，进入静态度量页面。
3. 用户可查看添加的静态度量目录、发起方（类型|值）、静态度量模式等。

# 1.2.6.3.3. 删除静态度量目录
在执行删除静态度量目录之前，可信管理人员需要进行充分的评估和备份，并确保了解删除静态度量目录可能带来的潜在风险。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “静态度量”，进入静态度量页面。
3. 勾选一个或多个静态度量目录，单击“删除”，弹出确认删除提示窗口。
注：您也可以单击目标静态度量目录所在行的 “删除”，删除单个静态度量目录。
4. 单击 “确定”，即可完成控制台上静态度量目录的删除操作。
删除后，系统不再对该目录的文件进行度量检测。

# 1.2.6.4. 可信进程
添加为可信进程后，系统将该进程视为可信进程，不再对可信进程进行检测。

# 1.2.6.4.1. 添加可信进程
注意：若指定的是一个路径或者文件，则该路径或文件必须存在。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信进程”，进入可信进程页面。
3. 单击 “添加”，进入添加可信进程页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/0d25124eb0ba71eea678c3995f1e21609fa97cb007cf4ca863628cdf37a3b6b4.jpg)
4. 输入可信进程的绝对路径。
5. 单击 “添加”，即可完成可信进程的添加操作。

# 1.2.6.4.2. 查看可信进程
用户可在可信进程策略列表中，查看已添加的可信进程、发起方（发起方|值）、动作等信息。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” > “可信管理” $>$ “可信进程”，进入可信进程页面。
3. 用户可查看已添加的可信进程，包含可信进程、发起方（发起方|值）、动作（NOCHECK）。

# 1.2.6.4.3. 删除可信进程
在执行删除可信进程之前，可信管理人员需要进行充分的评估和备份，并确保了解删除可信进程可能带来的潜在风险。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信进程”，进入可信进程页面。
3. 勾选一个或多个可信进程，单击“删除”，弹出确认删除提示窗口。
注：您也可以单击目标进程所在行的 “删除”，删除单个可信进程。
4. 单击 “确定”，即可删除添加的可信进程。

# 1.2.6.5. 可信策略
用户可对指定目录、指定运行脚本、操作系统或配置文件等提供可信保护。

# 1.2.6.5.1. 创建可信策略
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信策略”，进入可信策略页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e1de47f136770db6bee8a66602ea5bab6989c5ad3fee74b26c456794302b6ded.jpg)
3. 单击 “创建”，进入创建可信策略页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c1e6a6c308ed9bc4ab38467677fa8261506eb4980199e7c6904a4a75eec5b6b4.jpg)


# 4. 配置策略名称及相关信息。
<table><tr><td>发起方</td><td>目标</td><td>动作</td><td>说明</td></tr><tr><td rowspan="2">进程</td><td>文件</td><td>创建、读、写、删除</td><td>对于操作系统和TongWeb组件的配置文件；指定的运行脚本，如jar、war、jsp文件等提供防篡改保护。
只允许指定进程对其进行访问（创建、读、写、删除）的操作，未指定的进程无法进行上述操作。</td></tr><tr><td>目录</td><td>创建、读、写、删除</td><td>对于指定的工作目录以及指定的服务程序，例如java，提供可信防护。
阻止未授权的进程访问（创建、读、写、删除）
被保护的目录或服务程序，允许指定的进程访问受可信保护的目录或服务程序。</td></tr><tr><td>无类型</td><td>进程</td><td>·禁止停止
·禁止启动</td><td>允许禁止停止、禁止启动指定的进程。</td></tr></table>

# 5. 配置完成后，单击 “添加”，完成策略的创建操作。

# 1.2.6.5.2. 查看可信策略
用户可根据需要查看已创建的可信策略。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信策略”，进入可信策略页面。
3. 用户可查看已创建的可信策略，包含策略名称、发起方（类型|值）、目标（类型|值）、动作等信息。

# 1.2.6.5.3. 删除可信策略
删除可信策略后，系统不再对其进行防护，且删除后不可恢复，请谨慎操作。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信策略”，进入可信策略页面。
3. 勾选一个或多个目标可信策略，并单击列表右上方的 “删除”，弹出确认删除窗口。
注：您也可以单击目标可信策略所在行的 “删除”，删除单个可信策略。
4. 单击 “确定”，即可完成可信策略的删除操作。

# 1.2.6.6. 可信行为模型
可信行为模型借助机器学习技术，自动对进程行为进行采集（可采集到 TongWeb 的三级进程），进而生成可信行为模型数据库。用户可将可信行为模型数据库应用为可信策略，提供可信防护。

# 1.2.6.6.1. 添加采集任务
用户可自行创建采集任务，并自定义选择采集周期。采集周期越长，可信行为数据模型越完善。
采集任务创建完成后，当 “采集状态” 更新为 “采集结束” 时，表示生成可信行为模型数据库成功。用户可将该模型数据库应用为可信策略，提供可信防护。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信行为模型”，进入可信行为模型页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/9d7ef753fc34f26d6ebf6cfe78482fc598df72ae5833d9662baee9c549dbcd60.jpg)
3. 单击 “添加采集”，进入添加采集页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7e6e3b854a0e90bb6a455834eef894f94135d4ad8b39101cf53a0658aef1cee9.jpg)
4. 在 “采集周期” 下拉列表中，选择采集周期。
支持选择 7 天、15 天、30 天、45 天、60 天、90 天。
5. 配置完成后，单击 “添加”，页面弹出 “可信行为模型添加成功” 提示信息，并返回可信行为模型列表页面。
用户可通过 “采集状态” 实时了解采集任务进展。采集任务添加完成后，采集状态默认为 “采集中”。

# 1.2.6.6.2. 查看可信行为模型
用户可查看可信行为模型的 id、创建时间、创建主体、采集周期以及采集状态。
采集状态包含：采集中、采集结束以及采集异常。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信行为模型”，进入可信行为模型页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/67fc6a41f2d8d21f43701b6fcb5143c309e800a9efc7e18b4720ab2e1c278343.jpg)
3. 用户可查看可信行为模型的 id、创建时间、创建主体、采集周期以及采集状态等。
用户也可以输入 id、创建时间、创建主体、采集状态或者选择采集周期，搜索指定可信行为模型。
4. 单击可信行为模型的 id 对应链接，可查看详情。
可信行为模型／查看
id
sTWGdLOlsgE43Gj4JgWhgBo0Y0CFQl0w
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/6e7fb789061d3bd8007af4df61a419c767ca11459c88dd0b59c7dbf9379f663d.jpg)
建时间
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/fb7c456ab10653576d8f14016cf92aa2a8e1e9a05f26dfe5c44e211f9fc0e043.jpg)
16:03:02
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/0b8f464ac44df3b49b1ace18a25a0d7b6667bcf0054518b64c14b4f44c5220c4.jpg)
建主体
TongWeb
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e50e9e5e8b3c7cc56e315218b5c349265adebfbb8c1c331c669b19f2ab52c1aa.jpg)
采集周期
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/14ddb70ca4a2a9999925c34024ba70ebebf2dd4e7c5dbb8ffee882bfe84c4df1.jpg)
采集状态
采集异常
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/feec2b457744facf742e7f05def27ce88f7596aebf0cf540564099da0f7708c1.jpg)
星否创建策略
 false
5. 单击目标可信行为模型所在行的创建主体对应的链接，进入可信行为详情页面，可查看单一任务采集详情。
注：若需要查看所有任务的采集详情，可直接在左侧菜单栏中，单击 “可信行为详情”，即可查看所有任务的采集详情，详见可信行为详情。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/855b6489a1f5301fc60a3021ca514d2746363641b308b06bea7a093d3c0c54df.jpg)


# 1.2.6.6.3. 应用为可信策略
用户可将生成的可信行为模型库或单个采集到的数据应用为可信策略，提供可信防护。此外，用户还可根据自身需求同时应用多个模型库。

# 前置条件
已 添加采集任务且采集任务已采集结束。

# 方式1：应用可信行为模型库为可信策略
在将可信行为模型库应用为可信策略后，该模型所采集的全部行为数据都将被纳入可信策略中。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信行为模型”，进入可信行为模型页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ceecb313312f7125f374a7d1b8abaf09084b65b88be2d315e8d337bd9410a8ae.jpg)
3. 单击目标可信行为模型所在行的 “应用”，弹出确认应用可信行为模型提示窗口。
注：用户也可以勾选一个或多个可信行为模型，并单击列表左上角的 “应用”，即可应用可信行为模型。
4. 单击 “确定”，即可完成可信行为模型的应用操作。
5. 用户可单击左侧菜单栏中的 “可信策略”，进入可信策略页面，查看应用的可信行为模型。
策略名称为采集任务的 id，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/24c319ba3b271158dc5992abf49646e7998b59f209ef1a118f6392cc6db5edfe.jpg)


# 方式2：应用单个数据为可信策略
用户也可根据需要只应用采集到的某一个数据为可信策略，详见应用单个数据为可信策略。

# 1.2.6.6.4. 停止应用行为模型库
当不需要将采集的行为数据模型库转换为可信策略以实施可信防护时，可停止应用采集模型。一旦停止，已转换为可信策略的行为数据模型库会从可信策略页面自动移除。

# 前置条件
已 添加采集任务且采集任务已采集结束。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” > “可信管理” $>$ “可信行为模型”，进入可信行为模型页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/986fafcaecf3cbd561c51db33fe53e6596113ec85bd3667ac45199caa3aa165e.jpg)
3. 单击目标可信行为模型所在行的 “停止应用”，弹出确认停止可信行为模型提示窗口。
注：用户也可以勾选一个或多个可信行为模型，并单击列表左上角的 “停止应用”，即可停止应用可信行为模型。
4. 单击 “确定”，即可停止应用可信行为模型。
5. 在左侧菜单栏中，单击 “可信策略”，可查看到转换为可信策略的行为数据模型库已被移除。

# 1.2.6.6.5. 停止采集任务
当尚未达到预设的采集周期，但当期已采集的行为数据模型库已达到您的需求，此时您可以手动停止采集任务。

# 前置条件
已 添加采集任务且采集任务尚未结束。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信行为模型”，进入可信行为模型页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a4c1cc86f18b696b0080d1dfdd8d04db5d70bfc45c517f436a8d11367d8f2cc6.jpg)
3. 单击目标可信行为模型所在行的 “停止采集”，弹出确认停止采集可信行为模型提示窗口。
注：用户也可以勾选一个或多个可信行为模型，并单击列表左上角的 “停止采集”，即可停止采集可信行为模型。
4. 单击 “确定”，即可停止采集可信行为模型。
若页面弹出 “可信行为模型停止采集成功” 提示信息，并且 “采集状态” 更新为 “采集异常”，则说明停止采集任务成功。

# 1.2.6.6.6. 删除可信行为模型
当可信行为模型不再有使用需求时，为便于后续管理，用户可选择将其删除，以此释放存储空间、节省系统资源。
若待删除的可信行为模型当前处于已应用状态，那么在执行删除操作时，系统将同步删除所有由该模型转换而生成的可信策略。

# 前置条件
已 添加采集任务且采集状态处于非 “采集中”。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信行为模型”，进入可信行为模型页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a32a5d1cd18551ae881526cb5f689f7663391e8d0b1dab6a9e2ea8ca21069c2d.jpg)
3. 单击目标可信行为模型所在行的 “删除”，弹出确认删除可信行为模型提示窗口。
注：用户也可以勾选一个或多个可信行为模型，并单击列表左上角的 “删除”，即可删除可信行为模型。
4. 单击 “确定”，即可完成可信行为模型的删除操作。
若页面弹出 “可信行为模型删除成功” 提示信息，且列表中该可信行为模型已移除，则说明删除可信行为模型成功。

# 1.2.6.7. 可信行为详情

# 1.2.6.7.1. 查看可信行为详情
用户可查看单一任务采集详情以及所有任务的采集详情。
• 查看单一任务采集详情
单击目标可信行为模型所在行的创建主体对应的链接，进入可信行为详情页面，可查看单一任务采集详情。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/0509626edb64637ee9ab6c30b50b8f7016c0d16907f2b1dc6f55503f3a7062e6.jpg)


# • 查看所有任务的采集详情
在左侧菜单栏中，单击 “可信行为详情”，即可查看所有任务的采集详情。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/453717f2ffc4b991c0eed3a5547fb3a20548b428abb406a3f1f6b03f08fa0829.jpg)


# 1.2.6.7.2. 应用单个数据为可信策略
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” > “可信管理” > “可信行为详情”，进入可信行为详情页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/fa2d38cd69689bea70f46eb655e3e2fbc67a2837032567645925f2e0001d05b5.jpg)
3. 单击目标数据所在行的 “应用”，弹出确认应用该可信行为详情窗口。
注：用户也可勾选一个或多个数据，并单击列表左上角的 “应用”，应用一个或多个数据为可信策略。
4. 单击 “确定”，即可应用单一数据为可信策略。
若页面弹出 “可信行为详情应用成功” 提示信息，则说明应用为可信策略成功。
5. 进入 “可信策略” 页面，可查看到应用为可信策略的可信行为模型数据。

# 1.2.6.7.3. 删除可信行为详情
删除后不可恢复，请谨慎操作。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “可信行为详情”，进入可信行为详情页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/0334ee4ab1173a0dc5a92187990c63f113239b8257dc98011a3eddf7b0492b68.jpg)
3. 单击目标数据所在行的 “删除”，弹出确认删除该可信行为详情窗口。
注：用户也可勾选一个或多个数据，并单击列表左上角的 “删除”，删除一个或多个数据。
4. 单击 “确定”，即可完成可信行为详情数据删除。
若页面弹出 “可信行为详情删除成功” 提示信息，并且该数据从可信行为详情页面移除，则说明删除该可信行为详情成功。

# 1.2.6.8. 模式切换
用户可切换可信工作状态。

# 工作状态
• “WORK”：所有可信防护生效。
• “DEBUG”：所有可信防护关闭，但是保留审计功能。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” > “可信管理” $>$ “模式切换”，进入模式切换页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d3c3ec0800a917cf50884c3049844908438b321750ef1316ba6aaea249058de0.jpg)
3. 用户可根据需要切换模式，默认为 “WORK” 模式。
4. 切换后，单击 “更新”，即可完成可信防护模式的切换操作。

# 1.2.6.9. 审计列表
TongWeb 可信管理可对违反安全策略的行为进行审计，并进行采集和展示。

# 1.2.6.9.1. 查看审计列表
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “审计列表”，进入审计列表页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/86d12f9c5d990e4412ca5a97b156d77aa5600eca43c417554ad26605aa2ee4d0.jpg)
3. 用户可查看审计的终端名称、终端 IP、类型等，详细说明如下表所示。
<table><tr><td>参数</td><td>参数说明</td></tr><tr><td>终端名称</td><td>终端的名称。</td></tr><tr><td>终端IP</td><td>终端的IP地址。</td></tr><tr><td>类型</td><td>类型。包含“签名”、“静态度量”、“动态度量”、“自主访问控制”、“异常程序上报”、“自保护”、“软件包”、“白名单”、“引导审计”以及“完整性”。</td></tr><tr><td>主体类型</td><td>主体表示程序运行的主进程。主体类型即为进程。</td></tr><tr><td>主体值</td><td>程序运行的主进程的值。</td></tr><tr><td>客体类型</td><td>用户操作的进程、二进制执行文件、库文件、文件、文件夹等访问类型。</td></tr><tr><td>客体值</td><td>操作的进程、二进制执行文件、库文件、文件、文件夹等访问对象。</td></tr><tr><td>操作类型</td><td>操作的类型,包含“登录”、“读”、“写”、“执行”、“下载”、“上传”、“卸载软件”、“安装软件”、“增加白名单”、“删除白名单”、“创建”、“添加”、“删除”、“引导”以及“其它”等。</td></tr><tr><td>审计结果</td><td>审计结果,包含“成功”和“失败”。</td></tr><tr><td>时间</td><td>操作的时间。</td></tr></table>

# 1.2.6.9.2. 搜索审计日志
用户可根据需要通过输入终端名称、终端 IP、类型、主体类型、主体值、客体类型、客体值、操作类型、审计结果或者时间的方式查询指定审计日志。
1. 登录 TongWeb 管理控制台。
2. 选择 “默认实例” $>$ “可信管理” $>$ “审计列表”，进入审计列表页面。
3. 在搜索区域，输入终端名称、终端 IP、类型、主体类型、主体值、客体类型、客体值、操作类型、审计结果或者时间等。
4. 单击 “搜索”，即可搜索到指定审计日志。

# 2. 应用管理
企业级应用以服务器为中心，用户通过网络使用应用所提供的服务。一般来说，企业级应用应当具有的特征包括：并发支持、事务支持、交互支持、集群支持、Web支持、安全支持等。这些特征需要基础运行环境的支撑， TongWeb 作为一款符合Java EE标准体系的应用服务器，可以很好地为企业级应用提供运行环境，从而最大化的降低应用的开发难度。
应用管理是 TongWeb 管理控制台上提供的最重要的功能模块。
<table><tr><td>支持类型</td><td>说明</td></tr><tr><td>Java EE应用文件</td><td>·Web应用文件 (.war)
·EJB 应用文件 (.jar)
·Connector应用文件 (.rar)
·EAR应用文件 (.ear)
·其他应用文件 (.car)</td></tr><tr><td>部署应用</td><td>·控制台部署
·自动部署
·热部署
·命令行部署</td></tr><tr><td>应用管理</td><td>·查看应用
·编辑应用
·访问应用
·备份应用
·监视应用
·启动应用
·停止应用
·卸载应用</td></tr></table>

# 2.1. 应用类型
TongWeb 支持五种Java EE应用文件的类型，包括Web应用、EJB应用、Connector应用、EAR应用、其他。
<table><tr><td>类型</td><td>扩展名</td><td>用途和构成</td></tr><tr><td>Web应用</td><td>.war</td><td>包含Servlet和JSP等Web组件，EJB组件以及静态HTML页面、Jar文件、标记库等。</td></tr><tr><td>EJB应用</td><td>.jar</td><td>包含EJB实现以及EJB实现所需的类。</td></tr><tr><td>Connect应用</td><td>.rar</td><td>包含连接器（资源适配器）的实现类。</td></tr><tr><td>EAR应用</td><td>EAR</td><td>包含上述三种应用类型。</td></tr><tr><td>其它应用</td><td>.car</td><td>非标准格式的其他应用，选择此类应用文件后，只能通过后台获取其应用类型。</td></tr></table>

# 2.1.1. Web 应用
Web 应用指的是可以通过浏览器访问的应用。
Web 应用（WAR 应用）的扩展名为 “.war”，由动态资源（如 JSP、Servlet、JSP Tag 库等）和静态资源文件（如 HTML 页面和图片文件等）组成。
Web 应用的具体结构，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d0c8468e6b3db7415ef55a62fd3e2975d99e86cd4b1f0e424ae1fa0ff360a800.jpg)
WEB-INF 用来存储服务端配置文件信息和在服务端运行的类文件。WEB-INF 存储的文件不允许客户端直接访问。
WEB-INF 存储的各文件介绍，如下所示。
• classes：该目录下存放的是 Web 应用所需的类和资源，例如：Servlet、EJB、工具类以及 JavaBeans组件等。
• lib：该目录存放的是 Web 应用所需的类包。
• web.xml：Java EE 标准的部署描述文件。
在 Java EE8 规范中，由于应用的配置可以通过原注释的方式写到类中，因此，可以允许没有 web.xml 文件。
下图所示的 “test.war” 是一个符合 Java EE8 规范的典型 Web 应用，其结构满足 Web 应用由动态资源（
如 JSP、Servlet、JSP Tag 库等）和静态资源文件（如 HTML 页面和图片文件等）组成。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/90b5f3ce1fc819833669a07fe2fde61305f56f1c8aef5cbafb0e1fa1570ad48f.jpg)
在 “test.war” 中，classes 既可以是传统的小服务程序（Servlet），也可以是 EJB 应用。
Servlet（Server Applet）是 Java Servlet 的简称，称为小服务程序或服务连接器，是用 Java 编写的服务器端程序，具有独立于平台和协议的特性。主要功能在于生成动态 Web 内容和数据，实现交互式地浏览效果。
传统部署描述文件 web.xml 已经省略掉，应用的配置需要通过 Java EE 7 的注释定义在 servlet 类中。

# 2.1.2. EJB 应用
EJB (Enterprise Java Beans) 是基于分布式事务处理的企业级应用的组件。
EJB 是用于开发和部署多层结构、分布式、面向对象的 Java 应用系统的跨平台的构件体系结构。
EJB 应用可以部署在符合 Java EE 标准规范的应用服务器上。应用服务器及 EJB 容器提供了对象事务处理、日志记录、负载均衡、持久性机制、异常处理等系统级的服务。
因此，开发者只需重点关注应用的业务逻辑，从而可以大幅简化大型企业级应用的开发工作。
一个 EJB 应用应包含 EJB 实现以及 EJB 实现所需的类。
EJB 应用的具体结构，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/2907fa6e0bf1a74529e8e49f6e54f930e6b83cdaecf3727ee62a8d33c43fdd7b.jpg)
META-INF 文件夹相当于一个信息包，在 META-INF 中包含的目录和目录中的文件获得了 Java 平台的认可与解释，可以用来配置应用、扩展程序、类加载器和服务。
该文件夹和其中的 MANIFEST.MF 文件，是在 JAR 打包时自动生成的。
META-INF 可以包含如下配置文件。
• ejb-jar.xml：Java EE 标准部署描述文件。具体元素属性说明，请参见 ejb-jar.xml。
• tongweb-ejb-jar.xml：TongWeb 自定义部署描述文件，请参见 tongweb-ejb-jar.xml。
• persistence.xml：Entity 使用 JPA 时，所需的持久化配置文件。具体元素属性说明，请参见persistence.xml。
EJB 的 JAR 文件的配置定义，完全可以通过原注释的方式定义在EJB的类中。
如下图所示的 “test.jar” 是一个符合 EJB3.2 以上规范的 EJB 应用的 JAR 包，其 ejb-jar.xml 已经不再是必选的部分。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7731682a9120b863dc21cd6e6529b13cef7adc5865d8ff598b37f8cf2f3260d0.jpg)


# 2.1.3. Connector 应用
Connector 应用（连接器应用）是一种资源适配器。
在扩展名为 “.rar” 的文件里，包含了资源适配器的实现类，它允许 Java EE 应用组件访问企业信息信息系统
的底层资源管理器，并与之交互。
Connector 应用主要由符合 JCA 规范的 Connector 应用类（JAR 包形式）和符合 Java EE 标准的部署描述文件 “ra.xml” 组成。
具体结构，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/48fd452ad0a29655d1f26029dad6b28691d59b6974876f9956993e622de0c9ba.jpg)


# 2.1.4. EAR 应用
EAR 应用是企业级应用的项目集合，它将应用所包括的子项目的多个 jar 文件和 war 文件打包在一个 ear文件中，以便在应用服务器中整体部署。
EAR 应用可包含 Web 应用（.war）、EJB 应用（.jar）和公用包。
一个 EAR 应用可以包含一个或多个 Java EE 应用或者组件。
EAR 应用的具体结构，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f86bdbf3901a14c3b8f65702337735794fcdd157f91963329c1b2d8fedf2164c.jpg)
其中，application.xml 是 Java EE 标准的部署描述文件，APP-INF 是 EAR 应用的公共类。
“test.ear” 是一个典型的 EAR 应用，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/dea08bf5d135a4044deb9d929b4d2fddc06c6c0c9c93434f927dceaa2cde459a.jpg)


# 2.1.5. 其他应用
TongWeb 还支持 “.car” 扩展名的应用文件（指标准格式 jar、war、ear、rar 之外的扩展名），CAR 是Component Archive 的缩写。
J2EE 的 WEB 应用组件有一个严重的问题，问题来源于 J2EE 平台的 class loading 的模式。
每个 WEB 应用组件都独占一个 classloader，这两个 classloader 所装载的类是无法共享的。即同一个类在两个 WEB 应用中可能有两个副本，各不相干，这将导致下列问题。
• 导致了大量内存的浪费
当 EAR 中包含许多个 WAR 文件时，内存浪费尤其明显。
• 导致 ClassCastException 异常
由于不同 classloader 所装载的类的实例不能互换，而不同的 WAR 文件却是共享同一个 EAR classloader，在某些情况下（例如 cache），一个 WAR 下的对象可能会跑到另一个 WAR 的程序中，从而导致错误。
• 导致类的初始化问题
当有一个被两个 WAR 所共享的类（位于 EAR class loader）需要初始化时，需要先执行的 WAR 会抢先初始化该类，并用当前WAR的参数来初始化它。当第二个 WAR 被启动时，这个类的初始化状态有可能会发生错误。
例如，在同一个 EAR 中同时运行两个使用 Jakarta Turbine 框架的 WEB 应用，就会发生这样的问题。
org.apache.turbine.Turbine 类会被第一个 WEB 应用初始化，而第二个 WEB 应用将失败。
Webx Framework 通过引进了一种新的组件：Webx Component（文件名后缀为car），很好地解决了这个问题。
实际 CAR 文件的内部结构和 WAR 差不多，只是少了如下文件或目录：
• WEB-INF/web.xml：描述文件。
• WEB-INF/lib：目录。
与 WAR 组件一样，CAR 可以单独开发和调试，但在布署阶段，多个 CAR 被合并成一个 WAR 文件，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f7bd76295ffffc337a8e5b73d6848de71391472355b9eb57c3bc9802ca056d6d.jpg)


# 2.2. 部署源类型

# 2.2.1. 文件部署
文件部署即应用以应用包（如*.war，*.ear 等）的形式进行部署，该形式的部署支持所有类型的应用。
应用部署后，默认在 “${tongweb.base}/deployment” 目录。

# 说明：
当选择以指定应用程序包在服务器上位置的方式部署应用时，系统不会解压到
“${tongweb.base}/deployment” 目录，而是直接原地解压部署。

# 2.2.2. 目录部署
目录部署即应用以展开的目录形式进行部署，目录部署支持 Web 应用、EJB应用、Connector 和 EAR 应用等各种类型的应用。
目录部署的优点是方便应用的修改，当应用包含了需要频繁修改的文件时，使用目录部署会相对方便。

# 2.3. 类加载策略

# 类加载层级
TongWeb 类加载层级，从高到低：jvm boot $>$ jvm system $>$ TongWeb lib $>$ ejb $>$ TongWeb app > apploader
• 类库被附加到最底层（即 app loader 层级），与应用处于同一个层级；
• TongWeb app 位于所有应用上层，供所有应用共享；
• 再往上是 TongWeb 运行所必需的类，例如数据源的驱动。 lib/system 目录下的库是附加到 jvm system层级，位于整个 TongWeb 的上层。

# 类加载-放置 jar 文件
• 方式1：用户可将需要的 jar 文件放入 “${tongweb.home}/lib/system” 或“${tongweb.base}/lib/system” 目录下，以使其能被系统自动加载。
注：
◦ ${tongweb.home} 表示 TongWeb 安装路径。
◦ ${tongweb.base} 表示 TongWeb 实例运行路径，例如，默认实例运行路径为“${tongweb.home}/domains/domain1”。
适用于以下场景：
◦ 当应用程序需要某些 jar 包，但这些 jar 包并未打包在应用程序内部。
◦ 在使用 -javaaagent 参数时，所需的类库只能放在上述位置才能被加载到。
◦ 这种方式相当于在启动 java 应用时，通过 “java -classpath xxx.jar” 命令来指定额外的类路径参数。
• 方式2：通过设置 TW_CLASSPATH 环境变量的方式，扩展系统类加载路径。
在 Linux 环境中配置 MySQL JDBC 驱动环境变量，如下所示。
```txt
export TW_CLASSPATH=/home/tongweblib/redis/*.home/tongweblib/mysql-connector-java-8.0.11.jar
export PATH=$TW_CLASSPATH/bin:$PATH
```

# 类加载机制
在 TongWeb 部署应用时，可以选择是优先加载 TongWeb 自带类，或者优先加载应用自带类，优先加载TongWeb 自带类称为父优先，优先加载应用自带的类称为子优先。
• 实例目录 “${tongweb.base}/lib” 下的类仅对该实例有效。
• TongWeb 目录 “${tongweb.home}/lib” 下的类对所有实例有效。

# 类加载模式
加载模式分为父优先和子优先，若指定了类库，则会按照类库中的 jar 包的顺序加载。子优先包含强制从应用加载的类、强制从 TongWeb 加载的类、加载应用实现、Web 兼容模式。
• 强制从应用加载的类
会优先从部署的应用或者应用提供的 jar 包中加载该类，主要解决开启子优先的情况下，不会加载应用自带的某些特别的类。
• 强制从 TongWeb 加载的类
解决开启子优先的情况下，指定某些类必须使用 TongWeb 自带的类或“${tongweb.home}/lib”下的类。优先级高于“强制从应用加载的类”。
• 加载应用实现
解决某个规范或者功能，TongWeb 和应用自带均有实现的情况，此时会使用应用自带的实现。
说明：
若指定从应用中加载实现 “WebService”，需要先在 “基础配置” $>$ “全局配置” > “服务器” 中，打开 “启用 WebService” 开关，“加载应用实现” 选项中才会出现 “WebService”。
• Web 兼容模式
若您的应用是基于 Tomcat 或者其它 Servlet 容器开发的应用，则可以开启“Web 兼容模式”，以获得更好的兼容性。
开启 “Web 兼容模式” 后，TongWeb 将关闭 EJB、JCA 等服务，并尝试从应用自身加载JSF、JavaMail、WebService、XML 等技术实现。

# 类加载推荐策略
应用部署时，推荐使用 “默认” 配置。若部署应用出现类加载不对的问题时，请根据日志进行排查。
Web 应用建议打开 “Web 兼容模式”，ejb-jar、ear 应用不能开启 “Web 兼容模式”，可配置 “加载应用实现”。

# 2.4. 部署应用
TongWeb 上应用部署方式可分为 “单节点部署” 和 “集群管理部署” 两种。
• 单节点部署
适用于不需要集群的单机环境或在单机应用测试阶段使用。
• 集群管理部署
适用于集群环境，把应用批量部署到各个 TongWeb 节点上。
本章节介绍如何进行单节点部署，关于集群管理部署的详细信息，请参见集群管理。

# 2.4.1. 控制台部署
您可以通过如下两种方式部署应用：
• 通过控制台上传
在控制台选择并上传应用包，如 *.war ， *.ear 等格式的文件。
• 指定服务器位置
如果您已将应用程序包放置在服务器的某个位置，您可以在控制台指定该位置，以便服务器能够找到并
部署该应用程序包。
当指定位置后，系统部署应用时，将不会解压到 “${tongweb.base}/deployment” 目录，而是直接原地解压部署。

# 2.4.1.1. 注意事项
• 支持部署基于 Tomcat、Jetty、Undertow 嵌入式版本开发的 SpringBoot 应用 jar 包。
◦ 部署应用时，在应用的 “基本属性” 页面，开启 “SpringBoot 兼容”。
◦ SpringBoot 兼容是将 SpringBoot 的 jar 包转换成 war 包进行部署。
◦ 支持 SpringBoot 2.x 和 SpringBoot 3.x。
• 支持同时部署 “javax” 和 “Jakarta” 命名空间的应用。
部署应用时，在应用的 “其它” 页签，开启 “命名空间兼容” 即可。

# 注意：
◦ “命名空间兼容” 开关只用作 POC 测试。
◦ 若您打算单独部署 Jakarta 命名空间的应用，需要生成 Jakarta TongWeb 版本来部署 Jakarta 命名空间的应用。
详细信息，请参见版本生成。

# 2.4.1.2. 前置条件
• 已获取系统管理员账号和密码。
• 已准备好应用程序包。

# 2.4.1.3. 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。

# 说明：
◦ 您可以根据需要将应用部署在目标实例。
◦ 若部署在默认实例，则直接在控制台左上角单击“默认实例”，即可进入默认实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 单击 “部署”，进入部署应用页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e210ea1fd9370ec6b39487a79f00ce56bd4919504a61f9fa9ae7f921131f1cc5.jpg)
5. 设置服务器上应用程序的部署路径、选择 “虚拟主机” 以及设置 “启动优先级”。
◦ 部署路径：必填项，当 “应用来源” 选择 “服务器文件” 时，需要部署路径。
▪ 当选择 “应用来源” 选择 “服务器文件” 时，出于安全考虑，限定了读取文件的大小。用户可进入 “基础配置” $>$ “全局配置” $>$ “应用”，修改服务器文件大小限制。
▪ 用户也可以将 “应用来源” 切换为 “上传文件”，用户可通过上传文件的方式上传应用包。
默认情况下，控制台关闭了上传文件功能。若需要开启，用户可进入 “集中管理” > “安全配置” >“控制台安全”，关闭禁用文件上传，详见禁用文件上传。
◦ 虚拟主机： 必填项，应用所部署到的虚拟主机。
◦ 启动优先级： 必填项，用以约束应用启动的顺序，该值越小越优先启动。
其它关键参数特别说明，如下所示。
◦ 访问前缀：非必填，指定访问此应用的 Web 资源的根路径；若未设置，则使用应用文件的名称。
▪ 该功能仅支持 Web 类型（如 *.war）的应用。
▪ 当不同的应用均部署在同一台虚拟主机上时，系统不允许为它们配置相同的访问前缀；反之，当这些应用分别部署在不同的虚拟机上时，系统则支持为它们配置相同的访问前缀。
◦ 本地持久化：非必填，在 “会话与 Cookie” 页签下，若开启 “本地持久化”，应用在停止时会将当前内存中的会话持久化存储到本地（如 $\$ 1$ {tongweb.base}/data/app/session 目录）并在启动后重新载入内存。
◦ 会话服务器：非必填，在 “会话与 Cookie” 页签下，选择会话服务器后，将应用的 Session 存储到会话服务器，会话相关日志输出到独立的 “${tongweb.base}/logs/sessionha” 日志目录。
◦ 应用回收：非必填，在 “安全” 页签下，“应用回收” 默认开启，应用卸载后自动回收到应用回收中，用户可在应用回收列表中查看。关于应用回收的信息，详见应用回收。
◦ 加载 Class-path 资源：在 “资源加载” 页签下，开启 “Class-Path 资源” 后，系统将会根据应用根目录下的 “META-INF/MANIFEST.MF” 文件（Class-Path 参数）来加载更多的 jar 等文件到应用中。多个 jar 文件使用空格分隔。
配置示例，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/592b7a4fb3df994caaf5651ac4f9cd26a4d08c65218c65453f2db52c28b6b113.jpg)
◦ 附加响应头：在 “其它” 页签下，附加响应头允许使用 () 字符。
关于部署应用的更多参数说明，详见应用参数配置说明。
6. 配置完成后，单击 “添加”，完成应用部署操作。
若页面弹出 “应用添加成功” 提示信息，则说明应用部署成功。
在应用列表中，可查看已部署的应用，包含应用名、自动部署、部署路径、访问前缀、虚拟主机、应用版本、应用类型、应用状态等。
◦ 应用版本：可在部署页面的 “其它” 页签中进行配置。
◦ 应用状态，如下所示：
▪ “STARTED”：运行中
▪ “STOPPED”：停止
▪ “FAILED”：失败

# 注意：
若应用 “web.xml” 中已为应用设置 “<default-context-path>test</default-context-path>” 访问前缀，则应用的访问前缀为 “web.xml” 配置的访问前缀。

# 2.4.1.4. 手动修改 tongweb.xml
若需要手动对 tongweb.xml 文件进行修改，切不可随意修改 appId （应用名）参数的值。若因为业务调整或其它必要原因确实有需要修改此参数时，必须严格确保修改后的 appId 具备唯一性。

# 2.4.2. 自动部署
自动部署默认处于 “关闭” 状态。如果需要自动部署应用，请先开启自动部署开关。当开启自动部署后，您只需要将待部署的应用程序包（.war、.jar、.rar、.ear、.car 等）或者应用程序目录，放置在自动部署目录（默认路径为 “${tongweb.base}/autodeploy”）。
用户可以根据需要选择如下任一种方式，开启自动部署开关。
• 方式1：开启 “自动部署应用” 开关
进入 “基础配置” $>$ “全局配置” $>$ “应用” 下，开启 “自动部署应用”。
在开启 “自动部署应用” 后，系统默认打开 “自动更新” 开关，TongWeb 服务器将自动且持续监控该目录中的任何变动。一旦检测到新的应用程序包或应用程序目录被添加，它便会立即启动自动部署流程，无需手动干预。部署完成后，TongWeb 会在该目录下生成一个名为 “[应用名称].deployed” 的文件作为已部署标识。
• 方式2：开启 “启动时部署” 开关
进入 “基础配置” $>$ “全局配置” $>$ “应用” 下，开启 “启动时部署”。
在 TongWeb 启动完成后，扫描自动部署目录，仅执行一次应用自动部署。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e35f9dbffa6cb4dc541039b679432b1e09a63e9dc9d174090d71be44e4ebd405.jpg)


# 注意事项
• 支持 “应用程序包” 和 “目录” 两种自动部署方式。
• 并行部署对自动部署的多个应用生效。
用户可以进入 “基础配置” $>$ “全局配置” $>$ “服务器” 页签，设置 “任务并行度”，从而确保任务执行的最大并发数。
• 自动部署的应用，在 TongWeb 停机更新后，重启可自动解压新的应用包。
为了方便用户管理和监控已部署的应用，用户也可在 TongWeb 控制台界面的应用列表中，查看并管理自动部署的应用。

# 2.4.2.1. 开启自动部署
默认自动部署目录为 “${tongweb.base}/autodeploy”，您也可以根据需要自定义自动部署目录。
如下以开启 “自动部署应用” 开关为例进行说明。

# 注意事项
• 设置的自定义自动部署目录要求已存在，才能设置成功。
• 支持设置多个自动部署目录，可删除或增加新的目录。
• 自动部署目录内可识别文件和文件夹类型的应用，并在新增和更新后自动部署。
• 在删除自动部署目录后自动解部署应用，并同步操作 tongweb.xml 文件里的记录。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “基础配置” $>$ “全局配置” $>$ “应用”，进入应用页面。
4. 开启 “自动部署应用” 开关，开启自动部署。默认为 “不开启”。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7c9494f63c419ce8cf3b7d4238fabcff966f094df038291fce38ac487d4e6b00.jpg)


# 注意：
◦ 自动更新： 若关闭 “自动更新” 开关，则系统在检测到自动部署目录中的变动后，不会自动执行应用的重新部署操作。
◦ 生成状态标签：开启该功能后，自动部署的应用将会生成对应的标签文件，成功：.deployed，失败：.failed，卸载 *.unDeployed。
◦ 部署到 deployment：开启该功能后，自动部署的非文件夹类型应用将解压部署到${tongweb.base}/deployment 目录，关闭该功能将在原地解压部署。
◦ 自动部署目录：指定自动部署的目录，默认为 “${tongweb.base}/autodeploy”。
5. 其他参数，请根据需要选择配置。
6. 单击 “更新”，完成开启自动部署开启操作。
若页面弹出 “全局配置更新成功” 提示信息，则说明全局配置开启自动部署成功。

# 2.4.2.2. 自动部署应用
以如下信息为例进行说明。
• 默认自动部署目录：${tongweb.base}/autodeploy
• 应用程序包： $\$ 1$ {tongweb.home}\version*\examples\examples.war

# 注意事项

# • 部署场景
◦ 若部署成功，则生成 “[文件名称].deployed” 标识文件。
◦ 若部署失败，则生成 “[文件名称].failed” 文件，更新应用需要先卸载后再部署。

# • 卸载场景
◦ 删除应用（文件夹、*.war、*.jar、*.ear、或其对应的 “[文件名称].deployed” 文件），系统自动卸载应用，且生成 “[文件名称].unDeployed” 标识文件。
注：相关解压目录一并删除。
◦ 支持在页面上直接卸载自动部署应用。
◦ 卸载应用后，在 “应用回收” 页面，可查看卸载的应用。
◦ 在 “应用回收” 页面恢复卸载的应用后，恢复部署到 “${tongweb.base}/deployment” 目录，且不再是自动部署应用。

# • 自动部署的应用
◦ 自动部署的应用，支持在页面上进行更新其部署参数。
◦ 停止 TongWeb，将原本自动部署目录下的应用文件删除，再次启动 TongWeb 后，系统自动清理残留文件。
◦ 已经自动部署过的应用（即生成过 “[文件名称].deployed”），重启后不再触发自动部署。

# • 更改自动部署目录
原来的自动部署目录更新为非自动部署目录后，已被自动部署的应用不受影响。

# 操作步骤
1. 将应用程序包拷贝到自动部署目录 “${tongweb.base}/autodeploy”。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7be574d0b65539da3bf232f961ff80063bf51245424efc995543cd80801f8e7d.jpg)
2. 在应用列表中，查看已部署的应用。
应用状态为 “STARTED” 表示应用部署成功。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/76cfce513096594fb6865c39ae4f29e060d91ea31c0ba2dfb1e5bbad7b8beb74.jpg)
3. 在 “${tongweb.base}/autodeploy” 目录下，可查看到部署成功标识。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/b3b0199ebe06636b4aedf36902ed8e3fdfdcc397e3ba3ba3fdb372a3454a4623.jpg)


# 2.4.2.3. 预设自动部署配置信息
您可以通过配置自定义描述文件 “tongweb-web.xml” 的方式，预设自动部署的相关参数配置。

# 2.4.2.3.1. 配置生效优先级
web.xml $>$ tongweb-web.xml $>$ 用户输入（控制台、命令行、REST 等方式） > 默认参数
• 用户可以在应用内部放置一个 tongweb-web.xml 事先定下来所有的业务参数，以方便部署时无需再输入。
• 在部署完成后，再次通过控制台或其它接口编辑应用配置时，它的优先级也不变。
• 若这个属性在 tongweb-web.xml 中已经定义，其值是只读的，编辑不生效。
• 若需要编辑这个属性，需要删除 tongweb-web.xml 中定义的这个属性。

# 2.4.2.3.2. 准备 “tongweb-web.xml” 配置文件

# 方式1：下载 tongweb-web.xml 配置文件
若应用已备份或卸载，您可以在 “备份应用” 或者 “回收应用” 中，下载 “tongweb-web.xml” 配置文件。
注：控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。
如下操作以下载 “备份应用” 的配置文件为例说明。
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用备份”，进入应用备份列表页面。
4. 单击目标备份应用所在行的“下载”，选择 “*.tongweb-web.xml” 文件。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d74245bcaf6720e86f909500bec3cd75290a547e4795e7f71014ac4d7b794ced.jpg)
5. 单击 “确定”，即可下载 tongweb-web.xml 文件。

# 方式2：新建 tongweb-web.xml 配置文件
1. 新建一个 “tongweb-web.xml” 文件。
2. 在控制台部署应用，并且完成相关配置项的配置。
您可以选择使用如下任一种方式获取配置信息。

# ◦ 复制 “备份应用” 或者 “回收应用” 的配置信息
如下操作以复制 “备份应用” 的配置信息为例说明。
a. 进入 TongWeb 管理控制台。
b. 切换到目标实例。
c. 在左侧导航栏中，选择 “应用管理” $>$ “应用备份”，进入应用备份列表页面。
d. 单击 “创建”，将目标应用进行备份。
e. 备份完成后，在应用备份列表中，单击目标应用所在上的 “配置信息”，进入备份详细信息页面。
f. 复制 “配置信息” 内容，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/5961a1b34b39bff50a523e1be47aa96949a0aa9b2d0c3320b415cebf7532e640.jpg)
◦ 复制 “tongweb.xml” 中 <app $\mathbf { \nabla } / { > }$ 字段信息
a. 进入 “${tongweb.base}/conf” 目录。
b. 打开 “tongweb.xml” 文件。
c. 复制文件中的 <app $/ >$ 字段信息，如下所示。
```txt
<app XSSFilterEnabled="true" addWebinfClassesResources="true" allowCasualMultipartParsing="true" allowLinking="true" antiClickJackingEnabled="true" antiClickJackingOption="SAMEORIGIN" appFrom="fromServer" appld="test5" blockContentTypeSniffingEnabled="true" cacheMaxSize="102400" cacheObjectMaxSize="1024" cachingAllowed="true" contextRoot="test5"CorsAllowedHeaders="Origin,Accept,X-Requested-With,Content-Type,Access-Control-Request-Method,Access-Control-Request-Headers"CorsAllowedMethods="GET,POST,HEAD,OPTIONS"CorsPreflightMaxAge="1800"CorsSupportCredentials="false" crossContext="true" csvCacheSize="20" csvEntryPoints="/index.jsp,/index1.jsp" csvPrevention="true" enableCORSAccess="true" enablePooling="true" enableStatelessPoolMonitor="true" fileEncoding="UTF-8" fileProtectionPattern "*.html,*.jsp" filename="autodeploy/TongWebProperties" host="localhost" hstsEnabled="true" httpHeaderToken="true" javaEncoding="UTF-8" jspDevelopment="true" jspPrecompile="true" jspPrecompileThreadCount="4"mappedFile="true" maxActiveSessions="100000" quoteAttributeEL="true" reloadable="true" requestCharacterEncoding="UTF-8" responseCharacterEncoding="UTF-8" restrictedPorts="server" riskProtection="true" semaphoreEnabled="false" startupPriority="99" strictQuoteEscaping="true" threadPoolPolicy="1" tokenValidTimes="1" type="war" unloadDelay="20" useHttpOnly="true" useLegacyCookieProcessor="false" useRelativeRedirects="true" webModuleOnly="false" xssProtectionEnabled="true" cacheTtl="5001" delegateFirst="true" slowThreadEnabled="true" threshold="62" interruptThreadThreshold="63"/>
```

# 注意：
▪ “appId”：参数的值不能任意修改。若因为业务调整或其它必要原因确实有需要修改此参数时，必须严格确保修改后的 appId 具备唯一性。
▪ 配置信息中的相关参数说明，请参见《TongWeb_V8.0命令行工具手册》中 “支持的model、action” 章节 $>$ “应用” $>$ “支持的参数” 中的参数配置说明。
d. 粘贴到 “tongweb-web.xml” 文件中，如下图所示。
```csv
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
```
e. 保存并退出。

# 2.4.2.3.3. 将 “tongweb-web.xml” 文件放置到应用包的 “WEB-INF/” 中
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ed9181b6ba9ce85c8233ff48e486400de6089a61111c9844e2054ea2df0f6e26.jpg)


# 2.4.2.3.4. 将应用重新打包，并自动部署应用
将应用重新打包，并放在 “${tongweb.base}/autodeploy/” 目录下，系统将根据配置文件自动部署应用。

# 2.4.2.4. 设置多应用启动优先级
通过预设自动部署配置信息的方式，为每个应用添加 “startupPriority” 设置启动优先级。
设置启动优先级后，在服务器启动时，TongWeb 服务器会根据设置的值按从小到大的顺序启动。取值范围为 “0-99”。

# 2.4.3. 热部署
热部署是应用部署之后，在线实时对应用进行修改，结果会立刻展现。
• 开启 “热加载”，即开启热部署，当用户修改 “${tong.base}/deployment” 中的应用的类文件或应用的配置文件 web.xml 后，应用会自动进行重新部署并将最新的内容提供给用户。
• 若未开启 “热加载”，用户修改文件后，需要重启 TongWeb 或者手工在管理控制台重新部署应用才会生效。

# 注意事项
生产环境不建议开启。

# 操作步骤
当部署应用时，开启 “热加载”，即可开启热部署。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理”> “应用”，进入应用列表页面。
4. 单击 “部署”，进入应用部署页面。
5. 单击 “资源加载”，进入资源加载页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/5783246168d7c25a8dfad538b5add0af29e92b9db1740c2ea4251293c62f5b39.jpg)
6. 开启 “热加载”，即开启热部署。
7. 其他参数请根据需要进行配置。
8. 配置完成后，单击 “添加”，完成应用的部署操作。

# 2.4.4. 命令行部署
TongWeb 支持命令行部署。命令行的启动脚本是以 commandstool 命名的脚本文件，有 bat（Windows）和 sh（Linux/Unix）两个版本。
启动脚本路径：
• Windows：${tongweb.home}/bin/windows
• Linux：${tongweb.home}/bin
关于 commandstool 的执行方式及基本参数，请参见《TongWeb_V8.0命令行工具手册》，此处提供部署应用命令的使用说明。
使用 commandstool 部署 Web 应用，如下所示。
```batch
${tongweb.home}/bin> sh commandstool.sh --model=app --action=add --username=thanos
--password=thanos123.com --acceptAgreement=true --port=9060 --host=localhost appFrom=fromUpload
fromUpload=D:\tongweb\version*.x\examples\examples.war
```
相关参数说明，如下表所示。
<table><tr><td>参数</td><td>参数说明</td></tr><tr><td>--model</td><td>TongWeb管理控制台菜单对应的功能模块名称。您可以通过执行“commandstool[batlsh] --help”查看功能模块名称以及功能模块介绍。</td></tr><tr><td>--action</td><td>功能模块包含的操作。您可以通过执行“commandstool.[bat|sh] -model=]*name --help”查看操作名称以及操作的详细介绍。</td></tr><tr><td>--username</td><td>TongWeb 服务器授权管理用户的用户名。</td></tr><tr><td>--password</td><td>TongWeb 服务器授权管理用户的密码。</td></tr><tr><td>--acceptAgreement</td><td>设置为“true”，表示阅读并同意许可协议。同意许可协议才允许登录 TongWeb 服务器。</td></tr><tr><td>--host</td><td>应用部署的虚拟主机。</td></tr><tr><td>--port</td><td>监听网络请求的端口。</td></tr><tr><td>appFrom</td><td>应用来源，部署的应用可以从客户端上传，也可以通过服务端指定的位置读取。可设置为“fromUpload”或者“fromServer”。</td></tr><tr><td>fromUpload</td><td>应用的位置。服务器上应用程序的位置，通常是应用的程序包，如“.war”、“.jar”、“.ear”、“.rar”。</td></tr></table>

# 2.5. (可选)HTTPS 双向认证
HTTPS 双向认证要求客户端与服务器在建立连接时互相验证对方身份，通过交换并验证数字证书确保通信双方均为合法实体。这一机制在单向认证（仅服务器验证客户端）基础上增加了客户端证书验证环节，形成双重安全防护。
如下以 TongWeb 自带的证书为例进行说明。

# 步骤1：在 TongWeb 开启双向认证
1. 在左侧菜单栏中，选择 “Web 容器” $>$ “通道”，并进入指定通道详情页面。
2. 单击 “安全” 页签，进入安全配置页面。
3. 打开 “开启 SSL” 开关，配置双向认证 SSL 证书。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a2d0e853963c2be0f5443f34dc63d3c8347430eb22e63adad49ba4bf139828b8.jpg)
配置说明，如下所示。
◦ 服务器证书：在下拉列表中，选择 “server” 证书。
◦ 客户端认证：选择 “true”。
◦ 信任证书：在下拉列表中，选择 “server” 或 “client” 证书均可。
4. 配置完成后，单击 “更新”，页面弹出 “通道更新成功” 提示信息，说明开启 HTTPS 双向认证成功。

# 步骤2：在浏览器上安装 TongWeb 自带的证书
在访问应用的浏览器中导入证书（${tongweb.base}/conf/client.p12），然后通过 步骤1 中配置的通道来访问应用，即可实现 HTTPS 双向认证的应用访问。
注：若浏览器未安装证书，通过此通道访问应用会被拒绝，页面显示空白。

# 2.6. 访问应用
应用部署完成后，您可以通过管理控制台访问应用。

# 访问链接
链接地址代表本机地址，展示满足如下条件：
• 不是回环地址，如 IPv4 中的 “127.0.0.1” 或 IPv6 中的 “::1”。
• 判断是不是内网 IP。
◦ 若不是内网 IP，则取 IPv6。
◦ 若是内网 IP，则再判断是不是无线网卡和有线物理网卡；若是，则添加；若是虚拟网卡，则不取。

# 说明：
◦ IPv4 的地址本地地址分为三段：10.0.0.0 ~ 10.255.255.255、172.16.0.0 ~172.31.255.255、192.168.0.0 ~ 192.168.255.255。
◦ IPv6 的地区本地地址的前 12 位是 FEC，其他的位可以是任意取值，如：“FED0::” 和 “FEF1::” 都是地区本地地址。

# 前置条件
• 已获取管理控制台系统管理员账号和密码。
• 已部署应用。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 在应用所在行的操作列，单击 “链接”，进入链接详情页面。

# 应用／链接
状态:
true
消息:
应用链接成功
http://192.168.22.85:8088/examples
http:/[fe80:0:0:0:22e9:935f:683c:7147]:8088/examples
http://[fe80:0:0:0:8567:f333:7605:3b83]:8088/examples
http://[fe80:0:0:0:9d62:d814:94c9:9620]:8088/examples
http://[fe80:0:0:0:f2fa:4729:8fd6:4285]:8088/examples
5. 单击生成的链接，即可访问部署的应用，如下图所示。
注：如果应用所采用的通道开启了 HTTPS 双向认证，其传输协议会显示为 https。在此情形下，用户若要成功访问该应用，需要在浏览器中导入与之对应的信任证书，否则访问会被拒绝，页面显示空白。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/4f2971184843d10a0391d79ad4ce149a5bea52eda64b1b580288bcf89afee7ef.jpg)
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d84b1c7cd637de12ef6bf11b9edb1dd9ebb40a5e529c31b330bed9e984adca30.jpg)


# A不安全

# 192.168.22.85:8088/examples/

# Examples
· Servlets examples
· JSP Examples
·WebSocket Examples
· Jdbc NoXaDataSource用例说明
· Jdbc CompDataSource 用例说明
· Bean Validate2.0
·CDI2.0异步接口
· Java Json Binding JSON-B Examples
· Security Realm Examples用例说明
· JMX & REST Examples

# 2.7. 监视应用
您可以通过监视应用功能，实时监测应用的运行状况，包含阻塞/中断的线程数、当前会话数、资源缓存量、请求数、错误请求数、请求处理时间等。

# 补充说明
• 无状态 ejb 的监视合并显示，不再根据名称单独显示。
• war 中存在的 ejb 支持监视；ear 中存在 war 也支持监视。

# 前置条件
• 已获取管理控制台系统管理员账号和密码。
• 已部署应用。

# 查看监视视图
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 单击 “监视”，进入监视页面。
5. 您可以查看应用的实时阻塞的线程数、无状态实例总数、无状态实例活跃数、当前会话数等。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/86565626af6cfd3b0cffe2b307b112a69c4175f698516a568b89bbaf05c5d0f6.jpg)
6. 用户还可查看应用名称、应用状态、阻塞的线程名、Servlet 明细、中断的线程数、资源缓存量（KB）、请求处理总数、请求处理时间（毫秒）、每秒处理请求数(QPS)、平均响应时间(毫秒)、错误请求处理总数、错误率、启动时间以及启动耗时（毫秒）。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/9be72d3293c231a703063c645867224847de6ea93af817c4be270b8794562fb7.jpg)


# 说明：
阻塞的线程名为“-1”，表示未开启慢线程检测功能。
若需要开启 “慢线程检测”，则选择 “应用管理” > “应用”，进入目标应用的 “性能” 页签，打开 “慢线程检测” 开关即可。

# 下载监视视图
1. 进入应用列表页面。
2. 单击“监视”，进入监视视图页面。
3. 在监视视图页面，单击鼠标右键，可将监视视图另存为“.png”图片。

# 2.8. 管理应用

# 2.8.1. 查看应用
在应用列表中，部署的应用以应用名的 ASCII 码顺序进行排序。
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 您可以查看已部署应用的应用名、部署路径、访问前缀、虚拟主机、应用类型、自动部署、应用状态等。
应用状态，如下所示：
◦ “STARTED”：运行中
◦ “STOPPED”：停止
◦ “STARTING”：正在加载应用
◦ “DEPLOYING”：部署中
◦ “FAILED”：失败

# 2.8.2. 编辑应用
应用部署完成后，若需要修改应用所配置的参数，可通过管理控制台进行并编辑应用。
编辑完成后，系统将会重新部署该应用，使修改生效。

# 注意事项
• SpringBoot 兼容、命名空间兼容不允许编辑。
• 若当前部署的应用已被其他模块所引用，则系统将禁止对其执行编辑操作。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 单击 “应用名” 链接，进入编辑应用页面。
5. 您可以根据需要修改应用的相关属性配置。
◦ SpringBoot 兼容、命名空间兼容：不能修改。
◦ 其他参数：请根据需要进行修改。
6. 修改完成后，单击 “更新”，完成应用的编辑操作。
若页面弹出 “应用更新成功”，则说明编辑应用成功。

# 2.8.3. 启动应用
应用部署完成后，默认为 “STARTED” 的状态。若您的应用处于 “STOPPED” 状态，您可以通过管理控制台启动应用，使应用可以对外提供服务。

# 注意事项
该操作仅对 Web 类型的应用有效。

# 前置条件
已部署应用，且应用运行状态为 “STOPPED”。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 在应用所在行的操作列，单击 “启动”，启动应用。

# 说明：
用户可根据需要勾选一个或多个应用，并单击列表上方的 “启动” 按钮，批量启动应用。
5. 在弹出的确认窗口中，单击 “确定”，完成启动应用操作。
若页面弹出 “应用启动成功” 提示信息，则说明启动应用成功。

# 2.8.4. 停止应用
应用部署完成后，默认为 “STARTED” 的状态。若该应用需要停止对外提供服务，可对应用执行停止操作。停止应用后，该应用不再对外提供服务，继续访问该应用，页面将返回 404 错误码。

# 注意事项
• 该操作仅对 Web 类型的应用有效。
• 当停止应用时，容器调用 servlet、filter 等的 destory 方法，以便让 Servlet 相关对象可以释放它所使用的资源。如应用新建的端口、线程需要在 destory 方法中声明销毁。
当启动应用时，相当于进行了部署流程。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 在应用所在行的操作列，单击 “停止”，停止应用。

# 说明：
用户可根据需要勾选一个或多个应用，并单击列表上方的 “停止” 按钮，批量停止应用。
5. 在弹出的确认窗口中，单击“确定”，完成停止应用操作。
若界面弹出“应用停止成功”提示信息，则说明应用停止成功。
应用停止后，用户再次访问应用，页面返回“HTTP ERROR 404”，页面无法访问，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/456afba7b17310d5167052b9b8a043eb9bcb093b304bab3f91a1a3548b12ae6b.jpg)
找不到168.1.15.44的网页
找不到与以下网址对应的网页：http://168.1.15.44:8088/examples/
重新加载

# 2.8.5. 卸载应用
已部署的应用若需要停止应用的服务，可对应用执行卸载操作。
卸载应用后，TongWeb 将会把部署的应用从内存中卸载。对于自动部署和上传部署的应用，卸载后，应用会自动备份到 “${tongweb.base}/data/app/recycle” 目录。

# 注意事项
• 若部署的应用存在关联的“应用增量”，卸载应用时，系统将同步删除应用增量包，并与应用合并为一个应用，备份到 “${tongweb.base}/data/app/recycle” 目录。
• 若应用卸载后需要恢复应用，您可以在“应用回收”页面或者自动备份的文件，对卸载的应用进行恢复。

# 控制台卸载
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 在应用所在行的操作列，单击“卸载”，卸载应用。
说明： 用户可根据需要勾选一个或多个应用，并单击列表上方的 “卸载” 按钮，批量卸载应用。
5. 在弹出的确认窗口中，单击“确定”，完成卸载应用操作。
若页面弹出“应用卸载成功”提示信息，则说明应用卸载成功。

# 删除“应用名称.deployed”标志文件
针对自动部署的应用，可通过删除 “应用名称.deployed” 标志文件的方式卸载应用。
1. 进入 “${tongweb.base}/autodeploy” 目录。
2. 删除 “应用名称.deployed” 标志文件，即可卸载应用。

# 2.9. 应用模板
用户可以通过应用模板预定义部署应用的参数。当部署应用时，指定应用模板后，系统将会使用应用模板里的参数来部署应用。部署应用时指定的其他参数将会被忽略。
用户也可以在 “全局配置”中，指定全局应用模板。若部署应用时，没有指定应用模板，则会尝试使用 “全局配置” 里的 “全局应用模板”。

# 注意事项
若应用同时配置了自定义描述文件 tongweb-web.xml，则会优先使用 tongweb-web.xml 里面的配置参数。

# 2.9.1. 创建应用模板
本章节介绍如何创建应用模板。

# 前置条件
已获取管理控制台系统管理员账号和密码。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用模板”，进入应用模板页面。
4. 单击 “创建”，进入创建应用模板页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ee2e3f031342eb2d4ca7e93d00dc2cb3085806c40c38a5a547b480e943f2c2ff.jpg)
5. 设置应用模板名、虚拟主机、启动优先级等参数。
◦ 模板名：必填项，指定应用模板的名称。模板名需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 虚拟主机：必填项，应用所部署到的虚拟主机。
◦ 启动优先级：必填项，用以约束应用的启动顺序。
关于应用模板的其它相关参数说明，详见应用模板参数配置说明。
6. 配置完成后，单击 “添加”，完成应用模板的创建操作。
若界面弹出 “添加应用模板成功” 提示信息，则说明创建应用模板成功。

# 2.9.2. 使用应用模板
指定应用模板后，系统将会使用应用模板里的参数来部署应用。

# • 部署应用时指定应用模板
1. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
2. 部署应用或者编辑已部署的应用时，进入应用详情页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f57d17117afef969b73ecab31005e8cd74a43bc85f359ddf74045e88ea8346f6.jpg)
注：若是编辑应用时，重新应用模板，则应用模板的配置会覆盖原应用的配置。
3. 单击“添加”（部署应用时）或“更新”（编辑应用时），完成应用模板的应用。

# • 全局配置时指定应用模板
1. 在左侧导航栏中，选择 “基础配置” $>$ “全局配置” > “应用”，进入应用配置页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7b8bd5dee3b18cb8fda45aeef3a7e6a5d100389de9fbab18858eee809ad5690f.jpg)
2. 在 “全局应用模板” 下拉列表中，选择已创建的应用模板。
3. 单击 “更新”，更新全局配置。
若界面弹出 “全局配置更新成功” 提示信息，则说明更新全局配置成功。

# 2.9.3. 管理应用模板

# 查看应用模板
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用模板”，进入应用模板页面。
4. 您可以查看已创建的应用模板。
包含应用模板的序号、模板名等。
注：用户可根据需要输入模板的名称，单击 “搜索” 按钮，搜索指定应用模板。

# 编辑应用模板
应用模板配置信息修改后，引用该模板的应用需要更新应用（更新应用后，系统将应用重新部署）后才能生效。
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用模板”，进入应用模板页面。
4. 单击目标应用模板的模板名，进入应用模板详细配置信息页面。
5. 根据需要修改应用模板的相关信息。
注：应用模板的名称、SpringBoot 兼容、命名空间兼容不可修改。
6. 修改完成后，单击 “更新”，即可完成应用模板的编辑操作。

# 删除应用模板
已被应用应用的模板不可删除。
若需要删除应用模板，请先解除相关引用。删除后不可恢复，请谨慎操作。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用模板”，进入应用模板列表页面。
4. 单击目标应用模板所在行的“删除”，弹出确认删除窗口。
注： 用户可根据需要勾选一个或多个应用模板，并单击列表上方 “删除” 按钮，批量删除应用模板。
5. 单击 “确定”，完成应用模板的删除操作。

# 2.10. 更新应用
您可以通过创建应用增量的方式，以达到更新应用的目的。应用增量更新包是应用的局部更新文件。创建应用增量后，应用增量会和目标应用合并到一起，起到更新应用的作用。
一个目标应用可以安装多个增量包，合并时会根据增量包的时间依次叠加进行。

# 注意事项
• 应用增量更新包必须是 “*.zip” 类型。
• 若需要实现替换或新增应用文件，增量更新包文件组织结构与目标应用保持一致。
• 若需要实现移除目标应用中的文件，在增量更新包根目录建立 “DeleteFiles.txt” 文件，并在其中分行标记要移除的文件，每行记录一个文件，文件路径为相对于目标应用根目录的相对路径。
例如：移除应用中的 “sessions.html” 和 “snake.xhtml”。
1. 新建 “DeleteFiles.txt” 文件。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/238bf2b61e302ca538a210be9b0b5c89367b6c1d8c35e7a9e10a077d8d679f21.jpg)
2. 列举待删除文件。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/3b002a532df5264167eb5da022aa3854e5958f9c8f937d2a481cc2b3d952781f.jpg)
3. 将 “DeleteFiles.txt” 与增量文件压缩为 “*.zip” 包。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/bd2c5be06f1a25ab90ef313886f3fcfefb1d23390bf101b6833b83f7f6f51f78.jpg)


# 2.10.1. 创建应用增量
应用增量更新包创建成功后，存放在 “${tongweb.base}/data/app/update/应用名/patch/应用增量名称+时间”。

# 前置条件
• 已获取管理控制台系统管理员账号和密码。
• 已部署应用且准备好应用增量更新包 “*.zip”。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用增量”，进入应用增量页面。
4. 单击 “创建”，进入创建应用增量页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/1500e876fd0e8b7f0043b7909b6c79b65001b6133afe28cdb72209daaf16dd72.jpg)
5. 设置应用增量名称、选择目标应用、上传应用增量包或者设置应用增量包在服务器上的位置。
◦ 名称： 必填项，指定本次更新的名称。应用增量名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 目标应用： 必填项，在下拉列表中选择已部署且待更新的应用。
◦ 增量包来源： 用户可选择 “上传文件” 或 “服务器文件” 的方式上传增量包。
▪ 上传文件：通过上传文件的方式，上传增量包。
默认情况下，控制台关闭了上传文件功能。若需要开启，请进入 “集中管理” $>$ “安全配置” $>$ “控制台安全”，关闭 “禁用文件上传”，详见禁用文件上传。
▪ 服务器文件：通过指定增量包在服务器上位置的方式，上传增量包。
关于应用增量的其它相关参数说明，详见应用增量参数配置说明。
6. 配置完成后，单击 “添加”，完成应用增量的创建操作。
若界面弹出 “添加应用增量成功” 提示信息，则说明创建应用增量成功。

# 2.10.2. 查看应用增量
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用增量”，进入应用增量页面。
4. 您可以查看已创建的应用增量。
包含应用增量的名称、目标应用、创建日期等。
5. 单击目标应用增量，进入应用增量详细信息页面。
6. 您可以查看应用增量的名称、目标应用、创建日期等。

# 2.10.3. 回退应用增量
回退应用增量包后，应用回退到应用更新前。
回退应用增量包后，“${tongweb.base}/data/app/update/应用名/patch” 里对应的应用增量文件会同步删除。
回退应用增量更新包后，系统自动删除增量更新包，且不可恢复，请谨慎操作。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用增量”，进入应用增量列表页面。
4. 单击目标应用增量所在行的 “回退”，弹出确认回退窗口。
注: 用户可根据需要勾选一个或多个应用增量，并单击列表上方的 “回退” 按钮，批量回退应用增量。
5. 单击“确定”，完成应用增量文件的回退操作。
若界面弹出“应用增量回退成功”提示信息，则说明回退应用增量文件成功。
“${tongweb.base}/data/app/update/应用名/patch/”目录下的对应的应用增量文件也将被删除。

# 2.11. 应用备份

# 2.11.1. 备份应用
为了确保应用在被人为失误、操作不当等情况下删除或损坏后，能及时、有效地恢复应用，TongWeb 提供应用备份功能，保障应用能尽快恢复不影响业务运行。

# 注意事项
• 用户可以通过控制台备份当前生效的应用文件。
默认备份路径为 “${tongweb.base}/data/app/backup”。
说明：
用户可以进入 “基础配置” $>$ “全局配置” $>$ “应用”，自定义应用备份目录。
• 用户可进入 “基础配置” $>$ “全局配置” $>$ “应用” 页面，开启 “应用主动备份”。
开启后，系统会在应用部署后，主动执行一次备份。
• 同一个应用最多可创建三个备份，继续备份会清理较老的备份，请谨慎操作。

# 说明：
您也可以进入 “基础配置” > “全局配置” > “应用”，自定义应用备份数量，超过该值后，继续备份会清除较老的备份。
您也可以通过备份的应用文件，恢复当前应用，详细操作请参见恢复备份应用。

# 前置条件
• 已获取管理控制台系统管理员账号和密码。
• 已部署应用。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用备份”，进入应用备份页面。
4. 单击“创建”，进入创建应用备份页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a14e83db4180f92d75e46b584573ca8ad5ff8d3120c7e693c9fab5a956ee80d6.jpg)
5. 在 “备份应用” 下拉列表中，选择待备份的应用，并根据需要添加备份应用的相关描述信息。
6. 单击 “添加”，完成应用的备份操作。
7. 在应用备份列表中，可查看备份的应用。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/633e573d06f356a5782899b9f25469c474543c0904cc46f24d39b6d65bbc7201.jpg)
您也可以进入 “${tongweb.base}/data/app/backup”目录，查看备份的应用。
以 “部署的 examples 目录中应用” 为例，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/6265d0a64535ff03d068ea16ebe9df7daf9f0b96277105de7b0c82e960f25dcc.jpg)


# 2.11.2. 查看配置信息
在应用备份列表中，可查看备份应用的配置信息。
该配置信息详情页里的“配置信息”可用于自动部署的预置配置，详细信息请参见预置自动部署相关配置。

# 前置条件
• 已获取管理控制台账号和密码。
• 已存在备份的应用。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用备份”，进入应用备份列表页面。
4. 单击目标应用所在行的 “配置信息”，即可查看目标应用的配置信息详情。
包含备份应用、名称、应用文件、配置信息、备份日期、备份说明等。

# 应用备份
备份应用
examples.BackupFlag20221201172554
名称
examples.BackupElag20221201172554
应用文件
examples
配置信息
apmaxActivi"ctees"mibet"telse"st=spsactecoU"aaaamaoabreve=examples"reloadblease"bodlO"sHtpOnlytrue"teadPoy"acTt""achectae4"spilefeshbRelativeReditregasUdstrcotrueflEncinU-8apees"odiU-abeateleifefladeploteapSeioesotetfrpddptexampsouscotrrEnabled=faeserfsarridac"absevelopment="false"requestCharacterEncoding="UTF-8" enablePooling="true"state="STARTED"type="war"/>
备份日期
备份说明

# 2.11.3. 下载备份应用&配置文件
您可以根据需要下载已备份的应用或者配置文件（tongweb-web.xml）。并可以将下载的配置文件（tongweb-web.xml）用作自动部署应用时的预配置文件。

# 注意事项
控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。

# 前置条件
• 已获取管理控制台账号和密码。
• 已存在备份的应用。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用备份”，进入应用备份列表页面。
4. 在下载应用所在行的操作列，单击 “下载”，弹出选择需要下载的文件窗口。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d9bea8790f2aa0402d1d1026824cb2e2cca037897235cf636c3a2fada2599652.jpg)
5. 选择待下载的应用或者配置文件（tongweb-web.xml）。
6. 单击“下载”，即可下载文件。
下载以备份应用的名称命名的“.zip”包，解压后即可使用。

# 2.11.4. 恢复备份应用
您可以在应用备份列表中，直接单击目标应用备份所在行的“恢复”，恢复应用。恢复期间应用会被停止。若有存在的会话，则会话会丢失。

# 注意事项
• 恢复备份应用时，自动恢复部署到 “${tongweb.base}\deployment” 目录。
• 若在 “${tongweb.base}\backup\app\backup” 里应用备份文件被删除，应用备份列表里的备份应用记录也会被清除，则该应用将无法恢复，请谨慎操作。

# 前置条件
• 已获取管理控制台账号和密码。
• 已存在备份的应用。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用备份”，进入应用备份列表页面。
4. 在待恢复应用所在行的操作列，单击 “恢复”，恢复到本次备份。
若界面弹出 “应用备份恢复成功”提示信息，则说明恢复应用成功。

# 2.11.5. 管理应用备份

# 查看应用备份
在应用备份列表中，您可以根据需要进行查看、恢复、删除指定应用备份。
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用备份”，进入应用备份页面。
注：若在 “${tongweb.base}\backup\app\backup” 里应用备份里的备份文件被删除，应用备份列表里的备份应用记录也会被清除，请谨慎操作。
4. 您可以查看应用备份中已备份的应用。
包含备份应用的名称、应用文件、备份日期、备份说明等信息。
5. 单击应用备份名称，可以更新应用备份的备份说明。

# 删除应用备份
删除应用备份文件时，该组件引用的其它组件不会被删除。
删除应用备份里的应用备份文件时，“${tongweb.base}\backup\app\backup”里对应的应用文件会同步删除。
删除后不可恢复，请谨慎操作。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用备份”，进入应用备份列表页面。
4. 单击目标应用备份文件所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个应用备份，并单击列表上方的 “删除” 按钮，批量删除应用备份。
5. 单击 “确定”，完成应用备份文件的删除操作。
若界面弹出“应用备份删除成功”提示信息，则说明删除应用备份文件成功。
“${tongweb.base}/data/app/backup”目录下的对应的应用备份文件也将被删除。

# 2.12. 应用回收
应用回收里的应用是您卸载应用的备份，类似于回收站，您可以根据需要进行查看、恢复、删除指定应用。在部署应用时，若 “安全” 页签下的 “应用回收” 设置为开启状态（默认为开启），那么当该应用被卸载后，
系统会自动将该应用回收并加入到 “应用回收” 列表中。
您也可以到 “${tongweb.base}/data/app/recycle” 目录中，查看到回收的应用。

# 注意事项
• 采用目录方式部署的应用以及自动部署的应用在卸载后，均会进行回收。
• 同一个应用最多仅保留最近的三个回收备份。

# 2.12.1. 查看应用回收
本章节主要介绍如何查看应用回收。

# 前置条件
• 已获取管理控制台系统管理员账号和密码。
• 应用回收中存在已卸载应用。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用回收”，进入应用回收页面。

# 注意：
若在 “${tongweb.base}\backup\app\recycle” 里应用回收里的备份文件被删除，应用回收列表里的回收应用记录也会被清除，请谨慎操作。
4. 您可以查看应用回收中已卸载的应用。
包含卸载应用的名称、应用文件、卸载备份日期等信息。
5. 单击应用回收的名称，可查看应用回收详细信息。

# 应用回收
?备份应用
examples.BackupFlaq20.3314
名称
examples.BackupFlag203314
应用文件
examples
配置信息
pmaActie"tes"fssContext=etsoracteci-lsauiaarsifemaobldfeessiooeromprabebtrevedabe$= ^ { m }$ webModuleOleHpOlcee=eadyhchOee"wecompileeReativeRedteaftQotescasosrelesoroteepeIsedbeerreo=fasestarbseterEncoding="UTF-8" enablePooling="true" state="STARTED" type="war"/>
备份日期
备份说明
Automatic backup after app uninstallation.

# 2.12.2. 下载回收应用&配置文件
您可以根据需要下载已回收的应用或者配置文件（tongweb-web.xml），并可以将下载的配置文件（tongweb-web.xml）用作自动部署应用时的预配置文件。

# 注意事项
控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。

# 前置条件
• 已获取管理控制台账号和密码。
• 已存在回收的应用。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用回收”，进入应用回收列表页面。
4. 在待下载应用所在行的操作列，单击“下载”，弹出选择需要下载的文件窗口。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/4e8c0e2f8e3dc84c8ff58c94006206685ca299e872b405c1bf0285662f78ecdf.jpg)
5. 选择待下载的应用或者配置文件（tongweb-web.xml）。
6. 单击“下载”，即可下载文件。
下载以回收应用的名称命名的 “.zip” 包，解压后即可使用。

# 2.12.3. 恢复回收应用
您可以通过应用回收直接单击“恢复”，恢复应用。恢复期间应用会被停止，如果有存在的会话，则会话会丢失。
若在 “${tongweb.base}\backup\app\recycle” 里的应用备份文件被删除，应用回收列表里的回收应用记录也会被清除，则该应用将无法恢复，请谨慎操作。

# 前置条件
• 已获取管理控制台账号和密码。
• 已存在卸载的应用。

# 约束说明
• 恢复自动部署的应用时，自动恢复到 “${tongweb.base}\deployment” 目录。
• 若卸载的应用包含应用增量包，恢复应用时，系统仅展示应用与应用增量包合并的应用，不再展示应用增量包。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用回收”，进入应用回收列表页面。
4. 在待恢复应用所在行的操作列，单击 “恢复”，恢复到本次备份。
若界面弹出“应用回收恢复成功”提示信息，则说明恢复应用成功。

# 2.12.4. 删除应用回收
本章节主要介绍如何删除回收站中的应用备份文件。
删除回收站应用备份文件时，该组件引用的其它组件不会被删除。
删除应用回收里的应用备份文件时，“${tongweb.base}\backup\app\recycle”里对应的应用文件会同步删除。
删除后不可恢复，请谨慎操作。

# 前置条件
• 已获取系统管理员账号和密码。
• 已存在卸载的应用。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用回收”，进入应用回收列表页面。
4. 单击目标应用备份文件所在行的“删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个回收的应用，并单击列表上方的 “删除” 按钮，批量删除回收的应用。
5. 单击 “确定”，完成应用备份文件的删除操作。
若界面弹出“应用回收删除成功”提示信息，则说明删除应用备份文件成功。
“${tongweb.base}/data/app/recycle”目录下的对应的应用备份文件也将被删除。

# 2.12.5. 清空回收站
为了方便尽快用户清除回收站卸载的应用，TongWeb 提供一键清空回收站功能。
一键清空回收站后不可恢复，请谨慎操作。

# 前置条件
• 已获取系统管理员账号和密码。
• 已存在卸载的应用。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用回收”，进入应用回收列表页面。
4. 单击 “清空回收站”，弹出确认清空回收站窗口。
5. 单击 “确定”，完成一键清空回收站的操作。
若界面弹出“应用回收清空回收站成功”提示信息，则说明一键清空回收站成功。
“${tongweb.base}/data/app/recycle” 目录下的对应的应用备份文件也将被彻底删除。

# 2.13. 应用迁移
支持将部署在 Tomcat、TongWeb7（可在 “迁移配置” 中设置允许多端口迁移
）、WebLogic、WebSphere、JBoss、Nginx 或者 Jetty 上的应用迁移至 TongWeb。
用户可根据需要进行完整迁移（包含服务器配置、应用主体）或者仅迁移服务器配置。

# 前置条件
• 已准备好待迁移的 Tomcat、TongWeb7、WebLogic、WebSphere、JBoss、Nginx 或者 Jetty 应用。
• 对应用服务器 TongWeb7 进行应用迁移时，系统默认仅对一个端口（即 8089 端口）执行迁移操作。
若待迁移的应用服务器 TongWeb7 配置了多个端口，则需要先开启授权开关，才能完成迁移，详见迁移配置。

# 迁移备份
迁移操作会修改 “${tongweb.base}/conf/tongweb.xml” 文件。在修改该文件前，系统会在
“${tongweb.base}/data/migration” 目录下自动备份该文件，以防意外情况导致原 tongweb.xml 配置数据丢失。

# 迁移配置项
迁移 TongWeb7 时，支持迁移的必要配置项，如下所示。
• 通道：名称、端口、类型
• 虚拟主机：名称、别名
• 应用：名称、前缀（如果有）
• 数据源：名称、连接 url、驱动类名、用户名、密码、驱动所在路径
注意： 支持自动解密再加密 TongWeb7 的数据源的数据库连接用户名和密码。

# 迁移应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用迁移”，进入应用迁移页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/2da2d1a2c2ab7147b7670759907f91f43622d071644c7b42f4cc5f8166af6ce6.jpg)
4. 选择应用服务器的类型 “Tomcat”、“TongWeb”、“WebLogic”、“WebSphere”、“JBoss”、“Nginx” 或“Jetty”。
5. 输入应用服务器的根路径。
说明：支持批量迁移，单击 $^ { 6 6 } +$ 添加”，即可输入多个应用服务器的路径。
例如 “D:\tomcat8.5”。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/84826aa7a6d632872cd0efb38ce52f649baa3d8f7159313b26b6800dbadd5423.jpg)
6. 选择是否开启 “是否拷贝应用” 开关。
◦ 若开启 “是否拷贝应用”，则执行完整迁移，包括应用主体、服务器配置等。默认开启。
◦ 若关闭 “是否拷贝应用”，则仅迁移服务器的配置（如：仅迁移数据源）。
7. 选择是否开启 “是否迁移通道” 开关。
◦ 若开启 “是否迁移通道”，则可迁移通道（名称、端口、IP）。
说明：
针对 TongWeb7 应用服务器，若用户存在多个端口，还可以进入 “迁移配置” 界面，并开启 “允许多端口迁移” 选项，从而实现多个端口的迁移。
◦ 若关闭 “是否迁移通道”，则不迁移通道。
8. 配置完成后，单击 “迁移”，即可将指定应用迁移至 TongWeb。
若界面弹出 “应用迁移：有配置项发生变更，需重启 TongWeb 以使其生效” 提示信息，则说明迁移成功。
9. 重启 TongWeb 实例，使迁移生效。

# 迁移验证
1. 登录 TongWeb 控制台。
2. 切换到目标实例。
3. 选择 “应用管理” $>$ “应用”，进入应用列表。
4. 用户可查看到从 “Tomcat”、“TongWeb”、“WebLogic”、“WebSphere”、“JBoss”、“Nginx” 或“Jetty” 迁移的应用或应用的必要配置数据。

# 2.14. 迁移配置
在对应用服务器 TongWeb7 执行应用迁移时，系统默认仅对一个端口（即 8089 端口）执行迁移操作。若应用服务器 TongWeb7 配置了多个端口，在此情况下，需要开启授权开关才能迁移。该授权开关具备实时生效的特性，无需重启服务器即可生效。应用迁移完成后，保持原端口不变。

# 前置条件
已获取系统管理员账号和密码。

# 允许多端口迁移
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “迁移配置”，进入迁移配置页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e95c038b3eff1fa7d6d08faf725f26d8825ab4f421b95ca0d411c56ecb340c56.jpg)
4. 打开 “允许多端口迁移” 开关。
5. 单击 “更新”，即可允许多端口迁移操作。
注：该更新操作实时生效，无需重启服务器。

# 3. 配置管理

# 3.1. Web容器

# 3.1.1. 通道与虚拟主机的关系
通道定义为访问应用的端口，用于接收用户请求，包含了线程池、网络连接、SSL/TLS 等配置，通过配置这些参数可以为应用提供安全、高效的网络连接服务。
虚拟主机定义为用户访问应用的 IP 地址或域名。主要用于对应用进行分组管理。虚拟主机上可以配置一系列的资源，部署在其上的应用共享这些资源。除了 admin 通道（管理端口）外，其它任何通道均可以访问到虚拟主机。
通道与虚拟主机一起为用户提供监听地址和端口。虚拟主机提供IP地址，通道提供端口，例如：http://IP:port，用户即可通过您配置的 “http://IP:port” 访问部署的应用。
在部署应用时，可在 “安全” 页签下，勾选 “限定访问端口”，限定访问端口后，只有指定的端口可以访问该应用，其它端口的访问会被拒绝。
通道支持的网络层协议 “HTTP/1.1” 和 “AJP”。
系统提供默认 admin 通道 “0.0.0.0-9060” 和 server 通道 “0.0.0.0-8088”。
• admin 通道：提供给 TongWeb 管理控制台使用的通道。
• server 通道：提供给应用的通道。

# 3.1.2. 通道

# 3.1.2.1. 创建 HTTP 通道
本章节介绍如何创建 HTTP 通道。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “通道”，进入通道列表页面。
4. 单击 “创建”，进入 “创建通道” 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/6d0e1029da0defa022e5c7765c4c4e1aa6faaca301e19e5d006fb058424564b7.jpg)
5. 配置通道名、端口，协议选择 “HTTP/1.1”。
◦ 通道名：必填项，通道名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 端口：必填项，监听网络请求的端口，默认为 $" 8 0 8 9 "$ 。
◦ 协议：非必填，通道支持网络层协议，默认为 “HTTP/1.1”。
◦ 附加响应头：非必填，在 “HTTP 属性” 页签下，附加响应头允许使用 () 字符。
关于通道的更多参数说明，详见通道参数配置说明。
6. 配置完成后，单击 “添加”，完成通道的添加操作。
若界面弹出 “通道添加成功” 提示信息，则说明通道添加成功。

# 3.1.2.2. 创建 AJP 通道
本章节介绍如何创建 AJP 通道。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择“Web容器”>“通道”，进入通道列表页面。
4. 单击“创建”，进入“创建通道”页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/fa95c5e1e1395e84988d25dd4df5b912324d6c1df728615f5063bf64194f396e.jpg)
5. 设置通道名、端口，协议选择“AJP”。
◦ 通道名：必填项，通道名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 端口：必填项，监听网络请求的端口，默认为 $" 8 0 8 9 "$ 。
◦ 协议：非必填，通道支持网络层协议，选择 “AJP”。
关于通道的更多参数说明，详见通道参数配置说明。
6. 配置完成后，单击 “添加”，完成通道的添加操作。
若界面弹出 “通道添加成功” 提示信息，则说明通道添加成功。

# 3.1.2.3. 配置 SSL 证书示例
本章节介绍如何配置 SSL 证书。

# 前置条件
• 已获取系统管理员账号和密码。
• 已准备好 SSL 证书。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web容器” $>$ “通道”，进入通道列表页面。
4. 进入目标通道编辑页面，并在 “安全” 页签下打开 “开启 SSL” 开关，即可配置 SSL 证书相关信息。
注意：
勾选 “启用协议” 时，考虑安全问题，不建议启用 SSLv3 和 SSLv2Hello。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/9b68b5312f6294b2096971b70d997d8a7b48761ece8420352c32f4ea682cc0e7.jpg)


# 5. 配置证书相关信息。
如下配置的证书均为示例，请根据需要替换为您自己的标准证书。
<table><tr><td>条件</td><td>默认证书</td><td>默认存储路径</td><td>默认密码</td></tr><tr><td>打开“开启SSL”开关配置 SSL 证书</td><td>conf/server.keystore</td><td>${tongweb.base}/conf/server.keystore</td><td>changeit</td></tr><tr><td>不开启国密认证“客户端认证”设置为“true”配置信任证书</td><td>conf/server.keystore</td><td>${tongweb.base}/conf/server.keystore</td><td>changeit</td></tr><tr><td>开启国密认证配置加密证书和签名证书</td><td>•加密证书
conf/sm2.ENC.pfx
•签名证书
conf/sm2.sig.pfx</td><td>•加密证书路径
${tongweb.base}/conf/sm2 ENC.pfx
•签名证书路径
${tongweb.base}/conf/sm2.sig.pfx</td><td>•加密证书密码
12345678
•签名证书密码
12345678</td></tr></table>
6. 配置完成后，单击 “更新”，即可完成 SSL 的配置操作。

# 3.1.2.4. 应用通道
本章节介绍如何应用通道。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 单击 “部署”，进入部署页面。
以部署“${tongweb.home}/version*/examples/examples.war”为例说明。
5. 单击 “安全” 页签，勾选已创建的 “限定访问端口”。
以通道名为 “channel”，端口号以 “8089” 为例。
◦ 勾选已创建的通道：表示只有指定的端口可以访问本应用，其它端口的访问会被拒绝。
◦ 不勾选：表示不限制。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/72da9ffa0fe2be5debfcff48cd12a538b76a37e474994666837fcd02b040dc0d.jpg)
6. 其他参数请根据需要配置。
7. 单击“添加”，完成应用部署。

# 3.1.2.5. 验证通道
通道应用成功后，客户端即可通过此通道接入到服务器。
以部署的“${tongweb.home}\version*\examples\examples.war”应用为例。
1. 在左侧导航栏中，选择 “应用管理” > “应用”，进入应用列表页面。
2. 切换到目标实例。
3. 单击已部署应用所在行的 “链接” 访问应用，进入“应用/链接”页面。
可查看到对外提供服务的通道，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/4632cce023a933ddfb961bc18fdb910370644a1ee04fa88369f02c0d2584f9e3.jpg)


# 3.1.2.6. 监视通道
您可以通过监视通道的方式，了解通道的运行状况以及健康状态。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建通道。

# 查看监视视图
您可以查看通道的名称以及通道的活跃线程数、总线程数、当前请求总数以及待处理请求数。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “通道”，进入通道列表页面。
4. 单击目标通道所在行的 “监视”，进入监视页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f3724a7b5d8ca7fa645c6174f9b10b7ef46d73ed413d43d3201a9f95cf8861f6.jpg)
5. 可查看通道的活跃线程数、总线程数、当前请求总数、待处理请求数以及当前连接数。
左上角的 “server” 表示通道的名称。
6. 还可以查看通道的 “请求处理总数”、“慢请求总数”、“错误请求处理总数”、“错误率”、“请求处理总时间(毫秒)”、“平均响应时间(毫秒)”、“每秒处理请求数(QPS)”、“接收字节数”、“发送字节数” 以及 “启用的密码套件”。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/4287ebd486927eef9c7627c022c59bc9be6aaa00d1fc7feb20aa33f8d6678ae4.jpg)
属性说明，如下表所示。
<table><tr><td>属性</td><td>说明</td></tr><tr><td>请求处理总数</td><td>该通道累积处理的请求总数，“-1”表示不监控。当在该通道的“其它”页签下，打开了“启用网络数据监控”开关，即可查看到监视数据。</td></tr><tr><td>慢请求总数</td><td>当在该通道的“其它”页签下，打开了“启用网络数据监控”开关，并设置“慢请求阈值”，即可查看到监视数据。用户还可以打开“归零网络监控数据”，并设置“归零周期”。</td></tr><tr><td>错误请求处理总数</td><td>该通道累积处理的错误请求总数，“-1”表示不监控。当在该通道的“其它”页签下，打开了“启用网络数据监控”开关，即可查看到监视数据。</td></tr><tr><td>错误率</td><td>错误请求处理总数在请求处理总数中的占比，单位：百分比，“-1”表示不监控。</td></tr><tr><td>请求处理总时间（毫秒）</td><td>该通道处理请求的累积时间，“-1”表示不监控。当在该通道的“其它”页签下，打开了“启用网络数据监控”开关，即可查看到监视数据。</td></tr><tr><td>平均响应时间（毫秒）</td><td>所有请求的平均处理时间，单位：毫秒，“-1”表示不监控。</td></tr><tr><td>每秒处理请求数（QPS）</td><td>该通道平均每秒处理的请求总数，“-1”表示不监控。</td></tr><tr><td>接收字节数</td><td>服务器从客户端接收到的字节数，“-1”表示不监控。当在该通道的“其它”页签下，打开了“启用网络数据监控”开关，即可查看到监视数据。</td></tr><tr><td>发送字节数</td><td>服务器发送给客户端的字节数，“-1”表示不监控。当在该通道的“其它”页签下，打开了“启用网络数据监控”开关，即可查看到监视数据。</td></tr><tr><td>启用的密码套件</td><td>当在该通道的“安全”页签下，开启了SSL/TLS，监视里即可显示已启动的密码套件。</td></tr></table>

# 下载监视视图
1. 进入通道列表页面。
2. 单击目标通道所在行的“监视”，进入监视视图页面。
3. 在监视视图页面，单击鼠标右键，可将监视视图另存为“.png”图片。

# 3.1.2.7. 管理通道
名称为admin，IP和端口号为“0.0.0.0:9060”的通道是系统受管的通道，不能对其进行停止和删除操作。

# 查看通道
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “通道”，进入通道列表页面。
4. 在通道列表页面，您可以查看已创建的通道。
包含通道名称、协议、IP、端口、压缩级别、开启 SSL、支持 HTTP/2、管理端口、运行中等。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/13ef88f4846151b26afae98eb167d634933181da32477dffb7682dd677ab1416.jpg)


# 5. 查看提供给应用的通道。
例如：通道列表中包含 admin（0.0.0.0:9060）、server（0.0.0.0:8088）、channel（0.0.0.0:8089）通道。
部署应用后，单击应用所在行的 “链接”，可查看提供给应用的通道为 server（0.0.0:8088）和 channel（0.0.0.0:8089）。
admin（0.0.0.0:9060）仅提供给 TongWeb 管理控制台使用。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f6c618f14631727d8064c4e52c73cfd3d693976542d2fab3491efaa76a667d8f.jpg)


# 编辑通道
修改通道的 IP 和端口等信息后，不需要重启 TongWeb 服务器可实时生效。
若修改 admin 通道（提供给 TongWeb 管理控制台使用的通道）的相关信息，需要注意如下信息。
• 若 IP 和端口 “0.0.0.0:9060” 发生变更，需要使用修改后的 IP 或者端口进行重新登录。
• 若修改 admin 通道其他参数，需要按 “F5” 刷新页面后，方可实时生效。
操作步骤，如下所示。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “通道”，进入通道列表页面。
4. 单击待编辑通道的名称，进入编辑通道页面。
5. 根据提示信息修改相关参数（注：通道名不允许修改）。
6. 单击 “更新”，完成通道的编辑操作。
若界面弹出通道更新成功提示信息，则说明更新通道成功。

# 启动通道
启动通道后，客户端可通过此通道的IP和端口接入到服务器。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “通道”，进入通道列表页面。
4. 单击目标通道所在行的 “启动”，弹出确认启动通道窗口。

# 说明：
用户可根据需要勾选一个或多个通道，并单击列表上方的 “启动” 按钮，批量启动通道。
5. 单击“确定”，完成通道的启动操作。
若界面弹出“通道启动成功”提示信息，则说明通道启动成功。

# 停止通道
停止通道后，客户端将不能通过此链接接入到服务器。
• 通道名为 admin，IP 端口为 “0.0.0.0:9060” 的通道为系统受管的通道，专门提供给 TongWeb 管理控制台使用，该通道不能停止。
• 通道名为 server，IP 和端口为 “0.0.0.0:8088” 的通道为系统受管的通道，专门提供给应用使用，该通道不能停止。
操作步骤，如下所示。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “通道”，进入通道列表页面。
4. 单击目标通道所在行的 “停止”，弹出确认停止通道窗口。

# 说明：
用户可根据需要勾选一个或多个通道，并单击列表上方的 “停止” 按钮，批量停止通道。
5. 单击 “确定”，完成通道的停止操作。
若界面弹出 “通道停止成功” 提示信息，则说明通道停止成功。

# 删除通道
删除通道时，通道引用的其它组件不会被删除。
• 通道名为 admin，IP 和端口为 “0.0.0.0:9060” 的通道为系统受管的通道，专门提供给 TongWeb 管理控制台使用，无法删除。
• 通道名为 server，IP 和端口为 “0.0.0.0:8088” 的通道为系统受管的通道，专门提供给应用使用，该通道不能删除。
操作步骤，如下所示。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “通道”，进入通道列表页面。
4. 单击目标通道所在行的 “删除”，弹出确认删除窗口。

# 说明：
用户可根据需要勾选一个或多个通道，并单击列表上方的 “删除” 按钮，批量删除通道。
5. 单击 “确定”，完成通道的删除操作。
若界面弹出 “通道删除成功” 提示信息，则说明删除通道成功。

# 3.1.3. 虚拟主机

# 3.1.3.1. 创建虚拟主机
“localhost” 为系统默认虚拟主机。TongWeb 控制台部署在 “admin” 虚拟主机上。
部署应用时，默认使用 “localhost” 虚拟主机。若未指定特定的虚拟主机，则应用部署到系统默认主机上。
您可以根据需要创建新的虚拟主机，并将应用部署在指定虚拟主机上。

# 前置条件
已获取管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “虚拟主机”，进入虚拟主机页面。
4. 单击 “创建”，进入创建虚拟主机页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/66752cdc68d20b50e459281165502575621fb0a2adf4228f37c4676e3b94bd1d.jpg)


# 5. 配置虚拟主机相关参数。
◦ 主机名： 必填项，作为访问该虚拟机的域名。主机名需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
注：若主机名需要支持下划线("_")等特殊字符，可前往 “基础配置” > “全局配置” > “服务器” 页面，在 “主机名允许字符” 配置项中配置相关特殊字符。
创建的虚拟主机的主机名可以指定为 IP 地址或者域名，作为访问应用的域名。
▪ 若指定为域名，则需要有 DNS（Domain Name System，DNS）解析该域名，或直接写在浏览器客户端 hosts 表中。
例如，写在浏览器客户端 hosts 表中。进入“C:\Windows\System32\drivers\etc”，修改hosts文件，添加虚拟主机名与IP地址的映射。
▪ 虚拟主机名避免使用 IP 地址，若使用IP地址，则此 IP 只能供此虚拟主机下的应用使用，可能导致TongWeb 控制台无法访问。

# ◦ 关键参数附加说明：
<table><tr><td>参数</td><td>说明</td></tr><tr><td>默认安全域</td><td>若“默认安全域”下没有可选的安全域，请前往“Web容器”&gt;“安全域”，创建安全域。</td></tr><tr><td>单点登录</td><td>开启单点登录（SSO）后，优先使用虚拟主机的默认安全域而不是应用的安全域。在同一虚拟主机下使用相同安全域的应用可以实现多点登录，即登录一次访问多个应用。</td></tr><tr><td>会话服务器</td><td>若应用和虚拟主机均配置了会话服务器，则存在如下情况。·若虚拟主机同时开启了“Session共享”，则虚拟主机的会话服务器优先级高于应用配置的会话服务器。·若虚拟主机没有开启“Session共享”，则应用配置的会话服务器优先级高于虚拟主机的会话服务器。</td></tr><tr><td>Session共享</td><td>开启 Session共享后，同一虚拟主机的应用可实现 Session共享。Session共享是内存进行 Session共享。</td></tr></table>
◦ 关于虚拟主机的更多参数说明，详见虚拟主机参数配置说明。
6. 配置完成后，单击 “添加”，完成虚拟主机的创建操作。
若界面弹出 “虚拟主机创建成功” 提示信息，则说明创建虚拟主机成功。

# 3.1.3.2. 应用虚拟主机
本章节介绍如何应用虚拟主机。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建虚拟主机，且虚拟主机名“test”已有DNS解析，或者写在了浏览器客户端 hosts 表中。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” > “应用”，进入应用列表页面。
4. 单击 “部署”，进入部署页面。
以部署 “${tongweb.home}/version*/examples/examples.war” 为例说明。
5. 请根据需要选择默认或者已创建的 “虚拟主机”。
如下以勾选已创建的 “test” 虚拟主机为例说明。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/06dcee73b6812c9c537a23702fc1f8a9c52bd84356a8e2405ca818ccb1c170d2.jpg)
6. 其他参数根据需要配置。
7. 单击 “添加”，完成应用部署。

# 3.1.3.3. 验证虚拟主机
虚拟主机应用成功后，客户端即可通过此虚拟主机接入到服务器。
以部署的 “${tongweb.home}\version*\examples\examples.war” 应用为例。
1. 在左侧导航栏中，选择 “应用管理” > “应用”，进入应用列表页面。
2. 切换到目标实例。
3. 单击已部署应用所在行的 “链接” 访问应用，进入 “应用/链接” 页面。
可查看到对外提供服务的虚拟主机，如下图所示。
应用／链接
状态:
true
消息:
应用链接成功
http//test:3088/examples

# 3.1.3.4. 管理虚拟主机
用户可查看、编辑或删除虚拟机。

# 查看虚拟主机
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “虚拟主机”，进入虚拟主机列表页面。
4. 在虚拟主机列表页面，您可以查看已创建的虚拟主机。
包含主机名、别名、默认安全域、单点登录、Session 共享等。

# 说明：
◦ admin：TongWeb 控制台部署的 “admin” 虚拟主机。
◦ server：“localhost” 为系统默认虚拟主机。

# 编辑虚拟主机
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “虚拟主机”，进入虚拟主机列表页面。
4. 单击目标虚拟主机的主机名，进入编辑虚拟主机页面。
5. 根据提示信息修改虚拟主机相关参数。

# 说明：
虚拟主机名不能编辑。
6. 编辑完成后，单击 “更新”，更新虚拟主机配置信息。
若界面弹出 “虚拟主机更新成功” 提示信息，则说明编辑虚拟主机成功。

# 删除虚拟主机
admin 和 localhost 是系统受管的虚拟主机，不能对其进行删除操作。
虚拟主机若被其它组件引用，则该虚拟主机无法删除。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “虚拟主机”，进入虚拟主机列表页面。
4. 单击目标虚拟主机所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个虚拟主机，并单击列表上方的 “删除” 按钮，批量删除虚拟主机。
5. 单击 “确定”，完成虚拟主机的删除操作。
若界面弹出 “虚拟主机删除成功” 提示信息，则说明删除虚拟主机成功。

# 3.1.4. 数据源
数据源是 TongWeb 提供给应用访问数据库的方式，通过配置数据源的连接池大小、空闲、超时、泄漏、验证等方式，达到优化数据库和网络资源的利用率，从而提高数据访问的性能。
数据源的连接池采用了 FIFO 队列数据处理方式保持所有的数据库连接。
TongWeb 每次获取连接从队列头部获取，归还连接时放到队列尾部。获取连接和归还连接都会更新连接的时间戳，使得所有的连接被均匀地使用，进而保持所有连接的活跃性。
用户创建数据源后，TongWeb 会创建一定数量的连接，并将其放到连接池中。应用通过数据源的 JNDI 获取数据源对象，再通过数据源对象从连接池中获取数据库连接。通过数据库连接即可进行一系列数据库操作。连接使用完成后，应用调用连接对象的close()方法将连接返回连接池中供下次使用。

# 3.1.4.1. 创建数据源
本章节介绍如何创建数据源。

# 前置条件
• 已获取系统管理员账号和密码。
• 已提前准备好对应数据库的连接信息，比如：连接URL、驱动类、用户名、密码、相应版本对应的JDBC 的 jar 包。
数据源示例以如下信息为例说明。用户创建数据源时，请根据您的实际环境填写。
◦ 连接URL：jdbc:mysql://168.1.13.108:3316/zmm2
◦ 驱动类：com.mysql.cj.jdbc.Driver
◦ 用户名：root
◦ 密码：123456
◦ 驱动包：mysql-connector-java-8.0.11.jar
若已将驱动包存放在 “${tongweb.base}/lib/” 目录下，配置驱动包位置参数时，则不填写。
• 开通 TongWeb 所在机器和数据库服务器之间的端口，确保能够连接上。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源列表页面。
4. 单击 “创建”，进入创建数据源页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/92b96af52afdc41d42b8ef9347d3ede8f436a22e8cf132db8b26767d1369742f.jpg)
5. 配置数据源相关参数。
◦ 数据源名：必填项，数据源名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 绑定 JNDI：必填项，数据源的别名会被用作其绑定到 JNDI 资源树上的名称。
◦ 数据库连接方式：非必填，可选择 “使用 JDBC 标准方式”，或者使用自定义 Jdbc 模板。
当使用自定义 Jdbc 模板时，数据库名称支持为空。
◦ 连接 URL：必填项，连接到数据库的 URL。
◦ 驱动类：必填项，数据库驱动的全名称。
◦ 用户名/密码：连接数据库的用户名和密码。
通过控制台配置数据源时，输入明文用户名/密码，保存后在 tongweb.xml 里是密文。
手动修改 tongweb.xml 中数据源配置时，用户名和密码无论写明文还是密文都正常运行。
◦ 驱动包位置：非必填，数据库驱动类所在的 jar 文件的绝对路径。
◦ 驱动包类库：非必填，支持从公共类类库中加载驱动包。如果同时设置了 “驱动包位置”，那么将一起生效，且 “驱动包位置” 比 “驱动包类库” 更优先加载。
◦ 连接属性：当驱动类型为 Driver 时，Driver 连接数据库所需要的连接参数。
“连接参数” 页签的 “连接属性” 中，password 属性加密存储。
关于数据源的更多参数说明，详见数据源参数配置说明。
6. 配置完成后，单击 “添加”，完成创建数据源操作。
若界面弹出 “数据源创建成功” 提示信息，则说明数据源创建成功。
在数据源列表中，您可以查看数据源名、绑定 JNDI 名、缓存语句、自动关闭语句、监视慢 SQL、支持JTA、已验证等信息。
新创建的数据源默认处于 “启用” 状态。若当前无使用需求，可执行 “停止” 操作来将该其停用，详见停用数据源。

# 3.1.4.2. 测试数据源
您可以测试从系统 JNDI 查找该数据源，进而获取数据库连接对象，对此连接对象进行有效性检查。
调用数据源 lookup 代码，如下所示。

# 方式一：
数据源：jdbc/testdb
```javascript
dataSouce = (DataSource)-initialContext.lookup("jdbc/testdb");
```

# 方式二：
1. 数据源：jdbc/testdb
```javascript
dataSource = (DataSource)-initialContext.lookup("java:comp/env/jdbc/testdb");
```
2. web.xml 配置：
```xml
<resource-ref> <description>jdbc/testdb</description> <res-ref-name>jdbc/testdb</res-ref-name> <res-type>javax.sql.DataSource</res-type> <res-auth>Container</res-auth> </resource-ref>
```

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建数据源。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源列表页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/4d332820335e70c613666867d7950c470f879be446030e7ac0d5c5362b445b90.jpg)
4. 单击目标数据源所在行的 “测试”，弹出确认测试窗口。
5. 单击 “确定”，完成数据源的测试操作。
若界面弹出 “数据源测试成功” 提示信息，则说明测试数据源成功。

# 3.1.4.3. 监视数据源
您可以通过监视数据源的方式，获取该数据源运行的状态，了解当前数据源的健康状态。
本章节介绍如何监视数据源。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建数据源。

# 查看监视视图
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源列表页面。
4. 单击目标数据源所在行的 “监视”，进入监视页面。
可查看数据源的实时 “连接池大小”、“空闲连接数”、“活跃连接数”、“报备连接数”、“验证中连接数”、“线程等待数”、“慢SQL数”、“语句缓存数” 和 “回收器工作中” 等，如下图所示。

# 注意：
◦ 左上角的 “testdb” 表示数据源的名称。
◦ 报备连接数：正在建立数据库连接的连接数。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ec2dd514c4f907c7a9316ca861c02929335010130e3e230628830cd24a197860.jpg)
5. 在监视视图中，您也可以查看 SQL 明细。
注：开启 “数据源” > “语句管理” 中的 “监视慢 SQL” 才会显示 SQL 明细。
包含 SQL 语句、慢执行次数、最长时间时间、最长执行时的日志、最短执行时间、最短执行时的时间、总执行时间、执行失败次数、总 prepare 次数以及总 prepare 时间等。

# 下载监视视图
1. 进入数据源列表页面。
2. 单击目标数据源所在行的 “监视”，进入监视视图页面。
3. 在监视视图页面，单击鼠标右键，可将监视视图另存为 “.png” 图片。

# 3.1.4.4. 管理数据源

# 查看数据源
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源列表页面。
4. 在数据源列表页面，您可以查看已创建的数据源。
包含数据源名、别名、缓存语句、自动关闭语句、监视慢 SQL、支持 JTA、运行中等信息。

# 停止数据源
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源列表页面。
4. 单击目标数据源所在行的 “停止”，弹出确认停止数据源窗口。
5. 单击 “确定”，即可完成数据源的停止操作。

# 启动数据源
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源列表页面。
4. 单击目标数据源所在行的 “启动”，弹出确认启动数据源窗口。
5. 单击 “确定”，即可完成数据源的启动操作。

# 编辑数据源
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源列表页面。
4. 单击目标数据源名，进入编辑数据源页面。
5. 您可以根据提示修改数据源信息。
注：数据源名不可编辑。
6. 编辑完成后，单击 “更新”，更新数据源配置信息。
若界面弹出 “数据源更新成功” 提示信息，则说明编辑数据源成功。

# 删除数据源
删除数据源时，数据源引用的其它组件不会被删除。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源列表页面。
4. 单击目标数据源所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个数据源，并单击列表上方的 “删除” 按钮，批量删除数据源。
5. 单击 “确定”，完成数据源的删除操作。
若界面弹出 “数据源删除成功” 提示信息，则说明删除数据源成功。

# 3.1.5. 数据源模板
数据源模板是一组预先设置的数据源配置参数，在创建数据源时选择使用数据源模板，可快捷地配置数据源的参数。数据源模板一般常用于多个数据源需要共享同一套配置参数的场景。

# 3.1.5.1. 创建数据源模板
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源模板”，进入数据源模板列表页面。
4. 单击 “创建”，进入创建数据源模板页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ac47d9f2fa2105388a39a9f30bc5a35b2b8482747da25e1bcb312b9fed27bd7c.jpg)
5. 配置数据源模板相关参数。
数据源模板名：必填项，数据源模板名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
关于数据源模板的更多参数说明，详见 数据源模板配置参数说明。
6. 单击 “添加”，完成数据源模板的创建操作。

# 3.1.5.2. 应用数据源模板
以已创建的 “test” 数据源模板为例说明。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源列表页面。
4. 单击 “创建” 或者已创建数据源的名称。
5. 配置数据库相关参数。
◦ 数据源模板：下拉列表中，选择已创建的数据源模板（例如：test）。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/130504f31cef6a4542c10444665d79a8ecac48b24d72e3749f7d9cb795e1c415.jpg)
◦ 其他参数：请根据实际需要进行配置。
6. 单击 “添加” 或者 “更新”，即可完成数据源的配置操作。

# 3.1.5.3. 管理数据源模板
您可以根据需要查看、编辑或者删除已添加的数据源模板。

# 查看数据源模板
1. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源模板”，进入数据源模板列表页面。
2. 可查看数据源模板名称、缓存语句、自动关闭语句、监视慢 SQL、支持 JTA 等信息。

# 编辑数据源模板
1. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源模板”，进入数据源模板列表页面。
2. 单击数据源模板的名称，进入数据源模板详细信息页面。
可对数据源模板的基础属性、连接参数、连接池、健康管理、语句管理以及事务等信息。
注：数据源模板的名称不可编辑。

# 删除数据源模板
删除数据源模板前请解除该模板的引用，否则该模板无法删除。
删除后不可用恢复，请谨慎操作。
1. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源模板”，进入数据源模板列表页面。
2. 单击目标数据源模板所在行的 “删除”，弹出确认删除数据源模板窗口。
注：用户可根据需要勾选一个或多个数据源模板，并单击列表上方的 “删除” 按钮，批量删除数据源模板。
3. 单击 “确定”，即可删除该数据源模板。

# 3.1.6. Jdbc 模板
支持为数据源添加新的 Jdbc 模板，方便数据库连接的建立。
您可以根据需要自定义 Jdbc 模板，在创建数据源时，使用自定义 Jdbc 模板。

# 3.1.6.1. 创建 Jdbc 模板
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “Jdbc 模板”，进入 Jdbc 模板列表页面。
4. 单击 “创建”，进入创建 Jdbc 模板页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f593768565bbef262fd61219c614b840c6422fbc5a9ac6ad020f4ac5bd0ba772.jpg)


# 5. 配置 Jdbc 模板相关参数。
◦ 模板名称：必填项，Jdbc 模板名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 驱动类：必填项，连接数据库的驱动类的全名称。
◦ 连接 URL：必填项，连接数据库的 JDBC URL。
关于 Jdbc 模板的更多参数说明，详见 Jdbc 模板配置参数说明。
6. 单击 “添加”，完成 Jdbc 模板的创建操作。

# 3.1.6.2. 应用 Jdbc 模板
以已创建的 “dbtest” Jdbc 模板为例说明。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源”，进入数据源列表页面。
4. 单击 “创建” 或者已创建数据源的名称。
5. 配置数据库相关参数。
◦ 数据库连接方式：下拉列表中，选择已创建的 Jdbc 模板（例如：dbtest）。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/3d5a0c25f7453d6a7d071c030c1f256afab9adaaedb947689e73aab364fee24d.jpg)
◦ 其他参数：请根据实际需要进行配置。
6. 单击 “添加” 或者 “更新”，即可完成数据源的配置操作。

# 3.1.6.3. 管理 Jdbc 模板
您可以根据需要查看、编辑或者删除已添加的 Jdbc 模板。

# 查看 Jdbc 模板
1. 在左侧导航栏中，选择 “Web 容器” $>$ “Jdbc 模板”，进入 Jdbc 模板列表页面。
2. 可查看 Jdbc 模板的模板名称、IPv4 版本、驱动类、连接 URL 等信息。

# 编辑 Jdbc 模板
1. 在左侧导航栏中，选择 “Web 容器” $>$ “Jdbc 模板”，进入 Jdbc 模板列表页面。
2. 单击 Jdbc 模板的名称，进入 Jdbc 模板详细信息页面。
可对 Jdbc 模板的 IPv4 版本、驱动类、连接 URL 进行修改。
注：Jdbc 模板的名称不可编辑。

# 删除 Jdbc 模板
删除 Jdbc 模板前请解除该 Jdbc 模板的引用。若 Jdbc 模板被引用，该 Jdbc 模板无法被删除。
删除后不可用恢复，请谨慎操作。
1. 在左侧导航栏中，选择 “Web 容器” $>$ “Jdbc 模板”，进入 Jdbc 模板列表页面。
2. 单击目标 Jdbc 模板所在行的 “删除”，弹出确认删除 Jdbc 模板窗口。
注：用户可根据需要勾选一个或多个 Jdbc 模板，并单击列表上方的 “删除” 按钮，批量删除 Jdbc 模板。
3. 单击 “确定”，即可删除该 Jdbc 模板。

# 3.1.7. 数据源集群
数据源集群是对外暴露的一个资源地址，内部管理多个真实的数据源资源，能根据所选策略实现数据源的故障转移，负载均衡等能力。

# 3.1.7.1. 创建数据源集群
本章节介绍如何创建数据源集群。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建数据源。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择“Web 容器”>“数据源集群”，进入数据源集群列表页面。
4. 单击 “创建”，进入创建数据源集群页面。
数据源集群／创建☆
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/312262f3bf403255bd3f732d75010617ba317173fb42288dd28e2db3cf880785.jpg)
5. 配置数据源集群的相关参数。
◦ 名称：必填项，数据源集群的名称。数据源集群名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 数据源列表：在数据源列表中若没有可选的数据源，请选择 “Web 容器” > “数据源”，在数据源页面中 创建数据源。
◦ 调度策略：必填项，默认为 “default”，可选择 “default”、“round-robin” 或者 “random”。
关于数据源集群的更多参数说明，详见数据源集群配置参数说明。
6. 配置完成后，单击 “添加”，完成创建数据源集群操作。
若界面弹出 “数据源集群添加成功” 提示信息，则说明数据源集群创建成功。
在数据源集群列表中，您可以查看数据源集群的名称、JNDI 名、数据源列表、调度策略等信息。

# 3.1.7.2. 测试数据源集群
您可以测试从系统 JNDI 查找该数据源，进而获取数据库连接对象，对此连接对象进行有效性检查。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建数据源集群。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源集群”，进入数据源集群列表页面。
4. 单击目标数据源集群所在行的 “测试”，弹出确认删除窗口。
5. 单击 “确定”，完成数据源集群的测试操作。
若界面弹出 “数据源集群测试成功” 提示信息，则说明测试数据源集群成功。

# 3.1.7.3. 管理数据源集群
用户可根据需要查看、编辑或者删除数据源集群。

# 查看数据源集群
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源集群”，进入数据源集群列表页面。
4. 在数据源集群列表页面，您可以查看已创建的数据源集群。
包含数据源集群名称、JNDI 名、数据源列表、调度策略等。

# 编辑数据源集群
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源集群”，进入数据源集群列表页面。
4. 单击目标数据源集群名称，进入编辑数据源集群页面。
5. 您可以根据提示修改数据源集群列表或者调度策略。
注：数据源集群名称不可编辑。
6. 编辑完成后，单击 “更新”，更新数据源集群配置信息。
若界面弹出 “数据源集群更新成功” 提示信息，则说明编辑数据源集群成功。

# 删除数据源集群
删除数据源集群时，数据源集群引用的其它组件不会被删除。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “数据源集群”，进入数据源集群列表页面。
4. 单击目标数据源集群所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个数据源集群，并单击列表上方的 “删除” 按钮，批量删除数据源集群。
5. 单击 “确定”，完成数据源集群的删除操作。
若界面弹出 “数据源集群删除成功” 提示信息，则说明删除数据源集群成功。

# 3.1.8. 安全域
安全域是服务器定义和强制执行通用安全策略的范围，是存储用户和组信息及其关联的安全凭证的系统信息库。
安全域是 TongWeb 服务器用来保护 Web 应用资源的一种机制。在安全域中可以配置安全验证信息，即用户信息（包括用户名和口令）以及用户和角色的映射关系。
每个用户可以拥有一个或多个角色，每个角色拥有不同的可以访问的Web资源。一个用户可以访问其拥有的所有角色对应的Web资源。
注意：
• 登录与权限由 web.xml 指定，安全域仅提供数据的来源。
• 虚拟主机上配置安全域表示虚拟主机上部署的所有的应用都使用此安全域。
• 应用上配置安全域，表示该应用使用应用上配置的安全域。
• 应用上配置的安全域优先级高于虚拟主机上的安全域。

# 3.1.8.1. 安全域类型
TongWeb 支持如下类型的安全域：
• FILE
从本地文件读取用户和角色。
◦ 安全域用户仅适用于 FILE 类型的安全域，示例说明请参见安全域&安全域用户示例说明。
◦ 支持安全域用户是客户端证书用户，示例说明请参见安全域用户（客户端证书用户）示例说明。
• DATA_SOURCE
通过指定的数据源，从数据源中读取用户和角色。
• LDAP
TongWeb 服务器从轻量目录访问协议（LDAP）服务器中获取用户凭证。
• JAAS
服务器从自定义的 LoginModule 中获取用户凭证，支持用户使用自定义的 LoginModule 灵活地进行安全域的验证。

# 3.1.8.2. 创建 FILE 类型安全域
本章节介绍创建 FILE 类型的安全域。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域”，进入安全域列表页面。
4. 单击 “创建”，创建安全域。
安全域／创建☆
*名称
失败锁定?
安全域类型
。 FILE
DATA SOURCE
LDAP
JAAS

# 5. 配置安全域相关参数。
◦ 名称：必填项，安全域的名称，需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 安全域类型：必填项，选择 “FILE”。
关于安全域的更多参数说明，详见安全域配置参数说明。
6. 配置完成后，单击 “添加”，完成 FILE 类型安全域的创建操作。
若界面弹出 “安全域添加成功” 提示信息，则安全域创建成功。
安全域创建成功后，在 “${tongweb.base}/conf/realms” 目录下会自动生成以安全域名称命名的 “.xml”文件，用于存放用户和角色信息。

# 3.1.8.3. 创建 DATA_SOURCE 类型安全域
本章节介绍如何创建 DATA_SOURCE 类型的安全域。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域”，进入安全域列表页面。
4. 单击 “创建”，创建安全域。

# 安全域
＊名称
security
失败锁定
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/76ee780c27515f21a95b73acb8a1b3a2dafe51b681783ed8979f1a42febf23a4.jpg)
安全域类型
O DATA SOURCE
LDAP
JAAS
*数据源名称
*用户表
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f4b04d85f638553738d262f9fce6fbcc8250c8392f11224263ea4c99ee31c011.jpg)
*用户名列
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/5f39f79e700fd592dd9e30931ef9fa8888ee12249b49d4d413f6b3c240f3cb9a.jpg)
＊用户密码列
*角色表
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d4b7b9dbc0fbde68dd8d580f53758f33096e4dce538402dba2075955c8268b21.jpg)
*角色名列?

# 5. 配置安全域相关参数。
◦ 名称：必填项，安全域的名称，需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 安全域类型：必填项，选择 “DATA_SOURCE”。
关于安全域的更多参数说明，详见安全域配置参数说明。
6. 配置完成后，单击 “添加”，完成 DATA_SOURCE 类型安全域的创建操作。
若界面弹出 “安全域添加成功” 提示信息，则安全域创建成功。

# 3.1.8.4. 创建 LDAP 类型安全域
本章节介绍如何创建 LDAP 类型的安全域。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域”，进入安全域列表页面。
4. 单击“创建”，创建安全域。

# 安全域
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c7417a8559e02f87aab3a329c340d543b61a3c9882e2d38301ea4bb9f15fe4a0.jpg)
＊名称
security
失败锁定?
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/8de21192d11b6298b587e0c96c1b1e980c6e02d8d0891f7ae1e40c90a3bc4d9d.jpg)
安全域类型
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/9c85306bc86fe70b1902b81f1878c6530c0b8cff611ff57ae8279838eef9142d.jpg)
ODATA SOURCE
LDAP
O JAAS
* LDAP服务器IPO
127.0.0.1
* LDAP服务器端口③
用户名
连接密码
*用户基本域
ou=people,dc=mycompany,dc=com
*用户属性的名称
uid
用户角色属性名称?
*角色基本域?
ou=groups,dc=mycompany,dc=com
*角色属性的名称③
cn
*角色对应用户属性?
unigueMember
5. 配置安全域相关参数。
◦ 名称：必填项，安全域的名称，需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 安全域类型：必填项，选择 “LDAP”。
关于安全域的更多参数说明，详见安全域配置参数说明。
6. 安全域配置完成后，单击 “添加”，完成安全域的创建操作。
若界面弹出 “安全域添加成功” 提示信息，则安全域创建成功。

# 3.1.8.5. 创建 JAAS 类型安全域
本章节介绍如何创建 JAAS 类型的安全域。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域”，进入安全域列表页面。
4. 单击 “创建”，创建安全域。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/cea7cb5989778fa14146c6426244aa9c2212f996f732587efdfd8d51697ce23c.jpg)


# 5. 配置安全域相关参数。
◦ 名称：必填项，安全域的名称，需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 安全域类型：必填项，选择 “JAAS”。
◦ LoginModule 实现类：指定应用程序使用的 JAAS 登录模块全类名，需要实现
javax.security.auth.spi.LoginModule 接口。
注：用户实现 javax.security.auth.spi.LoginModule 接口的 jar 包，需要在 TongWeb 启动前放置于“${tongweb.base}/lib” 目录下。
◦ 控制标志：可根据需要选择 “required”、“requisite”、“sufficient” 或者 “optional” 作为控制标志。
关于安全域的更多参数说明，详见安全域配置参数说明。
6. 安全域配置完成后，单击 “添加”，完成安全域的创建操作。
若界面弹出 “安全域添加成功” 提示信息，则安全域创建成功。

# 3.1.8.6. 管理安全域
用户可查看、编辑或删除已创建的安全域。

# 查看安全域
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域”，进入安全域列表页面。
4. 在安全域列表页面，您可以查看已创建的安全域。
包含安全域的名称、失败锁、安全域类型等。

# 编辑安全域
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域”，进入安全域列表页面。
4. 单击目标安全域的名称，进入编辑安全域页面。
5. 根据提示信息修改安全域相关参数。
注：安全域的名称不可编辑。
6. 编辑完成后，单击 “更新”，更新安全域配置信息。
若界面弹出 “安全域更新成功” 提示信息，则说明编辑安全域成功。

# 删除安全域
应用或者虚拟主机引用的安全域无法删除。若需要删除，请先取消与应用或者虚拟主机的关联。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域”，进入安全域列表页面。
4. 单击目标安全域所在行的 “删除”，弹出确认删除窗口。
注: 用户可根据需要勾选一个或多个安全域，并单击列表上方的 “删除” 按钮，批量删除安全域。
5. 单击 “确定”，完成安全域的删除操作。
若界面弹出 “安全域删除成功” 提示信息，则说明删除安全域成功。

# 3.1.9. 安全域用户
安全域用户仅适用于 FILE 类型的安全域。
注意：
用户信息的变更需要重新应用安全域，才能生效。

# 3.1.9.1. 创建安全域用户
用于管理安全域中的用户，此管理仅适用于 “FILE” 类型的安全域。

# 注意事项
用户信息变更后，需要将安全域重新应用到虚拟主机或者应用才会生效。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建 “安全域类型” 为 “FILE” 的安全域。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域用户”，进入安全域用户列表页面。
4. 单击 “创建”，创建安全域用户。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/6e84a9062800beaec4ca652701a072e0b446df3c04d2569c9f26a7bfe7b13f93.jpg)
5. 配置安全域用户的相关参数。
◦ 用户名：必填项，用户的登录名。
◦ 密码：必填项，用户的登录密码。
◦ 安全域：必填项，在下拉列表中，选择已创建的 “FILE” 类型安全域。
若没有创建安全域，可选择 “Web 容器” $>$ “安全域”，创建 FILE 类型安全域。关于安全域更多信息，详见创建 FILE 类型安全域。
关于安全域用户的更多参数说明，详见安全域用户配置参数说明。
6. 配置完成后，单击 “确定”，完成安全域用户的创建操作。
若界面弹出 “安全域用户创建成功” 提示信息，则说明安全域用户创建成功。
创建成功后，您可以进入 “${tongweb.base}/conf/realms/” 目录中，打开创建安全域生成的 “.xml” 文件，查看是否生成了创建的安全域用户。
如下以创建的 security 安全域为例说明，如下所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/6dba076b40ef83643d14cf9bb998d647c5beaaf4d87e10e25a762f5182de964e.jpg)


# 3.1.9.2. 管理安全域用户
用户可根据需要查看、编辑或者删除安全域用户。

# 查看安全域用户
在安全域用户列表中可查看已安全域用户的用户名、角色及对应的安全域。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域用户”，进入安全域用户列表页面。
4. 在安全域用户列表页面，您可以查看已创建的安全域用户。
包含安全域、用户名、角色等。

# 编辑安全域用户
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域用户”，进入安全域用户列表页面。
4. 单击目标安全域的名称，进入编辑安全域用户页面。
5. 您可以根据提示修改安全域用户所属的安全域、安全域用户的密码以及角色等信息。
注: 安全域用户名不可编辑。
6. 编辑完成后，单击 “更新”，更新安全域用户配置信息。
若界面弹出 “安全域用户更新成功” 提示信息，则说明编辑安全域成功。

# 删除安全域用户
若安全域已作用于应用，删除安全域用户后，该用户访问该应用的权限将被取消。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域用户”，进入安全域用户列表页面。
4. 单击目标安全域用户所在行的 “删除”，弹出确认删除窗口。
注: 用户可根据需要勾选一个或多个安全域用户，并单击列表上方的 “删除” 按钮，批量删除安全域用户。
5. 单击 “确定”，完成安全域用户的删除操作。
若界面弹出 “安全域用户删除成功” 提示信息，则说明删除安全域用户成功。

# 3.1.10. 安全域&安全域用户示例说明
应用已授权安全域角色（以 examples.war 为例，安全域角色 admin、role1）。

# 3.1.10.1. 步骤1：创建安全域
安全域名以 “realm_test” 为例。
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域”，进入安全域页面。
4. 单击 “创建”，进入安全域创建页面。
5. 输入安全域名称 “realm_test”。
6. 安全域类型选择 “FILE” 类型。
7. 单击 “添加”，完成安全域的创建。

# 3.1.10.2. 步骤2：创建安全域用户
安全域用户以如下信息为例说明。
• 第一个安全域用户 “realm_user”、角色 “role1”。
• 第二个安全域用户 “realm_admin”、角色 “admin”。
操作步骤，如下所示。
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域用户”，进入安全域用户页面。
4. 单击 “创建”，进入创建安全域用户页面。
5. 输入用户名 “realm_user” 和密码，角色为 “role1”。
6. 安全域选择步骤1创建的 “realm_test”。
7. 单击 “添加”，完成安全域用户 “realm_user” 的创建。
8. 请参照如上步骤，完成安全域用户 “realm_admin”，角色为 “admin” 的创建。

# 3.1.10.3. 步骤3：绑定安全域用户角色
为应用绑定特定的安全域用户的角色，如 web.xml 中作如下描述。
如下所示，将 <role-name> 指定为 步骤2 创建的安全域用户的角色（admin，role1）。
其它需要指定的参数请根据需要填写。
```txt
...
<security-constraint>
display-name>Example Security Constraint</display-name>
web-resource-collection>
web-resource-name>Protected Area</web-resource-name>
--指定需要保护的资源的url（相对于应用前缀）--
<url-pattern>/jsp/security/protected/*</url-pattern>
--指定需要保护的方法--
DELETE</http-method>
GET</http-method>
```
```html
<http-method>POST</http-method>
<http-method>PUT</http-method>
</web-resource-collection>
<auth-constraint>
    <!-- 指定能访问受保护资源的角色 -->
    <role-name>admin</role-name>
    <role-name>role1</role-name>
</auth-constraint>
</security-constraint>
<login-config>
    <!-- 验证类型，BASIC、FORM、DIGEST或CLIENT-CERT -->
    <auth-method>FORM</auth-method>
    <form-login-config>
        <form-login-page>/jsp/security/protected/login.jsp</form-login-page>
        <form-error-page>/jsp/security/protected-error.jsp</form-error-page>
    </form-login-config>
</login-config>
...
```

# 3.1.10.4. 步骤4：编写登录页面
“j_security_check”、“j_username”以及“j_password”为固定写法，请参照如下代码编写。
```txt
<html>
<head>
<title>Login Page for Examples</title>
<body bgcolor="white">
<form method="POST" action="/%=response.encodeURL("j_security_check") %>%">
<table border="0" cellspacing="5">
    <tr>
        <th align="right">Username:</th>
        <td align="left"><input type="text" name="j_username"></td>
    </tr>
    <tr>
        <th align="right">Password:</th>
        <td align="left"><input type="password" name="j_password"></td>
    </tr>
    <tr>
        <td align="right"><input type="submit" value="Log In"></td>
        <td align="left"><input type="reset"></td>
    </tr>
</table>
</form>
```
```txt
</body>  
</html>  
...
```

# 3.1.10.5. 步骤5：应用安全域
安全域及安全域用户创建完成后，可将安全域作用于单个应用或者作用于虚拟主机上的所有应用。安全域用户可以访问其拥有的角色对应的Web资源。

# 作用于单个应用
以部署 “${tongweb.home}/version.x.x.x.x/examples” 中的 “examples.war” 为例说明。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 单击“部署”，进入部署应用页面。

# 应用
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c1cc8b75d17aead96cbaa5437352ac01e1fdb16275b05cd12e1cf3ddd04eb927.jpg)
5. 在 “安全域” 下拉列表中，选择为已创建的安全域 “realm_test”。
6. 其他参数，请根据需要进行配置。
7. 配置完成后，单击 “添加”，完成安全域的应用。

# 作用于部署在虚拟主机上的所有应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “虚拟主机”，进入虚拟主机页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/1d9e912b25827b6b9e753886dc1654b0d6547c2ba68c54448cab7a56cdcb1a01.jpg)
4. 在 “默认安全域” 下拉列表下，选择已创建的安全域 “realm_test”。
5. 其他参数，请根据需要进行配置。
6. 配置完成后，单击 “添加”，完成安全域的应用。

# 3.1.10.6. 步骤6：使用安全域用户访问应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 单击已部署的 examples.war 应用所在行的“链接”，进入应用/链接页面。
5. 单击生成的链接，访问应用。
6. 单击 “Security Realm Examples”，访问安全域示例应用，进入登录页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f110c4d9c5e8d80868efdaba366a5d460bcd725297622199ff464b76be9ea70f.jpg)
7. 使用安全域用户 “realm_user” 或者 “realm_admin” 登录页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ceae40d84333297cbcfc2f905dc2ceac098c6903219a6a77b753d0643be0bdfe.jpg)


# 3.1.11. 安全域用户（客户端证书用户）示例说明
若应用设置了SSL客户端认证，则需要指定安全域用户为客户端证书用户。在应用进行权限验证时，应用获取客户端证书的角色，不需要登录直接访问应用。

# 3.1.11.1. 准备工作
如下数据为示例信息，请根据实际情况替换。
• 信任证书：server.p12 和 client.p12（私钥密码如：123456）
• 设置SSL客户端认证的应用： $\$ 1$ {tongweb.home}/version*/examples/examples.war

# 3.1.11.2. 步骤1：安装证书
1. 将 “server.p12” 放入 “${tongweb.base}/conf” 目录。
2. 将 “client.p12” 安装到浏览器客户端。
如下以 Google Chrome 105.0 浏览器为例说明。
a. 打开 Google Chrome 浏览器。
b. 单击 “设置”，进入设置页面。
c. 选择 “隐私设置和安全性” $>$ “安全” $>$ “管理设备证书”，弹出证书窗口。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/01b0f0ba52c609a2d4e14f7670d176fe44f865c65d90a0384bca802a32a58e49.jpg)
d. 单击 “导入”，进入证书导入向导页面。
e. 单击 “下一步”，进入要导入的文件页面。
f. 单击 “浏览”，选择 “client.p12” 导入证书。
g. 单击 “下一步”，进入私钥保护页面。
h. 在密码文本框中，输入密码，为私钥键入密码。

# 说明：
该密码为私钥密码（例如 “123456”）。
i. 单击 “下一步”，进入证书存储页面。
j. 单击 “下一步”，进入正在完成证书导入向导页面。
k. 单击 “完成”，完成证书导入。

# 3.1.11.3. 步骤2：通道开启 “SSL”
例如：使用的系统提供的 server 通道。
1. 进入 TongWeb 管理控制台。
2. 在左侧导航栏中，选择 “Web 容器” $>$ “通道”，进入通道页面。
3. 单击 “server”，进入 server 通道编辑页面。
4. 单击 “安全”，进入安全页签。
5. 打开 “开启 SSL” 开关，并配置客户端认证。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e273ebadeddecf7f2195a5def48cc74ffc1e8c8b675ef59ac1389fbfb9e4d61a.jpg)
◦ 证书路径：采用默认值。
◦ 私有库密码：配置为 “changeit”。
◦ 信任证书路径：conf/server.p12。
◦ 信任库密码：私钥密码（如 123456），请根据实际情况填写。
◦ 其他参数：采用默认值。

# 3.1.11.4. 步骤3：创建安全域
安全域名以 “demo” 为例。
1. 进入 TongWeb 管理控制台。
2. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域”，进入安全域页面。
3. 单击 “创建”，进入安全域创建页面。
4. 输入安全域名称 “demo”。
5. 安全域类型选择 “FILE” 类型。
6. 单击 “添加”，完成安全域的创建。

# 3.1.11.5. 步骤4：创建安全域用户
证书登录用户名以 “CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown,C=Unknown” 为例。
1. 进入 TongWeb 管理控制台。
2. 在左侧导航栏中，选择 “Web 容器” $>$ “安全域用户”，进入安全域用户页面。
3. 单击 “创建”，进入创建安全域用户页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e7ff6bdadeedf28efafc7a89c8c38bf05061e55ea744e2e5083a61cb203ea60b.jpg)
4. 开启 “是客户端证书用户”，并设置用户名、角色、安全域信息。
◦ 用户名：用户的登录名，以 “CN=Unknown, OU=Unknown, O=Unknown, L $\cdot ^ { = }$ Unknown,ST=Unknown, $\complement =$ Unknown” 为例。
◦ 角色：用户的角色，以 “tongweb” 为例。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/2c3483f037d46d19a387e5b6a48708c7babe48cf4290d019d5e9364c8d488bf1.jpg)
◦ 安全域：选择步骤3创建的安全域 “demo”。
5. 配置完成后，单击 “添加”，完成安全域用户的创建。

# 3.1.11.6. 步骤5：绑定安全域用户角色
请参照 绑定安全域用户角色 绑定安全域用户角色。
以 “${tongweb.home}/version*/examples” 路径下的 “examples.war” 为例。
在 “examples.war” 应用中，修改 “web.xml” 文件，如下所示。
• 将 <role-name> 修改为 步骤4 创建安全域用户时对应的角色。
• 将 “<auth-method>FORM</auth-method>” 的 “FORM” 修改为 “CLIENT-CERT”。
“web.xml” 文件修改后，如下所示。
```txt
...
<security-constraint>
display-name>Example Security Constraint</display-name>
web-resource-collection>
web-resource-name>Protected Area</web-resource-name>
--指定需要保护的资源的url（相对于应用前缀）--
<url-pattern>/jsp/security/protected/*</url-pattern>
--指定需要保护的方法--
<http-method>DELETE</http-method>
<http-method>GET</http-method>
<http-method>POST</http-method>
<http-method>PUT</http-method>
</web-resource-collection>
auth-constraint>
--指定能访问受保护资源的角色--
<role-name>tongweb</role-name>
</auth-constraint>
</security-constraint>
<login-config>
--验证类型，BASIC、FORM、DIGEST或CLIENT-CERT--
<auth-method>CLIENT-CERT</auth-method>
<form-login-config>
<form-login-page>/jsp/security/protected/login.jsp</form-login-page>
<form-error-page>/jsp/security/protected误差.jsp</form-error-page>
</form-login-config>
</login-config>
...
```

# 3.1.11.7. 步骤6：部署设置 SSL 客户端认证的应用
将 步骤5 修改后的 “examples.war” 应用重新打包并部署。
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用页面。
4. 单击 “部署”，进入部署应用页面。
5. 设置文件在服务器上的位置，其他参数配置采用默认值。
6. 单击 “添加”，完成应用的部署。

# 3.1.11.8. 步骤7：访问部署的应用
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用页面。
4. 单击已部署应用所在行的 “链接”，进入应用/链接页面。
5. 单击生成的链接，访问应用。
可以发现不需要登录应用，可直接访问应用。

# 3.2. EJB 容器
EJB 容器是 TongWeb 为用户提供的 EJB 运行的环境，负责 EJB Bean 实例的生命周期管理、Bean 实例状态管理、JTA 事务、EJB http 协议、EJB w3 协议等管理。

# 3.2.1. EJB 实例池管理
EJB 实例池管理包括无状态会话 Bean 实例池、有状态会话 Bean 实例缓存和消息驱动 Bean 实例池。

# 3.2.1.1. 无状态会话 Bean 实例池
无状态会话 bean 是一种企业 bean，通常是用于执行独立操作。无状态会话 bean 不具有任何关联的客户端的状态，但它可能会保持其实例的状态。
EJB 容器通常创建一个容器池和无状态的 bean 的对象，并使用这些对象来处理客户端的请求。由于有容器池，实例变量的值不能保证跨查找/方法调用同一个。
为应对大量用户的访问，TongWeb 提供了实例池（Pool）机制进行 Bean 实例管理，避免了 EJB 容器为用户的每次方法调用都进行实例的创建与销毁，保证了系统性能。

# 3.2.1.2. 有状态 EJB
有状态会话 bean 是一种企业 bean，它会保留与客户端的会话状态。有状态会话Bean会根据其名称在其实例变量中保持关联的客户端状态。EJB 容器创建一个单独的有状态会话 bean 来处理客户端的每个请求。一旦请求范围已经结束，就会销毁 statelful 会话 bean。
由于 EJB 容器不会为每个客户端分别维护相应的 Bean 实例，并重复使用这些 Bean 实例，因此实例池不适用于有状态的 EJB。对于有状态 EJB，EJB 容器提供了 EJB 缓存、钝化等机制来管理大量的 Bean 实例。

# 3.2.1.3. 消息驱动 Bean
为提高消息驱动 Bean 的响应性能，与无状态会话 Bean 一样，EJB 容器提供了实例池机制进行 Bean 实例管理。实例池的使用方法和配置与无状态会话 Bean 的相同。

# 3.2.2. EJB 配置管理

# 3.2.2.1. 无状态 EJB
1. 在左侧导航栏中，选择 “EJB 容器” > “无状态 EJB”，进入无状态 EJB 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/33ff87ab010365deb4fc51e6387edc5acecdaa943166beb3799f7c78052f9a82.jpg)
2. 配置无状态 EJB 的相关参数。
关于无状态 EJB 的更多参数说明，详见无状态 EJB 配置参数说明。
3. 配置完成后，单击 “更新”，完成无状态 EJB 的更新操作。
若界面弹出 “无状态 EJB 更新成功” 提示信息，则说明无状态 EJB 配置成功。
系统在 “系统管理” > “系统通知” 中通知配置成功消息。
EJB 的配置项发生变更后，重启 TongWeb 方可生效。
4. 重启 TongWeb 服务器，使配置生效。

# 3.2.2.2. 有状态 EJB
1. 在左侧导航栏中，选择 “EJB 容器” $>$ “有状态 EJB”，进入有状态 EJB 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c9dea70552273189bd8a2011f2c5d0d8cace4f9dc16ff90341263ef18f5ba0de.jpg)
2. 配置有状态 EJB 的相关参数。
会话服务器：非必填，有状态 EJB 支持会话高可用，用户可前往 “资源管理” > “会话服务器”，在会话服务器页面创建会话服务器。
关于有状态 EJB 的更多参数说明，详见有状态 EJB 配置参数说明。
3. 配置完成后，单击 “更新”，完成有状态 EJB 的更新操作。
若界面弹出 “有状态 EJB 更新成功” 提示信息，则说明有状态 EJB 更新成功。
系统在 “系统管理” > “系统通知” 中通知更新成功消息。
EJB 的配置项发生变更后，重启 TongWeb 方可生效。
4. 重启 TongWeb 服务器，使配置生效。

# 3.2.2.3. 单例 EJB
单例 EJB 主要是对 TongWeb 的 EJB 容器的单例会话 bean 属性进行设置。
1. 在左侧导航栏中，选择 “EJB 容器” > “单例 EJB”，进入单例 EJB 页面。
单例 EJB@／编辑☆
等待超时（秒）
30
更新
2. 配置单例 EJB 的相关参数。
关于单例 EJB 的更多参数说明，详见单例 EJB 配置参数说明。
3. 配置完成后，单击 “更新”，完成单例 EJB 的更新操作。
若界面弹出 “单例 EJB 更新成功” 提示信息，则说明单例EJB更新成功。
系统在 “系统管理” $>$ “系统通知” 中通知更新成功消息。
EJB 的配置项发生变更后，重启 TongWeb 方可生效。
4. 重启 TongWeb 服务器，使配置生效。

# 3.2.2.4. 消息驱动 Bean
为提高消息驱动 Bean 的响应性能，EJB 容器提供了实例池机制进行 Bean 实例管理。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “消息驱动 Bean”，进入消息驱动 Bean页面。
消息驱动 Bean@／编辑☆
使用实例池③
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c5abe3252f4bd1c11113e83be5a409ad0e1ae07d43acb5d2d6e0c2892dbb8c49.jpg)
等待超时（秒）
5

关闭超时时间
(分钟) 
5

实例数
10
4. 配置消息驱动 Bean 的相关参数。
关于消息驱动 Bean 的更多参数说明，详见消息驱动 Bean 配置参数说明。
5. 配置完成后，单击 “更新”，完成消息驱动 Bean 的更新操作。
若界面弹出 “消息驱动 Bean 更新成功” 提示信息，则说明消息驱动 Bean 更新成功。
系统在 “系统管理” > “系统通知” 中通知更新成功消息。
消息驱动 Bean 的配置项发生变更后，重启 TongWeb 方可生效。
6. 重启 TongWeb 服务器，使配置生效。

# 3.2.3. EJB 网络协议

# 3.2.3.1. EJB http 协议
在部署远程 EJB 容器时，可以选择 HTTP 协议或者 EJB w3 协议，相对于 w3 协议，使用 HTTP 协议处理EJB 请求，虽然性能稍微差一些，但使用简单，并且通过可以穿透防火墙。
对于 EJB 客户端，在使用 HTTP 协议时，其连接串（JNDI 的 java.naming.provider.url 参数）示例为“http://IP:8088/ejbserver/job”。
启用 EJB http 协议后，可通过除 “管理端口” 外的所有 HTTP 通道访问远程EJB容器。例如：系统提供的默认访问 web 应用的端口为 “8088”。

# 3.2.3.1.1. 调用方式说明
```java
Properties p = new Properties();  
p.put("java.naming.factory.initial", "com.tongweb.tongejb.client.Remotel.InitialContextFactory");  
p.put("java.naming.provider.url", "http://IP:8088/ejserver/ejb "); // IP是部署 ejb 的 TongWeb 服务器 IP 地址。  
Context c1 = new InitialContext(p);  
ManagerBeanRemote mbr = (ManagerBeanRemote)c1.lookup("ManagerBeanRemote");  
mbr)VrmoteCall()
```

# 3.2.3.1.2. 开启 EJB http 协议
1. 在左侧导航栏中，选择 “EJB 容器” > “EJB http 协议”，进入 EJB http 协议页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/98a2806f9b34edcc4a119226639db826f4cfa03d1b064e81d6f95a4ee88f5afa.jpg)
2. 打开 “EJB http 协议” 开关，并根据需要选择是否限定访问端口。
3. 配置完成后，单击 “更新”，完成 EJB http 协议的更新操作。
若界面弹出 “EJB http 协议更新成功” 提示信息，则说明 EJB http 协议更新成功。
系统在 “系统管理” $>$ “系统通知” 中通知更新成功消息。
EJB 的配置项发生变更后，重启 TongWeb 方可生效。
4. 重启 TongWeb 服务器，使配置生效。

# 3.2.3.1.3. 下载客户端运行依赖包
若远程客户端不在 TongWeb 上，运行客户端项目需要下载依赖包，并引入项目中。

# 注意事项
控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。

# 操作步骤
1. 在左侧导航栏中，选择 “EJB 容器” > “EJB http 协议”，进入 EJB http 协议页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d92b9f29edaeb425da62e75dd13e9b09554303831abde07a0e73f3bb8f93a04f.jpg)
2. 单击 “下载”，弹出下载文件窗口。
3. 勾选 “tongweb-ejb-client-all.jar”。
4. 单击 “确定”，即可下载依赖包。

# 3.2.3.2. EJB w3 协议
在部署 EJB 容器时，可选 HTTP 协议或者 EJB w3 协议，相比 HTTP 协议，使用 EJB w3 协议处理 EJB 请求通常可获得更好的性能。
对于 EJB 客户端，使用不同协议，其连接串（JNDI 的 java.naming.provider.url 参数）示例如下所示。
• HTTP 协议
```txt
http://IP:8088/ejbserver/ejb
```
• EJB w3 协议
```txt
w3://IP:5200
```

# 3.2.3.2.1. 注意事项
使用此协议请确保防火墙不会拦截该协议的端口。

# 3.2.3.2.2. 调用方式说明
若需要通过 JNDI 进行资源访问，必须设置初始化上下文的参数，主要是设置 JNDI 驱动的类
名(java.naming.factory.initial) 和提供命名服务的 URL (java.naming.provider.url)。
您可以通过控制台设置命名服务的URL，而 JNDI 驱动类名（java.naming.factory.initial）需要在代码里进行设置。
• 访问本地 JNDI 资源
默认的本地 InitialContext 所需的环境属性不需要设置。
若特殊使用场景下必须配置 java.naming.factory.initial 属性时，可以按如下方式配置，以访问本地 JNDI资源。
```txt
java.naming.factory.initial=com.tongweb.naming.java.javaURLContextFactory
```
• 访问远程 JNDI 资源
远程的 InitialContext 所需的环境属性配置，如下所示。

# 说明：
<IP> 需要修改为 TongWeb 所在的 IP，<port>为 EJB 远程调用端口，如下以 w3 协议的默认端口“5200” 为例。
http 协议默认为 “8088”。
w3 协议默认为 “5200”，默认未开启。
```javascript
props.setProperty("java.naming.factory.initial","com.tongweb.tongejb.client.RemotelInitialContextFactory");  
props.setProperty("java.naming.provider.url", "http://IP:port/ejbserver/ejb");
```
设置上下文环境属性的代码示例，如下所示。
```java
Properties p = new Properties();  
p.put("java.naming.factory.initial", "com.tongweb.tongejb.client.RemotelInitialContextFactory");  
p.put("java.naming.provider.url", "http://10.10.4.28:8088/ejbserver/ejb ");  
InitialContext ic = new InitialContext(p);
```

# 3.2.3.2.3. 配置 EJB w3 协议
若不需要处理 EJB 或者受限于防火墙不能开放对应的端口，则可以不用启用此 w3 协议。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” > “EJB w3 协议”，进入 EJB w3 协议基本属性页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/61b332c8b546673dfedcb2e1c1297e14419608ac1d33fec7e117c21c47fcbf0e.jpg)
4. 配置 EJB w3 协议的 “基本属性”、“连接配置” 以及 “线程” 相关参数。
关于 EJB w3 协议的更多参数说明，详见EJB w3 协议配置参数说明。
注：您可以根据需要调整线程池，以达到提高性能的作用，详见调整线程池。
5. 配置完成后，单击 “更新”，完成 EJB w3 协议的更新操作。
若界面弹出 “EJB w3 协议更新成功” 提示信息，则说明EJB w3协议更新成功。
系统在 “系统管理” $>$ “系统通知” 中通知更新成功消息。
EJB 的配置项发生变更后，重启 TongWeb 方可生效。
6. 重启 TongWeb 服务器，使配置生效。

# 3.2.3.2.4. 下载客户端运行依赖包
若远程客户端不在 TongWeb 上，运行客户端项目需要下载依赖包，并引入项目中。

# 注意事项
控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” > “EJB w3协议”，进入 EJB w3 协议基本属性页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/35939fb3c8e8b8154dfbb88a848e5f7adc55d215f3bb2ff43391209df348a8a8.jpg)
4. 单击 “下载”，弹出下载文件窗口。
5. 勾选 “tongweb-ejb-client-all.jar”。
6. 单击 “确定”，即可下载依赖包。

# 3.2.3.2.5. 监视 EJB w3 协议
您可以通过监视 EJB w3 协议的方式，获取该 EJB w3 协议运行的状态，了解当前 EJB w3 协议的健康状态。

# 前置条件
• 已获取系统管理员账号和密码。
• 已开启 EJB w3 协议。

# 查看监视视图
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” >“EJB w3 协议”，进入 EJB w3 协议页面。
4. 单击 EJB w3 协议页面的下方的“监视”，进入监视页面。
可查看 EJB w3 协议的实时 “活跃线程数” 和 “总线程数” 等，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ef9a07a6dcbd853919ed8d1bad70122c2dede97529213857a197ad25ce7fbb0c.jpg)


# 下载监视视图
1. 进入 EJB w3 协议页面。
2. 单击 “监视”，进入监视视图页面。
3. 在监视视图页面，单击鼠标右键，可将监视视图另存为 “.png” 图片。

# 3.2.3.2.6. 兼容 IIOP 协议
开启兼容 IIOP 协议后，即可支持使用 IIOP 协议连接 EJB 服务，例如：iiop://IP:5200。

# 前置条件
已 EJB w3 协议页面的 “基本属性” 页签中，启用 EJB w3 协议。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “EJB w3 协议”，进入 EJB w3 协议基本属性页面。
4. 单击 “其它”，进入 “其它” 页面。
5. 开启兼容 IIOP 协议开关，即可开启 IIOP 协议。
6. 单击 “更新”，完成 EJB w3 协议更新操作。
7. 重启 TongWeb 服务器，使配置生效。

# 3.2.4. EJB 使用场景

# 3.2.4.1. 本地 EJB 和远程 EJB
根据其服务范围，EJB 可分为本地 EJB 和远程 EJB 两种类型。
• 本地EJB：只能在同一个应用内部访问的 EJB 模块。
• 远程EJB：可以跨应用、跨进程和跨网络进行访问的 EJB 模块。
对于远程 EJB，访问需要首先设置其网络协议，TongWeb 支持 HTTP 、W3 两种协议，并兼容 IIOP 协议。
• HTTP 协议：可在 “EJB http 协议” 进行开启，通过 “通道” 模块进行管理。
• W3 协议：可在 “EJB w3 协议” 模块进行管理。
• IIOP 协议：在 “EJB w3 协议” 模块启用 W3 协议后，再进入对应的 “其它” 页签，即可开启 “兼容 IIOP协议”。

# 3.2.4.2. 部署 EJB
TongWeb 支持 EJB 模块的部署，EJB 模块可打包在 .jar , .ear , .war 三种标准应用文件中，部署到 TongWeb服务器上。

# 3.2.4.3. 访问 EJB
访问 EJB 的第一步是要获得其所在 JNDI 的上下文 Context 对象。
• 本地 EJB：只需 new InitialContext() 即可。
• 远程 EJB：需要填写必要的远程信息。

# 注意：
若远程客户端不在 TongWeb 上，则需要在 TongWeb 控制台，进入 “EJB 容器” 模块，下载“tongweb-ejb-client-all.jar”，并引入到项目中。
示例说明，如下所示。

#可选，客户端连接池大小，默认值50，使用W3协议时会影响线程池活跃线程数，建议设置不超过EJB专用协议最大线程数
System.setProperty("tongejb.client.connection.pool.size", "50");

#客户端连接超时时间
System.setProperty("tongejb.client.connection.socket.timeout", "10000");

#客户端连接超时时间
System.setProperty("tongejb.client.connection.socket.read", "10000");

#客户端连接池等待超时时间
System.setProperty("tongejb.client.connection.pool.timeout", "10000");

#可选 PING_PING/PING_PONG，设置客户端socket连接处理方式，默认值 PING_PING,
当连接失效时不去重新创建连接；PING_PING当连接失效时，清空socket连接并创建新的连接
System.setProperty("tongejb.client.keepalive","PING_PING");

#设置连接程序，注：该程序位于 tongweb-ejb-client.jar内，需首先将该jar及其依赖jar放入客户端程序的类路径中
```txt
Properties p = new Properties();  
#固定参数值，不可更改  
p.put("java.naming.factory.initial","com.tongweb.tongejb.client.RemotelInitialContextFactory");  
#使用HTTP协议，与W3协议二选一，以根据服务器开放的服务为准  
p.put("java.naming.provider.url","http://IP:8088/ejbserver/ejb");  
#使用HTTPS协议，服务器通道需要开启SSL  
p.put("java.naming.provider.url","https://IP:8088/ejbserver/ejb");  
p.put("sslTrustStore","证书绝对路径");  
p.put("sslTrustStoreType","证书类型");  
p.put("sslTrustStorePassword","密码");  
#服务器通道SSL开启双向认证后需要添加  
p.put("sslKeyStore","证书绝对路径");  
p.put("sslKeyStoreType","证书类型");  
p.put("sslKeyStorePassword","密码");  
#使用W3协议，与HTTP协议二选一，以根据服务器开放的服务为准  
p.put("java.naming.provider.url","w3://IP:5200");  
#查找远程ejb的JNDI名，该JNDI名通常是EJB模块的mappedName，可选择添加JavaEE环境参数java:comp/env/，如ejbContext.lookup("java:comp/env/ManagerBeanRemote")  
Context ejbContext = new InitialContext(p);  
ManagerBeanRemote mbr = (ManagerBeanRemote)ejbContext.lookup("ManagerBeanRemote")  
#调用远程ejb的业务方法  
mbr)VrmCall();
```

# 3.2.4.4. 访问 EJB 集群
EJB 集群可用于支持故障转移需求，保障 EJB 服务的高可用。具体的故障转移策略包括：粘性、轮流、随机。
访问 EJB 集群与访问 EJB 唯一的区别在于: java.naming.provider.url 参数。
格式为: [strategy:]urlList

# 说明：
strategy 和 urlList 是变量。
• strategy：取值为 ”sticky“（亲和）、”round-robin“（轮转）、”random“（随机），此参数是可选的，默认是 ”sticky“。
• urlList：以英文逗号分隔的连接 URI 列表。

# 3.2.4.4.1. 配置说明
• 若 EJB Server 只有两个节点，使用如下配置方式，操作更加方便。
```javascript
("java.naming.provider.url","random:w3://IP1:5200,w3://IP2:5200");
```
• 若 EJB Server 存在多个节点，且后期可能会发生变化，则使用 THS $^ +$ TongWeb 集群方式。
当增减节点时，”java.naming.provider.url“ 值不变。

# 注意：
◦ 配置 THS 的 TCP 方式集群可实现 EJB W3、IIOP 集群。
◦ 配置 THS 的 http 集群可实现 EJB http 集群。
关于如何配置 THS 的 TCP 方式集群和 http 集群，可参见《TongHttpServer_V6.0用户手册》。

# 3.2.4.4.2. 配置示例
示例说明，如下所示。
```java
Properties p = new Properties();  
//使用HTTP协议的集群配置方式  
p.put("java.naming.provider.url", "sticky: http://IP:8088/ejbserver/ejb, http://IP2:8088/ejbserver/ejb");  
//使用HTTPS协议的集群配置方式  
p.put("java.naming.provider.url", "sticky: https://IP:8088/ejbserver/ejb, https://IP2:8088/ejbserver/ejb");  
p.put("sslTrustStore", "/usr/server.keystore");  
p.put("sslTrustStoreType", "JKS");  
p.put("sslTrustStorePassword", "12345678");  
#服务器通道SSL开启双向认证后需要添加  
p.put("sslKeyStoreType", "/usr/server.keystore");  
p.put("sslKeyStoreType", "JKS");  
p.put("sslKeyStorePassword", "12345678");  
//使用W3协议的集群配置方式  
p.put("java.naming.provider.url", "random:w3://IP:5200,w3://IP2:5200");  
...
```

# 3.2.5. JTA 事务
JTA（Java Transaction API）为 Java EE 平台提供了分布式事务服务，通过 JTA 可以使不同的资源（如非XA 事务分支）加入同一个 JTA 事务中。TongWeb 的全局事务是基于 JTA、XA 协议以及 EJB 远程调用协议而扩展出的跨应用服务器的事务服务。此全局事务的事务管理器仍然是一个 JTA 事务管理器，而加入JTA 事务中的资源不再局限于 XA 资源，还包括了远端应用服务器上部署的 EJB 资源。全局事务可以使得在一个 JTA 事务中调用到的某远端应用服务器上的 EJB 也将加入到这个 JTA 事务中，同样地，如果该 EJB 还调用了其他远端应用服务器上的 EJB，那么这些 EJB 也会加入到这个 JTA 事务中。

# 3.2.5.1. JTA 事务场景描述
全局事务的场景涉及多个 TongWeb。假设有 4 个 TongWeb，名称分别为 TW1、TW2、TW3、TW4；每个 TongWeb 上都部署了一个 EJB，名称分别为 EJB1、EJB2、EJB3、EJB4；每个 EJB 都使用了一个数据源，名称分别为 DS1、DS2、DS3、DS4；此外，EJB1 依次调用了 EJB2、EJB3，EJB3 又调用了 EJB4；以上场景即是一个典型的全局事务场景。在这种场景下 4 个数据源 DS1、DS2、DS3 和 DS4 将加入到同一个事务中，统一提交或回滚。
全局事务是在 JTA 事务的基础之上进行的功能增强，使得 JTA 事务可跨越 TongWeb 节点进行传播，可应用于更广泛的分布式场景下的事务实施，其具体特性介绍如下所示。

# 1. 跨 TongWeb 节点的事务传播
从一个 TongWeb 节点上的 EJB 事务方法通过 EJB 远程调用进入另一个 TongWeb 节点上的 EJB 事务方法，那么在第一个 TongWeb 节点上未提交的临时状态数据则对第二个 TongWeb 节点上 EJB 事务方法可见，同理该事务可以继续传播到更远的 TongWeb 节点上。

# 2. 全局事务的事务性保证
根据上述 “跨 TongWeb 节点的事务传播”，如果其中任何一个 TongWeb 节点上的 EJB 事务方法发生异常，则所有参与的 TongWeb 节点上的临时状态数据全部回滚，即保证数据的原子性，同时保证数据的一致性、持久性、隔离性等事务特性。

# 3. 全局事务的容错性
全局事务的容错性是指当 TongWeb 节点在事务处理过程中发生宕机，事务可以通过记录的事务日志得以恢复，而不破坏数据一致性，同时也支持 EJB 集群下部分节点宕机的事务容错性。

# 3.2.5.2. JTA 事务传播策略
TongWeb 的全局事务传播策略完全遵循 EJB 规范中定义的 3 种事务传播策略，即 MANDATORY,REQUIRED, SUPPORTS。

# 3.2.5.3. 配置 JTA 事务
1. 在左侧导航栏中，选择 “EJB 容器” > “JTA 事务”，进入 JTA 事务页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/74de9bb515a5391d86fcc51cf666b6598fb9c6fcc3f12d786d1f6de30fe8e966.jpg)
2. 配置 JTA 事务的相关参数。
关于 JTA 事务的更多参数说明，详见 JTA 事务配置参数说明。
3. 配置完成后，单击 “更新”，完成 JTA 事务的更新操作。
若界面弹出 “JTA 事务更新成功” 提示信息，则说明 JTA 事务更新成功。

# 3.2.5.4. 查看 JTA 事务监视
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “JTA 事务”，进入 JTA 事务页面。
4. 单击 “监视”，进入 JTA 事务监视页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/895ca2104ab37c15b4227b6f83016ec2ee96fe5cd7f7d3f725c8de73cc5c4641.jpg)
5. 可查看 JTA 事务的提交事务数、回滚事务数以及活跃事务数。

# 3.2.6. JCA 服务
JCA（Java Connector Architecture）提供了一个应用服务器和企业信息系统（EIS）连接的标准 Java 解决方案，以及把这些系统整合起来的方法。JCA 简化了异构系统的集成，用户只要构造一个基于 JCA 规范的连接器应用，并将该连接器应用部署到 Java EE 服务器上，不用编写任何代码就能实现 EIS 与 Java EE 应用服务器的集成。
TongWeb 中的 JCA 架构实现了 JCA1.7 规范，同时提供 Connector 连接池、托管对象资源。

# 3.2.6.1. JCA 连接池
通过构造一个基于 JCA 规范的 Connector 应用，并将其部署到 TongWeb，来实现 EIS 与 TongWeb 的集成。
JCA 连接池是一组用于特定 EIS 的可重复使用的连接。

# 3.2.6.1.1. 创建 JCA 连接池
本章节介绍如何创建 JCA 连接池。

# 前置条件
• 已获取系统管理员账号和密码。
• 已在 TongWeb 管理控制台部署 “*.rar” 类型的 Connector 应用。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “JCA 连接池”，进入 JCA 连接池列表页面。
4. 单击 “创建”，进入创建 JCA 连接池页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/0071a765cdf93b8f52e72a23f219ff31c57b024eb3a15dcc234daa71ae53d216.jpg)


# 5. 配置 JCA 连接池的相关参数。
◦ 连接池名称：必填项，JCA 连接池名称，需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 资源适配器：必填项，在下拉列表中，选择资源适配器。用于与外部企业信息系统连接。
◦ 连接定义：必填项，连接池的连接接口定义，在下拉列表中，选择连接定义。
◦ 其他属性：非必填，password 属性加密存储。
关于 JCA 连接池的更多参数说明，详见 JCA 连接池配置参数说明。
6. 配置完成后，单击 “添加”，完成创建JCA连接池操作。
若界面弹出 “JCA 连接池添加成功” 提示信息，则说明 JCA 连接池创建成功。
在 JCA 连接池列表中，您可以查看 JCA 连接池名称、JNDI 名、资源适配器、连接定义等信息。

# 3.2.6.1.2. 监视 JCA 连接池
您可以通过监视 JCA 连接池的方式，获取该 JCA 连接池运行的状态，了解当前 JCA 连接池的健康状态。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建 JCA 连接池。

# 查看监视视图
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “JCA 连接池”，进入 JCA 连接池列表页面。
4. 单击目标JCA连接池所在行的 “监视”，进入监视页面。
可查看线程池的实时 “活跃连接数” 和 “总连接数” 等，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/60a20688c92b5f7279ac2798ff8bfc4c1d33d0a0884a4679e61968899625de72.jpg)


# 下载监视视图
1. 进入 JCA 连接池列表页面。
2. 单击目标 JCA 连接池所在行的 “监视”，进入监视视图页面。
3. 在监视视图页面，单击鼠标右键，可将监视视图另存为 “.png” 图片。

# 3.2.6.1.3. 管理 JCA 连接池
用户可查看、编辑或删除创建的 JCA 连接池。

# 查看 JCA 连接池
1. 在左侧导航栏中，选择 “EJB 容器” $>$ “JCA 连接池”，进入 JCA 连接池列表页面。
2. 在 JCA 连接池列表页面，您可以查看已创建的 JCA 连接池。
包含 JCA 连接池名称、JNDI 名、资源适配器、连接定义等信息。

# 编辑 JCA 连接池
1. 在左侧导航栏中，选择 “EJB 容器” $>$ “JCA 连接池”，进入 JCA 连接池列表页面。
2. 单击目标 JCA 连接池名称，进入编辑 JCA 连接池页面。
3. 您可以根据提示修改 JCA 连接池信息。
注：JCA 连接池名称不可编辑。
4. 编辑完成后，单击 “更新”，更新 JCA 连接池配置信息。
若界面弹出 “JCA 连接池更新成功” 提示信息，则说明编辑 JCA 连接池成功。

# 删除 JCA 连接池
删除 JCA 连接池时，JCA 连接池引用的其它组件不会被删除。
1. 在左侧导航栏中，选择 “EJB 容器” $>$ “JCA 连接池”，进入 JCA 连接池列表页面。
2. 单击目标 JCA 连接池所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个 JCA 连接池，并单击列表上方的 “删除” 按钮，批量删除 JCA 连接池。
3. 单击 “确定”，完成 JCA 连接池的删除操作。
若界面弹出 “JCA 连接池删除成功” 提示信息，则说明删除 JCA 连接池成功。

# 3.2.6.2. JCA 托管对象
JCA 托管对象主要是封装了连接器应用中的托管对象（ra.xml 中定义的 adminobject）。

# 3.2.6.2.1. 创建 JCA 托管对象
本章节介绍如何 JCA 托管对象。

# 前置条件
• 已获取系统管理员账号和密码。
• 已部署 “*.rar” 类型的 Connector 应用（以部署 “${tongweb.home}/version*/examples” 路径下的“tmqjmsra.rar” 为例）。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “JCA 托管对象”，进入 JCA 托管对象列表页面。
4. 单击 “创建”，进入创建 JCA 托管对象页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/eb23159b6ef4feef61daacd0b6c388442dad00b56b0371f19f3630ee682a5abf.jpg)
5. 配置 JCA 托管对象的相关参数。
◦ 托管对象名称：必填项，托管对象的名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 资源适配器：必填项，在下拉列表中，选择资源适配器。用于与外部企业信息系统连接。
◦ 资源类型：必填项，在下拉列表中，选择资源类型。
◦ 其他属性：password 属性加密存储。
关于 JCA 托管对象的更多参数说明，详见 JCA 托管对象配置参数说明。
6. 配置完成后，单击 “添加”，完成创建 JCA 托管对象操作。
若界面弹出 “JCA 托管对象添加成功”提示信息，则说明 JCA 托管对象创建成功。
在 JCA 托管对象列表中，您可以查看 JCA 托管对象的名称、资源适配器、资源类型等信息。

# 3.2.6.2.2. 管理 JCA 托管对象
用户可查看、编辑、删除已创建的 JCA 托管对象。

# 查看 JCA 托管对象
1. 在左侧导航栏中，选择 “EJB 容器” $>$ “JCA 托管对象”，进入 JCA 托管对象列表页面。
2. 在 JCA 托管对象列表页面，您可以查看已创建的 JCA 托管对象。
包含 JCA 托管对象名称、JNDI 名、资源适配器、资源类型等信息。

# 编辑 JCA 托管对象
1. 在左侧导航栏中，选择 “EJB 容器” $>$ “JCA 托管对象”，进入 JCA 托管对象列表页面。
2. 单击目标 JCA 托管对象名称，进入编辑 JCA 托管对象页面。
3. 您可以根据提示修改 JCA 托管对象信息。
注：JCA 托管对象名称不可编辑。
4. 编辑完成后，单击 “更新”，更新 JCA 托管对象配置信息。
若界面弹出 “JCA 托管对象更新成功” 提示信息，则说明编辑 JCA 托管对象成功。

# 删除 JCA 托管对象
删除 JCA 托管对象时，JCA 托管对象引用的其它组件不会被删除。
1. 在左侧导航栏中，选择 “EJB 容器” $>$ “JCA 托管对象”，进入 JCA 托管对象列表页面。
2. 单击目标 JCA 托管对象所在行的 “删除”，弹出确认删除窗口。
注: 用户可根据需要勾选一个或多个 JCA 托管对象，并单击列表上方的 “删除” 按钮，批量删除 JCA 托管对象。
3. 单击 “确定”，完成 JCA 托管对象的删除操作。
若界面弹出 “JCA 托管对象删除成功” 提示信息，则说明删除 JCA 托管对象成功。

# 3.2.6.3. JCA 连接池& JCA 托管对象（使用示例）
以部署 “${tongweb.home}\version*\examples” 路径下的 “tmqjmsra.rar” 为例。

# 步骤1：创建并启动消息服务器实例
关于创建并启动消息服务器实例，请参见创建并启动消息服务器实例。

# 步骤2：创建 JCA 连接池&托管对象
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 部署消息服务器的适配器应用（tmqjmsra.rar）。
4. 创建JCA连接池，名称为 “testc”，连接定义选择 “javax.jms.ConnectionFactory”；
5. 创建JCA托管对象,名称为 “testd”，资源类型选择 “javax.jms.Queue”；
6. 创建JCA托管对象，名称为 “testa”，资源类型选择 “javax.jms.Topic”。

# 步骤3：部署并访问应用
1. 部署 jmsExample.war 应用。
应用路径： $\$ 1$ {tongweb.home}\version*\examples
2. 访问 jmsExample.war 应用。
单击 "/MessageSend"。
若输出 "testc: OK! testd: OK! send message …… send message successfully !" 代表验证成功。
单击其它三个链接，输出类似的信息代表验证成功。

# 3.2.7. JavaMail 资源
通过创建 JavaMail 资源，TongWeb 会创建 JavaMail 会话，并将 JavaMail 资源中设置的属性传递给JavaMail 会话。使用 JavaMail 会话应用即可进行收发邮件、回复邮件、转发邮件等操作。

# 3.2.7.1. 创建 JavaMail 资源
本章节介绍如何 JavaMail 资源。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “JavaMail 资源”，进入 JavaMail 资源列表页面。
4. 单击 “创建”，进入创建 JavaMail 资源页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/986f7bcd3545a9038d2af0faad581847b00c08804c89acc9be4abf6ed36c7609.jpg)
5. 配置 JavaMail 资源相关参数。
◦ 名称：必填项，JavaMail 名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 邮件服务器地址：必填项，默认为 “smtp.163.com”。
◦ 发件邮箱：必填项，默认的邮件发送者的邮箱地址。
◦ 登录用户名：必填项，连接邮件服务器时，使用的默认用户名。
◦ 登录密码：必填项，连接邮件服务器时，使用的默认密码。
关于 JavaMail 资源的更多参数说明，详见JavaMail 资源配置参数说明。
6. 配置完成后，单击 “添加”，完成创建 JavaMail 资源操作。
若界面弹出 “JavaMail 资源添加成功” 提示信息，则说明 JavaMail 资源创建成功。
在 JavaMail 资源列表中，您可以查看 JavaMail 资源的名称、JNDI 名、邮件服务器地址、邮件服务器端口、发件邮箱等信息。

# 3.2.7.2. 应用 JavaMail 资源

# • 预警策略应用 JavaMail 资源
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “预警策略”，进入预警策略页面。
4. 单击 “创建”，创建预警策略，或者编辑已有预警策略，进入编辑预警策略页面。
5. 单击 “处理办法”，开启 “发送邮件”。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/29e37d85d277429fceb4d34c19bb9b1a05760dd36c82613c3cdf026559a610c6.jpg)
6. 其他参数，请根据需要配置。
7. 单击 “添加”，完成 JavaMail 资源的配置操作。

# • 授权到期提醒应用 JavaMail 资源
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “基础配置” $>$ “全局配置” $>$ “授权”，进入全局配置的“授权”页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/17bcb64eeab668cd007cd4c07344613fedb023a3ad55e0aa387586b2fb40da87.jpg)
4. 根据需要设置邮件发送方式。
5. 配置完成后，单击 “更新”，完成授权到期时间提醒的邮件通知配置操作。

# 3.2.7.3. 管理 JavaMail 资源
用户可查看、编辑、删除已创建的 JavaMail 资源。

# 查看 JavaMail 资源
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “JavaMail 资源”，进入 JavaMail 资源列表页面。
4. 在 JavaMail 资源列表页面，您可以查看已创建的 JavaMail 资源。
包含 JavaMail 资源的名称、邮件服务器地址、邮件服务器端口、会话邮箱等信息。

# 编辑 JavaMail 资源
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “JavaMail 资源”，进入 JavaMail 资源列表页面。
4. 单击目标 JavaMail 资源名称，进入编辑 JavaMail 资源页面。
5. 您可以根据提示修改 JavaMail 资源信息。
注：JavaMail 资源名称不可编辑。
6. 编辑完成后，单击 “更新”，更新 JavaMail 资源配置信息。
若界面弹出 “JavaMail 资源更新成功” 提示信息，则说明编辑 JavaMail 资源成功。

# 删除 JavaMail 资源
删除 JavaMail 资源时，JavaMail 资源引用的其它组件不会被删除。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “JavaMail 资源”，进入 JavaMail 资源列表页面。
4. 单击目标 JavaMail 资源所在行的 “删除”，弹出确认删除窗口。

# 说明：
用户可根据需要勾选一个或多个 JavaMail 资源，并单击列表上方的 “删除” 按钮，批量删除 JavaMail 资源。
5. 单击 “确定”，完成 JavaMail 资源的删除操作。
若界面弹出 “JavaMail 资源删除成功” 提示信息，则说明删除 JavaMail 资源成功。

# 3.2.8. 工作管理器
工作管理器（commonj.work.WorkManager接口）是 JSR 237 定义的，用于在 Java EE 应用中并发编程的API，通常被称为 CommonJ。
通过工作管理器，可以并发编写在 Java EE 应用中的 EJB 和 Servlet 程序。

# 3.2.8.1. 创建工作管理器
本章节介绍如何创建工作管理器。

# 前置条件
已创建线程池（用于工作管理器的线程池）。
关于如何创建线程池，详见创建线程池。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “工作管理器”，进入工作管理器列表页面。
4. 单击 “创建”，进入创建工作管理器页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e40ffd7611cdcabc1acb65d468a1669e4f9449e663684406bc1e52b06ab476b4.jpg)
5. 配置工作管理器的相关参数。
◦ 名称：必填项，标识工作管理器唯一实例，同时也是绑定 JNDI 资源的名称，以 “work” 为例说明。工作管理器名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 工作管理器线程池：选择已创建并用于工作管理器的线程池。
关于工作管理器相关参数的详细说明，请参见工作管理器配置参数说明。
6. 配置完成后，单击 “添加”，完成工作管理器的添加操作。
7. 在左侧导航栏中，选择 “诊断管理” $>$ “JNDI 树”，进入 JNDI 树页面。
8. 可查看已添加的工作管理器。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/8554050367fd88f75d1dc5ec12226b5ab62792f4a0e1e6b01edec51159e0d132.jpg)


# 3.2.8.2. 使用工作管理器
以 Web 应用为例，说明应用如何通过资源引用来使用工作管理器实例。
1. 在 web.xml 中配置如下代码。
```xml
<resource-ref> <res-ref-name>wm/FooWorkManager</res-ref-name> <res-type>commonj.work.WorkManager</res-type> <res-auth>Container</res-auth> <res-sharing-scope>Shareable</res-sharing-scope> </resource-ref>
```
2. 根据 JNDI 名进行查找。
```javascript
Context ctx = new InitialContext();  
wm = (WorkManager) ctx.lookup("/java:/comp/env/WM/FooWorkManager");
```
3. 运用 commonj API 调度任务执行。

# 3.2.8.3. 管理工作管理器
您可以根据需要查看、编辑或者删除已添加的工作管理器。

# 查看工作管理器
1. 在左侧导航栏中，选择“EJB 容器”>“工作管理器”，进入工作管理器列表页面。
2. 在工作管理器列表页面，可查看工作管理器的名称、JNDI 名等信息。

# 编辑工作管理器
1. 在左侧导航栏中，选择 “EJB 容器” $>$ “工作管理器”，进入工作管理器列表页面。
2. 单击目标工作管理器的名称链接，进入工作管理器详细信息页面。
3. 您可根据需要修改工作管理器线程池。
注：工作管理器的名称不可编辑。

# 删除工作管理器
删除后，在 JNDI 树上不再显示相应的工作管理器资源。
1. 在左侧导航栏中，选择 “EJB 容器” $>$ “工作管理器”，进入工作管理器列表页面。
2. 单击目标工作管理器所在行的 “删除”，弹出确认删除工作管理器窗口。
注：用户可根据需要勾选一个或多个工作管理器，并单击列表上方的 “删除” 按钮，批量删除工作管理器。
3. 单击 “确定”，即可删除工作管理器。

# 3.3. 其它容器

# 3.3.1. OSGi 容器
OSGI（Open Service Gateway Initiative），即开放服务网关协议，是由 OSGI Alliance 组织制定的 Java 模块化规范。TongWeb 提供了 OSGi R7 规范的实现。
开启该功能后，TongWeb 将运行一个 OSGi 容器，用以部署 OSGi Bundle。
bundle 是以 jar 包形式存在的一个模块化物理单元，里面包含了代码、资源文件和元数据(metadata)，并且 jar 包的物理边界也同时是运行时逻辑模块的封装边界。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/836dded5d1fb4f469543925c1d36dba661993c8592e3bf15faea8b6bd8f11fd2.jpg)


# 3.3.1.1. 开启 OSGi 服务
开启 OSGi 服务后，才能部署 OSGi Bundle。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “OSGi 服务”，进入 OSGi 服务页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/94c1d0b7338f9ffcb7ecfec619d5c51454b6d301e0dab4677927e22a7fcc3935.jpg)
4. 打开 “启用” 开关，即可开启 OSGi 服务。
OSGi 部署目录默认为 “deployment-osgi”。
5. 单击 “更新”，开启 OSGi 服务成功。
若界面弹出 “OSGi 服务更新成功” 提示信息，则说明更新 OSGi 服务成功。

# 3.3.1.2. 部署 OSGi 应用
用户可根据需要自动部署 OSGi 应用或者手动上传 OSGi 应用。

# 前置条件
• 已获取系统管理员账号和密码。
• 已开启 OSGi 服务。

# 自动部署

# 1. 开启自动部署
a. 登录 TongWeb 管理控制台。
b. 切换到目标实例。
c. 在左侧导航栏中，选择 “其它容器” $>$ “OSGi 服务”，进入 OSGi 服务页面。
d. 打开 “自动部署” 开关。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/351e7e905bd0c7ecd9b90d0f13cb780443e4ff22ff8fa11a625c0c0ac991c7cd.jpg)
e. 用户可根据需要设置自动部署周期。
默认为 “2” 秒，表示系统每隔 2 秒扫描一次部署目录，自动检查是否有新的文件、更新的文件或删除的文件，以进行对应 Bundle 的部署、更新或卸载。
f. 设置完成后，单击 “更新”，完成自动部署功能的开启操作。
若界面弹出 “OSGi 服务更新成功” 提示信息，则说明更新 OSGi 服务成功。

# 2. 部署 OSGi 应用
部署的应用以 “${tongweb.home}/version*/examples/test-osgi.jar” 为例说明。
a. 复制 “${tongweb.home}/version*/examples/test-osgi.jar” 文件。
b. 并将复制的文件粘贴到 OSGi 应用自动部署目录，如 “${tongweb.base}/deployment-osgi”。
c. 登录 TongWeb 管理控制台。
d. 切换到目标实例。
e. 在左侧导航栏中，选择 “其它容器” $>$ “OSGi 应用”，进入 OSGi 应用列表页面。
f. 在 OSGi 列表中，用户可查看到已部署的 OSGi 应用，如下图所示。
部署的应用默认为 “启动” 状态。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d270c3a1f0a7273b60341bc471908b9d142e2e839083e251b036f14386c24704.jpg)


# 手动上传
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “OSGi 应用”，进入 OSGi 应用列表页面。
4. 上传 OSGi 应用 jar 包或者设置 OSGi 应用 jar 包在服务器上的位置，以“${tongweb.home}/version*/examples/test-osgi.jar” 为例。

# 注意：
上传文件：控制台默认关闭上传文件功能。若需要开启，请参见禁用文件上传。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/21279602ed31e2a81099bfb2c3045a43933cd310642e9d4364899501cd4db9c4.jpg)
5. 配置完成后，单击 “添加”，完成 OSGi 应用的添加操作。
若界面弹出 “OSGi 应用添加成功” 提示信息，则说明添加 OSGi 应用成功。
在 OSGi 列表中，用户可查看到已部署的 OSGi 应用。
部署的应用默认为 “启动” 状态。

# 3.3.1.3. 停止 OSGi 应用
停止 OSGi 应用，即关闭其对外提供的服务。
停止操作可能因为超时而提示失败，可在一段时间后刷新状态以确认是否停止成功。

# 前置条件
• 已获取系统管理员账号和密码。
• 已部署 OSGi 应用。

# 停止单个 OSGi 应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “OSGi 应用”，进入 OSGi 应用列表页面。
4. 单击目标 OSGi 应用所在行的 “停止”，弹出确认停止 OSGi 应用提示信息。
5. 单击 “确定”，即完成停止单个 OSGi 应用操作。

# 批量停止 OSGi 应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “OSGi 应用”，进入 OSGi 应用列表页面。
4. 勾选一个或多个 OSGi 应用前的复选框，单击列表上方的 “停止”，弹出确认停止 OSGi 应用提示信息。
5. 单击 “确定”，即完成停止单个 OSGi 应用操作。

# 3.3.1.4. 删除 OSGi 应用
在控制台界面删除 OSGi 应用时，部署目录（如 “${tongweb.base}/deployment-osgi”）中的应用 jar 包会同步删除。
OSGi 应用不同于应用管理中的应用，删除 OSGi 应用时，系统不会执行备份操作，请谨慎操作。

# 前置条件
• 已获取系统管理员账号和密码。
• 已部署 OSGi 应用。

# 删除单个 OSGi 应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “OSGi 应用”，进入 OSGi 应用列表页面。
4. 单击目标 OSGi 应用所在行的 “删除”，弹出确认删除 OSGi 应用提示信息。
5. 单击 “确定”，即完成删除单个 OSGi 应用操作。

# 批量删除 OSGi 应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “OSGi 应用”，进入 OSGi 应用列表页面。
4. 勾选一个或多个 OSGi 应用前的复选框，单击列表上方的 “删除”，弹出确认删除 OSGi 应用提示信息。
5. 单击 “确定”，即完成删除单个 OSGi 应用操作。

# 3.3.2. WebFlux 应用
部署和管理基于 Spring WebFlux 开发的应用程序。

# 3.3.2.1. 部署 WebFlux 应用
部署 WebFlux 应用时，系统采用原地解压部署模式。

# 准备工作
• 已获取系统管理员账号和密码。
• 已准备好 WebFlux 应用。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “WebFlux 应用”，进入 WebFlux 应用列表页面。
4. 单击 “创建”，进入创建 WebFlux 应用页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/3283c52bf2ea055e48f9d721e939175ae559a1a3c254f1b64381b547872f5b65.jpg)
5. 配置 WebFlux 应用的相关参数。
◦ 应用名：必填项，WebFlux 应用的名称，需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符
◦ 应用位置：必填项，指定服务器上应用文件的位置，需要是 “.war” 类型的文件。
关于 WebFlux 应用的更多参数说明，详见 WebFlux 配置参数说明。
6. 配置完成后，单击 “添加”，即可完成 WebFlux 应用的部署操作。
页面弹出 “WebFlux 应用添加成功” 提示信息，并返回 WebFlux 应用列表页面。
添加的 WebFlux 应用默认处于 “STARTED” 状态。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/6c4b28430af69467e5fd735902447dddb003f13ba23f47644dc6dec6207b5f85.jpg)


# 3.3.2.2. 停止 WebFlux 应用
停止 WebFlux 应用，即关闭其对外提供的服务。
停止操作可能因为超时而提示失败，可在一段时间后刷新状态以确认是否停止成功。

# 前置条件
• 已获取系统管理员账号和密码。
• 已部署 WebFlux 应用。

# 停止单个 WebFlux 应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “WebFlux 应用”，进入 WebFlux 应用列表页面。
4. 单击目标 WebFlux 应用所在行的 “停止”，弹出确认停止 WebFlux 应用提示信息。
5. 单击 “确定”，即完成停止单个 WebFlux 应用操作。

# 批量停止 WebFlux 应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “WebFlux 应用”，进入 WebFlux 应用列表页面。
4. 勾选一个或多个 WebFlux 应用前的复选框，单击列表上方的 “停止”，弹出确认停止 WebFlux 应用提示信息。
5. 单击 “确定”，即完成停止单个 WebFlux 应用操作。

# 3.3.2.3. 删除 WebFlux 应用
在控制台界面删除 WebFlux 应用时，操作仅针对控制台记录，不会同步清理部署目录和 war 包文件。

# 前置条件
• 已获取系统管理员账号和密码。
• 已部署 WebFlux 应用。

# 删除单个 WebFlux 应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “WebFlux 应用”，进入 WebFlux 应用列表页面。
4. 单击目标 WebFlux 应用所在行的 “删除”，弹出确认删除 WebFlux 应用提示信息。
5. 单击 “确定”，即完成删除单个 WebFlux 应用操作。

# 批量删除 WebFlux 应用
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “其它容器” $>$ “WebFlux 应用”，进入 WebFlux 应用列表页面。
4. 勾选一个或多个 WebFlux 应用前的复选框，单击列表上方的 “删除”，弹出确认删除 WebFlux 应用提示信息。
5. 单击 “确定”，即完成删除单个 WebFlux 应用操作。

# 3.4. 资源管理

# 3.4.1. 公共类库
公共类库是 “.jar” 文件的集合，用于管理可被应用加载的公共资源。
用户可指定该类库包含的 jar/class 文件在服务器上的位置，或者进行文件上传，上传的文件会保存到“${tongweb.base}/data/upload” 目录下。

# 注意事项
出于安全考虑，TongWeb 出厂设置禁用了文件上传功能，您可在 “控制台安全” 模块了解详情和进行相关的配置操作。

# 3.4.1.1. 创建公共类库
本章节介绍如何创建公共类库。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “资源管理” $>$ “公共类库”，进入公共类库列表页面。
4. 单击 “创建”，进入创建公共类库页面。
公共类库／创建☆
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/91c631ace70bd57e036c762e6edbf4084ff9502c992c61b22022a16d8577bec7.jpg)
5. 配置公共类库的相关参数。
◦ 类库名称：必填项，类库名称需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 类库路径：必填项，指定该类库包含的 jar/class 文件在服务器上的位置。
说明：
▪ 支持上传（选择上传、拖拽上传）类库文件。
▪ 可以根据需要添加或者删除添加的类库。
▪ 也可以移动类库的顺序，系统会根据类库从上往下的顺序加载类库中的类。
关于公共类库的更多参数说明，详见公共类库配置参数说明。
6. 配置完成后，单击 “添加”，完成创建公共类库操作。
若界面弹出 “公共类库添加成功” 提示信息，则说明公共类库创建成功。
在公共类库列表中，您可以查看公共类库的名称、描述等信息。

# 3.4.1.2. 使用公共类库
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 单击 “部署”，进入部署页面。
5. 单击 “类加载”，进入类加载页面，选择已添加的公共类库。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f5910705e9c489082d64c42d00dfda46925be5a8e2282b1c8aa74655fccc199d.jpg)
6. 其他参数，请根据需要配置。
7. 配置完成后，单击 “添加”，完成公共类库的应用操作。

# 3.4.1.3. 管理公共类库
用户可根据需要查看、编辑或者删除公共类库。

# 查看公共类库
1. 在左侧导航栏中，选择 “资源管理” > “公共类库”，进入公共类库列表页面。
2. 在公共类库列表页面，您可以查看已创建的公共类库。
包含公共类库的名称、描述等信息。

# 编辑公共类库
1. 在左侧导航栏中，选择 “资源管理” $>$ “公共类库”，进入公共类库列表页面。
2. 单击目标公共类库名称，进入编辑公共类库页面。
3. 您可以根据提示修改公共类库信息。
注：公共类库名称不可编辑。
4. 编辑完成后，单击 “更新”，更新公共类库配置信息。
若界面弹出 “公共类库更新成功” 提示信息，则说明编辑公共类库成功。

# 删除公共类库
删除公共类库时，公共类库引用的其它组件不会被删除。
1. 在左侧导航栏中，选择 “资源管理” $>$ “公共类库”，进入公共类库列表页面。
2. 单击目标公共类库所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个公共类库，并单击列表上方的 “删除” 按钮，批量删除公共类库。
3. 单击 “确定”，完成公共类库的删除操作。
若界面弹出 “公共类库删除成功” 提示信息，则说明删除公共类库成功。

# 3.4.2. 会话服务器
用户可以将服务端的会话信息备份到数据缓存服务中去，用以在服务器故障重启后保障会话信息不丢失，以获得会话高可用能力。
会话服务器作为 Session 存储库，当一个 TongWeb 节点宕机后，其它 TongWeb 节点可以从外部会话服务器中恢复 Session 数据，从而保证 Session 不丢失。

# 注意事项
• 会话服务器仅用于内部（TongWeb 本机搭建 TongDataGrid）、外部（单独搭建TongDataGrid、RDS、Hazelcast、Redis）会话服务器的资源汇总。
• 当应用使用会话服务器时，从汇总的会话服务器中选择指定的某一个会话服务器。

# 3.4.2.1. 支持的会话服务器
• TongDataGrid（简称 TDG）：东方通自研产品
• RDS：分布式内存数据缓存中间件，东方通自研产品
• Hazelcast
• Redis

# 3.4.2.2. 搭建会话服务器
本章节介绍如何 “搭建会话服务器（TongDataGrid）”。
关于 RDS、hazelcast 和 Redis 外部会话服务器的搭建，请参阅官方文档。

# 注意事项
内置 TongDataGrid 不建议供外部使用。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “资源配置” $>$ “TongDataGrid”，进入 TongDataGrid 页面。
4. 单击 “创建”，进入创建 TongDataGrid 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a1b7f115a2143bb882631fbf9c867c228829e70f6ece0e90ac048b5c57142e74.jpg)
5. 配置 TongDataGrid 相关参数。
◦ 名称：必填项，TongDataGrid 的名称。
◦ 所在节点：必填项，勾选 TongDataGrid 所在节点。
关于 TongDataGrid 的更多参数说明，详见TongDataGrid 配置参数说明。
6. 单击 “添加”，完成 TongDataGrid 添加操作。
若界面弹出 “TongDataGrid 添加成功” 提示信息，则说明 TongDataGrid 添加成功。
添加成功后，TongDataGrid 默认为 “false” 状态。

# 3.4.2.3. 创建会话服务器
创建会话服务器前，请先搭建会话服务器（TDG、RDS、Hazelcast 或者 Redis）。在创建会话服务器时，系统会自动在 “${tongweb.base}/logs” 目录下生成一个名为 “sessionha” 的子目录，并将与会话（session）相关的业务日志文件（如 sessionha.log）存储在该路径下。

# 前置条件
• 已获取系统管理员账号和密码。
• 已搭建会话服务器。
• 已获取会话服务器的地址、认证名和认证密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “资源管理” $>$ “会话服务器”，进入会话服务器列表页面。
4. 单击 “创建”，进入创建会话服务器页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/eed25b7d7aff72d1eb00d1dd73eb7c520fbb36b6311520bcce359364d34527a7.jpg)
5. 输入会话服务器名称。
6. 配置会话服务器相关参数。
◦ 使用 TongDataGrid
不需要开启 “使用外部会话服务器”，直接在 “TongDataGrid” 下拉列表中，选择已创建的TongDataGrid。
◦ 使用外部会话服务器
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ca2b830630990bbbb8dce410f29be71dced2c1a2fe0f41c287d4b75b00cb64b5.jpg)
▪ TongDataGrid
<table><tr><td>参数</td><td>说明</td></tr><tr><td>使用外部会话服务器</td><td>打开“使用外部会话服务器”开关。</td></tr><tr><td>服务器类型</td><td>必填项,选择“TongDataGrid”。</td></tr><tr><td>服务器地址</td><td>必填项,连接远端会话服务器的IP地址和端口。</td></tr><tr><td>认证名</td><td>必填项,创建TongDataGrid时系统自动生成的认证名和密码。用户可打开“${tongweb.base}/data/centralized/tdg/&lt;session_name&gt;/bin/tongdatagrid.xml”获取认证名 和密码 &lt;password&gt;。</td></tr><tr><td>认证密码</td><td>连接远端会话服务器的认证密码,需要使用加密后的密码。需要将获取的密码进行加密处理,操作步骤如下所示。a.进入TongWeb管理控制台。b.切换到目标实例。c.选择“基础配置” &gt; “加密工具”,进入加密工具页面。d.输入明文密码,选择“加密类型”为“对称加密”。e.单击“加密”,即可获得加密后的密码。</td></tr><tr><td>其他参数</td><td>请根据需要配置,配置说明详见会话服务器参数配置说明。</td></tr></table>
▪ RDS
<table><tr><td>参数</td><td>说明</td></tr><tr><td>使用外部会话服务器</td><td>打开“使用外部会话服务器”开关。</td></tr><tr><td>服务器类型</td><td>必填项，选择“RDS”。</td></tr><tr><td>连接模式</td><td>必填项，可选择“集群模式”、“哨兵模式”或“单例模式”。</td></tr><tr><td>服务器地址</td><td>必填项，连接远端会话服务器的IP地址和端口。</td></tr><tr><td>用户名</td><td>非必填，连接RDS服务器的用户名。</td></tr><tr><td>认证密码</td><td>非必填，连接RDS服务器的密码。支持RDS无密码场景。</td></tr><tr><td>其他参数</td><td>请根据需要配置，配置说明详见会话服务器参数配置说明。</td></tr></table>
▪ Hazelcast
<table><tr><td>参数</td><td>说明</td></tr><tr><td>使用外部会话服务器</td><td>打开“使用外部会话服务器”开关。</td></tr><tr><td>服务器类型</td><td>必填项，选择“Hazelcast”。</td></tr><tr><td>服务器地址</td><td>必填项，连接远端会话服务器的IP地址和端口。</td></tr><tr><td>认证名</td><td>必填项，连接会话服务器所需要的组名。</td></tr><tr><td>其他参数</td><td>请根据需要配置，配置说明详见会话服务器参数配置说明。</td></tr></table>
▪ Redis
<table><tr><td>参数</td><td>说明</td></tr><tr><td>使用外部会话服务器</td><td>打开“使用外部会话服务器”开关。</td></tr><tr><td>服务器类型</td><td>必填项，选择“Redis”。</td></tr><tr><td>连接模式</td><td>必填项，可选择“集群模式”、“哨兵模式”或“单例模式”。</td></tr><tr><td>服务器地址</td><td>必填项，连接远端会话服务器的IP地址和端口。
多个IP地址使用英文逗号分隔，如192.168.1.1:7001,192.168.1.2:7002。</td></tr><tr><td>其他参数</td><td>请根据需要配置，配置说明详见会话服务器参数配置说明。</td></tr></table>
7. 配置完成后，单击 “添加”，完成创建会话服务器操作。
若界面弹出 “会话服务器添加成功” 提示信息，则说明会话服务器创建成功。
在会话服务器列表中，您可以查看会话服务器的名称、使用外部会话服务器、服务器类型、服务器地址等信息。

# 3.4.2.4. 应用会话服务器
本章节介绍如何应用会话服务器。

# 前置条件
已创建会话服务器。

# 部署应用时应用会话服务器
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 单击 “部署” 或者已部署应用的名称。
5. 单击 “会话与 cookie”，进入会话与 cookie 页面。
6. 在下拉列表中，选择已创建的会话服务器。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7856efa605f3581c76a4fa062aca9caaebd2de3c52883ca73d2ef81e45c7d546.jpg)
7. 其他参数，请根据需要进行配置。
8. 完成应用的部署或者更新，即可完成会话服务器的应用。

# 虚拟主机应用会话服务器
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “Web 容器” $>$ “虚拟主机”，进入虚拟主机页面。
4. 单击 “创建” 或者已创建的虚拟主机的主机名。
5. 在 “会话服务器” 下拉列表中，选择已创建的会话服务器。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a563b5b4e01e03d991b97d4b800b5d39391d26171b206d96cccaa304dc763330.jpg)
6. 其他参数，请根据需要进行配置。
7. 完成虚拟主机的添加或者更新，即可完成会话服务器的应用。

# 有状态 EJB 应用会话服务器
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧菜单栏中，选择 “EJB 容器” > “有状态 EJB”，进入有状态 EJB 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c5a394fe81a7b3a4ecb22d2733a50081af85c95348a450cb59b6759b1124808d.jpg)
4. 在 “会话服务器” 下拉列表中，选择已创建的会话服务器。
5. 其他参数，请根据需要进行配置。
6. 单击 “更新”，即可完成有状态 EJB 应用会话服务器的操作。

# 3.4.2.5. 管理会话服务器
用户可根据需要查看、编辑或者删除会话服务器。

# 查看会话服务器
1. 在左侧导航栏中，选择 “资源管理” $>$ “会话服务器”，进入会话服务器列表页面。
2. 在会话服务器列表页面，您可以查看已创建的会话服务器。
包含会话服务器的名称、使用外部会话服务器、服务器类型、服务器地址等信息。

# 编辑会话服务器
1. 在左侧导航栏中，选择 “资源管理” $>$ “会话服务器”，进入会话服务器列表页面。
2. 单击目标会话服务器名称，进入编辑会话服务器页面。
3. 您可以根据提示修改会话服务器信息。
注：会话服务器名称不可编辑。
4. 编辑完成后，单击 “更新”，更新会话服务器配置信息。
若界面弹出 “会话服务器更新成功” 提示信息，则说明编辑会话服务器成功。

# 删除会话服务器
被引用的会话服务器不能删除。若需要删除，请先解除对该会话服务器的引用。
删除会话服务器时，会话服务器引用的其它组件不会被删除。
1. 在左侧导航栏中，选择 “资源管理” $>$ “会话服务器”，进入会话服务器列表页面。
2. 单击目标会话服务器所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个会话服务器，并单击列表上方的 “删除” 按钮，批量删除会话服务器。
3. 单击 “确定”，完成会话服务器的删除操作。
若界面弹出 “会话服务器删除成功” 提示信息，则说明删除会话服务器成功。

# 3.4.3. 短信服务
TongWeb 提供发送短信的服务。
用户可通过创建短信服务的方式，将自己的发送短信的实现类以及短信平台等相关信息添加到 TongWeb，并将创建的短信服务关联到预警策略；当监控的信息触发预警时，TongWeb 将及时发送短信通知。

# 3.4.3.1. 使用短信服务
本章节介绍如何使用短信服务，包含创建短信服务、创建预警策略、触发预警后查收短信等。

# 前置条件
• 已准备好发送短信的实现类，并在启动 TongWeb 之前，将相关的 jar 文件放置到“${tongweb.base}/lib” 目录下。
注：发送短信的实现类的要求，请参见短信服务配置参数说明。
• 已准备好短信平台相关信息，包含短信平台的认证标识、认证密钥等。
• 已在短信服务平台设置短信服务签名、短信服务 ID 等信息。
• 已创建采集模板。

# 操作步骤

# 1. 创建短信服务。
a. 登录 TongWeb 管理控制台。
b. 切换到目标实例。
c. 在左侧导航栏中，选择 “资源管理” $>$ “短信服务”，进入短信服务页面。
d. 单击 “创建”，进入创建短信服务页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/67a96b91aa579392cbf94b8bb3ab5e356fc61a7700a8d5b2c6be12b7245f072a.jpg)


# e. 配置短信服务的相关参数。
关于短信服务的更多参数说明，详见短信服务配置参数说明。
f. 单击 “添加”，完成短信服务的创建操作。
若界面弹出 “短信服务添加成功” 提示信息，则说明添加短信服务成功。
在短信服务列表中，可查看已添加的短信服务。

# 2. 创建预警策略。
通过创建预警策略的方式，触发预警并发送预警信息。
a. 在左侧导航栏中，选择 “诊断管理” $>$ “预警策略”，进入预警策略页面。
b. 单击 “创建”，进入创建预警策略页面。
c. 配置预警策略名称、触发条件等信息。
注：请根据实际需要进行配置。
d. 配置 “处理办法”，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/07ff1d5dd70964104b41c037747b2dcb1f57a2342a96e71be7cea831d2f74295.jpg)
配置说明，如下所示。
▪ 生成快照：选择一个已创建的采集模板。
▪ 发送短信：开启发送短信开关。
▪ 短信服务：选择步骤1中创建的短信服务。
▪ 短信服务签名：输入已在短信平台设置的短信服务签名。
▪ 短信服务ID：输入已在短信平台设置的短信服务ID。
▪ 接收人手机号：输入需要接收预警信息的手机号。
▪ 其他参数：请根据需要配置。
e. 单击 “添加”，完成预警策略的添加操作。
若界面弹出 “预警策略添加成功” 提示信息，则说明添加预警策略成功。
在预警策略列表中，可查看已添加的预警策略。
3. 触发预警后查收短信。
当触发设置的预警条件后，设置的接收人手机号即可接收到预警信息，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/934d0082556bf5f6e80d4441d6963522e626d45b925383248e470f3fceb8bc05.jpg)


# 3.4.3.2. 授权到期提醒设置短信通知
用户可根据需要设置授权到期短信提醒通知。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “基础配置” $>$ “全局配置” $>$ “授权”，进入全局配置的“授权”页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ea30f57b1a0180e1ccc053b959e8626463f4638f8895a6491e852e7c3e287a5b.jpg)
4. 根据需要设置短信发送方式。
5. 配置完成后，单击 “更新”，完成授权到期时间提醒的短信通知配置操作。

# 3.4.3.3. 管理短信服务
用户可以根据需要编辑、删除已添加的短信服务。

# 编辑短信服务
除了短信服务的名称，其它实现类、接口地址、认证ID、认证密码、附加参数均可根据需要进行修改。
1. 在左侧导航栏中，选择 “资源管理” $>$ “短信服务”，进入短信服务页面。
2. 单击目标短信服务所在行的短信服务名称链接，进入该短信服务详细信息页面。
3. 您可以根据需要修改该短信服务的相关信息。
4. 编辑完成后，单击 “更新”，即可完成短信服务的编辑操作。
若界面弹出 “短信服务更新成功” 提示信息，则说明更新短信服务成功。

# 删除短信服务
若需要删除已添加的短信服务，请确保已解除其它组件对该短信服务的引用，否则无法删除。
删除短信服务后，不可恢复，请谨慎操作。
1. 在左侧导航栏中，选择 “资源管理” $>$ “短信服务”，进入短信服务页面。
2. 单击目标短信服务所在行的 “删除”，弹出确认删除短信服务窗口。
注：用户可根据需要勾选一个或多个短信服务，并单击列表上方的 “删除” 按钮，批量删除短信服务。
3. 单击 “确定”，即可完成短信服务删除操作。

# 3.4.4. 线程池
线程池提供由服务器管理的线程池资源，可用来处理特定的应用业务。

# 3.4.4.1. 创建线程池
本章节介绍如何创建线程池。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “资源管理” $>$ “线程池”，进入线程池列表页面。
4. 单击 “创建”，进入创建线程池页面。
线程池／创建☆
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/8328010889b6fc2a506b0091200366f93db3c593e98123a00257125b559fce25.jpg)
5. 配置线程池的相关参数。
名称：必填项，线程的名称，需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
关于线程池的更多参数说明，详见线程池配置参数说明。
6. 配置完成后，单击 “添加”，完成创建线程池操作。
若界面弹出 “线程池添加成功” 提示信息，则说明线程池创建成功。
在线程池列表中，您可以查看线程池的名称、最大线程数、优先级等信息。

# 3.4.4.2. 使用线程池
当部署应用时，您可以根据需要在 “安全” 页签下，配置业务安全规则，使用双线池或者三线程池处理业务。
当使用双线程池或者线程池处理业务时，即可应用您创建的线程池。
您也可以将线程池用作工作管理器线程池，请参见创建工作管理器。

# 使用线程池处理业务
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “应用管理” $>$ “应用”，进入应用列表页面。
4. 单击 “部署”，进入部署页面。
5. 单击 “安全”，进入安全页面，业务安全规则选择双线程池或者三线程池，即可使用您创建的线程池。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e5213cab04ffe9189d9ed6feefbd0746ea5cfc56b2dcd44e84ee94b373301fcc.jpg)
6. 其他参数请根据需要配置。
7. 配置完成后，单击 “添加”，完成线程池的应用操作。

# 用作工作管理器线程池
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “EJB 容器” $>$ “工作管理器”，进入工作管理器列表页面。
4. 单击“创建”，进入创建工作管理器页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/374dcc8316985bd908a0bcfa118fb74bdf97166e725a3f563798a47820637fd6.jpg)
5. 配置工作管理器的相关参数。
◦ 名称：必填项，输入工作管理器的名称。
◦ 工作管理器线程池：必填项，选择已创建的线程池。
◦ 其他参数：非必填，请根据需要进行配置。
6. 配置完成后，单击 “添加”，完成工作管理器的添加操作。

# 3.4.4.3. 监视线程池
您可以通过监视线程池的方式，获取该线程池运行的状态，了解当前线程池的健康状态。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建线程池。

# 查看监视视图
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “资源管理” $>$ “线程池”，进入线程池列表页面。
4. 单击目标线程池所在行的 “监视”，进入监视页面。
可查看线程池的实时 “活跃线程数” 和 “总线程数” 等，如下图所示。
线程池
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/3a14f198185a4bd516daf287d902afc56980d53dfd47a68a90454cb0ebcfcb83.jpg)


# 下载监视视图
1. 进入线程池列表页面。
2. 单击目标线程池所在行的 “监视”，进入监视视图页面。
3. 在监视视图页面，单击鼠标右键，可将监视视图另存为 “.png” 图片。

# 3.4.4.4. 管理线程池
用户可根据需要查看、编辑或者删除线程池。

# 查看线程池
1. 在左侧导航栏中，选择 “资源管理” $>$ “线程池”，进入线程池列表页面。
2. 在线程池列表页面，您可以查看已创建的线程池。
包含线程池的名称、描述等信息。

# 编辑线程池
1. 在左侧导航栏中，选择 “资源管理” $>$ “线程池”，进入线程池列表页面。
2. 单击目标线程池名称，进入编辑线程池页面。
3. 您可以根据提示修改线程池信息。
注：线程池名称不可编辑。
4. 编辑完成后，单击 “更新”，更新线程池配置信息。
若界面弹出 “线程池更新成功” 提示信息，则说明编辑线程池成功。

# 删除线程池
删除线程池时，线程池引用的其它组件不会被删除。
1. 在左侧导航栏中，选择 “资源管理” $>$ “线程池”，进入线程池列表页面。
2. 单击目标线程池所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个线程池，并单击列表上方的 “删除” 按钮，批量删除线程池。
3. 单击 “确定”，完成线程池的删除操作。
若界面弹出 “线程池删除成功” 提示信息，则说明删除线程池成功。

# 3.4.5. JNDI 资源
创建特定的资源对象，并将其绑定到 TongWeb 的 JNDI 资源树上。

# 3.4.5.1. 创建 JNDI 资源
本章节介绍如何创建 JNDI 资源。

# 前置条件
• 已按规范编写工厂类，该工厂类已实现 javax.naming.spi.ObjectFactory 接口。
• 编程时，将该接口的 getObjectInstance 方法的第一个参数强转为 javax.naming.Reference 类型，以此获取到“资源类型”和“其它属性”的配置参数。
• 可提前将该工厂类所在的 jar 文件存放在 “${tongweb.home}/lib” 或者 “${tongweb.base}/lib” 目录下，再启动 TongWeb，“jar包位置”参数可不填写。

# 注意：
若 jar 文件没有放在 TongWeb 的 lib 目录下，或在启动 TongWeb 后再放到 lib 目录下，则 “jar 包位置”参数，需要填写为绝对路径。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “资源管理” $>$ “JNDI 资源”，进入 JNDI 资源页面。
4. 单击 “创建”，进入创建 JNDI 资源页面。
JNDI资源／创建☆
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/21a6df32dd5fbc5b9d762c18c6b030e3aac1279859e47becddddb0db4a311702.jpg)


# 5. 配置 JNDI 资源的相关参数。
◦ 名称：必填项，JNDI 资源名称，需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 工厂类：必填项，指定创建资源对象的工厂类全名称。
◦ 资源类型：必填项，指定要绑定的资源对象的类全名称。
关于 JNDI 资源的更多参数说明，详见JNDI 资源配置参数说明。
6. 单击 “添加”，完成 JNDI 资源创建操作。
若界面弹出 “JNDI 资源添加成功” 提示信息，则说明 JNDI 资源创建成功。

# 3.4.5.2. 查看添加的 JNDI 资源
查看绑定到 TongWeb 的 JNDI 树上的资源。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “JNDI 树”，进入 JNDI 树页面。
4. 单击 “server”，显示 server 资源。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/0dfe068c30266e36339db710fd76160a1e6e113fdb83755fcf019eebdc995fef.jpg)
5. 单击创建的 JNDI 资源名称，弹出创建的 JNDI 详细信息窗口。
包含对象名、对象类型、JNDI 路径、对象接口以及对象值信息。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/4b6c392c1023ad5f666b6b529516b78f0f8c3a10bcc3c92e5b658ef6d0fe2dfb.jpg)


# 3.4.5.3. 管理 JNDI 资源
您可以根据需要编辑或者删除已创建的 JNDI 资源。

# 编辑 JNDI 资源
1. 在左侧导航栏中，选择“资源管理”>“JNDI 资源”，进入 JNDI 资源页面。
2. 单击已创建的 JNDI 资源的名称，进入 JNDI 资源编辑页面。
3. 您可以根据需要修改 JNDI 资源的资源类型、其它属性、工厂类、jar 包位置等信息。
说明：
JNDI 资源的名称不可编辑。
4. 单击 “更新”，完成 JNDI 资源的编辑操作。
若界面弹出 “JNDI 资源更新成功” 提示信息，则说明 JNDI 资源更新成功。

# 删除 JNDI 资源
删除 JNDI 资源后，应用访问该 JNDI 资源对象将会失败。删除后不可恢复，请谨慎操作。
1. 在左侧导航栏中，选择 “资源管理” $>$ “JNDI 资源”，进入 JNDI 资源页面。
2. 单击目标 JNDI 资源所在行的 “删除”，弹出确认删除窗口。

# 说明：
用户可根据需要勾选一个或多个 JNDI 资源，并单击列表上方的 “删除” 按钮，批量删除 JNDI 资源。
3. 单击 “确定”，完成删除 JNDI 资源操作。
若界面弹出 “JNDI 资源删除成功” 提示信息，则说明删除 JNDI 资源成功。

# 3.4.6. 注册中心
注册中心可用于注册和发现 TongWeb 实例服务，也可用于存储和共享 TongWeb 实例配置。
• 用于注册和发现 TongWeb 实例服务
用户需要在 TongWeb 实例通过 “全局配置” $>$ “集中管理” 模块打开 “启用服务注册中心”，即可将实例服务注册到所选注册中心的服务器上。然后，在 TongWeb “集中管理” $>$ “服务管理” $>$ “注册实例” 模块管理该实例。
• 用于存储和共享 TongWeb 实例配置
用户需要在 TongWeb 实例的 “全局配置” $>$ “远程配置” 模块，打开 “启用配置注册中心”。当多个TongWeb 实例选择使用了相同的 “注册中心” 时，它们将共享彼此的配置参数。此时，通过集中管理中“服务管理” $>$ “注册实例” 列表，管理变更其中任何一个实例（也可以单独访问某个实例的管理控制台）的参数，都将自动同步到其它实例。

# 3.4.6.1. 支持的服务提供商
TongNCS、Nacos、Etcd、Zookeeper、Consul、Apollo
注：Apollo 仅支持作为配置中心，不支持作为注册中心。

# 3.4.6.2. 支持的版本
<table><tr><td>服务提供商</td><td>版本说明</td></tr><tr><td>TongNCS</td><td>2.0.1及以上版本</td></tr><tr><td>Nacos</td><td>2.0以上版本</td></tr><tr><td>Etcd</td><td>Etcd v3 版本</td></tr><tr><td>ZooKeeper</td><td>3.5及以上的版本</td></tr><tr><td>Consul</td><td>1.20及以上版本</td></tr><tr><td>Apollo</td><td>2.1及以上版本</td></tr></table>

# 3.4.6.3. 环境准备
• 搭建注册中心环境（如 TongNCS、Nacos、Etcd、Zookeeper、Consul 或 Apollo）。
• 获取注册中心相关的 jar 包以及所有的依赖。
用户可参考并获取 “扩展支持” 列出的注册中心相关版本的 jar 包及依赖信息。
◦ TongNCS
◦ Nacos
◦ Etcd
◦ ZooKeeper
◦ Consul
◦ Apollo

# 3.4.6.4. 注意事项

# • ZooKeeper
若选择 “ZooKeeper” 作为服务提供商，用户首先需要到 “ZooKeeper” 所在服务器手动创建“TongWeb”（区分大小写） 节点并开启所有权限，用于保存配置文件等数据。
若用户没有手动创建 “TongWeb” 节点，系统会自动创建，但不会设置权限，需要用户手动开启所有权限。

# • Nacos / TongNCS
若选择 Nacos 或 TonsNCS 作为服务提供商，当 Nacos 或 TonsNCS 的后台管理控制台看不到TongWeb 相关数据时，用户可在后台管理控制台手动创建 TongWeb 的命名空间 “TongWeb”。

# 3.4.6.5. 用于注册和发现 TongWeb 实例
如下示例中，服务提供商以 Nacos 为例进行说明。
注：其它服务提供商，请根据实际环境进行替换。

# 3.4.6.5.1. 步骤1：准备 TongWeb
如下以 “准备 2 个不同的 TongWeb” 为例进行说明。
• 一个作为集中管理端 TongWebA
• 一个作为远程实例端 TongWebB
在示例中，通过分别为 TongWebA 和 TongWebB 配置 “注册中心”，并在 TongWebB 中，打开 “服务注册中心” 的方式，将 TongWebB 的实例信息拉取到 TongWebA，由 TongWebA 进行统一查看和管理。

# 说明：
用户可根据需要，配置一个集中管理端获取多个远程 TongWeb 实例的信息。

# 3.4.6.5.2. 步骤2：放 jar 包及依赖
将下载的 jar 包及依赖包分别放到 TongWebA 和 TongWebB 的 “${tongweb.home}/lib” 目录下。

# 3.4.6.5.3. 步骤3：将 Nacos 添加到 TongWebB 注册中心
1. 登录 TongWebB 控制台。
2. 切换到默认实例。
3. 在左侧导航栏中，选择 “资源管理” $>$ “注册中心”，进入注册中心页面。
4. 单击 “创建”，进入创建注册中心页面。
5. 填写 Nacos 连接信息。
◦ 名称：必填项，注册中心的名称。
◦ 服务提供商：必填项，选择 “Nacos”。
◦ 服务地址：必填项，填写为部署 Nacos 的服务器的地址，例如 “192.168.1.2:8848”。
◦ 用户名：非必填，登录 Nacos 服务器的用户名。
◦ 密码：非必填，登录 Nacos 端服务器的用户密码。
◦ 标识符：必填项，设置唯一标识符，如：tw。
◦ 添加类库：非必填，请根据需要选择已添加的公共类库。若没有公共类库，则前往 “资源管理” > “公共类库”，添加公共类库。
关于注册中心的更多参数说明，详见注册中心配置参数说明。
6. 单击 “添加”，即可将 Nacos 添加到注册中心。

# 3.4.6.5.4. 步骤4：打开 TongWebB “服务注册中心”

# 1. 拷贝 TongWebA 的公钥
将 TongWebB 纳入到 TongWebA，由 TongWebA 进行集中管理。
a. 登录 TongWebA 控制台。
b. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
c. 在左侧导航栏中，选择 “服务管理” $>$ “集中配置”，进入集中配置页面。
d. 拷贝加密公钥。

# 2. 打开 TongWebB 的 “启用服务注册中心”
a. 登录 TongWebB 控制台。
b. 切换到默认实例。
c. 在左侧导航栏中，选择 “基础配置” $>$ “全局配置” $>$ “集中管理”，进入集中管理页面。
d. 打开 “支持集中管理” 开关，并将拷贝的加密公钥粘贴到 “加密公钥” 文本框。
e. 打开 “启用服务注册中心” 开关，并在 “服务注册中心” 下拉列表中，选择 已添加的注册中心。
f. 单击 “更新”，完成 “服务注册中心” 的配置操作。
注：用户可进入 TongWebB 的 “集中管理” $>$ “服务管理” $>$ “注册实例”，查看 TongWebB 的实例信息。

# 3.4.6.5.5. 步骤5：将 Nacos 添加到 TongWebA 注册中心
1. 登录 TongWebA 服务器。
2. 切换到默认实例。
3. 在左侧导航栏中，选择 “资源管理” > “注册中心”，进入注册中心页面。
4. 填写 Nacos 连接信息。
◦ 名称：注册中心的名称。
◦ 服务提供商：选择 “Nacos”。
◦ 服务地址：填写为部署 Nacos 的服务器的地址，例如 “192.168.1.2:8848”。
注：要求与 TongWebB 的服务地址保持一致。
◦ 用户名：登录 Nacos 服务器的用户名。
◦ 密码：登录 Nacos 端服务器的用户密码。
◦ 标识符：填写为 TongWebB 配置的标识符，如：tw。
注：配置的标识符要求与 TongWebB 一致，TongWebA 才能发现这个实例。
◦ 添加类库：可选，请根据需要选择已添加的公共类库。若没有公共类库，则前往 “资源管理” > “公共类库”，添加公共类库。
5. 单击 “添加”，即可将 Nacos 添加到注册中心。

# 3.4.6.5.6. 步骤6：在 TongWebA 查看 TongWebB 实例信息
1. 登录 TongWebA 控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “注册实例”，进入注册实例页面。
4. 用户即可查看到 TongWebB 的实例。
5. 单击 TongWebB 实例所在行的 “管理”，即可切换到该实例，并对其进行管理。

# 3.4.6.6. 用于存储和共享 TongWeb 实例配置
用户可将多个不同实例注册到同一个注册中心，并打开 “启用配置注册中心”，即可实现多个实例间的配置共享。
如下示例中，服务提供商以 Nacos 为例进行说明。
注：其它服务提供商，请根据实际环境进行替换。

# 3.4.6.6.1. 步骤1：准备 TongWeb
如下以 “准备两个不同的 TongWeb（TongWeb A 和 TongWeb B）” 为例进行说明。

# 3.4.6.6.2. 步骤2：将 Nacos 添加到 TongWeb A 和 TongWeb B 注册中心
1. 登录 TongWeb A 控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “资源管理” $>$ “注册中心”，进入注册中心页面。
4. 单击 “创建”，进入创建注册中心页面。
5. 填写 Nacos 连接信息。
◦ 名称：必填，注册中心的名称。
◦ 服务提供商：必填，选择 “Nacos”。
◦ 服务地址：必填，填写为部署 Nacos 的服务器的地址，例如 “192.168.1.2:8848”。
◦ 用户名：必填，登录 Nacos 服务器的用户名。
◦ 密码：必填，登录 Nacos 端服务器的用户密码。
◦ 标识符：必填，设置唯一标识符，如：tw。
◦ 添加类库：可选，请根据需要选择已添加的公共类库。若没有公共类库，则前往 “资源管理” > “公共类库”，添加公共类库。
6. 单击 “添加”，即可将 Nacos 添加到注册中心。
7. 参照如上步骤，将 Nacos 添加到 TongWeb B 注册中心。
注：保证 TongWeb A 和 TongWeb B 的服务地址、用户名、密码和标识符相同。

# 3.4.6.6.3. 步骤3：打开 TongWeb A 和 TongWeb B 的 “启用配置注册中心”
1. 登录 TongWeb A 控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “基础配置” $>$ “全局配置” $>$ “远程配置”，进入远程配置页面。
4. 打开 “启用配置注册注册中心”，并在 “配置注册中心” 下拉列表中，选择 已添加的注册中心。
5. 打开 “推送配置变更” 开关。
注：开启该开关后，才会推送配置变更；不开启则不推送。
6. 打开 “监听变更并重启” 开关，默认为 “开启” 状态。
注：开启该功能，要求先开启 “启动策略” 模块的 “宕机重启” 功能。
7. 单击 “更新”，完成 “配置注册中心” 的配置操作。
8. 参照如上步骤，完成 TongWeb B 的 “启用配置注册中心” 的配置操作。

# 3.4.6.6.4. 步骤4：验证推送效果
例如：在 TongWeb A 中手动创建一个名为 “test” 的通道，然后进入 TongWeb B 中，可查看到同步自动创
建了一个配置相同的名为 “test” 的通道。

# 3.5. 监视管理
监视管理包含操作系统负荷、TongWeb 负荷、应用数据源、操作系统、JVM、组合监视、守护监视、SNMP 服务、Prometheus 服务、OTLP 支持监视。

# 注意事项
• 无值的监视指标不在监视结果中显示。
• 所有模块监视数据（含组合监视、守护监视）的返回数据结构有变化。
若已通过 REST、JMX、命令行等接口与外部系统对接，则需要重新适配。

# 3.5.1. 监视概览
监视概览用于检测展示系统整体的健康状况，主要用于观测系统的性能瓶颈。
当使用网页端接入时，若某系统资源的性能符合达到 $80 \%$ ，其对应的网页上的指示器将会变为红色以给出警示。

# 进入 TongWeb 监视概览页面
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “概览”，进入概览页面。

# 查看操作系统负荷
您可以查看操作系统的 CPU 使用率、内存使用率、硬盘使用率等。
概览☆
操作系统负荷
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f143fb09dc7253a7fdf41a7535a0bda38ed644e46116c4f3621481f561b44946.jpg)
CPU使用率
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/8867d0247de376fa77b0f800bd097bf74a160598d26427d251c74004f931643d.jpg)
96 %
内存使用率
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/58331d55af55b6b53d019a4ac9e79926ba606c8c9fd4f12fae000c881ee99847.jpg)
硬盘使用率


# 查看 TongWeb 负荷
您可以查看 TongWeb 的使用中堆内存、通道活跃线程数等。
TongWeb 负荷
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e7cf636f7af461f03d73adceca3c4bfcc92c0378ed4be77c9fc253fd0dec2d97.jpg)
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/cb8d8ca23906441e2322bb0e79f178ee07e034faca0c385c27f5cbb03d670cc7.jpg)
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7a3f7ea25d1bddcbb2c8557782d0eb5f8d733b700dc81216a694565eaa29d11d.jpg)


# 3.5.2. 应用数据源
支持监视应用自行创建和管理的数据源的使用情况，包含 JDBC 连接池大小、活跃连接数、空闲连接数、线程等待数等。
在应用数据源列表页面，您可以查看应用数据源的名称、类型、类型以及所属应用。

# 支持的 JDBC 连接池类型
HikariCP、Druid、DBCP、C3P0、BeeCP、BoneCP、Tomcat Pool、Hulk。

# 注意事项
DBCP、C3P0、BoneCP 目前暂不支持监控“线程等待数”，即该监控值始终为“-1”。

# 前置条件
• 使用该功能前，请先进入 “基础配置” > “全局配置” > “应用” 页面，开启 “监视应用数据源”。
在应用数据源初始化完成后，即可监控到应用数据源使用情况。
• 已部署自带数据源的应用。

# 监视数据源
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” > “应用数据源”，进入应用数据源页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/1e6a31498598968561e9e302553d7281993deeeca478a1aa66f5428915c50102.jpg)
4. 单击应用数据源所在行的 “监视”，进入监视数据源页面。
左上角的 “Druid” 表示应用数据源的名称。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ed4237d6806264be228596287ba8cce4f224e5436b6e3d84c1d4fa0fb312b9c4.jpg)
5. 可以查看应用数据源的连接池大小、活跃连接数、空闲连接数以及线程等待数。

# 下载监视视图
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “应用数据源”，进入应用数据源页面。
4. 单击应用数据源所在行的 “监视”，进入监视数据源页面。
5. 在监视视图所在区域，单击鼠标右键，将监视视图另存为 “.png” 图片即可。

# 3.5.3. 操作系统
展示操作系统的基本信息。

# 进入 TongWeb 概览页面
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” > “操作系统”，进入操作系统页面。

# 查看操作系统
您可以查看操作系统的 CPU 使用率、内存使用率、硬盘使用率、空闲内存（GB）、空闲交换空间（GB）、当前虚拟内存（GB）、硬盘剩余（GB）等。
操作系统？／监视☆
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/4481a65f52d98a9327b461a5667b4a3de8314c51c3bedd8b2862d30703f1ab7c.jpg)


# 查看操作系统基本信息
您可以查看操作系统的名称、版本、架构、CPU 个数、总内存（GB）、总交换空间（GB）以及硬盘总量（GB）等。
<table><tr><td>名称</td><td>Windows 10</td></tr><tr><td>版本</td><td>10.0</td></tr><tr><td>架构</td><td>amd64</td></tr><tr><td>CPU个数</td><td>8</td></tr><tr><td>总内存（GB）</td><td>15.8</td></tr><tr><td>总交换空间（GB）</td><td>23.3</td></tr><tr><td>硬盘总量（GB）</td><td>74641.9</td></tr></table>

# 3.5.4. JVM
展示 Java 虚拟机（JVM）的版本、厂商等基本信息以及Java进程的堆内存、非堆内存等使用情况。

# 进入 TongWeb JVM 页面
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” > “JVM”，进入 JVM 页面。

# 3.5.4.1. 查看 JVM 使用情况
您可以查看 Java 虚拟机的线程总数、死锁线程数、使用堆内存以及使用中非堆内存等情况。
在监视视图页面，单击鼠标右键，可将监视视图另存为 “.png” 图片。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e4841a3a7de210633b11e8aaad2dc145bb0feae6d23d8c7eff9708c2433fc087.jpg)


# 3.5.4.2. 查看 JVM 版本等基本信息
您可以查看 Java 虚拟机规范名称、版本、JVM 软件名称、JVM 软件供应商、JVM 软件版本号、进程信息、启动时间、引导类路径、系统类路径、本地库路径、启动参数以及最大堆内存。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/5df997bc3f2f0af0fd0e34de4f7b5704d1a7fa164cb852380c4f5e65c8ec7423.jpg)


# 3.5.4.3. 垃圾回收
用户可单击 “垃圾回收”，回收 JVM 垃圾，回收后可查看 JVM 的折线有所变化，可以方便用户排查内存相关问题。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/6887fe6109fcb1184cf9df6f321a00864a0cad745b0fbd851d55bc9d289299d4.jpg)


# 3.5.5. 组合监视
通过配置不同的监视信息，定制您想要关注的监视信息，组合监视可以是一个也可以是多个。

# 3.5.5.1. 创建组合监视
您可以针对您关注的监视信息，创建多个组合监视，以保证监视明细展示更清晰。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “组合监视”，进入组合监视列表页面。
4. 单击 “创建”，进入创建组合监视页面。
组合监视／创建
＊监视信息
X

5. 配置组合监视的名称、监视信息等。
◦ 名称：组合监视的名称。名称约束规则，如下所示。
▪ 不能包含中文以及特殊字符（: $\because 1 < > | ( 0 \# )$ ）。
▪ 不能单独为非法文件名字符，且大小写均会被约束
（CON,PRN,AUX,CLOCK$,NUL,COM1,COM2,COM3,COM4,COM5,COM6,COM7,COM8,COM9,LPT1）。
注：可以与其他字符组合使用，如：abcCON。
◦ 监视信息：在下拉列表中选择需要监视的信息。
您可以监视应用、通道（admin）、通道（server）、JVM、操作系统、系统日志、EJB w3 协议等信息。
请根据选择监视信息，详见组合监视配置参数说明。
6. 配置完成后，单击 “添加”，完成组合监视的添加操作。
若界面弹出 “组合监视添加成功” 提示信息，则说明添加组合监视成功。

# 3.5.5.2. 查看监视明细
组合监视创建完成后，您可以获取组合监视的具体监视量的值，并支持非波动类型（可绘制折线图）数据的采集。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建组合监视。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “组合监视”，进入组合监视列表页面。
4. 单击组合监视所在行的 “监视”，即可查看组合监视的折线图和非折线图。
◦ 折线图
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/b4b010adb8ad1ddca87031c0eda4c1e3928c8e775fb91b8c9d1437bd56d137e6.jpg)
◦ 非折线图
通道(admin)：请求处理总数
通道(admin)：错误请求处理总数
通道(admin)：请求处理总时间 (毫秒)
?通道(admin):接收的字节数
通道(admin)：发送的字节数
③通道(admin):启用的密码套件
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384,TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA,TLS_ECDHE_ECDSA_WITHAES 256 CBC SHA.TLS AES 256 GCM SHA384TLS DHE DSS WITH AES 256 GCM SHA384.TLS DHE DSS WITH AES 256 CBC SHA256,TLS_DHE_DSS_WITH_AES_256_CBC_SHATLS_ECDH_RSA_WITH_AES_256_GCM_SHA384,LS_ECDH_ECDSA_WITH_AES_256_GCMSHA384,TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384,TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384,TLS_ECDH_RSA_WITH_AES_256 CBC SHA.TLS ECDH ECDSA WITH AES 256 CBC SHA,TLS ECDHE RSA WITH AES 128 GCM SHA256.TLS ECDHE ECDSA WITHAES_128_GCM_SHA256LS_ECDHE_RSA_WITH_AES_128_CBC_SHA256TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256TSCHERSA WITH AES 128 CBC SHA.TLS ECDHE ECDSA WITH AES 128 CBC SHA.TLS AES 128 GCM SHA256,TLS DHE DSS WITH AES128_GCM_SHA256TLS_DHE_DSS_WITHAES_128_CBC_SHA256TLS_DHE_DSS_WITHAES_128_CBC_SHATLS_ECDH_RSA_WITHAES_128 GCM SHA256TLS ECDH ECDSA WITH AES 128 GCM SHA256TLS ECDH RSA WITH AES 128 CBC SHA256TLS ECDH ECDSAWITH AES 128 CBC SHA256,TLS ECDH RSA WITH AES 128 CBC SHA,TLS ECDH ECDSA WITH AES 128 CBC SHA

# 3.5.5.3. 管理组合监视
您可以根据需要查看、编辑或者删除创建的组合监视。

# 查看组合监视
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “组合监视”，进入组合监视列表页面。
4. 在组合监视列表页面，您可以查看已创建的组合监视。

# 编辑组合监视
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “组合监视”，进入组合监视列表页面。
4. 单击目标组合监视名称，进入编辑组合监视页面。
5. 您可以根据提示修改组合监视信息。
注：组合监视名称不可编辑。
6. 编辑完成后，单击 “更新”，更新组合监视配置信息。
若界面弹出 “组合监视更新成功” 提示信息，则说明编辑组合监视成功。

# 删除组合监视
删除组合监视时，组合监视引用的其它组件不会被删除。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “组合监视”，进入组合监视列表页面。
4. 单击目标组合监视所在行的 “删除”，弹出确认删除窗口。
注: 用户可根据需要勾选一个或多个创建的组合监视，并单击列表上方的 “删除” 按钮，批量删除组合监视。
5. 单击 “确定”，完成组合监视的删除操作。
若界面弹出 “组合监视删除成功” 提示信息，则说明删除组合监视成功。

# 3.5.6. 守护监视
对创建的组合监视中的系统指标，在指定时间内进行周期性监视，监视结果持久存储在生成的“.txt”文件中。
您可以根据需要在控制台下载监视文件，或者进入 “${tongweb.base}\data\health\monitor” 目录下获取守护监视文件。

# 3.5.6.1. 创建守护监视
创建完成守护监视后，当到达守护监视的开始时间，系统会在 “${tongweb.base}\data\health\monitor” 目录下生成一个以守护监视名称命名的 “.txt” 文件。
所有的监视信息会追加到该 “.txt” 文件中，直到守护监视的结束时间。
您可以根据需要基于同一个组合监视创建多个守护监视。

# 前置条件
已创建组合监视。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “守护监视”，进入守护监视列表页面。
4. 单击 “创建”，进入守护监视页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c9ce98da08ac5d520abaf9873db451e323809b1cfc7b830dca49453050bae783.jpg)


# 5. 配置守护监视的相关参数。
◦ 名称：必填项，守护监视名称，约束规则如下所示。
▪ 不能包含中文以及特殊字符（: $\because 1 < > | ( 0 \# )$
▪ 不能单独为非法文件名字符，且大小写均会被约束（CON,PRN,AUX,CLOCK$,NUL,COM1,COM2,COM3,COM4,COM5,COM6,COM7,COM8,COM9,LPT1）。
注：可以与其他字符组合使用，如：abcCON。
◦ 组合监视：必填项，指定一个组合监视。
◦ 开始时间：必填项，指定守护监视的开始时间。
◦ 结束时间：必填项，指定守护监视的结束时间。
关于守护监视的更多参数说明，详见守护监视配置参数说明。

# 6. 配置完成后，单击 “添加”，完成守护监视创建操作。
若界面弹出 “守护监视添加成功” 提示信息，则说明守护监视创建成功。
在守护监视列表中，可查看已创建的守护监视，包含守护监视名称、组合监视、开始时间、结束时间、监视频率、是否启用、运行中等。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/41a3949ba07995fab6eb0c6b7ef9cfcfdf24a11f8e425ff490e0ef810d6471e0.jpg)


# 3.5.6.2. 查看历史监视信息
用户可查看已创建的守护监视在其指定的时间段内的历史监视信息。

# 注意事项
• 仅创建守护监视时设置的时间段内的监视数据可持久化。
• 不在守护监视时间段内的监视数据会丢失，不在控制台界面显示。
• 用户可通过守护监视查看当前实时的监视信息。

# 前置条件
已创建守护监视。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “守护监视”，进入守护监视列表页面。
4. 单击守护监视所在行的 “监视”，即可进入守护监视查看历史监视信息页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7391da368e6e23268637157f4e8ce9ab6f295d91ce895b1e25db06c0c69abfd5.jpg)
参数说明，如下所示。
◦ 自定义：可查看“自定义”前设置的开始时间与结束时间，时间段内的监视信息。
◦ 过去2小时：可查看当前时间过去的 2 小时内的监视信息。
◦ 过去30分钟：可查看当前时间过去的 30 分钟内的监视信息。
◦ 实时：可查看当前时间，实时监视信息。

# 3.5.6.3. 下载监视文件
守护监视创建完成后，当到达守护监视开始时间，即可生成守护监视 “.txt” 文件。
您可以根据在控制台界面下载守护监视文件，或者进入 “${tongweb.base}\data\health\monitor” 目录获取守护监视文件。

# 注意事项
控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。

# 前置条件
已创建守护监视，且已生成守护监视文件。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “守护监视”，进入守护监视列表页面。
4. 单击 “下载”，弹出下载监视文件窗口。
5. 勾选生成的守护监视文件。
6. 单击 “确定”，即可下载守护监视文件。

# 3.5.6.4. 管理守护监视
用户可以根据需要查看、编辑、删除已创建的守护监视。

# 查看守护监视
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “守护监视”，进入守护监视列表页面。
4. 可查看已创建的守护监视，包含守护监视名称、组合监视、开始时间、结束时间、监视频率、是否启用、运行中等。

# 编辑守护监视
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “守护监视”，进入守护监视列表页面。
4. 单击已创建守护监视的名称，进入守护监视详细信息页面。
5. 可根据需要修改守护监视的相关信息。

# 说明：
◦ 守护监视的名称不可编辑。
◦ 结束时间不能早于当前时间。
6. 单击 “更新”，即可完成守护监视的编辑操作。
若界面弹出“守护监视更新成功”提示信息，则说明更新守护监视信息成功。

# 删除守护监视
删除守护监视后，“${tongweb.base}\data\health\monitor” 目录下的守护监视文件会同步删除。
删除后不可恢复，请谨慎操作。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理” $>$ “守护监视”，进入守护监视列表页面。
4. 单击已创建守护监视所在行的 “删除”，弹出确认删除窗口。

# 说明：
用户可根据需要勾选一个或多个守护监视，并单击列表上方的 “删除” 按钮，批量删除守护监视。
5. 单击 “确定”，即可完成守护监视的删除操作。
守护监视删除后，“${tongweb.base}\data\health\monitor” 目录下对应的守护监视 “.txt” 文件会同步删除。

# 3.5.7. SNMP 服务
SNMP 是广泛应用于 TCP/IP 网络的网络管理标准协议，该协议能够支持网络管理系统，用以监测连接到网络上的设备是否有任何引起管理上关注的情况。
TongWeb 支持SNMP服务。开启SNMP服务后,可以通过SNMP工具查看 TongWeb 的服务器状态信息。
通过 SNMP 管理端获取 TongWeb 的监控数据。
支持 GET、GETBULK 调用，以 json 格式返回数据。

# 3.5.7.1. OID 与监控数据对应关系
• 1.3.6.1.4.1.55566.1.0：操作系统信息；
• 1.3.6.1.4.1.55566.1.1：Java虚拟机信息；
• 1.3.6.1.4.1.55566.
• 1.2：Java类加载信息；
• 1.3.6.1.4.1.55566.1.3：Java编译信息；
• 1.3.6.1.4.1.55566.1.4：Java线程信息；
• 1.3.6.1.4.1.55566.1.5：连接池信息；
• 1.3.6.1.4.1.55566.1.6：线程池信息；
• 1.3.6.1.4.1.55566.1.7：应用线程信息(线程个数、的状态)；
• 1.3.6.1.4.1.55566.1.8：服务信息(包含授权信息)。

# 3.5.7.2. 启用SNMP服务
在 TongWeb 开启 SNMP 服务后,您即可通过SNMP工具查看 TongWeb 的服务器状态信息。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “监视管理”> “SNMP 服务”，进入 SNMP 服务页面。
4. 在基本属性页签下，单击 “开启” 按钮，开启 SNMP 服务。

# SNMP 服务@／编辑

# 基本属性

# 身份认证

# 数据安全
*启用
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/b1435532aea1d0028106af6b9d1c5900429eeaaa27471edfc0c404160095c8e1.jpg)
*监听地址
127.0.0.1
*监听端口
161
*引擎ID0
62:a0:c1:81:11:c3:17:33

# 5. 配置基本属性参数，如下所示。
<table><tr><td>参数</td><td>参数说明</td></tr><tr><td>监听地址</td><td>SNMP 服务监听的 IP 地址，默认为“127.0.0.1”，即监听 TongWeb 所在的本机 IP。
若配置为“0.0.0.0”，则表示不限制，监听本机所有IP。</td></tr><tr><td>监听端口</td><td>SNMP监听的端口号，默认为“161”。</td></tr><tr><td>引擎ID</td><td>设置当前 SNMP 服务的唯一标识。配置为您本地设备的引擎 ID。
引擎 ID 是十六进制数字串，并且长度为14~32个十六进制数。
设备信息可以是 IP 地址、mac 地址或自己定义的十六进制数字串。</td></tr></table>

# 6. 配置监听的客户端的身份认证信息，如下所示。
<table><tr><td>参数</td><td>参数说明</td></tr><tr><td>认证名</td><td>客户端的认证名，用以识别客户端的身份（用于SNMP客户端连接SNMP服务的认证用户名，用户自定义）。</td></tr><tr><td>认证密码</td><td>客户端的认证密码，用以验证客户端的安全性（用于SNMP客户端连接SNMP服务的认证密码，用户自定义）。</td></tr><tr><td>认证算法</td><td>设置验证密码采用的摘要算法。支持的算法为“MD5”和“SHA-1”。</td></tr></table>
7. 配置数据安全信息，如下所示。
<table><tr><td>参数</td><td>参数说明</td></tr><tr><td>传输协议</td><td>SNMP代理服务器与网络管理系统之间所使用的传输协议。支持“UDP”和“TCP”。</td></tr><tr><td>加密算法</td><td>设置数据加密采用的算法。支持“AES128”和“DES”。</td></tr><tr><td>加密密码</td><td>设置数据加密的密码。</td></tr></table>
8. 单击 “更新”，即完成 SNMP 服务的启动操作。
若界面弹出 “SNMP 服务更新成功”，则说明更新 SNMP 服务成功。

# 3.5.7.3. 使用 Snmpwalk 查看 TongWeb 服务器信息
1. 下载 Snmpwalk。
下载地址：https://ezfive.com/snmpsoft-tools/。
2. 使用 Snmpwalk 查看 TongWeb 服务器信息：
当前 SNMP 服务支持的版本为 V2 和 V3，不支持 V1。

# 示例说明：
查看 OID 为 “1.3.6.1.4.1.55566.1.4” 的 Java 线程信息。
注：OID 值请进入管理控制台> “集中管理” > “扩展支持” > “支持列表”。单击 “SNMP”，进入 SNMP 使用说明页面，获取 OID 值。
```batch
SnmpWalk.exe -r:127.0.0.1 -p:161 -v:3 -sn:tongweb -aw:TongWeb@12.com -ap:SHA -pp:DES -pw:TongWeb@12.com1 -ei:62a0c18111c31733 -os:1.3.6.1.4.1.55566.1.4
```
参数说明，如下所示。
<table><tr><td>参数</td><td>说明</td></tr><tr><td>-r</td><td>SNMP 服务器监控的 IP 的地址，默认为“127.0.0.1”，即监听 TongWeb 所在的本机 IP。</td></tr><tr><td>-p</td><td>SNMP 监听的端口号，默认为“161”。</td></tr><tr><td>-v</td><td>SNMP 服务支持的版本，当前支持 V2 和 V3。如 V3 版本配置为“-v:3”。</td></tr><tr><td>-sn</td><td>客户端的认证名，用以识别客户端的身份（开启 SNMP 服务时，配置的认证名，用于连接 SNMP 服务端）。</td></tr><tr><td>-aw</td><td>客户端的认证密码，用以验证客户端的安全性（开启 SNMP 服务时，配置的认证密码，用于连接 SNMP 服务端）。</td></tr><tr><td>-ap</td><td>验证密码采用的摘要算法。</td></tr><tr><td>-pp</td><td>数据加密采用的算法。</td></tr><tr><td>-pw</td><td>加密数据的密码。</td></tr><tr><td>-ei</td><td>引擎 ID。</td></tr><tr><td>-os</td><td>OID 值。</td></tr></table>
返回结果如下所示。
```txt
PS D:\work\Env\SnpWalk>./.SnpWalk.exe -r:127.0.0.1 -p:161 -v:3 -sn:tongweb -aw:TongWeb@12.com -ap:SHA -pp:DES -pw:TongWeb@12.com1 -ei:62a0c18111c31733 -os
1.3.6.1.4.1.55566.1.4
SnpWalk v1.01 - Copyright (C) 2009 SnnpSoft Company
[ More useful network tools on http://www.snpsoft.com ]
OID=.1.3.6.1.4.1.55566.1.5, Type=OctetString, Value={'peakThreadCount":"62","totalStartedThreadCount":"102","threadCount":"59"} 
OID=.1.3.6.1.4.1.55566.1.6, Type=OctetString, Value={' }
OID=.1.3.6.1.4.1.55566.1.7, Type=OctetString, Value={'Connector':{'activeCount":"0","name":"admin","poolSize":"5"}},'name":"server","pool Size":"10”] }} 
OID=.1.3.6.1.4.1.55566.1.8, Type=OctetString, Value={' }
OID=.1.3.6.1.4.1.55566.1.9, Type=OctetString, Value={'consumer_name":"tongtech","end_date":"2022-12-31","TW Version_Number":"8.0","TW_Product_Name":"TongWeb"
",javaHome":"D:\Program Files\Java\jdk1.8.0.281","TW_Edition":"Full","tongwebHome":"D:\work\Env\TW8\tongweb_2022-10-17\tongweb","license_type":"Enterprise"
",bindip":"","dTongWeb","dTongBase":"D:\work\Env\TW8\tongweb_2022-10-17\tongweb\domains\domain1"]}
Total: 5
```

# 3.5.8. Prometheus 监控

# 3.5.8.1. 背景信息
Prometheus、PushGateway、Exporter 和 Grafana 是常用的监控和可视化工具，它们之间的关系如下所示。
• Prometheus：是一个开源的监控系统，用于对系统和服务的状态进行实时监控。Prometheus 使用 Pull模式来获取监控指标数据，从各个监控目标（通常是服务、应用程序或主机）定期拉取数据，并存储在时间序列数据库中。
• Exporter：Exporter 是一个用于从不同系统和服务中提取监控指标数据并暴露为 Prometheus 可以抓取的格式的工具。Exporter 可以作为单独的进程运行，通过暴露 HTTP 端点的方式将指标数据提供给Prometheus。常见的 Exporter 包括 Node Exporter（用于主机监控）、MySQL Exporter、RedisExporter 等。
• PushGateway：PushGateway 是一个 Prometheus 的中间件，用于接收短期任务实例产生的指标数据，然后让 Prometheus 可以拉取这些数据。通常用于临时任务或者短暂性的指标数据收集，不适合用于
持久性的存储。
• Grafana：是一个开源的数据可视化工具，用于创建、展示和监控数据仪表盘。Grafana 可以与Prometheus 进行集成，通过 Prometheus 数据源来查询和展示 Prometheus 中的监控数据，并通过创建仪表盘来可视化这些数据。Grafana 提供了丰富的图表和面板，用户可以自定义展示监控数据的方式，实现更直观的监控和分析。
因此，Prometheus 负责采集、存储监控数据，Exporter 用于提取并暴露各种数据源的监控数据，PushGateway 用于接收临时任务产生的指标数据，而 Grafana 则用于可视化展示 Prometheus 中的监控数据，从而实现全面的监控和分析。通过这些工具的配合使用，可以构建一个强大和灵活的监控系统。

# 3.5.8.2. 下载并安装 Prometheus
Prometheus 为免安装版本，解压即安装。
1. 下载 Prometheus。
2. 解压 Prometheus。

# 3.5.8.3. 启用 Prometheus 监控服务
开启 Prometheus 监控服务后，可以通过 Prometheus 控制台查看 TongWeb 的服务器监控信息。

# 注意事项
• 支持组合监视（用以限定监视系统的指标范围）或注册实例（注册实例为 Prometheus 提供监视数据，并推送注册实例信息）。
◦ 关于组合监视，详见 组合监视。
◦ 关于注册实例，详见 注册实例。
• 启用 Prometheus 服务时，数据上报方式支持 “拉取” 和 “推送”。
若选择 “推送” 方式，则需要提前搭建好 PushGateway 服务。
下载解压后，直接启动即可完成 PushGateway 的搭建操作。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/0d2a7c341b508ff1f6a92fd996412541268abbb5d51d92460916c9bb0272fafe.jpg)


# 前置条件
已 创建组合监视 或 注册实例。

# 操作步骤
1. 选择 “监视管理” $>$ “Prometheus 服务”，进入 Prometheus 服务页面。
2. 打开 “启用” 开关，启用服务。
3. 选择创建的组合监视，或者打开 “监视注册实例” 开关。

# 说明：
“组合监视” 为空时，表示监视所有受管实例的系统默认指标。
4. 选择并配置上报方式。
◦ “拉取” 方式上报数据
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a1b1bad29cd415a248af06930e7bfbb203c83813799a37edff2485c6b857e357.jpg)
a. 监听地址：填写为 TongWeb 本机的 IP 地址。
b. 监听端口：填写为将要开启监听服务的端口号。
c. metrics 地址：填写为监听服务的 metrics 路径。可根据需要以逗号分隔设置多个。
d. 认证类型：可选。
若选择“基础认证”，则需要配置认证的用户名和密码。用户名和密码配置请参见修改 prometheus配置文件。
◦ “推送” 方式上报数据
若选择 “推送” 方式上报数据，需要已搭建好 PushGateway 服务。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/378806492a699f2c3382bfc9fbd7d5e62642d5470462d5b571b5ccc555f3af8f.jpg)
a. PushGateway 地址：填写推送的目标服务(PushGateway)的地址。
不带 “http://” 等协议头，只需填写 IP/域名 $^ +$ 端口号(若有端口号)即可。
b. 推送间隔：设置每间隔多长时间推送一次数据。
5. 单击 “更新”，即完成对 Prometheus 监控的支持。
若界面弹出 “Prometheus 监控更新成功”，则说明更新成功。

# 3.5.8.4. 使用 Prometheus 查看 TongWeb 的监控信息
1. 修改 Prometheus 的配置文件 “prometheus.yml”。
启用 Prometheus 时，选择的上报方式不同，添加的配置则不同，如下所示。
◦ 若选择为 “拉取” 方式，则在配置文件最后，添加如下配置。

#拉取方式
```yaml
- job_name: "tongweb"
- staticconfigs:
  - targets: ["127.0.0.1:30188"]
```
targets 中的 IP 和端口对应 TongWeb 控制台启用 Prometheus 时，配置的 IP 和端口号。
若在 TongWeb 控制台配置启动 Prometheus 时，选择 “基础认证”，则需要在 Prometheus 的配置文件 “prometheus.yml”，添加如下配置信息。
```yaml
basic_auth: username: admin password:admin
```
完整的配置参考，如下所示。

#拉取方式
```yaml
- job_name: "tongweb"  
staticconfigs:  
    - targets: ["127.0.0.1:30188"]  
basic_auth:  
    username: admin  
    password: admin
```
完整的配置参考，如下图所示。
scrapeconfigs: #The job name is added as a label .job  $=$  <job_name> to any timeseries scraped from this config. -job_name:"prometheus" #metrics_path defaults to '/metrics' #scheme defaults to 'http'. staticconfigs: --targets:["localhost:9090"] #拉取方式 -job_name:"monitor_tongweb" staticconfigs: --targets:["127.0.0.1:30188"] basic_auth: username:admin password:admin
◦ 若选择为 “推送” 方式，则在配置文件最后，添加如下配置。

#推送方式
```yaml
- job_name: "monitor.pushGateway"  
staticConfigs:  
- targets: ["127.0.0.1:9091"]
```
targets 中的 IP 和端口对应 TongWeb 控制台启用 Prometheus 时，配置的 IP 和端口号。
配置参考，如下图所示。
```txt
21 scrapeConfigs: # The job name is added as a label 'job=<job_name>' to any timeseries scraped from this config.  
23 - job_name: "prometheus"  
24 metrics_path defaults to '/metrics'  
25 # metrics_path defaults to 'http'.  
26 # scheme defaults to 'http'.  
27 staticconfigs:  
28 targets: ["localhost:9090"]  
30 #拉取方式  
31 # - job_name: "monitor_tongweb"  
32 # staticConfigs:  
33 # - targets: ["127.0.0.1:30188"]  
34 # basic_auth:  
35 # username: admin  
36 # password: admin  
37 #推送方式  
38 #推送方式  
39 - job_name: "monitor.pushGateway"  
40 staticConfigs:  
41 - targets: ["127.0.0.1:9091"]
```
2. 启动 Prometheus。
```txt
./prometheus --config.file=prometheus.yml
```
3. 在浏览器地址栏中输入如下信息，即可访问 Prometheus 控制台查看 TongWeb 的监视信息。
```txt
http://localhost:9090/targets?search=
```

# 3.5.8.5. 查看 Prometheus 访问 TongWeb 的日志
Prometheus 访问 TongWeb 的日志记将录到访问日志中，路径为 “${tongweb.base}/logs/access” ，格式与现有访问日志保持一致。

# 3.5.9. OTLP 支持
OTLP 是一个用于传输跟踪和度量数据的开放标准协议，TongWeb 开启支持 OTLP，可将其自身监视数据以约定的格式输出。

# 前置条件
• 请先参考 “集中管理” $>$ “扩展支持” $>$ “支持列表” 里 “OTLP” 的使用说明，下载必需的 jar 包等。
```txt
opentelemetry-api-1.42.1.jar  
opentelemetry-context-1.42.1.jar  
opentelemetry-exporter-common-1.42.1.jar  
opentelemetry-exporter-otlp-1.42.1.jar  
opentelemetry-exporter-otlp-common-1.42.1.jar  
opentelemetry-exporter-server-okhttp-1.42.1.jar
```
```txt
opentelemetry-sdk-1.42.1.jar  
opentelemetry-sdk-common-1.42.1.jar  
opentelemetry-sdk-metrics-1.42.1.jar  
opentelemetry-sdk-extension-autoconfigure-spi-1.42.1.jar  
opentelemetry-sdk-trace-1.42.1.jar  
opentelemetry-api-incubator-1.42.1-alpha.jar  
opentelemetry-sdk-logs-1.42.1.jar  
okhttp-4.12.0.jar  
kotlin-standardlib-1.8.21.jar  
okio-3.6.0.jar  
okio-jvm-3.6.0.jar
```
• 已创建组合监视。
说明：
若组合监视中包含 JVM 相关信息，兼容 JVM 监视中的特殊字符。

# 操作步骤
1. 下载 1.42.1 版本需要的 jar 清单。
2. 将下载的 jar 包存放到 “${tongweb.home}/lib” 或 “${tongweb.base}/lib” 目录。
3. 启动 TongWeb，并访问控制台。
4. 开启 OTLP 服务。
a. 在左侧菜单栏中，选择 “监视管理” $>$ “OTLP 支持”，进入 OTLP 支持页面。
b. 打开 “启用” 开关。
c. 配置 OTLP 相关属性。
<table><tr><td>属性</td><td>说明</td></tr><tr><td>组合监视</td><td>在下拉列表中，选择已创建的组合监视。
若下拉列表中没有创建的组合监视，详见创建组合监视。</td></tr><tr><td>接收数据的地址</td><td>将数据推送到支持的OTLP的地址，默认为“http://localhost:4317”。</td></tr><tr><td>推送间隔</td><td>设置每隔多少秒推送一次数据，单位：秒。</td></tr></table>
d. 配置完成后，单击 “更新”，即完成 OTLP 支持的启用操作。
5. 访问配置的 “接收数据的地址”（如 “http://localhost:4317”），即可查看 TongWeb 监视数据。

# 3.6. 诊断管理

# 3.6.1. 采集模板
快照记录某一时刻 TongWeb 的整体信息，采集模板指明了这个整体信息锁包含的内容。
不同的采集模板可以满足某时间段或者某时刻堆 TongWeb 信息不同维度的记录。
快照文件是基于采集模板而生成，采集模板里定义快照文件的具体内容。

# 支持的分析工具：
“jstack”、“jmap”、“coredump”、“top”、“lsof”、“netstat”。

# 仅 Linux 平台有效的分析工具：
“coredump”、“top”、“lsof”、“netstat”。

# 日志类型
服务器日志、访问日志、GC 日志、hs_err日志。

# hs_err 日志说明
hs_err 日志文件是 Java HotSpot（TM） 虚拟机（JVM）生成的一种日志，通常出现在 Java 应用程序发生错误时，如遇到未捕获的异常或内部错误。这些日志文件包含了 JVM 的堆栈跟踪信息、异常信息、JVM 状态以及其他可能有助于诊断问题的详细信息。
hs_err 日志文件通常位于 Java 应用程序的工作目录，或者由 JVM 的 -XX:ErrorFile 参数指定的位置。
快照仅记录 TongWeb 域目录下的日志文件。因此，若需要记录 hs_err 日志，则需要将 hs_err 日志文件指定到 TongWeb 域目录下。

# 3.6.1.1. 创建采集模板
系统提供一个默认的基于 “jstack” 分析工具的采集模板（default，默认配置 “服务器日志” 和 jstack、top分析工具）供用户使用，用户可以根据需要对该模板进行编辑或删除等。
用户也可以根据需要创建不用的采集模板。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “采集模板”，进入采集模板列表页面。
4. 单击 “创建”，进入创建采集模板页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/786f84f8064feec3ce6d1906574acf847b14b953eca47509cd0757f2ca6ce3e0.jpg)
5. 配置采集模板的相关参数。
名称：必填项，采集模板的名称，需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。关于采集模板的更多参数说明，详见采集模板配置参数说明。
6. 配置完成后，单击 “添加”，完成采集模板的添加操作。
若界面弹出 “采集模板添加成功” 提示信息，则说明添加采集模板成功。

# 3.6.1.2. 应用采集模板

# 打快照
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “快照文件”，进入快照文件页面。
4. 单击 “打快照”，进入打快照页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/dcf7e49dd8dd511a4cde3a22d314e8f7586f35259d77c12847057ef9251d340b.jpg)
5. 在采集模板下拉列表中，选择已创建的采集模板。
6. 配置完成后，单击 “打快照”，即完成采集模板的应用操作。

# 3.6.1.3. 管理采集模板
用户可根据需要查看、编辑或删除采集模板。

# 查看采集模板
1. 在左侧导航栏中，选择 “诊断管理” $>$ “采集模板”，进入采集模板列表页面。
2. 在采集模板列表页面，您可以查看已创建的采集模板。
包含采集模板名称、配置信息、日志、分析工具、描述等信息。

# 编辑采集模板
1. 在左侧导航栏中，选择“诊断管理”>“采集模板”，进入采集模板列表页面。
2. 单击目标采集模板名称，进入编辑采集模板页面。
3. 您可以根据提示修改采集模板信息。
注：采集模板名称不可编辑。
4. 编辑完成后，单击 “更新”，更新采集模板配置信息。
若界面弹出 “采集模板更新成功” 提示信息，则说明编辑采集模板成功。

# 删除采集模板
删除采集模板时，采集模板引用的其它组件不会被删除。
1. 在左侧导航栏中，选择 “诊断管理” $>$ “采集模板”，进入采集模板列表页面。
2. 单击目标采集模板所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个采集模板，并单击列表上方的 “删除” 按钮，批量删除采集模板。
3. 单击 “确定”，完成采集模板的删除操作。
若界面弹出 “采集模板删除成功” 提示信息，则说明删除采集模板成功。

# 3.6.2. 快照文件
快照文件记录了某一时刻 TongWeb 服务器的整体信息，记录的内容可包括监视信息、配置信息、TongWeb 域目录下相应的日志文件，并生成指定分析工具的文件等。
采集模板对应生成的快照文件，如下所示。
<table><tr><td>勾选参数</td><td>生成的快照文件</td></tr><tr><td>基本信息</td><td>basicinfo.xml 文件。</td></tr><tr><td>监视信息</td><td>monitor.xml 文件。</td></tr><tr><td>配置信息</td><td>conf 文件夹或 bin 文件夹。
可下载“\$\{tongweb.base\}/conf”目录下的 xml 类型的文件。
若存在“\$\{tongweb.home\}/bin/JAVA_HOME.txt”，则会同时生成 JAVA_HOME.txt，并存放在“bin”文件夹。</td></tr><tr><td>日志</td><td>logs 文件夹
根据采集模板生成的快照日志文件，包含 server.log、access.log、gc.log。
·access.log、gc.log：需要开启访问日志和 GC 日志才会生成。
·hs_err.pid.log：需要将 hs_err 日志文件路径配置到 TongWeb 域目录下才可记录。</td></tr><tr><td>分析工具 jstack</td><td>jstack.txt 文件。</td></tr><tr><td>分析工具 jamp</td><td>heap.hprof 文件。</td></tr><tr><td>分析工具 coredump</td><td>coredump 文件。</td></tr><tr><td>分析工具 top</td><td>top.txt 文件。</td></tr><tr><td>分析工具 Isof</td><td>Isof.txt 文件。</td></tr><tr><td>分析工具 netstat</td><td>netstat.txt 文件。</td></tr></table>
当系统出现故障或者性能瓶颈，没来得及获取需要的信息时，可根据快照记录的全面内容分析故障、性能瓶颈的原因。
您可以根据需要手动创建快照文件，或者通过创建预警策略基于快照模块自动创建快照文件。

# 3.6.2.1. 打快照
本章节介绍如何打快照。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建采集模板。

# 手动打快照
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “快照文件”，进入快照文件列表页面。
4. 单击 “打快照”，进入打快照页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c20b3a2ca9eae3e321c4ae2c515859710ba58f92343a7f66aaee77cfd9dde436.jpg)


# 5. 配置快照文件的相关参数。
采集模板：选择已创建的采集模板。若您没有创建采集模板，请先创建采集模板。
关于采集模板的更多参数说明，详见快照文件配置参数说明。
6. 配置完成后，单击 “打快照”，完成打快照操作。
若界面弹出 “快照文件打快照成功” 提示信息，则说明打快照成功。

# 自动打快照
满足创建的预警策略自动打快照。
1. 登录 TongWeb 管理控制台。
2. 左侧导航栏中，选择 “诊断管理” $>$ “预警策略”，进入预警策略列表页面。
3. 单击 “创建”，进入创建预警策略页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d7bc81a78e61e952cd065dfe2d133af71feaba30facf0b0aefea31188f8c896b.jpg)
4. 在 “生成快照” 下拉列表中，选择已创建的采集模板。
其他参数，请根据需要进行配置。
5. 配置完成后，单击 “添加”，完成预警策略的创建。
若界面弹出 “预警策略添加成功” 提示信息，则说明预警策略添加成功。
6. 若系统触发已创建的预警策略，您可以在左侧导航栏中，单击“快照文件”，进入快照文件列表页面，查看自动打的快照。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c583957cb8e8ca9ad6cfe9610046010dbb704db20751d27505c09bf62e6fb89c.jpg)


# 3.6.2.2. 下载快照文件
本章节介绍如何下载快照文件。

# 注意事项
控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。

# 前置条件
• 已获取系统管理员账号和密码。
• 已打快照。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” > “快照文件”，进入快照文件列表页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/51d244da61bda4cb5d611cde3bf396147b352fe881b94f6c96e20b47f69dd871.jpg)
4. 单击目标快照文件所在行的 “下载”，弹出下载快照文件窗口。
5. 勾选待下载的快照文件。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/2d86258ca8e05b21a0be7ef45c18b1066fe1920e5011006ae24382147ebbef85.jpg)
6. 单击 “确定”，即可下载以快照时间命名的快照文件压缩包。

# 3.6.2.3. 管理快照文件
用户可根据需要查看、编辑或者删除快照文件。

# 查看快照文件
生成的快照文件按照生成快照的时间倒序展示。
1. 在左侧导航栏中，选择 “诊断管理” $>$ “快照文件”，进入快照文件列表页面。
2. 在快照文件列表页面，您可以查看已打的快照。
包含快照时间、是预警快照、预警策略名等信息。

# 删除快照文件
删除快照文件时，快照文件引用的其它组件不会被删除。
1. 在左侧导航栏中，选择 “诊断管理” $>$ “快照文件”，进入快照文件列表页面。
2. 单击目标快照文件所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个快照文件，并单击列表上方的 “删除” 按钮，批量删除快照文件。
3. 单击“确定”，完成快照文件的删除操作。
若界面弹出 “快照文件删除成功” 提示信息，则说明删除快照文件成功。

# 3.6.3. 预警策略
通过配置 CPU、内存、通道活跃链接、数据源活跃连接的阈值和GC时间的阈值，决定预警策略是否生效，以及生效后的处理办法，包括发送邮件、发送消息到队列、自动生成快照。
预警策略可以启动也可以设置多个，一个预警策略只有所有阈值都被超过才触发处理办法。

# 3.6.3.1. 创建预警策略
本章节介绍如何创建预警策略。

# 前置条件
• 已获取系统管理员账号和密码。
• 已创建采集模板。
• 至少满足以下任一预警条件：CPU 阈值大于 0、内存阈值大于 0、通道阈值大于 0 且至少选一个通道、数据源阈值大于0且至少选一个数据源或 GC 时间大于 0。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “预警策略”，进入预警策略列表页面。
4. 单击 “创建”，进入创建预警策略页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/61b19f670423e5ebefce6325825ab709351545ca76f6e11bf4df1bc1c8629319.jpg)


# 5. 配置预警策略的相关参数。
◦ 名称：必填项，预警策略的名称，需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 处理办法：“处理办法” 页签的配置说明，如下表所示。
<table><tr><td>参数</td><td>说明</td></tr><tr><td>生成快照</td><td>若需要生成快照，下拉列表中没有采集模板，请先创建采集模板。</td></tr><tr><td>发送JMS消息</td><td>若开启JMS通知，需要配置连接池和托管对象。请先创建连接池&amp;托管对象。..进入“EJB 容器”&gt;“JCA连接池”，创建jca连接池。..进入“EJB 容器”&gt;“JCA托管对象”，创建jca托管对象。</td></tr></table>
关于预警策略的更多参数说明，详见预警策略配置参数说明。
6. 配置完成后，单击 “添加”，完成预警策略的添加操作。
若界面弹出 “预警策略添加成功” 提示信息，则说明添加预警策略成功。

# 3.6.3.2. 管理预警策略
用户可查看、编辑或者删除已创创建的预警策略。

# 查看预警策略
1. 在左侧导航栏中，选择 “诊断管理” $>$ “预警策略”，进入预警策略列表页面。
2. 在预警策略列表页面，您可以查看已创建的预警策略。
包含预警策略的名称、是否启用、描述等信息。

# 编辑预警策略
1. 在左侧导航栏中，选择“诊断管理”>“预警策略”，进入预警策略列表页面。
2. 单击目标预警策略名称，进入编辑预警策略页面。
3. 您可以根据提示修改预警策略信息。
注：预警策略名称不可编辑。
4. 编辑完成后，单击 “更新”，更新预警策略配置信息。
若界面弹出 “预警策略更新成功” 提示信息，则说明编辑预警策略成功。

# 删除预警策略
删除预警策略时，预警策略引用的其它组件不会被删除。
1. 在左侧导航栏中，选择 “诊断管理” $>$ “预警策略”，进入预警策略列表页面。
2. 单击目标预警策略所在行的 “删除”，弹出确认删除窗口。
注: 用户可根据需要勾选一个或多个预警策略，并单击列表上方的 “删除” 按钮，批量删除预警策略。
3. 单击 “确定”，完成预警策略的删除操作。
若界面弹出 “预警策略删除成功” 提示信息，则说明删除预警策略成功。

# 3.6.3.3. 示例说明（慢 SQL 数阈值）
1. 进入 “Web 容器” > “数据源”，创建数据源（如：testdb）。
创建数据源时，在数据源的 “语句管理” 页签，开启 “监视慢 SQL”。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/375767ef15a1fdd0748bdc9cb26ed17647f8a9fa38c773e769518393e4f51e41.jpg)
2. 进入 “诊断管理” $>$ “采集模板”，创建采集模板（如：shottemplate）。
注： “监视信息” 选择 “数据源” $>$ “慢 SQL 数”。
3. 进入 “诊断管理” $>$ “预警策略”，创建预警策略，
◦ 基本属性
▪ 名称：输入预警策略名称。
▪ 是否启用：开启“是否启用”，开启后才能启动预警策略。
◦ 触发条件
▪ 数据源慢 SQL 数：设置慢 SQL 数的阈值，大于0时系统根据设置的阈值，触发预警。
▪ 监控慢 SQL 数的数据源：阈值大于 0 时生效，并勾选需要监视的数据源。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/942f0d12944a06aae65cf6926163622b23a4873c7bab0034ea2569561d97413f.jpg)


# ◦ 处理办法
▪ 生成快照：选择已创建的采集模板（如：shottemplate）。
▪ 保留文件个数：根据需要配置。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/61315ffa3dfa3cd7c140003aca30e72983a5bdefb5c3819f9d3283ceadcaeb84.jpg)
4. 单击 “添加”，完成预警策略的创建。
若触发预警条件，即可进入 “诊断管理” > “快照文件”，下载预警快照生成的快照文件。

# 3.6.4. 死锁线程
汇总死锁的线程，可查看死锁等待对象监视器或者同步器的线程栈，并可尝试中断死锁的线程。

# 3.6.4.1. 查看死锁线程

# 进入 TongWeb 死锁线程页面
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “死锁线程”，进入死锁线程页面。

# 查看死锁线程列表
您可以查看死锁线程的线程 ID、线程名、线程状态、等待的锁、锁占有线程ID、锁占有线程名等信息。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/2bad361bf4b44f0127947900ea3770af41e1d4d3f4c5df0032414431f0749f7e.jpg)


# 查看堆栈信息
单击目标线程的线程 ID，您可以查看该死锁线程的信息，包括其死锁的堆栈等。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/be9be0f1c3d96c2daefb43feef26b4ab9c6078ad7e5a9f1e6ec6ecdaed819ea2.jpg)


# 3.6.4.2. 强停死锁线程
仅线程状态处于 “WAITING” 或者 “TIMED_WAITING” 的线程，才能强停。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “死锁线程”，进入死锁线程页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/8d9e73b731d79ae7188f7022d8c9fa31f2e049be6f3b76f1d076d57b3a328daa.jpg)
4. 单击目标线程所在行的“强停”，弹出确认强停死锁线程窗口。
注：用户可根据需要勾选一个或多个死锁线程，并单击列表上方的 “强停” 按钮，批量强停死锁线程。
5. 单击 “确定”，即可停止线程。

# 3.6.5. 阻塞线程
您可以查看阻塞的堆栈及相同堆栈上阻塞的线程。

# 注意事项
• 开启 EJB w3 协议后，默认的监听线程将从阻塞线程列表移除。
• 若使用 JVisualVM（Java 虚拟机的监控工具）连接后，RMI 连接线程将从阻塞线程列表移除。

# 3.6.5.1. 查看阻塞线程
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “阻塞线程”，进入阻塞线程页面。
4. 您可以查看阻塞的堆栈及相同堆栈上阻塞的线程。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/fe116585fa8aaa1fa42ef6a3631256d2c8c4e978d083b85ac1c659eac5e041a1.jpg)
5. 单击阻塞线程 ID，可查看阻塞线程的详细信息。

# 阻塞线程／查看
线程ID 105
线程名 Abandoned connection cleanup thread
? 线程状态 TIMED WAITING
 线程栈 com.mysql.cj.jdbc.AbandonedConnectionCleanupThread.run(AbandonedConnectionCleanupThread.java:70) java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) java.lang.Thread.run(Thread.java:748)
® 阻塞方法  java.lang.Object.wait(Native Method)
? 相同阻塞线程数 1
相同阻塞线程 Abandoned connection cleanup thread
 支持强停 true

# 3.6.5.2. 强停阻塞线程
支持强制停止阻塞线程。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “阻塞线程”，进入阻塞线程页面。

# 阻塞线程／列表☆
Q搜索

# 序号 线程ID 线程名

# 线程状态

# 阻塞方法

# 相同阻寒线程数

# 操作
1

Abandoned connection cleanup thread
TIMED_WAITING
 java.lang.Object.wait(Native Method)
1

×强停
4. 单击目标线程所在行的 “强停”，弹出确认强停阻塞线程窗口。
注：用户可根据需要勾选一个或多个阻塞线程，并单击列表上方的 “强停” 按钮，批量强停阻塞线程。
5. 单击 “确定”，即可停止阻塞线程。

# 3.6.6. 忙碌线程
检测忙碌的线程，可查看线程 ID、信息、CPU 耗时、线程状态等信息。

# 3.6.6.1. 查看忙碌线程
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “忙碌线程”，进入忙碌线程页面。
4. 您可以查看线程 ID、信息、CPU 耗时以及线程状态等。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/5dcc680b113524c8db59a47e98680704f64c6cd6261e189ca053160de60f049f.jpg)
5. 您可以在忙碌线程列表上方基于线程 ID、信息、CPU 耗时或者线程状态筛选指定线程。
支持筛选线程状态，线程状态包含
NEW、RUNNABLE、BLOCKED、WAITING、TIMED_WAITING、TERMINATED。
6. 单击忙碌线程名，可查看忙碌线程的详细信息。

# 忙碌线程／查看
线程ID
1

? 信息
 main
 CPU耗时 (ms)
4031.0
 线程状态
TIMED WAITING
? 线程栈
 java.lang.Thread.sleep(Native Method)
com.tongweb.server.core.StandardServer.await(StandardServer.java:593)
com.tongweb.main.TongWeb.await(TongWeb.java:480)
com.tongweb.main.TongWeb.start(TongWeb.java:436)
sun.reflect.NativeMethodAccessorlmpl.invoke0(Native Method)
sun.reflect.NativeMethodAccessorlmpl.invoke(NativeMethodAccessorlmpl.java:62)
 sun.reflect.DelegatingMethodAccessorlmpl.invoke(DelegatingMethodAccessorlmpl.java:43)
 java.lang.reflect.Method.invoke(Method.java:498)
 com.tongweb.main.TongWebMain.main(Unknown Source)

# 3.6.7. 数据库连接
汇总和管理数据库连接池中的活跃连接对象，可对检测为泄漏的数据库连接进行手动回收。

# 3.6.7.1. 查看数据库连接
可查看数据库连接池中活跃的连接对象，包含连接对象哈希码、所属数据源、连接建立时间、使用中以及已
标记泄漏等。

# 前置条件
已创建数据源且该数据源已被相关应用调用。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 选择 “诊断管理” $>$ “数据库连接”，进入数据库连接页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/99e40b2a5aec0fb56ba2a99c379bf6540e86603e4ecdf0df453f68f579204c53.jpg)
4. 用户可查看数据库连接的相关信息。
5. 用户还可以输入连接对象哈希码、所属数据源、连接建立时间，或者在 “使用中”、“已标记泄漏” 下拉列表中选择 “true” 或 “false”，筛选指定数据库连接。

# 3.6.7.2. 回收数据库连接
支持手动回收检测为泄漏的数据库连接。

# 前置条件
• 已创建数据源且该数据源已被相关应用调用。
• 请确保数据源的 “健康管理” 页签中，已开启 “检查连接泄漏” 开关。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 选择 “诊断管理” $>$ “数据库连接”，进入数据库连接页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7d1153fc3d227057f8caebb768120528251bc03b40d0a91fcf8e88772b32fec4.jpg)
4. 单击目标数据库连接所在行的 “回收”，弹出确认是否回收数据库连接窗口。
5. 单击 “确定”，即可回收该数据库连接。

# 3.6.8. 类加载结构
类加载结构用于查看系统内应用的类加载器及其加载路径。

# 注意事项
支持显示公共类库中的 jar 文件。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 选择 “诊断管理” > “类加载结构”，进入类加载结构页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/161ef80bf211d611bb6dc7d36a3db76b4f5dfd26d2aca3dddd36a0b5c357d947.jpg)
4. 用户可通过单击定位查看系统级或应用级的类加载器，在弹出的信息窗口中，可查看对象名、加载顺序以及已加载的类。

# 注意：
“已加载的类” 仅适用于 Web 应用。若需要查看已加载类的明细，需在应用部署时，在 “资源加载” 页签中开启 “跟踪已加载类” 开关。
信息
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d227b2982b7e8decbed7d8a8b5cf788a37bedd463821b66121ed90c9d1d6d02d.jpg)
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f4f0193e1dbcd6577c241bf5bb800efd421e91b63f897b2efa67f83674b7b8c6.jpg)
对象名：com.tongweb.ee.server.TongWebWebappClassLoader@7c9e25c6
/${tongweb.base}/deployment/workManagerExample/
加载顺序:/${tongweb.base}/deployment/workManagerExample/WEB-INF/classes/
/${tongweb.home}/versionl /modules/jpa/tongweb-integration-app.jar
已加载的类:workmanager.WorkManagerServlet

# 3.6.9. 类资源分析
在已部署的应用中，您可以通过类资源分析工具查找指定的类的加载信息，包括类的所有分布位置和实际加载的位置。

# 前置条件
已部署应用。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 选择 “诊断管理” $>$ “类资源分析”，进入类资源分析页面。

# 类资源分析。／编辑
*查找类
 java.lang.Object
*查找范围
examples
分布位置
file:/D:/Program%20Files/Java/jdk1.8.0_281/jre/lib/rt.jarl/java/lang/Object.c
加载位置
加载器
4. 输入待查找的类的全名称，并选择类所在的应用。
关于类资源分析的更多参数说明，详见类资源分析工具配置参数说明。
5. 单击 “查找”，即可查找出类对应的分布位置、加载位置以及加载器等。

# 3.6.10. 类冲突检测
系统内置类冲突检测工具，可检查已部署应用类路径下是否存在版本冲突的类文件。

# 3.6.10.1. 检测应用类冲突
通过选择已部署的应用，检查该应用类路径下是否存在类冲突。

# 前置条件
已部署应用。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 选择 “诊断管理” $>$ “类冲突检测”，进入类冲突检测页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/5bf3aab44d4128c49729f0406acbf4e5120136ad2fa3b03977b35c43393b4850.jpg)
4. 单击列表左上角的 “检测”，进入类冲突检测应用选择页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ac2b78ea63012f462b038d098abbcc15ff1eef15a9ebe8e9a9ce881557075b98.jpg)
5. 在 “应用” 下拉列表中，选择指定应用，并单击 “开始检测”，即可完成类冲突检测的操作。
6. 单击目标检测应用所在行的 “预览”，进入检测结果页面。
7. 用户可查看应用的类冲突检测报表。
◦ 若没有类冲突，则显示无冲突的类。

# examples应用类冲突检测报告
共在0个文件及目录中发现冲突的类
报告生成时间：20 -04 10:29:16
◦ 若存在类冲突，则显示存在类冲突的路径。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/1d8bd9ad091e3f1f7d7279e964b5bb69cc02ae7212945a433727d1a699146592.jpg)


# 3.6.10.2. 下载类冲突检测报告
对指定应用进行类冲突检测后，用户可根据需要下载类冲突检测报告。

# 前置条件
• 已部署应用。
• 已对应用执行类冲突检测操作。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 选择 “诊断管理” > “类冲突检测”，进入类冲突检测页面。
4. 单击目标检测应用所在行的 “下载”，弹出报告选择窗口。
5. 勾选 “index.html”，并单击 “确定”，即可下载类冲突检测报告。

# 3.6.10.3. 删除类冲突检测报告
为了节省资源空间，用户可根据需要删除类冲突检测报告。

# 前置条件
• 已部署应用。
• 已对应用执行类冲突检测操作。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 切换到目标实例。
3. 选择 “诊断管理” $>$ “类冲突检测”，进入类冲突检测页面。
4. 单击目标检测应用所在行的 “删除”，弹出确认删除窗口。
注：用户也可以勾选一个或多个类冲突检测报告，单击列表左上角的 “删除”，批量删除类冲突检测报告。
5. 单击 “确定”，即可完成类冲突检测报告的删除操作。

# 3.6.11. JNDI 树
JNDI（Java Naming and Directory Interface）是用于从Java应用中访问名称和目录服务的一组API，为开发人员提供了查找和访问各种命名资源和目录服务的通用、统一的接口。
命名资源即将名称与对象相关联，以便能通过相应名称访问这些对象，而目录服务即其对象具有属性及名称的命名服务。
例如：当创建一个 JNDI 名为 “jdbc/oracleds” 的数据源时，会在全局的 JNDI 命名空间中绑定名为“jdbc/oracleds” 的数据源对象，在 JNDI 客户端可以通过 JNDI API 写入该对象的名称获取数据源对象。目前，TongWeb 不支持集成第三方的 JNDI 服务。

# 3.6.11.1. JNDI 环境属性
JNDI 系统需要设置环境属性，来配置 JNDI 系统的初始化上下文工厂、对象转换工厂等，一般分为本地JNDI 环境属性和远程 JNDI 环境属性两种。在 JNDI 环境属性中初始化上下文（InitialContext）工厂的配
置尤为重要。

# • 访问本地 JNDI 资源
默认的本地 InitialContext 所需的环境属性不需要设置。
若特殊使用场景下必须配置 java.naming.factory.initial 属性时，可以按如下方式配置，以访问本地 JNDI资源。
```txt
java.naming.factory.initial=com.tongweb.naming.java.javaURLContextFactory
```

# • 访问远程 JNDI 资源
远程的 InitialContext 所需的环境属性配置，如下所示。
```javascript
props.setProperty("java.naming.factory.initial","com.tongweb.tongejb.client.RemotelInitialContextFactory");  
props.setProperty("java.naming.provider.url", "http://IP:port/ejserver/ejb");
```
注：<IP> 需要修改为 TongWeb 所在的 IP，<port> 为 EJB 远程调用端口。
◦ http 协议默认为 $" 8 0 8 8 "$ 。
◦ w3 协议默认为 “5200”，默认未开启。
设置上下文环境属性的代码示例，如下所示。
```java
Properties p = new Properties();  
p.put("java.naming.factory.initial", "com.tongweb.tongejb.client.RemotelInitialContextFactory");  
p.put("java.naming.provider.url", "http://10.10.4.28:8088/ejbserver/ejb ");  
InitialContext ic = new InitialContext(p);
```

# 3.6.11.2. JNDI 命名空间
JNDI分为4种命名空间（NameSpace），全局命名空间、组件命名空间、应用命名空间、模块命名空间。
• 全局命名空间，即本机或其他机器都可以访问的 JNDI 命名空间，其对应一个 TongWeb 实例。
• 组件命名空间是指只能在本组件内部访问的命名空间，即组件之间是相互隔离的。
• Java EE 7规范根据应用部署包的结构，又定义了模块命名空间和应用命名空间这两种新的命名空间。

# 3.6.11.2.1. 全局命名空间
全局命名空间 java:global 中的名称可以被部署在同一个 TongWeb 实例中的所有应用共享。
Java EE 7规范中EJB全局命名空间java:global的定义，如下图所示。
```txt
java:global[/<app-name]/<module-name>/<bean-name>[!<fully-qualified-ifed-interface-name>]
```
<app-name> only applies if the session bean is packaged within an .ear file.Itdefaults to the basename ofthe.ear file with no filename extension,unless specified by the application.xml deploy-ment descriptor.
<module-name> is the name of the module in which the session bean is packaged.In a stand-aloneejb-jar file or .war file, the <module-name> defaults to the base name of the module with anyfilename extension removed.Inan ear file,the <module-name> defaults to thepathname of themodule with any filename extension removed, but with any directory names included.The default<module-name> can be overriden using the module-name element of ejb-jar.xml (for ejb-jarfiles) or web.xml (for .war files).
<bean-name> is the ejb-name of the enterprise bean.For enterprise beans defined via annotation,itdefaults to the ungualified name of the session bean class,unless specified in the contents of theStateless/Stateful/Singleton annotation name（） atribute.For enterprise beans defined viaejb-jar.xml, it's specified in the <ejb-name> deployment descriptor element.
属性介绍如下所示。
• app-name：应用名称，即当前应用去掉后缀名的名称。
• module-name：主要针对部署格式为EAR的应用，即EAR中子模块的名称。
• bean-name：当前EJB的bean实现的类名称。
• full-qualified-interface-name：后面为“!”全包名，这部分是可选的。

# 示例说明一：
当前部署的WAR应用名为myweb.war，EJB name为MyBean，EJB实现接口为com.tw.IHello。可以通过查询以下JNDI名调用EJB。
```txt
java:global/myweb/MyBean  
java:global/myweb/MyBean!com.tw.lHello
```

# 示例说明二：
当前部署的EAR应用名为myear.ear，EJB子模块的名称为myejb.jar，EJB name为MyBean，EJB实现接口为com.tw.IHello。可以通过查询以下JNDI名调用EJB。
```txt
java:global/myear/myejb/MyBean  
java:global/myear/myejb/MyBean!com.tw.IHello
```

# 3.6.11.2.2. 应用命名空间
应用命名空间 java:app 中的名称可以被单个应用中的所有模块的组件共享。单个应用指的是一个单独的部署单元，比如单个 .ear 文件，单个单机部署的模块等。
例如：在同一个 .ear 文件中的一个 .war 文件和 EJB 的 .jar 文件都能访问 java:app 命名空间中的资源。
当前部署的 EAR 应用名为 myear.ear，EJB 子模块的名称为 myejb.jar，EJB name 为MyBean，EJB 实现接口为 com.tw.IHello。在同一个 EAR 下面，所有的子模块可以通过查询以下 JNDI 名调用该 EJB。
```txt
java:app/myejb/MyBean
```
```txt
java:app/myejb/MyBean!com.tw.IHello
```

# 3.6.11.2.3. 模块命名空间
模块命名空间 java:module 中的名称只能被一个模块的所有组件共享。
例如，单个 EJB 模块中的所有企业 Bean 或一个 Web 模块中的所有组件。
当前部署的 EAR 应用名为 “myear.ear”，EJB name 为 MyBean，EJB 实现接口为 “com.tw.IHello”。那么在同一个 EAR 的同一个 “myejb.jar” 下面，其 Java EE 组件可以通过 lookup 以下 JNDI 名调用该 EJB。
```txt
java:module/MyBean   
java:module/MyBean!com.tw.IHello
```

# 3.6.11.2.4. 组件命名空间
组件命名空间的标准上下文环境是 “java:comp/env”，应用组件使用 “java:comp/env” 查找对象时，不必关注对象真正的 JNDI 名称，只需要在部署描述文件中配置该对象的引用名到 JNDI 名的映射，即可降低应用组件代码与 JNDI 名称的耦合性。

# 3.6.11.3. JNDI 树

# 3.6.11.3.1. 服务器资源域
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “JNDI 树”，进入 JNDI 树页面。
4. 单击 “server”，进入 JNDI 树 server 页面。

# JNDI树／树☆
server
localhost examples
localhost StatefulRemoteWAR
田 Deployment
田 local
田 remote
· SecurityService
TransactionManager
田global
田 Container
服务器资源域说明，如下所示。
◦ global：全局资源域。
◦ local：本地 EJB 域。
◦ remote：远程 EJB 域。
◦ 其它资源域：服务器内部 JNDI 资源。

# 3.6.11.3.2. 应用域
以部署的 “${tongweb.home}/version*/examples” 路径中 “examples.war” 为例说明。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “诊断管理” $>$ “JNDI 树”，进入 JNDI 树页面。
4. 单击 “localhost_examples”，进入 JNDI 树 localhost_examples 页面。
JNDI树／树☆
server
田module
 localhost_examples
localhost_StatefulRemoteWAR
田app
上图中命名空间说明，如下所示。
◦ global 命名空间（全局命名空间）
所有应用资源的绑定空间，按照应用名分类存放。通过该空间可访问任何应用定义的资源，访问时需要指定应用名（ear 应用需要，web 和 ejb 则不需要）来区分查找的应用。
◦ app 命名空间（应用命名空间）
某个应用内部资源的绑定空间，按照模块名分类存放。通过该空间可访问到同一个应用下任何模块定义的资源，访问时需要指定模块名来区分查找的模块。
◦ module 命名空间（模块命名空间）
某个模块（ejb 模块、web 模块）内部资源的绑定空间。通过该空间可访问到同一个模块下的其他资源。为兼容旧规范，java:module 命名空间下绑定了应用中所有模块定义的资源，访问时只需要指定资源名即可（无需应用名和模块名）。
◦ comp 命名空间（组件命名空间）
绑定了对任何一个组件可见的资源，包括服务提供的资源和应用自定义的资源。服务提供的资源绑定在 java:comp/ 命名空间下，应用自定义的资源绑定在 java:comp/env 命名空间下。

# 3.6.11.4. 使用事务 JNDI

# 3.6.11.4.1. UserTransaction
使用 TongWeb 的事务管理器，可以通过 javax.transaction.UserTransaction 接口对事务进行管理
，UserTransaction 实例不需要创建，可以通过 JNDI 查找的方式获得。
```txt
...
InitialContext ic= new InitialContext();
UserTransaction ut = (UserTransaction)ic.lookup("java:comp/UserTransaction");
ut.begin();
datasource = (DataSource)ic.lookup("jdbc/oracle1");
conn = datasource.getConnection();
PreparedStatement prestate=conn.prepareStatement(sql);
prestate.ExecuteUpdate();
conn.close();
ut.commit();
...
```

# 3.6.11.4.2. TransactionManager
对于用户的应用，推荐使用 UserTransaction 来管理事务。但在某些特殊应用场景下，存在必须使用TransactionManager 的情况。
用户可以在应用中 lookup 这个 JNDI 名称来获取 TransactionManager。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/daab8bfed8eb26fc4114b0ced7f4bcee81833a81ac9310d833aca618f9060bd9.jpg)
示例如下所示。
```java
...
InitialContext ic= new InitialContext();
TransactionManager txm=(TransactionManager) ic.lookup("java:comp/TransactionManager ");
if(txm != null){
txm.begin();
```
```txt
Transaction tx = txm.getTransaction();   
txm.commit();   
}
```

# 3.6.11.4.3. TransactionSynchronizationRegistry
TransactionSynchronizationRegistry 注入事务同步资源，该接口应用在系统级应用服务器组件上，如：持久化管理、资源适配器、EJB 和 Web 应用组件。
TongWeb 为 TransactionSynchronizationRegistry 绑定的JNDI名称为
“java:comp/TransactionSynchronizationRegistry”。
用户可以在应用中 lookup 这个 JNDI 名称来获取 TransactionSynchronizationRegistry。
```txt
...
InitialContext ic = new InitialContext();
TransactionSynchronizationRegistry txm = (TransactionSynchronizationRegistry) ic.lookup("java:comp/TransactionSynchronizationRegistry");
if(txm != null) {
txm.begin();
Transaction tx = txm.getTransaction();
......
txm.commit();
}
```

# 3.6.11.5. 使用 JNDI 示例
Java 客户端通过 InitialContext 环境属性访问 TongWeb 中已部署的 EJB 的 JNDI 名，具体的操作步骤如下所示。

# 注意事项
• http 协议默认为 $" 8 0 8 8 "$ 。
• w3 协议默认为 “5200”，默认未开启。

# 操作步骤
如下以 w3 协议的默认端口 “5200” 为例。
1. 登录 TongWeb 管理控制台。
2. 部署 EJB。
3. 编写 Java 客户端访问 EJB 应用代码。
...
```java
public static void main(String[] args) {  
Properties p = new Properties();  
p.put("java.naming.factory.initial", "com.tongweb.tongejb.client.Remotel.InitialContextFactory");  
p.put("java.naming.provider.url", "http://10.10.4.28:8088/ejserver/ejb ");  
StatelessSessionRemote ClientA;  
Context ctx;  
try {  
ctx = new InitialContext(p);  
ClientA = ( StatelessSessionRemote) ctx.lookup(" StatelessSessionRemote");  
ClientA.Name("ClientA");  
System.out.print("Invoke the remote interface of SLSB, result is=" + ClientA.getName() + "<br>")  
} catch (Exception e) {  
e.printStackTrace();  
}  
}
```

# 3.7. 日志管理

# 3.7.1. 系统日志

# 3.7.1.1. 配置系统日志
系统日志主要是对 TongWeb 服务器的日志进行配置。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “日志管理” > “系统日志”，进入系统日志页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/275e18a14e7091272f96d6af168eaf7ea2d11c10b11671ae4dafdd19b38fa42f.jpg)
4. 配置基础属性、日志文件、日志级别和在线日志等。
关于系统日志的更多参数说明，详见系统日志配置参数说明。

# 注意：
◦ 在 “日志级别” 页签，开启 “模块日志级别”，可为不同模块设置不同的日志级别。
◦ 日志级别分别为 “debug”、“info”、“warn” 以及 “error”，只有当严重程度等于或高于设置的级别时，才会记录日志。
5. 配置完成后，单击 “更新”，完成系统日志的更新操作。
若界面弹出 “系统日志更新成功” 提示信息，则说明系统日志更新成功。

# 3.7.1.2. 监视系统日志
本章节介绍如何监视异步日志缓冲数量。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “日志管理” > “系统日志”，进入系统日志页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/3c6e5dd2fc08bb176dd772d58eacd69463522ba52e3a48d736c76b6084d98570.jpg)
4. 单击 “监视”，进入监视页面。
可查看系统日志的 “异步日志缓冲数”。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/64285dbfa394853aa517eeeb4f7e9802f711cf588aff5eca61db6e13d6998b44.jpg)


# 3.7.1.3. 在线实时查看系统日志
本章节介绍如何在线实时查看系统日志。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 设置查看在线日志的行数、刷新、最大行数等。
a. 在左侧导航栏中，选择 “日志管理” $>$ “系统日志”，进入系统日志页面。
b. 单击 “在线日志” 页签，设置实时查系统日志的初始加载行数、日志刷新大小以及最大显示行数。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/36e078c9816968b632938ee237605e19eb279ecb4d813379156e175c5f2a16ff.jpg)
c. 设置完成后，单击 “更新”，完成在线系统日志的设置操作。
2. 查看在线系统日志。
a. 进入 “系统日志” 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f38bafc2f756c03705b486ee7801f8be6c0cbdbcc7cbf0a63050be26e22c9dbc.jpg)
b. 单击页面中的 “在线日志” 按钮，弹出在线日志窗口。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/77ff7f6fcd68f7a6cbf7f4d239941512e77fc339b211d51cdd4601bbbc9634b7.jpg)
3. 用户可以实时查看系统日志。

# 说明：
“自动滚动” 开关默认打开，日志信息可以自动滚动。
4. 用户还可以输入 “关键字”、日志搜索内容块区间，或者选择 “开始时间”/“结束时间”，搜索指定日志。

# 3.7.1.4. 下载系统日志
本章节介绍如何下载系统日志。

# 注意事项
控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “日志管理” $>$ “系统日志”，进入系统日志页面。
4. 单击页面下方的 “下载”，弹出选择需要下载的文件窗口。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/fcfdee28445a14720e5b81a2249d6caa6ecd2114bde5379b4936c7d63ad7405a.jpg)
5. 勾选待下载的系统日志文件。
6. 单击 “确定”，完成系统日志文件的下载操作。

# 3.7.2. 访问日志配置
访问日志配置主要针对 TongWeb 服务器的访问生成的日志进行相关配置。
访问日志默认不启用。启用访问日志后，用户可根据需要配置访问日志的基本信息、日志文件以及在线日志。

# 3.7.2.1. 启用访问日志
启用访问日志后，HTTP 请求的时间、URI、响应码等信息可以被记录到日志文件里。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “日志管理” $>$ “访问日志配置”，进入访问日志配置页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/b88523dc68c00f5f2d4a890d0e029ba73c0cb04dc9447d25b8b710b9584f7839.jpg)
4. 配置访问日志相关参数。
关于访问日志的更多参数说明，详见访问日志配置配置参数说明。
5. 配置完成后，单击 “更新”，完成访问日志配置的更新操作。
若界面弹出 “访问日志配置更新成功” 提示信息，则说明访问日志配置更新成功。

# 3.7.2.2. 自定义日志格式说明
为了方便用户将日志系统从其它服务器迁移至当前环境，可使用自定义格式定义访问日志的内容记录格式。
自定义访问日志的内容记录格式说明，如下表所示。
<table><tr><td>配置项</td><td>说明</td></tr><tr><td>%a</td><td>远程主机的IP地址</td></tr><tr><td>%A</td><td>本地IP地址</td></tr><tr><td>%b</td><td>发送的字节数，不包含HTTP头。若没有发送字节数，则记录为“-”</td></tr><tr><td>%B</td><td>发送的字节数，不包含HTTP头信息。</td></tr><tr><td>%h</td><td>远程主机名，若connector没有开启DNS反向查找，则为远程主机的IP地址。</td></tr><tr><td>%H</td><td>请求的协议</td></tr><tr><td>%m</td><td>请求方法,如GET、POST等</td></tr><tr><td>%p</td><td>接受请求的本地端口</td></tr><tr><td>%q</td><td>查询字符串,若存在,则加一个“?”,否则是一个空字符串</td></tr><tr><td>%r</td><td>请求头的第一行(方法和请求URI)</td></tr><tr><td>%s</td><td>响应的HTTP状态码</td></tr><tr><td>%S</td><td>用户的session id</td></tr><tr><td>%t</td><td>日期和时间,通用的日志格式</td></tr><tr><td>%u</td><td>被认证的远程用户,若没有则记录“-”</td></tr><tr><td>%U</td><td>请求的URL路径</td></tr><tr><td>%v</td><td>本地服务器名</td></tr><tr><td>%D</td><td>请求处理的时间,以毫秒为单位。</td></tr><tr><td>%T</td><td>请求处理的时间,以秒为单位。</td></tr><tr><td>%F</td><td>提交响应花费的时间,以毫秒单位</td></tr><tr><td>%i</td><td>当前请求的线程名称</td></tr><tr><td>{%xx}i</td><td>写入请求头名为xxx的值</td></tr><tr><td>{%xx}o</td><td>写入响应头名为xxx的值</td></tr><tr><td>{%xx}c</td><td>写入cookie名xxx的值</td></tr><tr><td>{%xx}r</td><td>写入ServletRequest名为xxx的值</td></tr><tr><td>{%xx}s</td><td>写入HttpSession属性名为xxx的值</td></tr><tr><td>{%xx}t</td><td>请求的时间戳使用SimpleDateFormat模式xxx格式化,并记录在请求的最后</td></tr></table>

# 3.7.2.3. 在线实时查看访问日志
本章节介绍如何在线实时查看访问日志。您也可以进入 “日志管理” > “访问日志明细”，查看详细的访问日志信息，详见访问日志明细。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 设置查看在线日志的初始加载行数、日志刷新大小和最大显示行数。
a. 在左侧导航栏中，选择 “日志管理” $>$ “访问日志配置”，进入访问日志配置页面。
b. 单击 “在线日志” 页签，进入在线日志页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/482860b771a5819a84d5ebbf0a12c37ece04acdeb2672f77575a30de2bb1753d.jpg)
c. 设置初始加载行数、日志刷新大小和最大显示行数。
d. 设置完成后，单击 “更新”，完成在线访问日志的设置操作。
2. 查看在线访问日志。
a. 进入 “访问日志” 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/34fd07ba6c88bdc09ffdb59b984259af868d02cc4c9f966ba8f6f3c2d657dea7.jpg)
3. 单击 “在线日志” 按钮，弹出在线日志窗口。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/01100343a03a52519e2415f0278285314634a976d2737bf69cdaf09df0390f65.jpg)
4. 用户可以实时查看访问日志。

# 说明：
“自动滚动” 开关默认开启，日志信息可以自动滚动。
5. 用户还可以输入 “关键字”、日志搜索内容块区间，并选择 “开始时间”/“结束时间”，搜索指定访问日志。

# 3.7.2.4. 下载访问日志
本章节介绍如何下载访问日志。

# 注意事项
控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。

# 前置条件
已启动访问日志。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “日志管理” $>$ “访问日志配置”，进入访问日志配置页面。
4. 单击页面下方的“下载”，弹出选择需要下载的文件窗口。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e8b00539149aee8124e1e8c62ed5f9f4b914d76c32ed73d1db43a7982761bd51.jpg)
5. 勾选待下载的访问日志文件。
6. 单击 “确定”，完成访问日志文件的下载操作。

# 3.7.3. 访问日志明细
记录业务请求的处理情况，包括处理时间、数据、端口、处理结果等信息。

# 前置条件
• 已获取系统管理员账号和密码。
• 已启动访问日志。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “日志管理” $>$ “访问日志明细”，进入访问日志明细页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a341eabe226ca000f8e9ddba981c24cb59381d96fdb33b3027f580b587efdbaf.jpg)
4. 用户可查看访问日志的时间、客户端 IP、请求方法、协议、Http 状态码、请求地址、发送字节数、会话ID、线程名、客户端域名、本地端口以及应用名。

# 3.7.4. 审计日志
TongWeb 服务器的审计日志，可用于追踪记录用户对服务器的操作。
用户可通过配置查询条件，精确查找问题发生时的操作及详情，降低发现、定位、解决问题的时间和人力成
本。
TongWeb 服务器的审计日志可查找包含管理员、操作对象、操作类型、操作结果、请求地址、客户端 IP等信息，帮助用户快速、有效的定位并解决问题。
注意：
只有具备 auditor 安全审计员角色权限的用户才可查看审计日志。
auditor 安全审计员角色权限说明，详见 “安全审计员 auditor” 章节。

# 3.7.4.1. 启动审计日志
“审计日志” 默认处于启用状态。一旦开启，管理员登录 TongWeb 进行的操作将被详细记录，并保存到经过加密处理的审计日志文件中。
若因为特殊原因关闭了审计日志，可参照如下步骤启动审计日志。

# 前置条件
已获取安全审计员（auditor）账号和密码。

# 操作步骤
1. 以安全审计员账号（auditor）登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “安全配置” $>$ “审计配置”，进入审计配置页面。
审计配置／编辑☆
启用审计日志
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/42741adbcfaf77923f087fec331c93cf0f3f2f3e5f12d977dfb9da4b633b5338.jpg)
使用系统配置
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f44e2c7ca6b4007bf42e6ee4e44d828bb1d435e72c34491d9911e3091f1239b4.jpg)
更新
4. 打开 “启用审计日志” 开关，并单击 “更新”，即可完成审计日志的启用操作。
若界面弹出 “审计配置更新成功” 提示信息，则说明更新审计配置成功；“更新” 配置后，立即生效。

# 3.7.4.2. 审计配置
用户可自定义审计配置，包含审计日志目录、追加类型目录、轮转、保留文件个数、文件编码、缓冲写入、缓冲大小等信息。

# 前置条件
已获取安全审计员（auditor）账号和密码。

# 操作步骤
1. 以安全审计员账号（auditor）登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “日志管理” $>$ “审计配置”，进入审计配置页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/142ac9a778f044a1ac6a2f6b25982f1af39134752be88034fd9f42fbcac9cfa2.jpg)
4. 配置审计日志的相关参数。
关于审计配置的更多参数说明，详见审计配置参数说明。
5. 单击 “更新”，更新审计日志配置。
若界面弹出 “审计配置更新成功” 提示信息，则说明更新审计配置成功。

# 3.7.4.3. 审计配置参数说明
持久化位置：conf/tongweb.xml:tongweb>server>loggers>audit
Table 1. 审计配置的【基本属性】
<table><tr><td>参数</td><td>名称</td><td>参数说明</td></tr><tr><td>enabled</td><td>启用审计日志</td><td>启用审计日志后，管理员登录TongWeb进行的操作将被记录到加密的审计日志文件里。</td></tr><tr><td>baseFile</td><td>文件目录</td><td>将日志文件存放到指定的目录下。</td></tr><tr><td>appendTypeDir</td><td>追加类型目录</td><td>启用后，将在指定的文件目录下增加一个audit目录以存放日志文件。</td></tr><tr><td>rollingFile</td><td>日志文件轮转</td><td>将日志信息按文件大小或时间进行轮转，确保日志文件不会过大。</td></tr><tr><td>append</td><td>日志追加</td><td>启用日志追加模式，日志信息将追加到现有日志文件中而不是覆盖。</td></tr><tr><td>rotationDay</td><td>按天轮转</td><td>将每日未达到大小阈值的日志在零点切割到一个新文件中。</td></tr><tr><td>rotationBySize</td><td>按大小轮转</td><td>当日志文件大小（单位：MB）达到该阈值时，将切割出一个新的日志文件。注：设置为0表示不启用此功能。</td></tr><tr><td>keepMaxFiles</td><td>保留文件个数</td><td>指定在清理日志文件时，须保留文件的个数。</td></tr><tr><td>compression</td><td>日志文件压缩</td><td>是否开启日志文件压缩功能。开启后，对轮转后的日志文件进行压缩。</td></tr><tr><td>chunk</td><td>文件编码</td><td>指定日志文件的编码格式。</td></tr><tr><td>buffered</td><td>缓冲写入</td><td>是否开启文件缓冲写入功能。开启后，当持续记录的日志内容大小（单位：字节）之和达到缓冲大小时才一次性写入文件，而不是每条日志都立即写入文件（在服务器停止时会全部写入），这通常可以提高日志记录性能。关闭后，每条日志都立即写入文件。</td></tr><tr><td>bufferedSize</td><td>缓冲大小</td><td>缓冲写入的阈值，当持续记录的日志内容大小（单位：字节）之和达到此值时，一次性写入进文件。</td></tr></table>

# 3.7.4.4. 查看审计日志
1. 以安全审计员账号（auditor）登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “日志管理” $>$ “审计日志”，进入审计日志页面。
4. 可以查看服务器的审计日志，包含操作时间、管理员、操作对象、操作类型、操作结果、请求地址、客户端 IP、日志文件等。

# 3.7.4.5. 在线查看已归档日志
用户可审计日志页面，选择查看已归档的日志文件。
1. 以安全审计员账号（auditor）登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “日志管理” $>$ “审计日志”，进入审计日志页面。
4. 在 “日志文件” 下拉列表中，选择指定日期的日志文件，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/bff49bc0c51a18d2b19b879c2543efa1578d3d0aac1e22af30e41c59cc5b45c0.jpg)
5. 选择完成后，单击 “搜索”，即可在线查看已归档的日志文件。

# 3.7.4.6. 搜索审计日志
1. 进入审计页面。
2. 在搜索栏中，根据需要选择输入操作时间、管理员、操作对象、操作类型、操作结果、请求地址或者客户端 IP 地址。
例如：搜索操作对象 “home”。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/20a2e67d22ff969b1a5846591cc4f61d5573b08ba9094244a1aa9e7d318eb199.jpg)
3. 单击 “搜索”，即可搜索指定日志信息。

# 3.7.5. ES 推送
将 TongWeb 的运行日志实时推送到远端日志存储服务器（如 Elasticsearch）上，以便于统一管理。
开启本功能后，TongWeb 的日志除了在本地文件存储之外，还会推送到指定的日志存储服务器。

# 注意事项
当无法连接到日志服务器时，日志推送将会失败，并且目前 TongWeb 不会进行补充推送。

# 推送的日志
• 系统日志（server.log）
• 访问日志（access.log）
• 审计日志（audit.log）

# 前置条件
• 已获取系统管理员账号和密码。
• 已搭建 ES 服务。

# 开启 ES 推送
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧菜单栏中，选择 “日志管理” > “ES 推送”，进入 ES 推送页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e59ba423acaa226bf5c9dfd4bffed0af6dae44fa9d134a927d40ab4fcc03ae51.jpg)
4. 打开 “启用” 开关。
5. 配置 “推送地址”、“索引”、“用户名” 以及 “密码” 等。

# 注意：
索引：Elasticsearch 服务器存放日志数据的索引，请确保日志数据索引的唯一性。
6. 配置完成后，单击 “更新”，完成 ES 推送的配置操作。
若界面弹出 “ES 推送更新成功” 提示信息，则说明开启 ES 推送成功。

# 3.7.6. Syslog 推送
支持将 TongWebTongWeb 的运行日志推送到远端 Syslog 服务上，以便于统一管理。开启本功能后，TongWeb 的日志除了在本地文件存储之外，还会推送到指定的日志存储服务器。

# 注意事项
当无法连接到日志服务器时，日志推送将会失败，并且目前 TongWeb 不会进行补充推送。

# 推送的日志
• 系统日志（server.log）
• 访问日志（access.log）

# 前置条件
• 已获取系统管理员账号和密码。
• 已搭建 Syslog 服务。

# 开启日志推送
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧菜单栏中，选择 “日志管理” $>$ “Syslog 推送”，进入 Syslog 推送页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f59e1e6408a03eef8fb0b274c5c439fa6503c2897344077052c45d7058ee73b6.jpg)
4. 打开 “启用” 开关。
5. 配置 “服务器地址”、“端口”、“协议”、“编码”、“日志类型” 以及 “设施” 等。
<table><tr><td>属性</td><td>说明</td><td>默认值</td></tr><tr><td>服务器地址</td><td>Syslog 服务器的 IP 地址。</td><td>localhost</td></tr><tr><td>端口</td><td>Syslog 服务的端口。</td><td>514</td></tr><tr><td>协议</td><td>设置向 Syslog 服务发送数据的协议。可选择为“UDP”或“TCP”。</td><td>UDP</td></tr><tr><td>编码</td><td>发送日志数据的编码类型。</td><td>UTF-8</td></tr><tr><td>日志类型</td><td>发送到 Syslog 的日志类型，可选择系统日志“server”以及访问日志“access”。</td><td>server</td></tr><tr><td>设施</td><td>LOCAL0-LOCAL7 为本地自定义设施，用于标识日志消息的来源类型，可帮助用户对日志进行分类、过滤和路由。当日志类型为多个时，可以为每种类型指定一个设施。</td><td>LOCAL0</td></tr></table>
关于 Syslog 参数的更多说明，详见 Syslog 配置参数说明。
6. 配置完成后，单击 “更新”，完成 Syslog 推送的配置操作。
若界面弹出 “Syslog 推送更新成功” 提示信息，则说明开启 Syslog 推送成功。

# 查看日志信息
1. 登录到搭建 Syslog 服务所在的服务器。
2. 执行如下命令，打印日志，即可查看推送到 Syslog 服务的日志信息。
```batch
tail -f /var/log/messages
```

# 3.8. 安全管理

# 3.8.1. 安全策略
您可以根据需要配置系统的全局安全策略。

# 3.8.1.1. 配置安全策略
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “安全管理” $>$ “安全策略”，进入安全策略的 “文件防篡改” 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c9092a69376ee002178afc50c444590d8a3b323d0430ae73293f30cf2b59504c.jpg)
4. 配置安全策略的相关参数。
关于安全策略的更多参数说明，详见安全策略配置参数说明。
5. 配置完成后，单击 “更新”，完成安全策略的配置操作。
若界面弹出 “安全策略更新成功” 提示信息，则说明安全策略更新成功。
所有更新配置在 TongWeb 下一次重启后生效。

# 3.8.1.2. RMI 服务使用说明
RMI（Remote Method Invocation）远程方法调用，用于不同虚拟机之间的通信，可以在相同或不同的主机上。
提供服务的一方称为服务端，而实现远程调用的一方称为客户端。

# 3.8.1.2.1. 服务端示例代码
通过 RMI 提供的相关类，将 remoteObj 服务注册到 RMI 服务上。RMI 的默认端口 “1099”。
public class server{ public void contextInitialized(ServletContextEvent sec){ try{ IRemoteObj remoteObj  $=$  new RemoteObjImpl(); //将RMI服务注册到1099端口 Registryr  $=$  LocateRegistry.createRegistry(1099); //注册remoteObj服务，服务名为“remoteObj” r.bind("remoteObj",remoteObj); }catch(Exception e){ thrownewRuntimException(e); 1

# 3.8.1.2.2. 客户端示例代码
连接 RMI 服务器，在客户端实现 RMI 调用。
public class client{ public static void main(String[] args) throws Exception, NoteException { //连接服务器，例如127.0.0.1，端口1099 Registry registry  $=$  LocateRegistry.getRegistry("127.0.0.1",1099); //查找名称为“remoteObj”的服务并强制转型为IRemoteObj接口 IRemoteObj remoteObj  $=$  (IRemoteObj)registry.lookup("remoteObj"); System.out.println(pleaseobj)sayHello("abc")); }

# 3.8.1.2.3. 使用示例

# 步骤1：设置 RMI 服务主机名
1. 登录 TongWeb 管理控制台。
2. 在左侧导航栏中，选择 “安全管理” > “安全策略” > “通信”，进入通信页面。
3. 设置 “RMI 服务主机名”。

# 注意：
◦ 您也可以在 “基础配置” $>$ “启动参数” 中，设置 “-Djava.rmi.server.hostname” 的值。
◦ 设置为 TongWeb 所在主机的 IP。
◦ 在 “系统管理” $>$ “远程 JMX”中，开启 JMX 服务后，服务 IP 将覆盖此配置（-Djava.rmi.server.hostname）。
4. 单击 “更新”，完成 RMI 服务主机名的配置。

# 步骤2：部署 RMI war 包
1. 请根据服务端示例代码，开放 RMI 服务端口，默认为“1099”。
2. 编写服务端相关业务代码。
3. 将服务端代码打包为应用 war 包。
4. 打包完成后，部署在 TongWeb。

# 部署3：客户端 RMI 调用
1. 请参照客户端示例代码，连接 RMI 服务器。
2. 编写相关调用代码，实现 RMI 调用。

# 3.8.2. 密码安全
为了加固系统密钥的安全性。TongWeb 提供密码安全功能。

# 3.8.2.1. 无痕密钥
为了降低密钥泄漏的风险，用户可启用 “无痕密钥”。一旦启动无痕密钥，TongWeb 的密钥将不会以任何形式存储在文件系统上。
首次启用 “无痕密钥” 功能时，需重启 TongWeb 服务器，并在重启（即启动）TongWeb 服务器过程中，需要设置一个启动密码。后续每次启动 TongWeb 时，均需要输入此启动密码，因此请务必妥善保管该密码。

# 约束说明
• 仅对 “startserver” 脚本方式启动的 TongWeb 服务器生效，且不对集中管理中的密钥生效。
• 无痕密钥的开启和关闭，均会导致之前已经存储的密码解密错误，此时需要进行密码重置。
首先停止 TongWeb 服务器，然后删除 “${tongweb.base}/data/secure/secure”，再启动 TongWeb 服务器。
若还有具体模块设置过密码，需要单独重置密码。例如：数据源，需要在控制台对数据源的密码进行手动更新。

# 操作步骤
1. 开启 “无痕密钥”
a. 登录管理控制台。
b. 切换到目标实例。
c. 在左侧菜单栏中，选择 “安全管理” $>$ “密码安全”，进入密码安全页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c6f81594610fc5f9a87ae9a1e9d48a7cb4cc1a96998d22245d3495eb43e0a31d.jpg)
d. 打开 “无痕密钥” 开关。
e. 单击 “更新”，完成无痕密钥的开启操作。

# 2. 重置系统已存储的密码
注：使用集中管理的场景，不能通过删除 “secure” 文件来进行重置密码；否则会导致内部通信异常。
a. 停止 TongWeb 服务器。
b. 进入 “${tongweb.base}/data/secure” 目录。
c. 手动删除 “secure” 文件。

# 注意：
若还有具体模块设置过密码，需要单独重置密码。例如：数据源，需要在登录管理控制台后，对数据源的密码进行手动更新。

# 3. 启动 TongWeb，并设置启动密码
a. 进入 “${tongweb.home}/bin” 目录。
b. 使用 “startserver” 脚本，启动 TongWeb 服务器。
提示信息，如下所示。
```ini
[root@centos bin]# sh startserver.sh Execute the command: server Please enter the in-private key:
```
c. 根据提示信息，输入启动密码，并按 Enter，设置启动密码。
注：请务必妥善保管该启动密码，后续每次启动 TongWeb 时，均需要输入该启动密码。
d. 根据提示信息，再次输入启动密码，并按 Enter，即可启动 TongWeb 服务器。
```html
20xx-xx-xx 15:23:36 >>> Ready to <start> TongWeb: domains/domain1 Please enter the in-private key:
```
若回显信息出现 “Server startup in xx seconds” 字样，则说明启动 TongWeb 服务器成功。

# 3.8.2.2. 全局加密算法
TongWeb 全局采用的有效加密算法（默认为 DESede），该算法适用于多种需要加密保护的场景，包含数据源的数据库连接密码、通道的 AJP 协议密钥、私有库密码等各类敏感信息，以及其他需要经过解密操作才能获取原始密码的场景。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/55d6f8afbfd0a0eebde4c411a8ba66ab366a0e5180c66b095feb2c6d6e114370.jpg)
支持的算法，如下所示。
• SM4：SM4 是中国国家密码管理局发布的一种分组密码算法，属于国密算法体系（国产商用密码算法），主要用于数据加密保护。
• DESede：DESede（Triple DES）是一种对称加密算法，是 DES（Data Encryption Standard）算法的改进版本，通过三次加密增强数据安全性，适用于需要高安全性但无法直接升级到 AES 的旧系统场景。
• AES：AES（高级加密标准）是一种广泛使用的对称加密算法，它以块的形式对数据进行加密。在 AES算法中，明文被分成多个块，每个块通常是 128 位，然后使用密钥对这些块进行多轮加密以生成密文。AES 支持多种长度的密钥，如 128 位、192 位和 256 位，不同的密钥长度决定了加密过程中的轮数。

# 3.8.3. 证书管理
管理 TongWeb 建立 SSL 通道时可选用的证书文件。

# 3.8.3.1. 导入证书
系统内置了一个普通证书和两个国密证书。用户可根据自身实际需求，将个人证书导入至 TongWeb 系统中。导入完成后，用户可在 TongWeb 控制台对证书进行集中统一管理。如此一来，当需要建立 SSL 通道时，用户便能够直接选用。

# 内置证书
• 普通 JKS：conf/server.keystore
• 国密 PKCS12：conf/sm2.enc.pfx
• 国密 PKCS12：conf/sm2.sig.pfx

# 导入证书格式要求
PKCS12、JKS

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “安全管理” $>$ “证书管理”，进入证书管理页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/08e74304cbf76d8ceb0929ce3601a5025c605b042b45ec4d4a37fd6dbb2122b2.jpg)
4. 单击 “导入”，进入导入证书页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/0229ab4d7fbfd09ce7b0cb0c1afa0605e38af676513552598146d54fd14f6aa2.jpg)
5. 配置导入证书相关参数。
◦ 名称：必填项，证书名称。需要使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
◦ 类别：必填项，支持 PKCS12、JKS。
◦ 证书路径：必填项，通过 “上传文件” 或者指定 “服务器文件” 的方式上传证书。
说明：
控制台默认关闭上传文件功能。若需要开启，单击控制台左上角的 “集中管理”，并选择 “安全配置”$>$ “控制台安全”，进入控制台安全页面。在控制台安全页面，关闭“禁用文件上传”，并重启TongWeb 服务器即可。
◦ 证书密码：必填项，证书的密码。
关于导入证书的更多参数说明，详见证书管理参数配置说明。
6. 配置完成后，单击 “导入”，即可将证书导入。
在证书管理列表中，可查看到导入的证书和证书相关信息，包含名称、类别、格式、别名、算法以及失效时间。

# 3.8.3.2. 使用证书
导入证书后，当需要建立 SSL 通道时，用户便能够直接选用。
用户也可根据需要使用内置证书。

# 前置条件
已导入证书。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧菜单栏中，选择 “Web 容器” $>$ “通道”，进入通道页面。
4. 单击目标通道，进入编辑通道页面，并单击 “安全”，进入安全页签。
5. 单击 “开启 SSL”，用户可选择已导入的证书，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7a655a03b1e32ff5e66f3d99246485d7d8fcfdcd6341c32c44b966d1b54fb9f4.jpg)
6. 配置完成后，单击 “更新”，即可完成证书的选用。

# 3.8.3.3. 导出证书
支持导出证书管理列表中的证书，导出为以 “keystore-xxxx.zip” 命名的压缩包。
内置证书也支持导出。

# 前置条件
已导入证书。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “安全管理” > “证书管理”，进入证书管理页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f0caaaf9880d3f1709ee15347b9a750aaf3c6b3c20aec28f2277bebc633fe5ec.jpg)
4. 单击 “导出”，弹出选择下载文件窗口。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7a0a4f15e4b67f42cee3b7f95737ab54740cd6844880f3ed698b86379d9d3a9d.jpg)
5. 勾选目标证书，并单击 “确定”，即可导出证书。

# 3.8.3.4. 删除证书
当用户个人上传的证书不再使用时，为有效节省系统资源与存储空间，可对该证书执行删除操作。

# 注意事项
内置证书不允许删除。

# 前置条件
已上传证书。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “安全管理” $>$ “证书管理”，进入证书管理页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/527ded8d7c31abaff070a315e60ead8b7002d8886bb8e0c88b473584c40782ef.jpg)
4. 单击目标证书所在行的 “删除”，弹出确认删除证书窗口。
5. 单击 “确定”，即可完成证书的删除操作。

# 3.8.4. 可信文件
可信文件功能旨在确保 TongWeb 执行过程中所使用的可执行文件（如 java）的安全性。
在 TongWeb 执行受可信文件功能管理的可信文件之前，均会检查其 MD5 哈希值，当哈希值不匹配时会抛出错误并终止执行。
受管的可信文件列表存储在 “${tongweb.base}/data/secure/trusted-files.txt”。
“trusted-files.txt” 每行记录一个文件的哈希值及其文件路径，格式为：哈希值|文件路径。
其中，文件路径可使用 ${tongweb.home} 和 ${tongweb.base} 替换符。

# 步骤1：获取可执行文件 MD5 哈希值
可执行文件的哈希值可以是自己代码 MD5 哈希值，也可以通过 “admin.[sh|bat]” 脚本获取。
如下以 “Linux 系统，通过 “admin.sh” 获取 MD5 哈希值”为例说明。
1. 进入 “${tongweb.home}/bin” 目录。
2. 执行如下命令，计算可执行文件的 MD5 哈希值。
可执行文件以 “/home/jdk1.8.0_261/bin/java” 为例。
```txt
sh admin.sh checksum /home/jdk1.8.0_261/bin/java
```
回显信息，如下所示。
```txt
Execute the command: checksum  
file MD5 checksum:  
4BA98972DE5B19AFB2EF93A081873F6C | /home/jdk1.8.0_261/bin/java  
Copy the above format and paste in \({}^{\#}\{tongweb.base\}/data/secure/trusted-files.txt to add trusted files
```
3. 获取并保存 MD5 哈希值及文件路径。
如 “4BA98972DE5B19AFB2EF93A081873F6C | /home/jdk1.8.0_261/bin/java”。

# 步骤2：将可执行文件添加到可信文件
1. 进入 “${tongweb.base}/data/secure” 目录。
2. 新建 “trusted-files.txt” 文件。
3. 打开新建的 “trusted-files.txt” 文件。
4. 输入需要纳入管理的可信文件。
格式要求：哈希值|文件路径
将 步骤 1 中获取的 MD5 哈希值和文件路径，复制并粘贴到 “trusted-files.txt” 文件中，如下所示。
```txt
4BA98972DE5B19AFB2EF93A081873F6C | /home/jdk1.8.0_261/bin/java
```
5. 配置完成后，保存并退出。

# 步骤3：查看已添加的可信文件
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “安全管理” $>$ “可信文件”，进入可信文件列表页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/2985acb7d6bfe16e6dbb18f57332ae96673e375f72a5f671b29309bfa8b22355.jpg)
4. 在可信文件列表中，可查看到已添加的可信文件。

# 3.8.5. 巡检基线
支持对 “一键巡检” 内容进行配置，丰富安全基线的巡检指标和报告等。
巡检基线功能默认处于关闭状态，只有在手动 “启用基线检查” 功能后，执行一键巡检操作时，系统才会根据配置的基线开展检查工作。

# 启用基线检查
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “安全管理” $>$ “巡检基线”，进入巡检基线页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/5beecbf0896bdb0819446b9d55298d6d1540aec8af15a83779b2589bc524b587.jpg)
4. 打开 “启用基线检查” 开关，并根据需要配置巡检检查项目。
关于巡检基线的参数说明，详见巡检基线配置参数说明。
5. 配置完成后，单击 “更新”，弹出 “巡检基线更新成功” 提示信息，说明启用基线检查成功。

# 一键巡检
进入 “集中管理” > “系统管理” > “一键巡检” 页面，即可执行巡检操作，详见一键巡检。

# 3.9. 基础配置

# 3.9.1. 全局配置

# 3.9.1.1. 更新全局配置
您可以通过该页面配置 TongWeb 服务器的全局属性。
全局属性被修改更新后在 TongWeb 服务器下次重启后生效。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “基础配置” $>$ “全局配置”，进入全局配置的 “服务器” 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/0942e6580a4c752423d4543e272791f8ec615701ee74f65ae83da0291497d8e0.jpg)
4. 配置全局配置的相关参数。
关键参数说明，如下表所示。
<table><tr><td>参数</td><td>说明</td></tr><tr><td>加密公钥</td><td>非必填，在“全局配置”&gt;“集中管理”页签中，开启“支持集中管理”有效。
·开启后，需要在本机TongWeb管理控制台的“服务管理”&gt;“集中配置”获取“加密公钥”，并填入远程节点的“全局配置”&gt;“集中管理”&gt;“支持集中管理”的“加密公钥”。
·该功能主要用于手动创建节点，详见手动创建节点。</td></tr><tr><td>开启本地JMX</td><td>非必填，在“全局配置”&gt;“JMX”页签中，打开“开启本地JMX”开关后，可将服务器实例的配置管理和监视接口注册到本地MBean，详见本地JMX。</td></tr><tr><td>附加响应头</td><td>非必填，在“服务器”页签下，附加响应头允许使用()字符。</td></tr><tr><td>其他参数</td><td>请根据实际需要配置，详见全局配置参数说明。</td></tr></table>
5. 配置完成后，单击 “更新”，完成全局属性的配置操作。
若界面弹出 “全局配置更新成功” 提示信息，则说明全局配置更新成功。
所有更新配置在 TongWeb 下次重启后生效。

# 3.9.1.2. 下载全局配置
若您需要将您管理的 TongWeb 相关配置进行迁移或者备份，您可以通过管理控制台下载“${tongweb.home}/conf” 下的 xml 类型的配置文件。
• console.xml：集中管理和 TongWeb 账号相关配置。
• tongweb.xml：TongWeb 主配置文件。

# 注意事项
控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “基础配置” $>$ “全局配置”，进入全局配置的 “服务器” 页面。
4. 单击页面下方的 “下载”，弹出选择需要下载的文件窗口。
5. 勾选待下载的配置文件。
6. 单击 “确定”，完成全局配置文件的下载操作。

# 3.9.2. JVM 配置
JVM 配置用于管理 TongWeb 应用服务器的 JVM 属性。
支持对内存大小、GC 策略、堆转储、JVM 日志、环境变量、IP 版本等配置。

# 注意事项
• JVM 日志文件：支持输入百分号（%），如 “%t” 占位符来实现时间戳；并支持其它 JVM 规范的占位符，如 %p（进程 ID）等。
• 垃圾回收器：支持 “JVM 默认”、“串行”、“并行”、“并发”、“G1” 以及 “ZGC” 策略。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 左侧导航栏中，选择 “基础配置” > “JVM 配置”，进入 JVM 配置的 “内存大小” 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/a4365a594c729f6f96ef5f32318a2bb6bfc78f9b322c338f65f00a58473794e6.jpg)
4. 请根据需要更新 JVM 的相关参数。
关于 JVM 配置的更多参数说明，详见JVM 配置参数说明。
5. 配置完成后，单击 “更新”，完成 JVM 属性的配置操作。
若界面弹出 “JVM 配置更新成功” 提示信息，则说明 JVM 配置更新成功。
6. 重启 TongWeb 服务器，使配置生效。
JVM 配置更新后，需要重启 TongWeb 服务器才能生效。

# 3.9.3. 启动参数

# 3.9.3.1. 默认启动参数
<table><tr><td>启动参数</td><td>参数说明</td><td>仅 Linux有效</td><td>默认开启</td></tr><tr><td>-Xms2048m</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-Xmx2048m</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-Djava.security.egd.file:/dev/.urandom</td><td>null</td><td>true</td><td>true</td></tr><tr><td>-Djava.securitymanager</td><td>null</td><td>false</td><td>false</td></tr><tr><td>-Djava.security.policy=conf/tongweb.policv</td><td>null</td><td>false</td><td>false</td></tr><tr><td>-server</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-Djava.net preferenceIPv6Addresses=false</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-Djava.awt.headless=true</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-agentlib:jdwp=transport=dt_SOCKET,serve=r,suspend=n,address=0.0.0.0:8888</td><td>null</td><td>false</td><td>false</td></tr><tr><td>-Dtongweb.home=${tongweb.home}</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-Dtongweb.base=${tongweb.base}</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-Djava.utilloggingmanager=com.tongweb.logger.JulLogManager</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-XX:+HeapDumpOnOutOfMemoryError</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-XX:HeapDumpPath=logs/heap$\{TW_TimeStamp\}.hprof</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-XX:+UnlockDiagnosticVMOptions</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-XX:+LogVMOutput</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-XX:LogFile=logs/jvm/jvm.log</td><td>null</td><td>false</td><td>true</td></tr><tr><td>-XX:ErrorFile=logs/hs_err pid%p.log</td><td>null</td><td>false</td><td>true</td></tr></table>

# 3.9.3.2. 创建启动参数
本章节介绍如何创建启动参数。

# 注意事项
• 启动参数中发生配置变更，需要重启 TongWeb 服务器，配置才会生效。
• 启动参数支持使用 “${tongweb.home}”、“${tongweb.base}” 变量。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “基础配置” $>$ “启动参数”，进入启动参数列表页面。
4. 单击 “创建”，进入创建启动参数页面。
启动参数／创建☆
*参数
启用
仅 Linux 有效
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e98ae88bdf9cd1f6a435b3b156a2906a6412590bd16fc09abe4ad6a409141acf.jpg)
限定JRE版本
描述
5. 配置启动参数的相关参数。
◦ 参数：必填项，用于 JVM 启动时的进程入参。
▪ 必须以 [-X, -D, -agentlib, -server, -client, -javaagent, -verbose] 开头。
▪ 不允许使用空白字符或特殊字符：[#, ?, `, |, (, ), !, ^]
◦ 限定 JRE 版本：非必填，支持 8-24 版本。
关于启动参数的更多说明，详见启动参数配置说明。
6. 配置完成后，单击 “添加”，完成启动参数的添加操作。
若界面弹出 “启动参数添加成功” 提示信息，则说明添加启动参数成功。
当启动参数配置项更新后，系统在 “系统管理” > “系统通知” 中通知更新成功消息。
7. 重启 TongWeb 服务器，使配置生效。

# 3.9.3.3. 可添加启动参数
<table><tr><td>启动参数</td><td>说明</td></tr><tr><td>-Dtongweb.checkdisabled=length,age,composition</td><td>更新密码时，禁用密码校验。分别表示要禁用长度、期限、复杂度。默认不配置，表示不禁用。</td></tr></table>

# 3.9.3.4. 管理启动参数
用户可根据需要查看、编辑或删除启动参数。

# 查看启动参数
1. 在左侧导航栏中，选择 “基础配置” $>$ “启动参数”，进入启动参数列表页面。
2. 在启动参数列表页面，您可以查看已创建的启动参数。
包含启动参数、启用、仅 Linux 有效、限定 JRE 版本、限定区间等信息。

# 编辑启动参数
启动参数中发生配置变更，需要重启 TongWeb 服务器，配置才会生效。
1. 在左侧导航栏中，选择 “基础配置” $>$ “启动参数”，进入启动参数列表页面。
2. 单击目标启动参数，进入编辑启动参数页面。
3. 您可以根据提示修改启动参数信息。
4. 编辑完成后，单击 “更新”，更新启动参数配置信息。
若界面弹出 “启动参数更新成功” 提示信息，则说明编辑启动参数成功。
当启动参数配置项更新后，系统在 “系统管理” $>$ “系统通知” 中通知更新成功消息。
5. 重启 TongWeb 服务器，使配置生效。

# 删除启动参数
删除启动参数时，启动参数引用的其它组件不会被删除。
注：启动参数中发生配置变更，需要重启 TongWeb 服务器，配置才会生效。
1. 在左侧导航栏中，选择 “基础配置” $>$ “启动参数”，进入启动参数列表页面。
2. 单击目标启动参数所在行的 “删除”，弹出确认删除窗口。
注：用户可根据需要勾选一个或多个启动参数，并单击列表上方的 “删除” 按钮，批量删除启动参数。
3. 单击 “确定”，完成启动参数的删除操作。
若界面弹出 “启动参数删除成功” 提示信息，则说明删除启动参数成功。
当启动参数配置项更新后，系统在 “系统管理” > “系统通知” 中通知更新成功消息。
4. 重启 TongWeb 服务器，使配置生效。

# 3.9.4. 启动策略
启动策略包含开机自启、宕机重启以及定时重启。

# 3.9.4.1. 约束说明
• 仅对使用脚本启动的 TongWeb 实例有效，对集中管理内部管理的实例无效。
• 开启启动策略后，TongWeb 主进程将会到后台运行。

# 3.9.4.2. 功能说明
• 开机自启
仅在 TongWeb 位于 Linux 系统时有效。
虚拟机开机后，自动启动当前 TongWeb 实例。关于集中管理实例的开机自启，详见集群开机自启。
虚拟机开机脚本默认需要 root 用户，但用户可以修改 tongweb.service 的内容，修改为其它用户启动
TongWeb，详见开机自启动方案说明。

# 开机自启动方案说明
开机自启动是基于 linux 的 systemd 机制实现，如下所示。
1. 创建服务文件。
TongWeb 会优先使用 “/etc/systemd/system” 目录（若该目录不存在，则使用
“/usr/lib/systemd/system” 目录），在该目录下创建 domain1.service 文件，其中 “domain1” 为TongWeb 的实例名。
2. 在服务文件中，写入如下内容。
[Unit]   
Description  $\equiv$  TongServer   
After  $\equiv$  network.target   
[Service]   
Type  $\equiv$  forking #进程类型（根据应用类型选择）   
Environment  $=$  "JAVA_HOME  $\equiv$  xxxx" #可选   
ExecStart=/bin/bash /opt/TongWeb/bin/startd.sh #指向TongWeb的启动脚本   
PrivateTmp=false   
TimeoutSec=0   
User  $\equiv$  your_username #指定运行用户   
Group  $\equiv$  your_groupname #指定运行组   
[Install]   
WantedBy  $\equiv$  multi-user.target
3. 安装和卸载自启动服务。
▪ 安装：
```txt
systemctl enable domain1.service
```
▪ 卸载：
```txt
systemctl disable domain1.service
```
• 宕机重启
检测频率 5 秒一次。
该机制仅对使用脚本启动的 TongWeb 实例有效，对集中管理内部管理的实例无效。
开启此机制后，TongWeb 主进程将会到后台运行。
• 定时重启
仅对使用脚本启动的 TongWeb 实例有效，对于集中管理启动的实例无效。

# 3.9.4.3. 前置条件
已获取系统管理员账号和密码。

# 3.9.4.4. 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧菜单栏中，选择 “基础配置” $>$ “启动策略”，进入启动策略页面。
4. 您即可开启或者关闭 “开机自启” 、 “宕机重启” 或 “定时重启”。

# 说明：
定时重启支持 cron 表达式。Cron 表达式配置完成后，单击 “更新”，即可显示计划重启日期。
关于启动参数的详细配置说明，请参见启动策略配置参数说明。
启动策略/ ☆
开机自启
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/9bef0bedf402390f495fd6011295930e9040c7c2504218ffc6216321a4607531.jpg)
岩机重启
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/750f370a63147958f649abf92f167ea0f3c66f69a7a00994dc9199ea26a60fb6.jpg)
定时重启
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/45702628e7417b9361b6e0d63eaf69b94cfd689f176ebfebdc2874e9848a3991.jpg)
*Cron表达式
0*/40 ***？
执行时间
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/2389c18b09c0535448b81e2bf633b3ccbb39f970cb424fe40ca4464caadc9338.jpg)
停止时间
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/9d20bd62b806c6ee8858be3e16c6bdb221adf6472726c3b3a5557b99d1746705.jpg)
计划重启日期0
2023-08-01.14:00:00.2023-08-01.14:40:00.2023-08-01.15:00:00.2023-08-01
15:40:00.2023-08-01.16:00:00
5. 单击 “更新”，完成启动策略的更新。
6. 重启 TongWeb 服务器，使配置生效。

# 3.9.5. 远程 JMX
所有实例支持独立开启本实例的远程 JMX 接口。
本章节介绍如何开启实例的远程 JMX，关于如何配置与使用，详见 远程 JMX。

# 前置条件
已获取系统管理员账号和密码。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “基础配置” $>$ “远程 JMX”，进入远程 JMX 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7409879927030d7980d8015f77775238dd6a1a4f82af160fba93c5a93f9dd669.jpg)
4. 打开 “启用” 开关，开启远程 JMX。
5. 配置远程 JMX 相关属性。
◦ 服务IP：指定 JMX 监听服务绑定的 IP 地址，即 TongWeb 所在 IP 地址，默认为 “0.0.0.0”。
若设置为 “127.0.0.1”，则只能本机调用，远程客户端将无法访问。
◦ 端口：指定 JMX 监听服务绑定的端口。默认为 “7200”。
◦ 开启认证：开启认证后，需要设置访问的用户名和密码。当通过远程 JMX 访问该实例时，系统会要求输入该用户名和密码以完成身份认证。
◦ 开启 SSL：默认关闭。开启后，使用 TLS 加密网络数据。
关于远程 JMX 的更多参数说明，详见远程 JMX 配置参数说明。
6. 配置完成后，单击 “更新”，即可完成远程 JMX 启用操作。

# 3.9.6. 系统通知
通知主要是用于给管理员提供关于系统需要重启、授权到期等提示信息。
当有系统配置属性发生改变，服务器需要重新启动才能生效时，系统会给出一条通知，其“详情”一般表示具体的发送变化的属性名，以及其变化前后的值。
此外，属性发生变化后，若再次编辑将其恢复为启动之初的值，则重启通知会取消。
若变化的属性有多个，则会以分号分隔来表示。

# 查看系统通知
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “基础配置” > “系统通知”，进入系统通知页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d32112cf2d7f835ec15312eb8be7242ba615fb49c4f55a7143911e7ef160fc9a.jpg)
4. 您可以查看系统通知组件、消息、细节等信息。

# 3.9.7. 加密工具
加密工具主要是对密码等敏感数据进行加密，如数据库密码、证书密码等。

# 注意事项:
• 为了安全考虑，每个 TongWeb 实例的密钥不同，一个 TongWeb 实例加密的结果，其它 TongWeb 实例无法解密。
• 仅 “系统管理员” 以及被授权的 “系统用户” 有使用加密工具的权限（审计员和安全员没有加密工具的访问权限）。

# 3.9.7.1. 控制台加密
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧导航栏中，选择 “基础配置” > “加密工具”，进入加密工具页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/cfa2d1221a6836ae5df8650f1a7a143781177ef77d1eed7ba18554651f4073a6.jpg)
4. 配置加密工具的相关参数。
◦ 待加密字符：必填项，输入待加密的字符。
◦ 加密类型：非必填，支持对称（symmetic）、非对称（asymmetric）、摘要（digest）以及特殊字符。
特殊字符适用于：使用 REST 等接口需要传递的 # ？ & : % + 以及空白符等参数。
关于加密工具的更多参数说明，详见加密工具配置参数说明。
5. 单击 “更新”，可在加密结果文本框中，查看加密后的结果，如下图所示。
若界面弹出 “加密已完成，请妥善保管加密结果” 提示信息，则说明加密成功。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/4ed6128eb441fa4d3800a276ab6895ae23e8252c7d7f5dbedc40dc33a9121a7c.jpg)


# 3.9.7.2. admin 脚本加密
可通过 ./admin.[bat|sh] password 命令加密密码，例如：数据库连接密码、HTTP 证书密码等。
加密密码默认用于 domain1 实例。若需要应用于其它实例，可在命令后指定实例名。
以 Linux 环境 “加密 domain2 的 thanos123.com 密码” 为例。操作步骤如下所示。
1. 进入 “${tongweb.home}/bin” 目录。
2. 执行如下命令，加密 domain2 的 thanos123.com 密码。
./admin.sh password thanos123.com domain2
若回显信息中出现加密后的密文密码，则说明加密成功。

# 4. 集中管理

# 4.1. 集群管理

# 4.1.1. 集群简介

# 4.1.1.1. TongWeb 集群
TongWeb 企业版支持负载均衡、大规模稳定的集群、会话（session）缓存、弹性伸缩集群等功能。
TongWeb 企业版主要是面向大规模应用环境和对可靠性要求高的应用场景。在实际应用中存在多种高并发的业务场景，需要构建 Web 应用服务器集群予以支撑。
TongWeb 集群由多个同时运行的 TongWeb 实例、负载均衡器以及 TDG 组件共同组建而成。该集群具备一键式快速部署能力，能够迅速搭建全新的集群环境，并支持批量启动多个 TongWeb 实例。在集群的搭建过程中，支持任意增加 TongWeb 实例、负载均衡器、TDG 节点，且各组件无启动顺序要求。
TongWeb 集群架构，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/9d6bf583cc322b73a4920d10da11578bd8dd2d1fc2ea9271e4a867a9e11c8f0d.jpg)
负载均衡器部署在前端，当客户端访问应用时，访问的是负载均衡器地址，负载均衡器将客户端请求按一定规则分发到 TongWeb 各个节点上。
组件说明，如下表所示。
<table><tr><td>参数</td><td>参数说明</td></tr><tr><td>集中管理</td><td>您可以通过管理控制台的集中管理组建集群等。</td></tr><tr><td>集群</td><td>由多个主机节点上的多个TongWeb实例共同为用户提供的服务,称为TongWeb 集群。</td></tr><tr><td>负载均衡器</td><td>TongWeb是通过负载均衡器实现的集群功能。支持各类软、硬件负载均衡器。东方通也提供自研的TongHttpServer(THS)负载均衡器,您可以根据需要进行选择。负载均衡器负责合理的分配多个服务器之间请求,可有效避免其中一台超负荷而其他服务器没有充分发挥处理能力的问题。若其中一台服务器宕机,则其它服务器会继续接管请求进行处理。负载均衡器部署在前端,客户端访问的是负载均衡器地址,负载均衡器将客户端请求按一定规则分发到后台TongWeb各个节点上。负载均衡器可单独安装在一台服务器上,也可以跟TongWeb安装在同一台服务器上。通过管理控制台创建负载均衡器时,您可以采用东方通自研的TongHttpServer(THS)负载均衡器,也可以采用开源的Nginx、Apache等负载均衡器。</td></tr><tr><td>节点</td><td>节点是安装并运行TongWeb实例的主机。TongWeb可以部署在不同的主机节点上,一个主机节点可以部署并运行多个TongWeb实例,多个主机节点上的TongWeb应用服务器实例共同为客户提供更高性能的服务。</td></tr><tr><td>实例</td><td>实例是可运行的TongWeb逻辑服务器,即创建的TongWeb域,目前生成在“${tongweb.home}\domains”下,在业务上表示一种独立的工作环境。您可以创建并运行多个TongWeb实例,每个实例都有独立的配置、数据、日志、缓存等文件,并与其它实例共享脚本、类库、系统应用等资源。多个TongWeb服务器实例可以同时服务于开发、测试、生产等不同的业务环境。</td></tr><tr><td>会话服务器</td><td>用户可以将服务端的会话信息备份到数据缓存服务中去,用以在服务器故障重启后保障会话信息不丢失,以获得会话高可用能力。TongWeb支持TongDataGrid(东方通自研)、Hazelcast、Redis会话服务器作为Session存储库。当一个TongWeb节点宕机后,其它TongWeb节点可以从会话服务器中恢复Session数据,从而保证Session不丢失。</td></tr></table>

# 4.1.1.2. TongHttpServer(THS)
东方通自研的 TongHttpServer （THS）是一款功能强大、稳定高效、高性价比、易于使用、便于维护的负载均衡器软件产品。
THS不仅可以满足用户对负载均衡服务的需求，提升系统可靠性、高效性、可扩展性及资源利用率，还具有很高的性价比，可以有效降低系统的建设成本、维护成本，并且使用简单、维护便捷。
THS的“智能化”特点能够极大地提升系统的运维效率、减少运维工作量、降低因误操作引发事故的几率。
THS 的 “云特性” 使其既能够为传统架构的业务系统提供具有云计算优势的负载均衡服务，也可以应用到云计算平台中提供负载均衡服务。
提供的主要功能如下：
• 支持 OSI 四层七层负载均衡功能
• 支持 HTTP、HTTPS、国密 HTTPS、HTTP2
• 支持静态文件、索引文件及自动索引
• $3 x x - 5 x x$ 重定向
• 支持 FastCgi 协议
• URL 重写
• 基于 IP 地址、HTTP 密码、子请求、HTTP 头的访问控制
• 基于名称和基于 IP 的虚拟主机配置
• 支持 TCP、HTTP 主动健康检查方式
• 支持 gziping、byte ranges、chunked responses响应
• 支持多种负载均衡策略
• 自定义访问日志格式、日志文件轮转
• 限制单个 IP 客户端连接数
• 邮件代理
• 支持高可用功能，支持浮动 IP
• 管理控制台配置

# 4.1.1.3. TongDataGrid(TDG)
东方通自研的会话服务器 TongDataGrid（TDG）集群可作为 session 存储库，当其中一个 TongWeb 节点宕机时，其他 TongWeb 节点可以从 TDG 中恢复 Session 数据，从而保证 Session 不丢失。
会话服务器不是必配项，若应用有单点登录（SSO）功能，则完全可以不使用会话服务器，SSO为最佳选择。
TongWeb 虚拟主机可开启“Session 共享”功能。开启后，选择已创建的会话服务器，同一虚拟主机的应用通过会话服务器实现 Session 数据共享。
开启 Session 共享后，虚拟主机上配置的会话服务器优先级高于应用“会话与cookie”页面配置的会话服务器。

# 4.1.1.4. 消息服务器
消息服务器作为网络的节点，专门用来存储、转发网络上的数据、信息等。
TongWeb 内置自研的 TongWeb-MQ 作为 JMS Server，同时也支持通过 JCA 集成外部消息服务器
（OpenMQ 等）。
关于集成外部消息服务器的信息，请参见OpenMQ。

# 4.1.1.5. 基本概念

# 4.1.1.5.1. 节点
运行 TongWeb 实例的主机。可以理解为一台主机安装的一套 TongWeb。节点启动指的是默认域 domain1的启动，该默认域 domain1 通常作为管理节点使用。
在无需集群使用、测试移植的场景下，默认域 domain1 可以作为实例使用。

# 4.1.1.5.2. 实例
指创建的 TongWeb 域，目前生成在 “${tongweb.home}\domains” 下。

# 4.1.1.5.3. 集中管理
选取安装 TongWeb 节点的其中一个节点做为集中管理，将其它节点及实例管理起来。被管理的其它节点控制台将被关闭不可用。

# 4.1.1.5.4. 开机自启
假设安装一个 TongWeb 节点，创建了实例、负载、TDG。
• 节点 “开机自启” 是通过做 tongweb.service 服务，当主机节点启动时把 domain1 启动起来。
• 其它新建实例设为 “自启动”。当把节点启动后，调用系统的 tongweb.service 服务把 domain1 启动起来，domain1 再把其它实例带动起来。
• 节点 “开机启动”做成 linux 的自启动需要使用 root 用户，不支持 windows。
• 实例、负载、TDG 的 “自启动”是在节点启动后，由节点带起来。在 linux、windows 下均可。
• 节点进程可以监控本机所有实例、负载、TDG，可以实现实例宕机重启。

# 4.1.1.5.5. 节点停止
执行 stopserver.sh 停止节点，则仅停止节点默认域 domain1，由节点带动启动的其它实例不受影响。

# 4.1.2. 环境准备
组建 TongWeb 集群需要准备安装运行 TongWeb、负载均衡器（以TongHttpServer（简称THS）为例）和会话服务器 TongDataGrid（简称 TDG）的平台环境和系统环境。

# 4.1.2.1. 平台环境
<table><tr><td>环境</td><td>版本</td></tr><tr><td>操作系统</td><td>·Windows
Microsoft Windows 系列。
·Linux
RedHat 系列、Suse Linux 系列、麒麟操作系统、统信 uos 操作系统、中科方德操作系统等。
·Mac OS
Mac OS 系列</td></tr><tr><td>芯片</td><td>支持国内主流的 ARM、X86、MIPS、LoongArch 芯片架构。
例如：华为鲲鹏(ARM)、飞腾(ARM)、海光(X86)、兆芯(X86)、龙芯(MIPS/LoongArch)等。</td></tr><tr><td>数据库</td><td>主流数据库：Oracle、MySQL5、MySQL8、Sybase
15、dameng、Kingbase、Kingbase8、Oscar、HSQL、Sybase type 4 for Sybase 11.x、jtds sybase、postgres、SQLServer、Derby Client、Derby Embedded、IBM Type
4、gbase8t、gbase8s、sr、db2、highgo、uxdb、GaussDB 100、InspurK-DB、linkoopdb、oceanbase、MogDB 等。</td></tr></table>

# 4.1.2.2. 系统环境
<table><tr><td>系统组件</td><td>系统要求</td></tr><tr><td>Java 环境</td><td>JDK8-JDK24
·支持 Oracle JDK,但部分 Oracle JDK 版本商用收费,在生产使用时请注意商业授权,或采用 Open JDK、Tong JDK。
·启用国密认证,JDK 要求 JDK8-JDK11。
·使用虚拟线程,JDK 要求 JDK21。
·需要安装 JDK,不能仅安装 JRE。仅安装 JRE 会导致 TongWeb 部分功能不能使用。
·Linux 下若使用 IBM JDK,则需要手动放置如下 jar 包到“${tongweb.home}/lib/compatible”目录,否则启动 TongWeb 失败。
    ·JDK 8.0
        bcprov-jdk15on-1.70.jar
    ·JDK 8.0+
        bcprov-jdk18on-1.78.1.jar</td></tr><tr><td>内存</td><td>不低于80MB</td></tr><tr><td>硬件空间</td><td>不低于1024MB
推荐最低配置：4核CPU、4G内存、20G硬盘</td></tr><tr><td>浏览器</td><td>Microsoft IE 9/11、Mozilla Firefox 66.0-102.0、Google Chrome 75.0-105.0</td></tr></table>

# 4.1.3. 搭建前准备

# 4.1.3.1. 获取 TongWeb 安装包
已购买 TongWeb 产品，在 TongWeb 产品光盘中提供 TongWeb 安装包。

# 4.1.3.2. 获取 TongWeb license
如下以 “license.dat” 进行本地授权认证为例。
购买 TongWeb 产品后， TongWeb 产品光盘中提供了 license 文件。
TongWeb 支持轻量版、标准版、企业版及教学版。
版本功能差异通过 license 进行控制，请获取指定版本的 license。

# 4.1.3.3. 获取负载均衡器安装包（以 THS 为例）
THS 安装包命名格式为 TongHttpServer_6.x.x.x_arch_tar.gz。
其中，6.x.x.x 为版本号；arch 通常为硬件架构，如 aarch64、mips64el、x86_64 等。Linux 可使用 arch 命令查看，不同硬件架构使用不同安装包。
THS 主要由三部分组成：
• 主程序：httpserver，负载均衡、静态资源服务器功能。
• 高可用程序：httpserverHA，配置主备集群。
• 管理控制台：thsconsole-6.x.x.x.x.jar，控制台程序。
<table><tr><td>类别</td><td>说明</td></tr><tr><td>THS 安装包</td><td>·TongHttpServer_6.x.x.x_mips64el.tar.gz（龙芯 Linux）
·TongHttpServer_6.x.x.x_x86_64.tar.gz（x86 Linux）
·TongHttpServer_6.x.x.x_aarch64.tar.gz（ARM Linux）</td></tr></table>

# 4.1.4. 搭建规划
您可以在本机或者任一指定节点安装 TongWeb，并访问 TongWeb 管理控制台。
在 TongWeb 管理控制台通过创建节点、负载均衡器、TongDataGrid、集群的方式搭建集群。
在集群中可以任意增加负载均衡器、TongWeb 实例、TDG 节点，且无启动顺序要求。
如下示例以安装 TongWeb、创建两个远程节点、两个负载均衡器、两个实例、两个 TongData 为例进行说明。
规划图如下所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f91b63a1aa3b933e0d2f0cd38b79229b99ac9bcd8b994abcbb14955d18c1072d.jpg)
规划图说明，如下表所示。
<table><tr><td>组件</td><td>组件说明</td></tr><tr><td>集中管理</td><td>以将TongWeb安装在node01（168.1.15.44）节点为例进行说明。
您也可以根据需要将TongWeb安装在本机或者您准备的任一主机节点。</td></tr><tr><td>两个节点</td><td>node01（168.1.15.44）、node02（168.1.15.45）</td></tr><tr><td>两个负载均衡器（以THS为例）</td><td>ths01（主节点）、ths02（备节点）
说明：
以安装在node01（168.1.15.44）、node02（168.1.15.45）为例进行说明。</td></tr><tr><td>两个实例</td><td>TongWeb01、TongWeb02</td></tr><tr><td>两个会话服务器</td><td>session01、session02</td></tr></table>

# 4.1.5. 搭建运行环境

# 4.1.5.1. 安装及启动 TongWeb

# 4.1.5.1.1. 安装 TongWeb
完成安装包解压即完成 TongWeb 产品的安装。
由于node01（168.1.15.44）节点为 Linux 系统，本演示步骤为在 Linux 安装 TongWeb。
若您安装 TongWeb 的主机节点为 Windows，则请参照《TongWeb_V8.0安装与使用指引》中的“Windows 平台下安装 TongWeb”。
如下 “以将 TongWeb 安装在 node01（168.1.15.44）节点为例” 进行说明。
1. 登录 node01（168.1.15.44）节点。
2. 将安装包上传到待安装 TongWeb 的目录，以“home/test/”为例。
3. 执行如下命令，进入“home/test/”目录。
```txt
cd /home/test/
```
4. 执行如下命令，解压安装包，解压到的目录即为产品的安装目录。
安装包以“TongWebx.x.x.x.tar.gz”为例说明。
```txt
tar -zxf TongWebx.x.x.tar.gz
```

# 4.1.5.1.2. 安装 license
将获取的 license.dat 文件复制到安装完成的 TongWeb 根目录下：${tongweb.home}，如下图所示。
```txt
[root@n-stertongweb]#ll   
总用量79532   
drwxr-xr-x 3 root root 186 11月 18 02:05 bin   
drwxr-xr-x 3 root root 21 11月 18 02:04 domains   
drwxr-xr-x 3 root root 17 11月 18 02:04 lib   
-rwxr-xr-x 1 root root 1410 11月 18 02:04 license.dat   
drwxr-xr-x 12 root root 263 11月 18 13:54 version.1.3.1-FFP   
-rw-r--r-- 1 root root 81435448 11月 18 02:05 version.1.5.1-FFPOT.zip
```

# 注意：
• License 将根据授权产品名称、授权版本、版本类型以及授权 IP 来判断与产品是否匹配。
• 对于永久 license，用户在启动 TongWeb 后，系统会自动激活该 license，并且与 127.0.0.1 对应的 mac地址进行绑定。
◦ 若永久 license 的创建时间（create_time）处于 90 天以内，用户可自由拷贝，且拷贝后的 license均能正常完成激活与绑定操作。
◦ 若永久 license 的创建时间已超过 90 天，则该 license 将自动失效，无法再进行激活与绑定，进而导致 TongWeb 无法正常启动。

# 4.1.5.1.3. 启动 TongWeb
由于 node01（168.1.15.44）节点为 Linux 系统，本演示步骤为在 Linux 系统下启动 TongWeb。
若您安装 TongWeb 的主机节点为 Windows，则请参照《TongWeb_V8.0安装与使用指引》中的“Windows 环境下启动 TongWeb”。

# 注意：
Linux 环境下建议以后台模式启动服务器实例，执行 startd.sh 脚本，可防止 SSH 断开后 TongWeb 进程停止。

# 前置条件
• 已安装 TongWeb。
• 已安装 license。
• 已安装 JDK 并配置 JDK 环境变量。

# 操作步骤
1. 进入 “${tongweb.home}/bin” 目录。
2. 运行 ./startd.sh ，以后台模式启动 TongWeb 服务器默认实例。
若回显信息出现 “Server startup in xx seconds”，则说明启动 TongWeb 成功。
关于启停 TongWeb 的更多信息，详见《TongWeb_V8.0安装与使用指引》的 “启停 TongWeb” 章节。

# 4.1.5.2. 安装及启动 THS
TongHttpSever 的安装配置及管理控制台使用，请参见《TongHttpServer_V6.0用户手册》。
您可以将 THS 与 TongWeb 安装同一主机节点上或者不同主机节点上。
THS6仅包含Linux版本。
如下“以在 Linux 环境下安装并启动THS，且与 TongWeb 安装在同一主机节点”为例说明。
分别安装在 node 01节点 “168.1.15.44” 和 node02 节点 “168.1.15.45”，node 01 节点“168.1.15.44” 作为THS 主节点。

# 4.1.5.2.1. 安装 THS
以安装路径 “/home/opt/THS” 为例，安装过程说明，如下所示。
1. 分别将THS安装包上传到 node 01 节点 “168.1.15.44/home” 和 node02 节点 “168.1.15.45/home”。
2. 执行如下命令，进入 “/home” 目录。
cd home/
3. 执行如下命令，解压THS安装包，-C指定安装目录。
tar -zxvf THS_xxx.tar.gz -C /opt
注意：
◦ 若路径中带空格，则路径参数前后要加英文格式的引号。
◦ 路径最后面不要带“/”，执行完成后整个目录就不要移动到其它目录。

# 4.1.5.2.2. 安装 license
THS 主程序需要安装 license 才能启动。
只需将 license.dat 文件放在 THS 目录内或者 THS 同级目录即可。
注意：
THS 目录内 license 优先级高于 THS 同级目录。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/8b7e8abc4d238e24c38a5f8ccc37a0be71e7621b7b9212a90faafe07aabd0181.jpg)


# 4.1.5.3. 访问 TongWeb 控制台
关于访问 TongWeb 控制台的详细操作，请参见登录管理控制台。

# 4.1.6. 搭建集群
在完成 TongWeb 实例、负载均衡器、TDG 组件的准备后，用户可一键快速搭建集群。集群搭建成功后，用户可对集群中的多个 TongWeb 实例进行批量启停、统一维护管理。

# 4.1.6.1. 创建节点
集群是由一个或者多个节点上运行的实例组成。搭建集群时首先需要创建节点。
如下操作步骤，以 “SSH” 方式创建节点为例说明。手动创建节点的相关操作，请参见手动创建节点。

# 注意事项
在完成节点创建后，用户可使用 ps -ef|grep tongweb 命令，来查看业务进程。关于查看进程的更多信息，详见《TongWeb_V8.0安装与使用指引》的 “查看 TongWeb 进程” 章节。

# 前置条件
• 已获取管理员管理控制台账号和密码。
• 已准备好远程节点的 IP、端口、登录账号、密码。
• 远程节点已安装 JDK 1.8 及以上版本。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “节点”，进入节点页面。
4. 单击 “创建”，进入创建节点页面。

# 节点
＊名称
node01
168.1.15.44
*管理端口
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/740c9ebfaf56f847c05678afc19ecff6662d6650164b88864aa53b296d5a6a9c.jpg)
9061
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/240798b97c552661ce17c930e75cc69d06e5cb848a3e402072e8aaec9a1189ad.jpg)
*注册方式
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/996dd7ef84d0b6dc80c9bd338dc882c6bb3e7cdb998a61661c32e52f7346eb3e.jpg)
SSH
开机自启
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/8ccf20637c6db26b333c754e1c5dcc123cd80a97f163b256d274a78f85b70270.jpg)
22
*SSH用户名
root
认证方式
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/eee7cdce822fd389135686e9d1ba3f800fdeeae472ede6bff769fbdb66dc2878.jpg)
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/2bafed1c4bb1da8ec118e3ddc83270922ad292bfd12898499642130bb03f9ad1.jpg)
ne/test/tongweb
 JAVA HOME ?
/etc/test/jdk
$\textcircled{9}$

# 5. 配置节点相关参数。
请根据实际环境填写，如下信息为集群搭建规划的取值样例。
◦ 名称：node01
◦ IP：168.1.15.44
◦ 管理端口：9061
◦ 注册方式：SSH
◦ 开机自启：不开启
◦ SSH 端口：22
◦ SSH 用户名：root
◦ 认证方式：密码
◦ SSH密码：123456
◦ 安装路径：/home/test/tongweb
◦ JAVA_HOME：/etc/test/jdk
6. 单击 “添加”，完成节点（node01）添加操作。
若界面弹出 “节点添加成功” 提示信息，则说明节点添加成功。
添加成功后，节点默认处于 “启动” 状态。
注：若节点不为启动状态，请检查节点的相关配置的正确性，例如：JAVA_HOME 等。

# 7. 请参照 步骤3~步骤6，完成节点 node02 的创建。
◦ 节点名称：node02
◦ 节点IP：168.1.15.45
◦ 其他参数：请根据实际情况填写。
创建完成后，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/068b86e054617fd7ea2fac4e304379406f48155077d2ee0da129139621ecc4c3.jpg)


# 4.1.6.2. 创建 TongDataGrid
可选，您可以根据需要选择是否创建 TongDataGrid。
为了保证 session 不丢失，建议创建 TongDataGrid。
TongWeb 提供会话服务器 TongDataGrid（TDG）作为 Session 的存储库。
用户在控制台上创建的多个会话服务器会自动搭建为 TDG 集群，当其中一个会话服务器所在节点发生故障后，能保障 session 数据不丢失。
创建 TongDataGrid 后，您可以在 “${tongweb.base}/data/centralized/tdg/” 查看到创建的 session 实例。

# 前置条件
• 已获取管理控制台账号和密码。
• 已创建节点且节点 “运行中” 为 “true”。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “资源配置” $>$ “TongDataGrid”，进入 TongDataGrid 页面。
4. 单击 “创建”，进入创建 TongDataGrid 页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/e6cb097b0b35f448c9426c7f3cfe1e009c99a394778e40218780ba941688617d.jpg)
5. 配置 TongDataGrid 相关参数，如下所示。
◦ 名称：session
◦ 所在节点：node01、node02
◦ 实例数量：1
◦ 其他参数：请根据需要填写。
6. 单击 “添加”，完成 TongDataGrid（session）添加操作。
若界面弹出 “TongDataGrid 添加成功” 提示信息，则说明 TongDataGrid 添加成功。
添加成功后，TongDataGrid 运行中默认 “false” 状态。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/64ead0bd7ff28d39d561eaf065b0ffe409744c35eeafe14c3f2b73dd2279d294.jpg)
7. 单击目标 TongDataGrid 所在行的 “启动”，弹出确认启动窗口。
8. 单击 “确定”，完成 TongDataGrid 的启动操作。
若界面弹出 “TongDataGrid 启动成功” 提示信息，则说明 TongDataGrid 启动成功。
运行中状态更新为 “true”。

# 4.1.6.3. 创建负载均衡器
TongWeb 支持东方通自研的 THS6.0、Nginx1.20 以及 Apache2.2 负载均衡器。
创建负载均衡器前，请先安装负载均衡器。
<table><tr><td>负载均衡器</td><td>支持的版本</td><td>安装说明</td></tr><tr><td>THS</td><td>THS6.0</td><td>请参见 安装及启动ths。</td></tr><tr><td>Nginx</td><td>Nginx1.20</td><td>请参见 官网。</td></tr><tr><td>Apache</td><td>Apache2.2</td><td>请参见 官网。</td></tr></table>
为了保障集群高可用性，您可以启动负载均衡器的高可用功能。
如下示例 “以东方通自研的 THS6.0 负载均衡器为例” 进行说明。

# 前置条件
• 已获取管理控制台账号和密码。
• node01、node02 节点上已安装 THS 负载均衡器。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “负载均衡器”，进入负载均衡器页面。
4. 单击 “创建”，进入创建负载均衡器页面。

# 负载均衡器创建☆
*名称
ths01
宕机重启
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/975b9da69b1239e4926e382d3fb65372f3734c37c48c83f7101ec48a94c6f32e.jpg)
自启动
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/7d5681bc86e88a87e84381e2ffaadaf569f4d91bc049f7549c74e045711b9a68.jpg)
*类型
THS
Nginx
THS 控制台地址
所在节点
node01
*安装路径
/home//THS

# 5. 配置负载均衡器相关参数。
请根据实际环境填写，如下信息为集群规划的取值样例。
◦ 名称：ths01
◦ 宕机重启：不开启
◦ 自启动：不开启
◦ 类型：THS
◦ THS 控制台地址：不填写
◦ 所在节点：node01
◦ 安装路径：/home/test/THS
6. 单击 “添加”，完成负载均衡器（ths01）添加操作。
若界面弹出 “负载均衡器添加成功” 提示信息，则说明负载均衡器添加成功。
添加成功后，节点 “运行中” 默认为 “false” 状态。
7. 单击负载均衡器所在行的 “启动”，启动负载均衡器。
8. 参照步骤 4 ~ 步骤 7，完成负载均衡器（ths02）的添加操作。
创建并启动负载均衡器后，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/50b727ab3c7ea34e98aab4d7a567b3f7dd971a8087d24a8fcd61f1b2dcd10182.jpg)


# 4.1.6.4. 创建集群
节点和负载均衡器创建完成后，即可开始创建集群。

# 注意事项
在创建集群时，默认在每个节点上创建一个实例。
若需要给集群的节点增加实例，请参见 扩容集群实例。

# 前置条件
• 已获取管理控制台账号和密码。
• 已创建节点且节点 “运行中” 为 “true”。
• 已创建负载均衡器。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “集群”，进入集群页面。
4. 单击 “创建”，进入创建集群页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/d49e9c744506241c84b5745a70b98320807358ff6932fb3ca7e60ac7c8743c6e.jpg)
5. 配置集群相关参数，如下所示。
请根据实际环境填写，如下信息为集群规划的取值样例。
<table><tr><td>参数</td><td>取值</td></tr><tr><td>名称</td><td>cluster</td></tr><tr><td>节点</td><td>node01、node02</td></tr><tr><td>负载均衡器</td><td>ths01、ths02</td></tr><tr><td>负载均衡器监听端口</td><td>9200</td></tr><tr><td>其他参数</td><td>采用默认值，也可以根据需要修改配置。</td></tr></table>
6. 单击 “添加”，完成集群（cluster）的添加操作。
若界面弹出 “集群添加成功” 提示信息，则说明集群添加成功。
添加成功后，集群 “运行中” 默认为 “false” 状态。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/afa401a1c47c151fb0106d4134ac82f69dada105499c28b7ae6928a42f359660.jpg)
7. 在左侧导航栏中，单击 “实例”，可查看创建集群时创建的实例。
实例 “运行中” 为 “false”，则说明创建集群时自动创建的实例默认处于 “停止” 状态。

# 4.1.6.5. 启动集群
集群创建成功后，运行中状态默认为 “false”。部署应用前，您需要启动集群。

# 前置条件
• 已获取管理控制台账号和密码。
• 已创建节点且节点 “运行中” 为 “true”。
• 已创建负载均衡器。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “集群”，进入集群页面。
4. 单击目标集群所在行的 “启动”，弹出确认启动集群窗口。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/ad7ec9b7223d5f8458473b51cd360cc683066bfbf99d3aa24641575faad53abf.jpg)
5. 单击 “确定”，完成集群启动操作。
若界面弹出 “启动集群成功” 提示信息，则说明启动集群成功。
集群运行中状态变更为 “true”。
用户可单击 “实例数量” 对应的数字，跳转到实例列表页面。同时可查看到实例也同步启动。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/c28eafbd199f13c896c9c58bd1aa07819a6459edb5bec0ffc63b365083e5008c.jpg)


# 4.1.6.6. 切换集群
集群启动成功后。为了能对目标集群进行管理，您需要切换到该集群。

# 前置条件
• 已获取管理控制台系统管理员账号和密码。
• 已创建且启动集群。

# 操作步骤
1. 进入 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “集群”，进入集群页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/685332eef854b0b5dc2785ca554a573edb6b605821e1c48d51c38f699870342d.jpg)
4. 单击目标集群所在行的 “管理”，切换到指定集群。
您即可在该集群上进行应用管理、Web 容器、EJB 容器、其它容器、资源管理、监视管理等管理。

# 4.1.6.7. 管理集群
通过如上操作，用户即可实现对不同节点上的多个实例进行统一管理。用户可根据实际业务需求，针对目标集群的多个实例进行应用管理、Web 容器、EJB 容器、其它容器、资源管理、监视管理等操作。
关于应用管理、Web 容器、EJB 容器等相关配置操作，详见 应用管理 和 配置管理。

# 注意：
• 通过集群的 “管理” 入口修改通道配置时，若没有主动编辑 IP 和端口，系统将不会下发这两个值到所包含的实例上，以减小可能的端口冲突风险。
• 为了避免普通运维人员对默认实例 domain1 进行操作，系统支持用户采用权限分配的方式，将默认实例domain1 隐藏，详见权限分配。

# 4.1.6.8. 示例说明

# 4.1.6.8.1. 部署应用
集群搭建完成后，您可以在集群的实例上部署应用。通过集群部署应用，应用会同时部署在每个 TongWeb节点实例上。

# 前置条件
• 已获取管理控制台的账号和密码。
• 已搭建集群。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标集群。
3. 在左侧导航栏中，选择 “应用管理” > “应用”，进入应用页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/eb55ec82b366b4b3dde8316836d6706c120d90c7bdce02af0a6d3fd20b2f3d69.jpg)
4. 单击 “部署”，进入部署应用页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/52faf6b6aeea03a3d9a9f99deb63e05dc25f3f0c49618079d2b93cde53a8f19a.jpg)
5. 单击 “选择文件”，上传应用。
◦ 应用来源：上传文件，当前以 “${tongweb.home}\version*\examples\examples.war” 为例。
◦ 上传应用：控制台默认关闭上传文件功能。若需要开启，请参见禁用文件上传。
◦ 其他参数：请根据需要进行配置。
6. 单击 “添加”，完成应用的添加。
若界面弹出 “应用添加成功” 提示信息，则说明应用添加成功。
您可以登录到各节点上，查看各实例上已部署该应用。

# 4.1.6.8.2. 客户端访问应用
负载均衡器部署在最前端，客户端访问的是负载均衡器地址。
本次搭建集群示例中，创建负载均衡器时，负载均衡器的主节点IP为 “168.1.15.44”。
您可以通过管理控制台的应用列表中的“链接”，访问应用。

# 前置条件
• 已获取管理控制台的账号和密码。
• 已搭建集群。
• 已部署应用。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 切换到目标集群。
3. 在左侧导航栏中，选择 “应用管理” > “应用”，进入应用列表页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/9c2a28dacfdc2968de038efd76ee703dcf975fc8a5b16f93c3b60bcb159b9d58.jpg)
4. 单击目标应用所在行的 “链接”，进入应用链接页面。
可查看到生成的应用链接的 IP 和端口为负载均衡器的 IP 和端口。
注：当使用负载均衡器时，固定为 http 。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/0587bf40330a2901bd122e218f0d97e0b24d251ec4654fbfe1b471c3e2932eb7.jpg)
5. 单击生成的应用链接，即可访问应用。

# 4.2. 服务管理

# 4.2.1. 集群管理
为了构建 TongWeb 集群，您需要使用 THS 和 TDG 会话服务器。
通过集中管理，用户可以方便地在企业生产环境中管理和配置多个 TongWeb 实例以及轻松组建 TongWeb集群。这为用户管理 TongWeb 集群提供了便利。

# 4.2.1.1. 扩容集群节点
若当前集群中的节点无法满足您的需求，您可以为集群添加额外的节点。

# 前置条件
• 已获取管理员管理控制台账号和密码。
• 已准备好远程节点的IP、端口、登录账号、密码。
• 节点已安装 JDK 1.8 及以上版本。

# 步骤1：创建节点
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “节点”，进入节点页面。
4. 单击 “创建”，进入创建节点页面。
5. 配置节点相关参数。
◦ 节点名称：以 “node03” 为例。
◦ 其他参数：请根据实际情况配置。
关于创建节点的操作，详见创建节点。
6. 配置完成后，单击 “添加”，完成节点创建的相关操作。

# 步骤2：创建实例
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例页面。
4. 单击 “创建”，进入创建实例页面。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/655aacbfad70d7fef5f81e154fe6743acd75016da412dc51d3a81eadcfbb6703.jpg)
相关配置信息，如下所示。
◦ 所在节点：选择 步骤1 中创建的节点（node03）。
◦ 所属集群：选择待扩容节点的集群（cluster）。
◦ 其他参数：请根据需要配置。

# 5. 单击 “添加”，完成实例的创建。
在集群列表页面，可查看扩容实例以及实例对应的节点。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/38e7a49e366c08616a411a77f45543fa5c04543a6c98d5845463ad3492e0d29f.jpg)
6. 在左侧导航栏中，单击 “集群”，您即可对该节点实例进行管理。

# 4.2.1.2. 扩容集群实例
若当前节点的实例不能满足您的需求时，您可以为集群增加实例。
您可以为已在集群中的节点添加实例，或者创建额外的节点，在额外的节点上添加实例，然后关联到集群。
本章节介绍为已在集群中的节点添加实例。 关于创建额外节点，并在额外节点上添加实例，然后关联到集群的操作，请参见扩容集群节点。

# 前置条件
已添加集群。

# 操作步骤
如下“以集群为 cluster、节点为 node01、添加的实例名称为 instance03 为例”说明。
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例页面。
4. 单击 “创建”，进入创建实例页面。

# 实例e
*名称
instance03
宕机重启
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/43d4dc6528c2596524655ec71b2cae94981bc61aac902e8e2b9e151ecb770e5d.jpg)
自启动
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/5dff7ad24bb2d570f149ad4d43ddf06dd3475de1a232e5b85dcdf8e4503642f6.jpg)
别名
所在节点
node01
实例模板
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/112d6f9a82d785d820d62ffaa34fd52bbe4f707931db5cb26cc5f9c090a92c8a.jpg)
指定安装目录
所属集群
cluster
应用端口
建管理端口
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/1ee266822bebe14399995b9dcd8f442fe66f200dd01a048ad8d12517c8c0af5b.jpg)
管理端口
配置信息，如下所示。
◦ 名称：instance03
◦ 所在节点：node01
◦ 所属集群：cluster
◦ 其他参数：请根据实际情况填写。
5. 配置完成后，单击 “添加”，完成实例的添加操作。
在实例列表页面，您可以查看到已添加到集群中的实例 instance03，如下图所示。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/cbc128545134b3ef30061b000c9402e23b40dc26745c59717591f3675048301c.jpg)


# 4.2.1.3. 集群开机自启
当您已创建节点、TongDataGrid、负载均衡器、集群和实例，且开启了 “开机自启”。
• 节点开启 “开机自启”，是通过做 tongweb.service 自启动服务，使主机节点的默认实例 domain1 启动起来。
虚拟机开机脚本默认需要 root 用户，但用户可以修改 tongweb.service 的内容，修改为其它用户启动TongWeb，详见开机自启动方案说明。
注：Windows 系统不支持节点开机自启。

# 节点
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/f8fa70c1cb0251165a2bb6351ae9cbe2f1e0f88db887030002decc84b04600e4.jpg)
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/16a90606dd30e947574da623bc03921c6d2d5e7e8ba131414b89403298a4d374.jpg)
• 节点启动后，自动启动默认实例 “domain1”。通过默认实例 “domain1” 带动 TongDataGrid、负载均衡器、集群和其它实例启动。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/2e0511f1d64af7f8fc526db43278ba739bec7799e94e17da6ed7ee12663f3e00.jpg)


# 4.2.1.4. 管理集群
本章节介绍如何创建、查看、切换、编辑、启动、停止、强停、删除集群以及移除集群记录。

# • 创建集群
节点和负载均衡器创建完成后，即可开始创建集群。
注：支持创建空集群，用户可根据需要在集群中添加实例，更多信息请参见 扩容集群实例。
1. 选择 “集中管理” $>$ “服务管理” $>$ “集群”，进入集群页面。
2. 单击 “创建”，进入创建集群页面。
3. 配置集群的相关参数。
名称： 必填项，输入集群的名称。请使用常规英文字母，避免使用空格、斜杠、标点等特殊字符。
关于集群的更多参数说明，详见集群配置参数说明。
4. 单击 “添加”，即可完成集群的添加操作。

# • 查看集群
1. 选择 “集中管理” $>$ “服务管理” $>$ “集群”，进入集群页面。
2. 在集群列表页面，您可以查看已创建的集群。
包含集群的名称、运行中、实例数量、负载均衡器、实例版本、待升级等信息。
说明：
用户可单击集群对应的实例数量，跳转到实例列表页面。

# • 查看集群链接
您可以通过 HTTP 协议访问该集群的 URL。
注：若当前集群没有使用负载均衡器，则该集群链接显示为实例的链接 URL。
1. 选择 “集中管理” $>$ “服务管理” $>$ “集群”，进入集群页面。
2. 单击目标集群所在行的 “链接”，进入 “集群/链接” 页面。
▪ 链接 IP：负载均衡器的 IP 地址。
▪ 链接端口：负载均衡器的监听端口。
若您已部署应用，您可以在该链接地址后，加上应用的访问前缀，即可访问该应用。

# 集群／链接
状态:
true
消息:
集群链接成功
http://168.1.15.44:9200
http://168.1.15.45:9200

# • 切换集群
通过集群您可以将应用批量部署到集群的各个 TongWeb 节点上。在部署应用前需要切换到目标集群。已创建集群且该集群 “运行中” 状态为 “true”。若不为 “true”，请先启动集群。启动集群后方可切换集群。
1. 选择 “集中管理” $>$ “服务管理” $>$ “集群”，进入集群页面。
2. 单击目标集群所在行的 “管理”，即可切换到目标集群。
在管理控制台的左上角，可查看已进入该集群所在页签，您即可对该集群进行操作，包含应用管理、Web 容器、EJB 容器、资源管理、基础配置等。

# • 编辑集群
1. 选择 “集中管理” $>$ “服务管理” $>$ “集群”，进入集群页面。
2. 单击目标集群名称，进入编辑集群页面。
3. 您可以根据提示修改集群信息。
说明：
集群名称不可编辑。
4. 编辑完成后，单击 “更新”，更新集群配置信息。
若界面弹出 “集群更新成功” 提示信息，则说明编辑集群成功。

# • 启动集群
已创建集群，且集群处于 “停止” 状态时可启动集群。启动集群的同时，集群中的实例会同步启动。
1. 选择 “集中管理” $>$ “服务管理” $>$ “集群”，进入集群页面。
2. 单击目标集群所在行的 “启动”，弹出确认启动窗口。
说明：
用户可根据需要勾选一个或多个集群，并单击列表上方的 “启动” 按钮，批量启动集群。
3. 单击 “确定”，启动集群。
若界面弹出 “集群启动成功” 提示信息，则说明启动集群成功。

# • 停止集群
已创建集群，节点处于 “运行” 状态时可停止集群。停止集群的同时，集群中的实例会同步停止。
1. 选择 “集中管理” $>$ “服务管理” $>$ “集群”，进入集群页面。
2. 单击目标集群所在行的 “停止”，弹出确认停止窗口。
说明：
用户可根据需要勾选一个或多个集群，并单击列表上方的 “停止” 按钮，批量停止集群。
3. 单击 “确定”，停止集群。
若界面弹出 “集群停止成功” 提示信息，则说明停止集群成功。

# • 强停集群
当集群长时间难以成功停止，或者停止过程出现意外阻塞的情况时，您可以选择使用强制停止进程功能，强制停止通常是以强制杀进程的方式实现。集群状态处于 “运行中”。
1. 选择 “集中管理” $>$ “服务管理” $>$ “集群”，进入集群页面。
2. 单击目标集群所在行的 “强停”，弹出强制停止确认窗口。
说明：
用户可根据需要勾选一个或多个集群，并单击列表上方的 “强停” 按钮，批量强停集群。
3. 单击 “确定”，强制停止该集群。
若界面弹出 “集群强停成功” 提示信息，则说明集群强制停止成功。

# • 重启集群
重启集群可将集群下的所有实例进行重启。若开启了 “滚动更新”，实例重启操作将会逐个进行，否则多个实例会同时进行。
1. 选择 “集中管理” $>$ “服务管理” $>$ “集群”，进入集群页面。
2. 单击目标集群所在行的 “重启”，弹出确认重启集群窗口。
3. 单击 “确定”，即可重启集群。

# • 删除集群
若需要删除集群，请先停止集群，并解除集群与其它组件的关联。删除后不可恢复，请谨慎操作。删除集群时，集群引用的其它组件不会被删除。
1. 选择 “集中管理” $>$ “服务管理” $>$ “集群”，进入集群页面。
2. 单击目标集群所在行的 “删除”，弹出确认删除窗口。

# 说明：
用户可根据需要勾选一个或多个集群，并单击列表上方的 “删除” 按钮，批量删除集群。
3. 单击 “确定”，完成集群的删除操作。
若界面弹出 “集群删除成功” 提示信息，则说明删除集群成功。

# 4.2.2. 实例管理

# 4.2.2.1. 多实例场景
通常情况下一台服务器只需要安装一套 TongWeb。
若存在如下场景，则可通过创建多个实例的方式解决。
<table><tr><td>场景</td><td>场景说明</td></tr><tr><td>场景一</td><td>服务器CPU、内存比较大，可通过创建多个TongWeb实例，充分利用系统资源。</td></tr><tr><td>场景二</td><td>不同应用需要使用不同JDK版本，关于如何给不同实例配置不同的JDK版本，请参见不同实例配置不同JDK版本。</td></tr><tr><td>场景三</td><td>应用之间互相冲突，需要分别部署在不同TongWeb实例上。</td></tr><tr><td>场景四</td><td>应用有内存溢出或占用线程资源多，频繁出问题的放一个TongWeb实例上运行，不影响其它应用。</td></tr></table>

# 4.2.2.2. 创建实例
• 绝对路径实例管理：支持将 TongWeb 实例安装到一个指定的绝对目录（若目录不存在，TongWeb 将则会自动建立）。
注：Windows 下创建实例时，若需要指定安装目录，可能需要管理员启动 TongWeb。
• 相对路径实例管理：若未指定安装目录，则默认安装到 “${tongweb.base}/domains” 目录下。

# 注意事项
• 用户可通过创建无控制台端口的实例。创建实例时，在创建实例页面，关闭 “创建管理端口” 开关即可。用户也可通过 “admin.[bat|sh]” 脚本创建无控制台端口实例。详见 domain。
• 无控制台端口的实例不支持远程管理，用户仅能对该实例进行启停操作。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例页面。
4. 单击 “创建”，进入创建实例页面。
5. 配置实例的相关参数。
◦ 名称：必填项，实例的名称，唯一标识。
◦ 所在节点：必填项，在下拉列表中选择实例所在的集群。
关于实例的更多参数说明，详见实例配置参数说明。
6. 配置完成后，单击 “添加”，完成实例的添加操作。

# 4.2.2.3. 启停实例
用户可通过控制台界面启动实例，也可通过脚本启动实例，详见脚本启停实例。

# 启动实例
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例列表页面。
4. 单击目标实例所在行的 “启动”，弹出确认启动窗口。

# 说明：
用户可根据需要勾选一个或多个实例，并单击列表上方的 “启动” 按钮，批量启动实例。
5. 单击 “确定”，启动实例。
若界面弹出 “实例启动成功” 提示信息，则说明启动实例成功。

# 停止实例
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例列表页面。
4. 单击目标实例所在行的 “停止”，弹出确认停止窗口。

# 说明：
用户可根据需要勾选一个或多个实例，并单击列表上方的 “停止” 按钮，批量停止实例。
5. 单击 “确定”，停止实例。
若界面弹出 “实例停止成功” 提示信息，则说明停止实例成功。

# 4.2.2.4. 切换实例
本章节介绍如何切换到实例。

# 前置条件
• 已获取管理控制台系统管理员（thanos）的账号和密码。
• 实例列表中存在不隶属于集群的实例。
• 实例处于 “启动” 状态。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台的左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例列表页面。
4. 单击目标实例所在行的 “管理”，切换到目标实例。
您即可对当前实例进行相关操作。

# 4.2.2.5. 下载日志
实例所在节点处于“启动中”时，您才可以下载该实例运行的日志，包含gc.log、jvm.log、access.log、server.log、audit.log 等。

# 注意事项
控制台默认关闭文件下载功能。若需要开启，请参见禁用文件下载。

# 前置条件
• 已获取系统管理员（thanos）账号和密码。
• 实例列表已有实例。
• 实例所在节点 “运行中” 为 “true”。

# 操作步骤
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “服务管理” $>$ “实例”，进入实例列表页面。
4. 单击目标实例所在行的 “下载”，弹出选择待下载日志文件窗口。
![image](https://cdn-mineru.openxlab.org.cn/result/2026-02-02/fbf12dc5-4b4f-43db-b04c-4f7f4b5aaccc/9840f6890abcc7338eb0b604966a7eb0e697a9eb6edc5b72376a2a1d07e4ce35.jpg)
5. 勾选需要下载的日志文件。
6. 单击 “确定”，即可将日志下载到本地。
下载的日志文件的压缩包以实例名称命名。

# 4.2.2.6. 管理实例
本章节介绍如何查看、管理、编辑、强停、删除实例以及移除实例记录。

# 查看实例
1. 选择 “集中管理” $>$ “服务管理” $>$ “实例”，进入实例列表页面。
2. 在实例列表页面，您可以查看已创建的实例。
包含实例的名称、运行中、别名、管理端口、所在节点、所属集群、实例版本、待升级以及应用端口等信息。

# 管理实例
用户可以根据需要将应用部署在集群的指定实例。
1. 选择 “集中管理” > “服务管理” $>$ “实例”，进入实例列表页面。
2. 单击目标实例所在行的 “管理”，进入指定实例管理页面。
用户可根据需要部署、管理应用等。

# 编辑实例
注：用户可根据需要重命名实例名称。
1. 选择 “集中管理” $>$ “服务管理” $>$ “实例”，进入实例列表页面。
2. 单击目标实例名称，进入编辑实例页面。
3. 您可以根据提示修改实例信息。
4. 编辑完成后，单击 “更新”，更新实例配置信息。
若界面弹出 “实例更新成功” 提示信息，则说明编辑实例成功。

# 强停实例
当实例长时间难以成功停止，或者停止过程出现意外阻塞的情况时，您可以选择使用强制停止进程功能，强制停止通常是以强制杀进程的方式实现。
您可以通过控制台界面方式强停实例，也可以通过执行 “forcestop.[bat|sh]”脚本强制停止实例。
若需要强制停止指定实例，则执行 “./forcestop.[bat|sh] 实例名”。
1. 选择 “集中管理” $>$ “服务管理” $>$ “实例”，进入实例列表页面。
2. 单击目标实例所在行的 “强停”，弹出强制停止确认窗口。

# 说明：
用户可根据需要勾选一个或多个实例，并单击列表上方的 “强停” 按钮，批量强停实例。
3. 单击 “确定”，强制停止该实例。
若界面弹出 “实例强停成功” 提示信息，则说明实例强制停止该实例成功。

# 重启实例
1. 选择 “集中管理” $>$ “服务管理” $>$ “实例”，进入实例列表页面。
2. 单击目标实例所在行的 “重启”，弹出重启确认窗口。
3. 单击 “确定”，即可重启实例。

# 删除实例
删除实例时，实例引用的其它组件不会被删除。
1. 选择 “集中管理” $>$ “服务管理” $>$ “实例”，进入实例列表页面。
2. 单击目标实例所在行的 “删除”，弹出确认删除窗口。

# 说明：
用户可根据需要勾选一个或多个实例，并单击列表上方的 “删除” 按钮，批量删除实例。
3. 单击 “确定”，完成实例的删除操作。
若界面弹出 “实例删除成功” 提示信息，则说明删除实例成功。

# 移除实例记录
当该实例无法删除或者冗余时，可从控制台实例列表中删除记录。

# 注意事项
• 当实例所在节点处于运行中时，不允许直接移除记录。
• 移除记录前，请先停止实例，并解除实例与其它组件的关联。
• 移除记录后，服务器的日志记录了完整的信息日志；当出现误删除时，可以通过该信息进行恢复。

# 操作步骤
1. 选择 “集中管理” $>$ “服务管理” $>$ “实例”，进入实例列表页面。
2. 单击目标实例所在行的 “移除记录”，弹出确认移除记录窗口。