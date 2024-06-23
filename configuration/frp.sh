wget https://github.com/fatedier/frp/releases/download/v0.54.0/frp_0.54.0_linux_amd64.tar.gz
tar -zxvf ...
cd 

https://gofrp.org/zh-cn/docs/setup/

# server
```vi frps.toml
bindPort = 7000 # server port
```

./frps -c frps.toml

# in Screen
screen -S frp


# client
```vi frpc.toml
serverAddr = "x.x.x.x" # ip of server
serverPort = 7000

[[proxies]]
name = "test-tcp"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 6000
```

./frpc -c frpc.toml

# auto start
vi /etc/rc.local

# test
ssh -o Port=6000 root@x.x.x.x