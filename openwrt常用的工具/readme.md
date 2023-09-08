# lucky工具
```
# host模式, 同时支持IPv4/IPv6, Liunx系统推荐
docker run -d --name lucky --restart=always --net=host gdy666/lucky
# 桥接模式, 只支持IPv4, Mac/Windows推荐,windows 不推荐使用docker版本
docker run -d --name lucky --restart=always -p 16601:16601 gdy666/lucky
```

