# 原创k8s+helm部署tongweb7云容器版（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/147266614

---

安装准备
1.联系销售获取安装包和授权（例如：tongweb-cloud-7.0.C.6_P3.tar.gz）。
2.已安装docker和k8s集群，参考：
k8s集群搭建
3.有对应的docker私库，没有的可以参考：
harbor搭建
4.docker已经拉取对应的一些基础镜像，例如jdk（版本不低于1.8）。
5.安装helm，可参考
Helm安装
测试和打包镜像
拿到安装包后，先解压并放入授权测试，测试可以正常运行并输出日志（需安装并配置jdk环境变量）。
然后看看logs目录下是否有日志滚动，如下为正常显示：
cd
/opt/tongweb-cloud-7.0.C.6/tongweb/kernel/bin
./startservernohup.sh
停止tongweb（可以直接ps -ef |grep tongweb然后kill掉进程id，或者执行stopserver.sh这个脚本）。
把dockerfile-example复制过来，改名为Dockerfile：
cd到Dockerfile所在的目录，执行下面指令（tongweb:v70c6可根据需要修改）：
docker build -t tongweb:v70c6 -f Dockerfile
.
之后看看docker images里是否有对应镜像，测试是否能跑通
#tongweb:v70c6是指镜像名和版本
docker run -itd --name my_tongweb -p
8099
:8080 -v /opt/tongweb-cloud-
7.0
.C.6/tongweb:/opt/Tongweb tongweb:v70c6
查看日志没问题的话，打包和push到私库（192.168.10.126:80是本地安装好的harbor的私库地址）
docker tag tongweb:v70c6
192.168
.10.126:80/tongweb7/tongweb:v70c6
docker push
192.168
.10.126:80/tongweb7/tongweb:v70c6
查看私库是否已经有对应的镜像，例如可视化页面，或者指令：
[
root@master .docker
]
# curl -u 'admin:harbor12345' -X GET
'http://192.168.10.126/api/v2.0/projects/tongweb7/repositories/tongweb/artifacts
'
[
{
"accessories"
:null,
"addition_links"
:
{
"build_history"
:
{
"absolute"
:false,
"href"
:
"/api/v2.0/projects/tongweb7/repositories/tongweb/artif
acts/sha256:6cfc4c6c6c14d1111d496b830285d13c4ca24f6fab1c10dd95bce9f17260ec67/add
itions/build_history"
}
}
,
"digest"
:
"sha256:6cfc4c6c6c14d1111d496b830285d13c4ca24f6
fab1c10dd95bce9f17260ec67"
,
"extra_attrs"
:
{
"architecture"
:
"amd64"
,
"author"
:
""
,
"config"
:
{
"ArgsEscaped"
:true,
"Entrypoint"
:
[
"/opt/TongWeb/kernel/bin/startserver.sh"
]
,
"Env"
:
[
"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/jvm
/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin"
,
"LANG=C.UTF-
8"
,
"JAVA_HOME=/usr/lib/jvm/java-1.8-
openjdk"
,
"JAVA_VERSION=8u212"
,
"JAVA_ALPINE_VERSION=8.212.04-
r0"
,
"TZ=Asia/Shanghai"
]
,
"ExposedPorts"
:
{
"8088/tcp"
:
{
}
}
}
,
"created"
:
"2025-04-
10T11:12:32.784615336+08:00"
,
"os"
:
"linux"
}
,
"icon"
:
"sha256:0048162a053eef4d4ce3fe
7518615bef084403614f8bca43b40ae2e762e11e06"
,
"id"
:2,
"labels"
:null,
"manifest_media
_type"
:
"application/vnd.docker.distribution.manifest.v2+json"
,
"media_type"
:
"appl
ication/vnd.docker.container.image.v1+json"
,
"project_id"
:4,
"pull_time"
:
"2025-04-
10T03:25:46.345Z"
,
"push_time"
:
"2025-04-
10T03:20:42.567Z"
,
"references"
:null,
"repository_id"
:2,
"size"
:139075466,
"tags"
:
[
{
"artifact_id"
:2,
"id"
:2,
"immutable"
:false,
"name"
:
"v70c6"
,
"pull_time"
:
"0001-01-
01T00:00:00.000Z"
,
"push_time"
:
"2025-04-
10T03:20:42.607Z"
,
"repository_id"
:2
}
]
,
"type"
:
"IMAGE"
}
]
[
root@master .docker
]
#
导出tongweb镜像以防万一，然后删掉docker里的tongwbe镜像，试试看能不能重新拉取下来：
docker save -o tongwebcloud_7.0.c.6.tar tongweb:v70c6
docker rmi -f
192.168
.10.126:80/tongweb7/tongweb:v70c6
docker pull tongweb:v70c6
helm安装
下载地址
#解压安装包
tar
-zxvf helm-v3.15.2-linux-amd64.tar
mv
linux-amd64/helm /usr/local/bin/helm
helm version
到解压好的tongweb7的目录下，在对应路径找到chart.yaml（最好是自己单独复制一个helm目录出来去执行，这里只是为了演示方便）
修改helm目录下的values.yaml
将最新的tongweb.xml放入到helm的configs目录下
cd到helm目录的上一级目录，执行以下指令（其中default是k8s的命令空间，tongweb是指release_name，如果需要用其他的命令空间，可以使用指令：kubectl create namespace 自行创建）。
helm
install
--namespace default tongweb helm/
提示信息解读：
helm/:
如截图所示，这个路径指向 /opt/tongweb-cloud-7.0.C.6/tongweb/extends/templates/helm，
而该路径包含了一个 Helm chart 目录。
目录包含重要文件如 Chart.yaml 和 values.yaml，以及 templates/ 目录。
Chart.yaml 存储了 chart 的元信息，如名称、版本等。
values.yaml 用于定义 chart 的默认配置值。
templates/ 目录里面通常存储了 Kubernetes 资源的 YAML 模板。
命令结果:
Helm 成功将名为 tongweb 的 release 安装到了 default 命名空间中。
STATUS: deployed 表示资源已成功部署。
NOTES: 部分提供了一些使用提示，比如如何获取应用的 URL。这通常是 chart 定义者提供的信息，用于
帮助用户更好地使用部署后的应用。
使用kubectl get pods查看状态
如果状态如上图所示，可以使用指令
#tongweb-7849bf9554-gzf46为Name显示的信息
kubectl describe pod tongweb-7849bf9554-gzf46
这种情况下，修改仓库配置完毕后，卸载重装，卸载指令如下：
#其中tongweb为安装指令里的release-name
[
root@master templates
]
# helm uninstall tongweb
release
"tongweb"
uninstalled
[
root@master templates
]
# kubectl get pods
No resources found
in
default namespace.
[
root@master templates
]
# helm list
NAME NAMESPACE REVISION UPDATED STATUS CHART APP VERSION
[
root@master templates
]
#
重新安装和检查
[
root@master templates
]
# kubectl get pods |grep tongweb
tongweb-bbff654f-v4h2r
1
/1 Running
0
2m29s
[
root@master templates
]
# kubectl describe pod tongweb-bbff654f-v4h2r
Name: tongweb-bbff654f-v4h2r
Namespace: default
Priority:
0
Node: node2/192.168.10.128
Start Time: Thu,
10
Apr
2025
15
:20:50 +0800
Labels: app.kubernetes.io/instance
=
tongweb
app.kubernetes.io/name
=
tongweb
pod-template-hash
=
bbff654f
Annotations: sidecar.istio.io/inject:
false
Status: Running
IP:
10.244
.2.10
IPs:
IP:
10.244
.2.10
Controlled By: ReplicaSet/tongweb-bbff654f
Containers:
tongweb:
Container ID:
docker://9a93d33bc315273dce919dede39c33ee5129509d2b2591d5b85e3d2cc80a95f6
Image:
192.168
.10.126:80/tongweb7/tongweb:v70c6
Image ID: dockerpullable://192.168.10.126:80/tongweb7/tongweb@sha256:6cfc4c6c6c14d1111d496b83028
5d13c4ca24f6fab1c10dd95bce9f17260ec67
Ports:
8088
/TCP,
8443
/TCP
Host Ports:
0
/TCP,
0
/TCP
State: Running
Started: Thu,
10
Apr
2025
15
:20:52 +0800
Ready: True
Restart Count:
0
Environment:
ENV_TYPE: cloud
POD_NAME: tongweb-bbff654f-v4h2r
(
v1:metadata.name
)
MEM_REQUEST:
0
(
requests.memory
)
MEM_LIMIT: node allocatable
(
limits.memory
)
Mounts:
/opt/TongWeb/kernel/autodeploy from autodeploy-volume
(
rw
)
/opt/TongWeb/kernel/conf/tongweb.xml from tongweb-volume
(
rw,path
=
"tongweb.xml"
)
/opt/TongWeb/kernel/logs from log-volume
(
rw
)
/var/run/secrets/kubernetes.io/serviceaccount from default-token-jj8c9
(
ro
)
Conditions:
Type Status
Initialized True
Ready True
ContainersReady True
PodScheduled True
Volumes:
log-volume:
Type: HostPath
(
bare
host
directory volume
)
Path: /home/work/logs
HostPathType: DirectoryOrCreate
autodeploy-volume:
Type: EmptyDir
(
a temporary directory that shares a pod's lifetime
)
Medium:
SizeLimit:
<
unset
>
tongweb-volume:
Type: ConfigMap
(
a volume populated by a ConfigMap
)
Name: tongweb
Optional:
false
登录dashboard，可以看到有相关信息：
values.yaml文件配置说明
default-token-jj8c9:
Type: Secret
(
a volume populated by a Secret
)
SecretName: default-token-jj8c9
Optional:
false
QoS Class: BestEffort
Node-Selectors:
<
none
>
Tolerations: node.kubernetes.io/not-ready:NoExecute
op
=
Exists
for
300s
node.kubernetes.io/unreachable:NoExecute
op
=
Exists
for
300s
Events:
Type Reason Age From Message
---- ------ ---- ---- -------
Normal Scheduled 2m40s default-scheduler Successfully assigned
default/tongweb-bbff654f-v4h2r to node2
Normal Pulling 2m39s kubelet Pulling image
"192.168.10.126:80/tongweb7/tongweb:v70c6"
Normal Pulled 2m39s kubelet Successfully pulled image
"192.168.10.126:80/tongweb7/tongweb:v70c6"
in
83
.379623ms
Normal Created 2m39s kubelet Created container tongweb
Normal Started 2m38s kubelet Started container tongweb
登录dashboard，可以看到有相关信息：
values.yaml文件配置说明
Plain Text
Default values
for
tongweb.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.
replicaCount:
1
#镜像地址和拉取策略
image:
repository: tongweb
tag: latest
pullPolicy: Always
#secret配置
imagePullSecrets:
[
]
nameOverride:
"tongweb"
fullnameOverride:
""
#配置tongweb运行所需的环境变量
env:
#环境类型为云上
- name: ENV_TYPE
value:
"cloud"
- name: POD_NAME
valueFrom:
fieldRef:
fieldPath: metadata.name
- name: MEM_REQUEST
valueFrom:
resourceFieldRef:
resource: requests.memory
- name: MEM_LIMIT
valueFrom:
resourceFieldRef:
resource: limits.memory
#tongweb端口暴露配置
ports:
#tongweb http端口配置
- port-http:
8088
# tongweb https端口配置
- port-https:
8443
#tongweb挂载文件配置当前值支持hostpath,nfs,emptyDir,configmap挂载方式配置
#参数说明:
#name:表示挂载名称
#mountPath表示k8s容器中需要挂载的目录或者文件
#subPath 表示k8s容器中需要挂载的子目录或者文件
#下面介绍每一种挂载方式配置:
#hostpath挂载
#hostpah挂载参数说明
#hostPath:宿主机挂载目录
#hostpath挂载示例
#- name: log-volume
# mountPath: /opt/TongWeb/kernel/logs
# hostPath: /home/work/logs
#
#nfs挂载
#nfs挂载参数说明
#nfsPath:表示nfs服务器上面的挂载目录
#nfsServer:表示nfs服务器的ip地址
#nfs挂载示例
#- name: log-volume
# mountPath: /opt/TongWeb/kernel/logs
# nfsPath: /home/work/logs
# nfsServer: 127.0.0.1
#
#emptyDir挂载
#emptyDir挂载参数说明
#emptyDir:采用空目录挂载
#emptyDir挂载示例
#- name: log-volume
# mountPath: /opt/TongWeb/kernel/logs
# emptyDir: {}
#
#configMap挂载
#configMap参数说明
#configMapName: configMap名称
#configMap挂载示例
#- name: tongweb-volume
# mountPath: /opt/TongWeb/kernel/conf/tongweb.xml
# subPath: tongweb.xml
# configMapName: tongweb
#pvc挂载配置
#- name: autodeploy-volume
# mountPath: /opt/TongWeb/kernel/autodeploy
# pvc: autodeploy-pvc
mounts:
- name: log-volume
mountPath: /opt/TongWeb/kernel/logs
hostPath: /home/work/logs
- name: autodeploy-volume
mountPath: /opt/TongWeb/kernel/autodeploy
emptyDir:
{
}
- name: tongweb-volume
mountPath: /opt/TongWeb/kernel/conf/tongweb.xml
subPath: tongweb.xml
configMapName: tongweb
#pvc配置
#persistence:
# enabled: 开关
# pvc:
# - name: pvc名称
# accessMode: 访问模式
# size: 请求资源大小
# storageClass: storageClass名称
# annotations: 注解
persistence:
enabled:
false
pvc:
- name: log-pvc
accessMode: ReadWriteOnce
size: 500Mi
storageClass: nfs-client
annotations:
{
}
- name: autodeploy-pvc
accessMode: ReadWriteOnce
size: 500Mi
storageClass: nfs-client2
annotations:
{
}
# initContainer容器配置，主要是支持应用的部署和文件的上传,利用initcontainer可以部署应用和上
传jar包
# initContainer参数说明
# enabled: initcontainer开关
# containers：容器配置
# - image: 镜像地址
# name: 容器名称
# packagePath: 镜像中文件的路径，建议都放置到同一个路径下面。采用同一个路径可以把所有的文件
都复制下来。
# mounts: 需要挂载到容器中的哪个挂载配置
# mountName: 挂载名称,对应上面的mounts的name配置
initContainers:
enabled:
false
containers:
- image: testwar
name: application
packagePath: /opt/app/.
mounts:
- mountName: autodeploy-volume
#为了方面用户修改或替换tongweb.xml等配置文件，无需重新制作镜像，或者单独的创建每一个
configMap。tongweb helmchart提供一次性的创建所有的configMap,需要把配置文件放到根目录的
configs目录下，通过helm install就可创建所有的configmap
#configMapfile:
#- key: configMap中的key
# value: 配置文件的路径
# configMapName: configMap的名称
#configMapfile配置示例
#configMapfile:
#- key: "tongweb.xml"
# value: "configs/tongweb.xml"
# configMapName: tongweb
configMapfile:
- key:
"tongweb.xml"
value:
"configs/tongweb.xml"
configMapName: tongweb
serviceAccount:
# Specifies whether a service account should be created
create:
false
# Annotations to add to the service account
annotations:
{
}
# The name of the service account to use.
# If not set and create is true, a name is generated using the fullname
template
name:
""
podAnnotations:
{
}
podSecurityContext:
{
}
# fsGroup: 2000
securityContext:
{
}
# capabilities:
# drop:
# - ALL
# readOnlyRootFilesystem: true
# runAsNonRoot: true
# runAsUser: 1000
# service访问配置
# type: 外部访问方式
# portParam:
# - name: port名称
# port: 内部访问端口配置
# targetPort: 目标端口配置
#当type类型为NodePort时可以固定nodePort
# nodePort: 外部访问端口
service:
type: NodePort
portParam:
- name: port-http
port:
9060
targetPort:
8088
# nodePort: 30021
ingress:
enabled:
false
annotations:
{
}
# kubernetes.io/ingress.class: nginx
# kubernetes.io/tls-acme: "true"
hosts:
- host: chart-example.local
paths:
[
]
tls:
[
]
# - secretName: chart-example-tls
# hosts:
# - chart-example.local
resources:
{
}
# We usually recommend not to specify default resources and to leave this as a
conscious
# choice for the user. This also increases chances charts run on environments
with little
# resources, such as Minikube. If you do want to specify resources, uncomment
the following
# lines, adjust them as necessary, and remove the curly braces after
'resources:'
.
# limits:
# cpu: 100m
# memory: 128Mi
# requests:
# cpu: 100m
# memory: 128Mi
autoscaling:
enabled:
false
minReplicas:
1
maxReplicas:
100
targetCPUUtilizationPercentage:
80
# targetMemoryUtilizationPercentage: 80
nodeSelector:
{
}
tolerations:
[
]
affinity:
{
}