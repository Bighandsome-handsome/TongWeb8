# 原创TongWeb-k8s部署运行TongWeb嵌入版应用

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/134268114

---

基础环境要求：
K8s至少两台服务器，一台作为master一台作为node，以及需要私有仓库用于节点镜像拉取
创建一个Dockerfile，用于构建Docker镜像，与应用jar同级
这个Dockerfile使用了openjdk:8作为基础镜像，并将Url.jar复制到镜像中，并设置了启动命令
构建Docker镜像。在命令行中，进入项目根目录，执行命令构建镜像
docker build -t url:v1 .
查看构建好的镜像  docker images
为构建好的镜像打上标签
docker tag url:v1 192.168.18.105:5000/url:v1
上传到私有仓库
docker push 192.168.18.105:5000/url:v1
列出私有仓库的所有镜像
curl http://192.168.18.105:5000/v2/_catalog
创建一个Kubernetes的Deployment文件。在项目根目录下创建一个名为deployment.yaml的文件
这个Deployment文件定义了一个名为" url-deployment"的Deployment，使用镜像仓库中的镜像，并暴露了容器的8088端口
创建一个Kubernetes的Service文件。在项目根目录下创建一个名为service.yaml的文件
这个Service文件定义了一个名为"url-service"的Service，将流量转发到之前创建的Deployment中的Pod
使用kubectl命令部署应用程序。在命令行中，进入到项目根目录，并执行以下命令来部署应用程序
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
验证部署是否成功。使用kubectl命令检查Pod和Service的状态：
kubectl get pods
kubectl get services
查看运行pod日志，是否启动成功
kubectl logs url-deployment-5fd7db7d45-4xl2p
用k8s生成的ip和对外端口80测试访问
curl http://192.130.150.7:80
附件：