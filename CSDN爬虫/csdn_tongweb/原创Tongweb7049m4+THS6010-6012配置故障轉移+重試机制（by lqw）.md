# 原创Tongweb7049m4+THS6010-6012配置故障轉移+重試机制（by lqw）

> 原文地址: https://blog.csdn.net/weixin_39938069/article/details/142854919

---

使用场景
1.ths代理tongweb多套后端，假如有其中一套tongweb因为服务器重启或者宕机后没有及时启动，导致ths一直轮询在这个出故障的节点上。
2.即使在tongweb重启了，有的应用启动也需要一定的时间，这个时候只是启动了应用端口，ths仍有可能轮询在对应的tongweb上。
说明：
本文仅供参考，里面的参数配置，最终请根据自身业务场景进行调整。
服务器配置
本次示范使用两台服务器（113和114），分别搭建两套ths和两套tongweb做负载均衡和反向代理，浮动ip使用151，tongweb部分配置了测试用的ssl证书(如何配置ssl的可自行百度)。
httpserver.conf配置
#user  nobody;
worker_processes auto
;
worker_cpu_affinity auto
;
#error_log  logs/error.log;
#error_log  logs/error.log  notice;
error_log logs/error.log info
;
pid logs/httpserver.pid
;
events
{
worker_connections
1024
;
use epoll
;
}
http
{
include mime.types
;
default_type application/octet-stream
;
log_format main
'
$remote_addr
-
$remote_user
[
$time_local
] "
$request
" '
'
$status
$body_bytes_sent
"
$http_referer
" '
'"
$http_user_agent
" "
$http_x_forwarded_for
"'
;
#access_log  logs/access.log  main;
access_log off
;
sendfile on
;
#tcp_nopush     on;
#keepalive_timeout  0;
keepalive_timeout
60
;
# 设置5秒的超时时间
#proxy_connect_timeout 5s;
# 连接超时
#proxy_read_timeout 5s;
# 读取超时
#proxy_send_timeout 5s;
# 发送超时
# 配置切换到其他后端的条件，包括超时和错误状态码
proxy_next_upstream error
timeout
http_404 http_500 http_502 http_503 http_504 http_403
;
#gzip  on;
upstream tongweb
{
#ip_hash;
#server后填写对应所有前端机器的ip
server
192.168
.10.113:8088
max_fails
=
3
fail_timeout
=
2s
;
server
192.168
.10.114:8088
max_fails
=
3
fail_timeout
=
2s
;
#keepalive 200;
health_check
interval
=
30000
rise
=
1
fall
=
3
type
=
ssl_hello
;
#keepalive_requests 10000;
}
server
{
server_name localhost_ths_monitor
;
listen
49151
;
access_log off
;
allow
127.0
.0.1
;
deny all
;
location /thsapi/
{
api /status
;
}
}
server
{
listen
8080
;
server_name localhost
;
#charset koi8-r;
#access_log  logs/host.access.log  main;
access_log off
;
#proxy_next_upstream error timeout http_404 http_500 http_502 http_503 http_504 http_403;
location /
{
root html
;
index index.html index.htm
;
}
#error_page  404              /404.html;
# redirect server error pages to the static page /50x.html
error_page
500
502
503
504
/50x.html
;
location
=
/50x.html
{
root html
;
}
# proxy the PHP scripts to Apache listening on 127.0.0.1:80
#
#location ~ \.php$ {
#    proxy_pass   http://127.0.0.1;
#}
# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#
#location ~ \.php$ {
#    root           html;
#    fastcgi_pass   127.0.0.1:9000;
#    fastcgi_index  index.php;
#    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
#    include        fastcgi_params;
#}
# deny access to .htaccess files, if Apache's document root
# concurs with httpserver's one
#
#location ~ /\.ht {
#    deny  all;
#}
}
server
{
listen
443
ssl
;
server_name localhost
;
# 配置 SSL 证书和密钥
ssl_certificate tools/crt_demo/server.crt
;
ssl_certificate_key tools/crt_demo/server.key
;
proxy_next_upstream error
timeout
http_404 http_500 http_502 http_503 http_504 http_403
;
location /
{
proxy_pass https://tongweb
;
}
}
# HTTPS server
#server {
#listen       443 ssl;
#server_name  localhost;
#ssl_protocols TLSv1.2 TLSv1.3;
#GMTLS key
#ssl_gmtls on;
#ssl_certificate      crts/SS.pem crts/SE.pem;
#ssl_certificate_key  crts/SS.key.pem crts/SE.key.pem;
#https key
#ssl_certificate      crts/common_cert/server.crt;
#ssl_certificate_key  crts/common_cert/server.key;
#ssl_session_cache    shared:SSL:1m;
#ssl_session_timeout  5m;
#ssl_ciphers  HIGH:!aNULL:!MD5;
#ssl_prefer_server_ciphers  on;
#location / {
#root   html;
#index  index.html index.htm;
#}
#}
}
其中核心配置部分主要是这两个地方：
备注：
1.proxy_next_upstream error timeout http_404 http_500 http_502 http_503 http_504 http_403;作用在http，server和location块，请不要配置在其他地方，一般情况下建议可以配在http块里。
测试
先測試113和114部署的應用是否能正常訪問
然後測試用ths的端口訪問是否能正常訪問（包括浮動ip）：
然後可以自己在命令行頁面kill掉其中一台服务器上的tongweb进程，或者在其中一台tongweb控制台上停止该应用（生产环境不推荐，本文只是做测试才用）。
再去访问停掉的应用，发现是访问不了的：
去访问ths和浮动ip，仍然是正常的：