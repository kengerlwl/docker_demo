# 踩坑一

该docker程序不能在mac上运行

docker 开启的服务中，4444端口在服务器不能够直接通过公网访问，只有本机ip发出的访问才能受理。

所以我用nginx做了本地代理


建议还是多看官方的文档
https://hub.docker.com/r/selenium/node-chrome-debug

# 启动docker-compose
流程不再赘述。但是这个镜像有点大

# 查看Chrome的执行情况。

使用vnc工具。

根据selenium-hub开放的端口连接进取

# selenium使用翻墙代理

用到了一个叫作proxy的类


# vnc

chrome vnc 的密码： secret

