# 原创TongWeb8 错误码查询方法及说明

> 原文地址: https://blog.csdn.net/realwangpu/article/details/144113497

---

TongWeb8可通
过
./admin.[bat|sh] error-code [Error Code]
命令查
找错误码
说
明。
如：./admin.sh error-code  显示所有错误码说明。
./admin.sh error-code  008  显示008错误码的说明。
Execute the command: error-code
****** TongWeb ErrorCode Info ******
000:
%s
%s
%s
001:
部署应用的名称或ID冲突，例如EJB应用的名字已被其它应用占用
部署應用的名稱或ID沖突，例如EJB應用的名字已被其它應用占用
The name or ID of the deployed application conflicts, for example, the name of the EJB application is already occupied by another application
002:
请检查实例或集群状态
請檢查實例或集群狀態
Please check instance or cluster status
003:
未找到所需要的文件或文件访问权限受限：%s
未找到所需要的文件或文件訪問權限受限：%s
The required file not found or file access restricted: %s
004:
启用JTA支持，要求驱动类型为XA类型，您也可以配置JTA事务允许非XA事务分支
啟用JTA支持，要求驅動類型為XA類型，您也可以配置JTA事務允許非XA事務分支
To enable JTA support, the driver type is required to be XA type, you can also configure JTA transactions to allow non-XA transaction branches
005:
使用指定的驱动和URL无法连接到数据库
使用指定的驅動和URL無法連接到數據庫
Cannot connect to the database using the specified driver and URL
006:
指定的目录或文件没有创建成功
指定的目錄或文件沒有創建成功
The specified directory or file was not created successfully
007:
PersistenceUnit需要JTA支持，但没有定义支持JTA的数据源
PersistenceUnit需要JTA支持，但沒有定義支持JTA的數據源
PersistenceUnit requires JTA support, but no data source is defined to support JTA
008:
数据库驱动类加载失败，请确保已经正确配置了数据库 JDBC 驱动包
數據庫驅動類加載失敗，請確保已經正確配置了數據庫 JDBC 驅動包
The database driver class failed to load, please ensure that the database JDBC driver package has been configured correctly
009:
文件须是 *.zip 类型的
文件須是 *.zip 類型的
The file must be *.zip type
010:
服务器正在启动中或相关服务尚未就绪，请稍后重试
服務器正在啟動中或相關服務尚未就緒，請稍後重試
The server is starting or related services are not ready, please try again later
011:
无法加载 servlet 类：%s
無法加載 servlet 類：%s
Unable to load servlet class:%s
012:
没有这样的方法，类型：%s，操作：%s
沒有這樣的方法，類型：%s，操作：%s
No such method, type: %s , operation: %s
013:
数据源资源 (%s) 未找到且未成功自动创建
數據源資源 (%s) 未找到且未成功自動創建
DataSource Resource(%s) not found and not automatically created successfully
014:
请检查端口 [%s] 是否正确
請檢查端口 [%s] 是否正確
Please check if the port [%s] is correct
015:
远程服务器[%s:%s]请求错误：%s。 请查看日志以获取详细信息
遠程服務器[%s:%s]請求錯誤：%s。 請查看日誌以獲取詳細信息
Remote server [%s:%s] request error: %s. Please check the logs for details
016:
配置文件[%s]没有找到
配置文件[%s]沒有找到
Configuration file [%s] not found
017:
尝试指定应用程序附带的 JSF 实现的使用
嘗試指定應用程序附帶的 JSF 實現的使用
Try to specify the use of the JSF implementation that comes with the application
018:
无法正常识别应用类型，请检查要部署的应用文件是否合法
無法正常識別應用類型，請檢查要部署的應用文件是否合法
The app type cannot be recognized properly, so check whether the app file to be deployed is legitimate
019:
部署的应用程序名称不支持包含特殊字符，例如#: %s
部署的應用程序名稱不支持包含特殊字符，例如#: %s
The name of the deployed application cannot contain special characters such as #: %s
020:
找不到应用备份
找不到應用備份
App backup not found
021:
应用程序增量更新文件必须是 *.zip 类型
應用程序增量更新文件必須是 *.zip 類型
The application incremental update file must be of the *.zip type
022:
不支持删除系统预置的通道：%s
不支持刪除系統預置的通道：%s
Cannot delete a system managed connector: %s
023:
不支持停止系统预置的通道：%s
不支持停止系統預置的通道：%s
You cannot stop the system managed connector: %s
024:
不支持删除系统预置的虚拟主机
不支持刪除系統預置的虛擬主機
Deleting a system managed virtual host is not supported
025:
该实例已加入集群[%s]，不支持此操作
該實例已加入集群[%s]，不支持此操作
The instance is already joined to a cluster [%s] and does not support this operation
026:
SSH身份验证失败，请检查用户名、密码或密钥是否正确
SSH身份驗證失敗，請檢查用戶名、密碼或密鑰是否正確
SSH authentication failed, please check if the username, password or secret key is correct
027:
SSH获取执行结果超时，请检查执行状态或重试
SSH獲取執行結果超時，請檢查執行狀態或重試
SSH timed out to get the execution result, please check the execution status or try again
028:
SSH获取执行发生未知异常，请查看日志详情
SSH獲取執行發生未知異常，請查看日誌詳情
An unknown exception occurred during SSH fetch execution, please check the log details
029:
安全域连接异常，请检查连接信息
安全域連接異常，請檢查連接信息
Realm connection is abnormal, please check the connection information
030:
当前服务器正在运行中，不支持此操作，请停止后重试
當前服務器正在運行中，不支持此操作，請停止後重試
The current server is running, this operation is not supported, please stop and try again
031:
不支持构建的版本类型[ %s ]
不支持構建的版本類型[ %s ]
Version types [ %s ] not supported for builds
032:
证书密码不正确
證書密碼不正確
KeyStore password was incorrect
033:
不是一个有效的升级文件
不是一個有效的升級文件
Not a valid upgrade file
034:
该版本正在被域 [ %s ] 使用，不可进行更新、删除等操作
該版本正在被域 [ %s ] 使用，不可進行更新、刪除等操作
This version is being used by domain [ %s ] and cannot be updated, deleted, etc
035:
实例[%s]获取remotekey失败，请检查remotekey配置
實例[%s]獲取remotekey失敗，請檢查remotekey配置
Instance [%s] failed to obtain the remotekey, please check the remote configuration
036:
名称[%s]已被使用，如列表中没有，请检查节点的domains目录下是否已存在同名文件夹
名稱[%s]已被使用，如列表中沒有，請檢查節點的domains目錄下是否已存在同名文件夾
The name [%s] has already been used, if not in the list, please check whether a folder with the same name already exists in the domains directory of the node
037:
应用端口[%s]已被使用
應用端口[%s]已被使用
App port [%s] is used
038:
管理端口[%s]已被使用
管理端口[%s]已被使用
Manage port [%s] is used
039:
不支持
不支持
Not supported
040:
请检查节点[%s]是否启动或管理端口[%s]是否配置正确
請檢查節點[%s]是否啟動或管理端口[%s]是否配置正確
Please check if node [%s] is started or if management port [%s] are configured correctly
041:
未找到节点[%s]
未找到節點[%s]
Node [%s] not found
042:
轻量模式下不支持部署 *.jar(ejb) *.ear *.rar 类型的应用，请选择 *.war 类型的应用文件
輕量模式下不支持部署 *.jar(ejb) *.ear *.rar 類型的應用，請選擇 *.war 類型的應用文件
Deploying *.jar(ejb) *.ear *.rar type apps is not supported in lightweight mode, please select an application file of *.war type
043:
文件权限不足:%s
文件權限不足:%s
File permission denied:%s
044:
端口[%s]已被使用
端口[%s]已被使用
Port [%s] is used
045:
须是一个合法的目录
須是一個合法的目錄
Must be a legal directory
046:
无法创建符号链接，可能是因为缺少必要的权限
無法創建符號鏈接，可能是因為缺少必要的權限
Failed to create symbolic link, possibly because the necessary permissions are missing
047:
该类型的版本已存在，无需再次生成
該類型的版本已存在，無需再次生成
A version of the type already exists and does not need to be built again
048:
已经存在相同名称的应用
已經存在相同名稱的應用
A application with the same name already exists
049:
转换为TongWeb应用时发生异常，应用部署失败
轉換為TongWeb應用時發生異常，應用部署失敗
An exception occurred while converting to TongWeb app. The app deployment failed
050:
类 %s 未找到
類 %s 未找到
Class %s not found
051:
公钥参数错误
公鑰參數錯誤
The public key parameter is incorrect
052:
admin 通道重启中，请稍后再试
admin 通道重啟中，請稍後再試
The admin connector is restarting, please try again later
053:
Redis身份验证失败，请检查用户名、密码是否正确
Redis身份驗證失敗，請檢查用戶名、密碼是否正確
Redis authentication failed, please check if the username, password  is correct
054:
Redis连接异常，请检查redis服务是否启动或者网络是否能够连接
Redis連接異常，請檢查redis服務是否啟動或者網路是否能夠連接
If the Redis connection is abnormal, check whether the Redis service is enabled or whether the network can be connected
055:
OSGi 服务异常
OSGi 服務異常
The OSGi service is abnormal
056:
OSGi 服务未启动
OSGi 服務未啟動
The OSGi service did not start
057:
文件须是 *.jar 类型的
文件須是 *.jar 類型的
The file must be *.jar type
058:
服务器未安装docker环境，版本生成失败
服務器未安裝docker環境，版本生成失敗
The server does not have the docker environment installed, and the version generation fails
059:
构建docker镜像超时或出错，详情请查看日志
構建docker鏡像超時或出錯，詳情請查看日誌
If the Docker image is built with a timeout or error, see the log for details
060:
不被信任的文件：%s
不被信任的文件：%s
Untrusted file: %s
061:
连接注册中心失败，原因：%s
連接注冊中心失敗，原因：%s
Failed to connect to the registry for reason: %s