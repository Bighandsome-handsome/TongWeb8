# 原创k8s一键部署tongweb7容器版脚本（by why+lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/149016827

---

声明
此贴仅供参考，请根据自身需求在测试环境测试和修改。
安装准备
1.获取对应的安装包和授权,并将授权和安装包放在同一个目录下：
2.docekr已配置远程仓库
3.提前拉取jdk的镜像（这里配置了使用openjdk:8）
安装
将以下内容复制到k8s_deploy_TongWeb.sh里：
#!/bin/bash
# TongWeb Kubernetes 全自动部署脚本（支持镜像仓库）
# 使用说明：
# 文件准备统一在同级目录下：
# /部署目录/
# ├── k8s_deploy_TongWeb.sh  部署脚本
# ├── license.dat      产品授权
# └── tongweb-cloud-7.0.C.6_P5.tar.gz  安装包
# 执行权限：chmod +x k8s_deploy_TongWeb.sh
# 运行部署：sudo ./k8s_deploy_TongWeb.sh
# 配置信息
APP_NAME
=
"tongweb"
APP_VERSION
=
"7.0.C.6_P5"
TAR_PACKAGE
=
"tongweb-cloud-
${APP_VERSION}
.tar.gz"
INSTALL_DIR
=
"/opt/tongweb-cloud-7.0.C.6"
NAMESPACE
=
"tongweb-namespace"
IMAGE_NAME
=
"tongweb:v70c6"
K8S_DIR
=
"/tmp/tongweb-k8s-manifests"
# 镜像仓库配置（根据实际情况修改）
REGISTRY_URL
=
"192.168.10.108:5000"
# 镜像仓库地址
REGISTRY_PROJECT
=
"tongweb7-cloud"
# 仓库中的项目/命名空间名称（若无可留空）
REGISTRY_USER
=
"admin"
# 仓库用户名
REGISTRY_PASSWORD
=
"Harbor12345"
# 仓库密码
APP_VERSION
=
"7.0.C.6_P5"
# 需在脚本中定义版本变量
# 完整镜像地址格式：
REMOTE_IMAGE_NAME
=
"
${REGISTRY_URL}
/
${REGISTRY_PROJECT}
/tongweb:
${APP_VERSION}
-
$(
date
+%Y%m%d%H%M
)
"
# 初始化环境
init_env
(
)
{
# 创建临时目录
mkdir
-p
"
$K8S_DIR
"
# 检查必需命令
for
cmd
in
docker kubectl
tar
;
do
if
!
command
-v
$cmd
&>
/dev/null
;
then
echo
"错误：必需命令
$cmd
未找到！"
exit
1
fi
done
}
# 解压安装包
extract_package
(
)
{
if
[
!
-f
"
$TAR_PACKAGE
"
]
;
then
echo
"错误：安装包
$TAR_PACKAGE
不存在！"
exit
1
fi
echo
"正在解压安装包..."
tar
-zxvf
"
$TAR_PACKAGE
"
-C /opt
cp
license.dat
"
$INSTALL_DIR
"
}
# 配置Kubernetes
setup_kubernetes
(
)
{
# 创建命名空间
if
!
kubectl get namespace
"
$NAMESPACE
"
&>
/dev/null
;
then
kubectl create namespace
"
$NAMESPACE
"
fi
# 创建ConfigMap
kubectl create configmap license
\
--from-file
=
license.dat
\
-n
"
$NAMESPACE
"
}
# 构建并推送镜像
build_and_push_image
(
)
{
# 基础镜像配置（可根据需要修改）
local
BASE_IMAGE
=
"openjdk:8"
# 生成Dockerfile
echo
"正在生成Dockerfile..."
cat
>
"
$INSTALL_DIR
/Dockerfile"
<<
EOF
FROM
${BASE_IMAGE}
ENV TZ=Asia/Shanghai
\\
LANG=C.UTF-8
ADD tongweb /opt/TongWeb
EXPOSE 8088 8443
ENTRYPOINT ["/opt/TongWeb/kernel/bin/startserver.sh"]
EOF
# 构建本地镜像
echo
"正在构建本地镜像..."
if
!
docker build -t
"
$IMAGE_NAME
"
-f
"
$INSTALL_DIR
/Dockerfile"
"
$INSTALL_DIR
"
;
then
echo
"镜像构建失败！"
exit
1
fi
# 标记并推送镜像
echo
"正在标记镜像..."
docker tag
"
$IMAGE_NAME
"
"
$REMOTE_IMAGE_NAME
"
echo
"登录镜像仓库..."
if
!
docker login -u
"
$REGISTRY_USER
"
-p
"
$REGISTRY_PASSWORD
"
"
$REGISTRY_URL
"
;
then
echo
"镜像仓库登录失败！"
exit
1
fi
echo
"正在推送镜像到仓库..."
if
!
docker push
"
$REMOTE_IMAGE_NAME
"
;
then
echo
"镜像推送失败！"
exit
1
fi
echo
"镜像推送成功：
$REMOTE_IMAGE_NAME
"
}
# 生成部署文件
generate_manifests
(
)
{
# 生成Deployment
cat
>
"
$K8S_DIR
/deployment.yaml"
<<
EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name:
$APP_NAME
spec:
  selector:
    matchLabels:
      app:
$APP_NAME
replicas: 1
  template:
    metadata:
      labels:
        app:
$APP_NAME
spec:
      containers:
      - name:
$APP_NAME
image:
$REMOTE_IMAGE_NAME
# 使用仓库镜像地址
        imagePullPolicy: Always    # 总是从仓库拉取
        env:
        - name: CONFIG_REMOTE_ENABLE
          value: "false"
        - name: ENV_TYPE
          value: "cloud"
        ports:
        - name: port-http
          containerPort: 8088
        - name: port-https
          containerPort: 8443
        volumeMounts:
        - name: log-volume
          mountPath: /opt/TongWeb/kernel/logs
        - name: autodeploy-volume
          mountPath: /opt/TongWeb/kernel/autodeploy
        - name: license
          mountPath: /opt/TongWeb/kernel/license.dat
          subPath: license.dat
      volumes:
      - name: log-volume
        hostPath:
          path: /home/work/logs
          type: DirectoryOrCreate
      - name: autodeploy-volume
        hostPath:
          path: /home/work/autodeploy
          type: DirectoryOrCreate
      - name: license
        configMap:
          name: license
EOF
# 生成Service（保持不变）
cat
>
"
$K8S_DIR
/service.yaml"
<<
EOF
apiVersion: v1
kind: Service
metadata:
  name:
${APP_NAME}
srv
spec:
  selector:
    app:
$APP_NAME
type: NodePort
  ports:
  - name: port-http
    nodePort: 30080
    port: 9060
    targetPort: 8088
  - name: port-https
    nodePort: 30081
    port: 9443
    targetPort: 8443
EOF
}
# 部署应用到集群
deploy_to_cluster
(
)
{
echo
"正在部署应用..."
kubectl apply -f
"
$K8S_DIR
/deployment.yaml"
-n
"
$NAMESPACE
"
kubectl apply -f
"
$K8S_DIR
/service.yaml"
-n
"
$NAMESPACE
"
# 等待Pod就绪
local
retry
=
0
while
[
$retry
-lt
15
]
;
do
local
pod_status
=
$(
kubectl get pod -n
"
$NAMESPACE
"
-l
app
=
$APP_NAME -o
jsonpath
=
'{.items[0].status.phase}'
)
local
image_pulled
=
$(
kubectl get pod -n
"
$NAMESPACE
"
-l
app
=
$APP_NAME -o
jsonpath
=
'{.items[0].status.containerStatuses[0].state}'
)
if
[
"
$pod_status
"
==
"Running"
]
;
then
echo
-e
"
\n
Pod 已正常运行！"
kubectl get pod -n
"
$NAMESPACE
"
return
0
elif
[
[
"
$image_pulled
"
==
*
"ErrImagePull"
*
]
]
;
then
echo
-e
"
\n
错误：镜像拉取失败！请检查："
echo
"1. 镜像地址是否正确：
$REMOTE_IMAGE_NAME
"
echo
"2. 仓库认证信息是否正确"
exit
1
fi
echo
-n
"."
((
retry
++
))
sleep
5
done
echo
-e
"
\n
错误：Pod 启动超时！"
kubectl describe pod -n
"
$NAMESPACE
"
-l
app
=
$APP_NAME
exit
1
}
# 主流程
main
(
)
{
init_env
    extract_package
    setup_kubernetes
    build_and_push_image
    generate_manifests
    deploy_to_cluster
echo
""
echo
"═"
*50
echo
"部署完成！"
echo
"镜像地址：
$REMOTE_IMAGE_NAME
"
echo
"如部署应用访问地址：http://<节点IP>:30080"
echo
"管理命令："
echo
"  kubectl get pod -n
$NAMESPACE
"
echo
"  kubectl logs -f <pod名称> -n
$NAMESPACE
"
echo
"═"
*50
}
# 执行主流程
main
执行以下指令：
执行权限：chmod +x k8s_deploy_TongWeb.sh
运行部署：sudo ./k8s_deploy_TongWeb.sh
执行后，使用以下指令查看日志
# 通过该指令查看pod名称
kubectl get pod -n tongweb-namespace
 kubectl logs -f
