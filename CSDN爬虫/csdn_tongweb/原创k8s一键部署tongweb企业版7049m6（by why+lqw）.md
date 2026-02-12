# 原创k8s一键部署tongweb企业版7049m6（by why+lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/149052348

---

声明
1.此贴仅供参考，请根据自身需求在测试环境测试和修改。
安装准备
1.获取对应的安装包和授权,并将授权和安装包放在同一个目录下
2.docekr已配置远程仓库
3.提前拉取jdk的镜像（这里配置了使用openjdk:8）
安装
将以下内容复制到k8s_deploy_TongWeb7049m6.sh里：
#!/bin/bash
# TongWeb Kubernetes 全自动部署脚本（支持镜像仓库）
# 使用说明：
# 文件准备统一在同级目录下：
# /部署目录/
# ├── k8s_deploy_TongWeb.sh  部署脚本
# ├── license.dat      产品授权
# └──TongWeb7.0.4.9_M6_Enterprise_Linux.tar.gz  安装包
# 执行权限：chmod +x k8s_deploy_TongWeb7049m6.sh
# 运行部署：sudo ./k8s_deploy_TongWeb7049m6.sh
# 配置信息
APP_NAME
=
"tongweb"
APP_VERSION
=
"7.0.4.9_M6_Enterprise_Linux"
TAR_PACKAGE
=
"TongWeb7.0.4.9_M6_Enterprise_Linux.tar.gz"
INSTALL_DIR
=
"/opt/tongweb-7049m6"
NAMESPACE
=
"tongweb7049m6cloud-namespace"
IMAGE_NAME
=
"tongweb:7049m6"
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
"tongweb7-cloud-7049m6"
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
"7.0.4.9_M6_Enterprise_Linux"
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
mv
"/opt/TongWeb
${APP_VERSION}
"
"
$INSTALL_DIR
"
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
kubectl create configmap license7049m6
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
# 时区配置
ENV TZ=Asia/Shanghai
\\
LANG=C.UTF-8


# 拷贝TongWeb
#ADD tongweb /opt/TongWeb
ADD . /opt/TongWeb


# 暴露端口（按需求改）
EXPOSE 8080 8443 9060


# 启动命令
#ENTRYPOINT ["/opt/TongWeb/bin/startservernohup.sh"]
# 启动命令
ENTRYPOINT ["/opt/TongWeb/bin/startserver.sh"]


RUN echo "[
$(
date
'+%Y-%m-%d %H:%M:%S'
)
] TongWeb
${APP_VERSION}
镜像构建成功"
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
        - name: http
          containerPort: 8080
        - name: https
          containerPort: 8443
        - name: admin
          containerPort: 9060
        volumeMounts:
        - name: log-volume
          mountPath: /opt/TongWeb/logs
        - name: autodeploy-volume
          mountPath: /opt/TongWeb/autodeploy
        - name: license
          mountPath: /opt/TongWeb/license.dat
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
          name: license7049m6
EOF
# 生成Service
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
  - name: http
    port: 8088
    targetPort: 8088
    nodePort: 30808  # 修改为有效范围内的端口
  - name: https
    port: 8443
    targetPort: 8443
    nodePort: 32443  # 修改为有效范围内的端口
  - name: admin
    port: 9060
    targetPort: 9060
    nodePort: 30906  # 修改为有效范围内的端口
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
echo
-n
"等待Pod启动"
local
retry
=
0
local
max_retries
=
30
# 把重试次数增加为30
local
sleep_time
=
15
# 增加检查间隔为10秒
while
[
$retry
-lt
$max_retries
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
$sleep_time
done
echo
"错误：Pod 启动超时！"
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
"TongWeb 7.0.4.9_M6 部署完成！"
echo
"管理控制台： http://<节点IP>:30906/console"
echo
"管理控制台初始账号：thanos"
echo
"管理控制台初始密码：thanos123.com"
echo
"如部署应用，访问： http://<节点IP>:30808"
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
# 执行权限：
chmod
+x k8s_deploy_TongWeb7049m6.sh
# 运行部署：
sudo
./k8s_deploy_TongWeb7049m6.sh
执行后，使用以下指令查看日志：
kubectl get pod -n tongweb7049m6cloud-namespace
 kubectl logs -f
<
pod名称
>
-n tongweb7049m6cloud-namespace
如果安装有问题，需要删掉pod重新操作，可执行以下指令：
#先查pod名称
kubectl get pod -n tongweb7049m6cloud-namespace
#删除pod
kubectl delete pod pod名 -n tongweb7049m6cloud-namespace
#删除跟license相关的configmap
kubectl delete configmap license -n tongweb7049m6cloud-namespace
#删除命名空间（前提是该命名空间只有tongweb相关的资源和配置）
kubectl delete namespace tongweb7049m6cloud-namespace