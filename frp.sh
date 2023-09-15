wget https://github.com/fatedier/frp/releases/download/v0.51.3/frp_0.51.3_linux_amd64.tar.gz
tar -zxvf ...
cd 
vi frps.ini
```
[common]
# frp监听的端口，默认是7000，可以改成其他的
bind_port = 7000
# 授权码，请改成更复杂的
token = 52010  # 这个token之后在客户端会用到

# frp管理后台端口，请按自己需求更改
dashboard_port = 7500
# frp管理后台用户名和密码，请改成自己的
dashboard_user = admin
dashboard_pwd = admin
enable_prometheus = true
```
frps.exe -c ./frps.ini


frpc.exe -c frpc.ini
```
[common]
server_addr = 服务器ip
 # 与frps.ini的bind_port一致
server_port = 7000
 # 与frps.ini的token一致
token = 52010

vi frpc.ini 
# 配置ssh服务
[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
 # 这个自定义，之后再ssh连接的时候要用
remote_port = 6000 
```

开机自启
win + r
shell:startup
新建frp.bat
```
D:
cd D:\frp_0.51.3_windows_amd64
frpc.exe -c frpc.ini
```

for linux
sudo vim /lib/systemd/system/frps.service
```
[Unit]
Description=Frp Server Service
After=network.target

[Service]
Type=simple
User=nobody
Restart=on-failure
RestartSec=5s
ExecStart=/dist/faci/frp_0.51.3_linux_amd64/frpc -c /dist/faci/frp_0.51.3_linux_amd64/frpc.ini

[Install]
WantedBy=multi-user.target
```