<
pod名称
>
-n tongweb-namespace
如果安装有问题，需要删掉pod重新操作，可执行以下指令（）
#先查pod名称
kubectl get pod -n tongweb-namespace
#删除pod
kubectl delete pod pod名 -n tongweb-namespace
#删除跟license相关的configmap
kubectl delete configmap license -n tongweb-namespace
#删除命名空间（前提是该命名空间只有tongweb相关的资源和配置）
kubectl delete namespace tongweb-namespace
本地完整日志如下，可供参考
[
root@k8s-master tongweb7-cloud
]
# sudo ./k8s_deploy_TongWeb.sh
正在解压安装包
..
.
tongweb-cloud-7.0.C.6/
tongweb-cloud-7.0.C.6/tongweb/
tongweb-cloud-7.0.C.6/tongweb/kernel/
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/luncher.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/jdk-tool.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/tw.env
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/env.options
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/external.vmoptions
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/startdebug.bat
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/startdebug.sh
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/startserver.bat
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/startserver.sh
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/startservernohup.sh
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/stopserver.bat
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/stopserver.sh
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/version.bat
tongweb-cloud-7.0.C.6/tongweb/kernel/bin/version.sh
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/security/
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/security/twgroups.properties
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/security/twusers.properties
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/ssl/
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/ssl/gm.pfx
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/ssl/mykey.cer
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/ssl/mykey.p12
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/ssl/sm2.enc.pfx
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/ssl/sm2.sig.pfx
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/ssl/tongweb.cer
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/ssl/tongweb.keystore
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/ssl/ss.keystore
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/prometheus.properties
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/default-web.xml
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/application.properties
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/logging.properties
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/monitor.properties
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/server.properties
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/tongweb.policy
tongweb-cloud-7.0.C.6/tongweb/kernel/conf/tongweb.xml
tongweb-cloud-7.0.C.6/tongweb/kernel/autodeploy/
tongweb-cloud-7.0.C.6/tongweb/kernel/tmp/
tongweb-cloud-7.0.C.6/tongweb/kernel/logs/
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-jsp.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-commons.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-license.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-websocket.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-core.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-boot.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-log.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-session.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-config.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-cmd.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/lib/tongweb-servlet-simple.jar
tongweb-cloud-7.0.C.6/tongweb/kernel/README.md
tongweb-cloud-7.0.C.6/tongweb/extends/
tongweb-cloud-7.0.C.6/tongweb/extends/templates/
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/configs/
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/configs/tongweb.xml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/templates/
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/templates/NOTES.txt
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/templates/_helpers.tpl
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/templates/configmap.yaml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/templates/deployment.yaml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/templates/pvc.yaml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/templates/serviceaccount.yaml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/templates/ingress.yaml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/templates/service.yaml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/Chart.yaml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm/values.yaml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/operator/
tongweb-cloud-7.0.C.6/tongweb/extends/templates/operator/tongweb_operator_all.yaml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/operator/tongweb_samples.yaml
tongweb-cloud-7.0.C.6/tongweb/extends/templates/docker-set-env.env
tongweb-cloud-7.0.C.6/tongweb/extends/templates/docker-swarm-template-sample.tpl
tongweb-cloud-7.0.C.6/tongweb/extends/templates/k8s-template-job.sh
tongweb-cloud-7.0.C.6/tongweb/extends/templates/k8s-template.sh
tongweb-cloud-7.0.C.6/tongweb/extends/templates/docker-swarm-template.sh
tongweb-cloud-7.0.C.6/tongweb/extends/templates/k8s-template-job-nfs.tpl
tongweb-cloud-7.0.C.6/tongweb/extends/templates/k8s-set-env.options
tongweb-cloud-7.0.C.6/tongweb/extends/templates/k8s-template-deployment-hostpath.tpl
tongweb-cloud-7.0.C.6/tongweb/extends/templates/k8s-template-service.tpl
tongweb-cloud-7.0.C.6/tongweb/extends/templates/docker-image-run.sh
tongweb-cloud-7.0.C.6/tongweb/extends/templates/docker-repo-run.sh
tongweb-cloud-7.0.C.6/tongweb/extends/templates/docker-swarm-template-config.options
tongweb-cloud-7.0.C.6/tongweb/extends/templates/docker-repo-transfer.sh
tongweb-cloud-7.0.C.6/tongweb/extends/templates/k8s-set-job.options
tongweb-cloud-7.0.C.6/tongweb/extends/templates/k8s-template-deployment-nfs.tpl
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/heapinfo.sh
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/showbusyjavathreads.sh
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/licenseinfo.sh
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/connectorinfo.sh
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/licenseinfo.bat
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/deadlockcheck.sh
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/loganalysis.sh
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/cloud-granfan-k8s-template.json
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/cloud-granfan-template.json
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/testjdbcconnection.sh
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/topobjectmemorycheck.sh
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/jdbcconnectioninfo.sh
tongweb-cloud-7.0.C.6/tongweb/extends/scripts/image-upgrade.sh
tongweb-cloud-7.0.C.6/tongweb/extends/tools/
tongweb-cloud-7.0.C.6/tongweb/extends/tools/image/
tongweb-cloud-7.0.C.6/tongweb/extends/tools/image/convertor/
tongweb-cloud-7.0.C.6/tongweb/extends/tools/image/convertor/convertor.bat
tongweb-cloud-7.0.C.6/tongweb/extends/tools/image/convertor/convertor.sh
tongweb-cloud-7.0.C.6/tongweb/extends/tools/image/convertor/tongweb-convertor.jar
tongweb-cloud-7.0.C.6/tongweb/extends/tools/image/Dockerfile-example
tongweb-cloud-7.0.C.6/tongweb/extends/tools/encipher/
tongweb-cloud-7.0.C.6/tongweb/extends/tools/encipher/cipher-tool.jar
tongweb-cloud-7.0.C.6/tongweb/extends/tools/encipher/cipher-tool.sh
tongweb-cloud-7.0.C.6/tongweb/extends/tools/encipher/cipher-tool.bat
tongweb-cloud-7.0.C.6/tongweb/extends/libs/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/libssl.so.1.1
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/libssl.so
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/libtwnative-1.la
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/libapr-1.so.0
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/libtwnative-1.so.0
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/libcrypto.so
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/libcrypto.so.1.1
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/libtwnative-1.so.0.2.24
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/libtwnative-1.so
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/aarch64/libtwnative-1.a
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/mips64/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/mips64/libapr-1.so.0
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/mips64/libtwnative-1.so.0
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/mips64/libtwnative-1.la
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/mips64/libtwnative-1.so
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/mips64/libssl.so.10
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/mips64/libtwnative-1.so.0.2.24
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/mips64/libtwnative-1.a
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/mips64/libcrypto.so.10
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/x64/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/x64/libtwnative-1.a
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/x64/libssl.so.10
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/x64/libtwnative-1.so.0.2.24
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/x64/libapr-1.so.0
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/x64/libtwnative-1.la
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/x64/libtwnative-1.so
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/x64/libtwnative-1.so.0
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/linux/x64/libcrypto.so.10
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/windows/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/windows/x64/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/windows/x64/twnative-1.dll
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/windows/x86/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/apr/windows/x86/twnative-1.dll
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/aarch64/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/aarch64/libzlog.so.1.2
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/aarch64/libzlog.so.1
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/aarch64/libzlog.a
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/aarch64/libzlog.so
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/mips64/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/mips64/libzlog.a
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/mips64/libzlog.so
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/mips64/libzlog.so.1
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/mips64/libzlog.so.1.2
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/x86_64/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/x86_64/libzlog.a
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/x86_64/libzlog.so.1
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/x86_64/libzlog.so
tongweb-cloud-7.0.C.6/tongweb/extends/libs/fastlog/x86_64/libzlog.so.1.2
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/json-databind-2.11.0_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/tongweb-dynamic.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/pool2-2.6.2_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/json-core-2.11.0_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/client.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/monitor-core-1.0.0_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/simpleclient-common.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/simpleclient.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/HdrHistogram-2.1.11_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/ws-mini-0.0.1.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/Latencyutils-2.0.3_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/json-annotations-2.11.0_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/logger-adapter-1.0.0_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/tw-cm-Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/HulkCP-java7-7.3.9.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/common-socket-7.0.0.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/tongweb-jdk9plus-api.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/monitor-enhance-1.0.0_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/license-client-4.5.1.7.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/host/tongweb-jdbc.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/app/
tongweb-cloud-7.0.C.6/tongweb/extends/libs/goova-22.0_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/tongweb-c.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/tongweb-gmssl-1.0.0.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/lang3-3.10_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/nacos-api-1.2.0_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/tongweb-servlet-all.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/nacos-common-1.2.0_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/nacos-client-1.2.0_Tianfu.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/kafka-clients.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/atomikos-integration-extension.jar
tongweb-cloud-7.0.C.6/tongweb/extends/libs/dynamic-agent.jar
tongweb-cloud-7.0.C.6/tongweb/extends/plugins/
tongweb-cloud-7.0.C.6/tongweb/extends/plugins/pinpoint-plugins/
tongweb-cloud-7.0.C.6/tongweb/extends/plugins/pinpoint-plugins/tongweb-pinpoint-plugin-1.5.2.jar
tongweb-cloud-7.0.C.6/tongweb/extends/plugins/skywalking-plugins/
tongweb-cloud-7.0.C.6/tongweb/extends/plugins/skywalking-plugins/tongweb-skywalking.jar
namespace/tongweb-namespace created
configmap/license created
正在生成Dockerfile
..
.
正在构建本地镜像
..
.
Sending build context to Docker daemon
97
.22MB
Step
1
/5
:
FROM openjdk:8
 ---
