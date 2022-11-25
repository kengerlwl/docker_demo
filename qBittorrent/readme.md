```
docker run -d \
  --name=qbittorrent \
  -p 7881:7881 \
  -p 7881:7881/udp \
  -p 18080:18080 \
  -v $PWD/data/qbittorrent/config:/etc/qBittorrent \
  -v $PWD/data/qbittorrent/downloads:/downloads \
  --restart unless-stopped \
  helloz/qbittorrent
```


```
docker run -it \
  --name=qbittorrent \
  -p 7881:7881 \
  -p 7881:7881/udp \
  -p 18080:18080 \
  -v $PWD/data/qbittorrent/config:/etc/qBittorrent \
  -v $PWD/data/qbittorrent/downloads:/downloads \
  --restart unless-stopped \
  helloz/qbittorrent
```