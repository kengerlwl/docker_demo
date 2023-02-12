```
docker run -d --net host --name xray --restart=always -v $PWD/xray:/etc/xray teddysun/xray

```

v2ray
```
sudo docker run -it --name v2ray -v $PWD/v2ray/config.json:/etc/v2ray/config.json -p 52333:52333 v2fly/v2fly-core:v4.31.0 
```