>
b273004037cc
Step
2
/5
:
ENV
TZ
=
Asia/Shanghai
LANG
=
C.UTF-8
 ---
>
Running
in
983a90545142
Removing intermediate container 983a90545142
 ---
>
e51ff15d78bb
Step
3
/5
:
ADD tongweb /opt/TongWeb
 ---
>
59bfa478c0a3
Step
4
/5
:
EXPOSE
8088
8443
---
>
Running
in
8ebd49b60b53
Removing intermediate container 8ebd49b60b53
 ---
>
3be34a57ffe5
Step
5
/5
:
ENTRYPOINT
[
"/opt/TongWeb/kernel/bin/startserver.sh"
]
---
>
Running
in
1c62c83a212d
Removing intermediate container 1c62c83a212d
 ---
>
ffb67754d9f5
Successfully built ffb67754d9f5
Successfully tagged tongweb:v70c6
正在标记镜像
..
.
登录镜像仓库
..
.
WARNING
!
Using --password via the CLI is insecure. Use --password-stdin.
WARNING
!
Your password will be stored unencrypted
in
/root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/
#credentials-store
Login Succeeded
正在推送镜像到仓库
..
.
The push refers to repository
[
192.168
.10.108:5000/tongweb7-cloud/tongweb
]
a45ec45194fc: Pushed 
6b5aaff44254: Layer already exists 
53a0b163e995: Layer already exists 
b626401ef603: Layer already exists 
9b55156abf26: Layer already exists 
293d5db30c9f: Layer already exists 
03127cdb479b: Layer already exists 
9c742cd6c7a5: Layer already exists
7.0
.C.6_P5-202506232031: digest: sha256:153f17b4146a6e822c1e4482ca296cf721e86cc77e4ba7450ccc4abc80dc75e2 size:
2007
镜像推送成功：192.168.10.108:5000/tongweb7-cloud/tongweb:7.0.C.6_P5-202506232031
正在部署应用
..
.
deployment.apps/tongweb created
service/tongwebsrv created
..
..
Pod 已正常运行！
NAME                       READY   STATUS    RESTARTS   AGE
tongweb-5f8c8bb459-p4zvv
1
/1     Running
0
27s

