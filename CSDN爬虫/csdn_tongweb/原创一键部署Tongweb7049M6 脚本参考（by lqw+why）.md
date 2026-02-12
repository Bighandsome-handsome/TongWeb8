# 原创一键部署Tongweb7049M6 脚本参考（by lqw+why）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/148847236

---

安装前准备
1.安装包和授权已放上服务器
2.已安装并配置jdk环境（jdk不低于1.8）
3.使用root账号进行安装。
安装说明
本帖提供的是脚本的形式进行安装，需提前将脚本内容copy到deploy_TongWeb.sh,赋权后执行，安装目录在opt下的TongWeb7.0.4.9_M6_Enterprise_Linux，下面是脚本内容：

```bash
#!/bin/bash
# 虚机全自动TongWeb部署脚本
#使用说明：
#文件准备统一在同级目录下：
#/部署目录/
#├── deploy_TongWeb.sh  部署脚本
#├── license.dat      产品授权
#└── TongWeb7.0.4.9_M6_Enterprise_Linux.tar.gz  安装包
#执行权限：chmod +x deploy_TongWeb.sh
#运行部署：sudo ./deploy_TongWeb.sh

#!/bin/bash
# =================================================================
# 虚机全自动 TongWeb 部署脚本
# 运行部署：sudo ./deploy_TongWeb.sh
# =================================================================

# --- 配置信息 ---
TARGET_DIR="/opt"
INSTALL_NAME="TongWeb7.0.4.9_M6_Enterprise_Linux"
CURRENT_DIR=$(cd "$(dirname "$0")"; pwd)
INSTALL_PACKAGE="${CURRENT_DIR}/${INSTALL_NAME}.tar.gz"
LICENSE_FILE="${CURRENT_DIR}/license.dat"
SERVICE_NAME="TongWeb"

# 颜色输出函数
error_echo() { echo -e "\033[31m$1\033[0m"; }
success_echo() { echo -e "\033[32m$1\033[0m"; }

# 1. 环境校验
check_env() {
    [ $(id -u) -eq 0 ] || { error_echo "错误：必须使用 root 权限执行！"; exit 1; }
    [ -f "$INSTALL_PACKAGE" ] || { error_echo "错误：安装包 ${INSTALL_NAME}.tar.gz 不存在！"; exit 1; }
    [ -f "$LICENSE_FILE" ] || { error_echo "错误：授权文件 license.dat 不存在！"; exit 1; }
}

# 2. 安装流程
install_process() {
    # 清理旧版本
    echo "正在清理旧版本..."
    rm -rf "${TARGET_DIR}/${INSTALL_NAME}"

    # 解压安装包
    echo "正在解压安装包至 ${TARGET_DIR}..."
    if ! tar -zxvf "$INSTALL_PACKAGE" -C "$TARGET_DIR" > /dev/null; then
        error_echo "安装包解压失败！"
        exit 1
    fi

    # 部署授权文件
    cp "$LICENSE_FILE" "${TARGET_DIR}/${INSTALL_NAME}/"

    # 安装系统服务 (systemd)
    echo "正在初始化系统服务..."
    cd "${TARGET_DIR}/${INSTALL_NAME}/bin" || exit 1
    chmod +x *.sh
    ./installservice.sh

    # 启动服务
    echo "正在启动服务..."
    nohup ./startservernohup.sh > /dev/null 2>&1 &
    
    sleep 5
}

# 3. 安装验证
verify_installation() {
    local PID_FILE="${TARGET_DIR}/${INSTALL_NAME}/bin/tongweb.pid"
    local retry=0
    local max_retry=5
    local found_pid=false

    echo "正在等待服务初始化并生成 PID 文件..."
    while [ $retry -lt $max_retry ]; do
        if [ -f "$PID_FILE" ]; then
            local pid=$(cat "$PID_FILE" 2>/dev/null)
            if ps -p "$pid" > /dev/null; then
                success_echo "服务验证通过，进程 PID: $pid"
                found_pid=true
                break
            else
                echo "检测到无效 PID: $pid，清理并重试..."
                rm -f "$PID_FILE"
            fi
        fi
        ((retry++))
        echo "等待中 ($retry/$max_retry)..."
        sleep 5
    done

    if ! $found_pid; then
        error_echo "服务启动异常，请检查日志！"
        error_echo "可能原因：1. JDK未安装 2. 端口占用 3. 授权过期"
        exit 1
    fi
}

# --- 主流程 ---
main() {
    check_env
    install_process
    verify_installation

    echo "------------------------------------------------------"
    success_echo "TongWeb 安装成功！"
    echo "安装目录：${TARGET_DIR}/${INSTALL_NAME}"
    echo "管理控制台：http://服务器IP:9060/console"
    echo "实时日志查询：tail -f ${TARGET_DIR}/${INSTALL_NAME}/logs/server.log"
    echo "------------------------------------------------------"
}

# 执行主流程
main
```

安装后提示如下：
安装同时会生成/etc/systemd/system/tongweb.service，可以安装后重启服务器，测试是否会开机自启动：如果不想用这种形式安装，可以参考：TongWeb7-绿色版安装及启动停止和控制台访问
