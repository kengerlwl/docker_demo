```
docker pull linuxserver/qbittorrent:4.4.2

docker run -d \
  --name=qbittorrent \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -e WEBUI_PORT=8088 \
  --net=host \
  -v $PWD/config:/config \
  -v $PWD/downloads:/downloads \
  --restart unless-stopped \
  linuxserver/qbittorrent:4.4.2
```


启动后默认用户名：admin

密码为:adminadmin

**设置**

![image-20230115185504965](/Users/lwl/Library/Application Support/typora-user-images/image-20230115185504965.png)