═*50
部署完成！
镜像地址：192.168.10.108:5000/tongweb7-cloud/tongweb:7.0.C.6_P5-202506232031
如部署应用访问地址：http://
<
节点IP
>
:30080
管理命令：
  kubectl get pod -n tongweb-namespace
  kubectl logs -f
<
pod名称
>
-n tongweb-namespace
═*50
[
root@k8s-master tongweb7-cloud
]
# kubectl get pod -n tongweb-namespace
NAME                       READY   STATUS    RESTARTS   AGE
tongweb-5f8c8bb459-p4zvv
1
/1     Running
0
46s
[
root@k8s-master tongweb7-cloud
]
# kubectl logs -f tongweb-5f8c8bb459-p4zvv -n tongweb-namespace
[
2025
-06-25
11
:47:01.638
]
[
INFO
]
[
config
]
[
Logging started
]
[
2025
-06-25
11
:47:01.709
]
[
INFO
]
[
console
]
[
----------------License Info------------------
]
[
2025
-06-25
11
:47:01.710
]
[
INFO
]
[
console
]
[
Consumer_Name:            金融
]
[
2025
-06-25
11
:47:01.710
]
[
INFO
]
[
console
]
[
Project_Name:             国产化
]
[
2025
-06-25
11
:47:01.711
]
[
INFO
]
[
console
]
[
License_Type:             trial
]
[
2025
-06-25
11
:47:01.711
]
[
INFO
]
[
console
]
[
Max_Number:               -1
]
[
2025
-06-25
11
:47:01.711
]
[
INFO
]
[
console
]
[
Expiry_Date:
2025
-09-09
]
[
2025
-06-25
11
:47:01.711
]
[
INFO
]
[
console
]
[
Product_Name:             TongWeb
]
[
2025
-06-25
11
:47:01.711
]
[
INFO
]
[
console
]
[
Product_Edition:          Cloud
]
[
2025
-06-25
11
:47:01.712
]
[
INFO
]
[
console
]
[
Product_version:
7.0
.C
]
[
2025
-06-25
11
:47:01.712
]
[
INFO
]
[
console
]
[
----------------License Info------------------
]
[
2025
-06-25
11
:47:02.027
]
[
INFO
]
[
config
]
[
TongWeb init success
]
[
2025
-06-25
11
:47:02.608
]
[
INFO
]
[
web-container
]
[
Initializing ProtocolHandler
[
"http-nio-8088"
]
]
[
2025
-06-25
11
:47:02.688
]
[
INFO
]
[
web-container
]
[
Starting
service
[
TongWeb
]
]
[
2025
-06-25
11
:47:02.689
]
[
INFO
]
[
web-container
]
[
Starting Servlet engine:
[
TongWeb/7.0.C.6_P5
]
]
[
2025
-06-25
11
:47:02.834
]
[
INFO
]
[
web-container
]
[
Starting ProtocolHandler
[
"http-nio-8088"
]
]
[
2025
-06-25
11
:47:02.865
]
[
INFO
]
[
boot
]
[
TongWeb Server Started
]