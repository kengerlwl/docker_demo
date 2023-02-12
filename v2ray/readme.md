```
docker run -d --net host --name xray --restart=always -v $PWD/xray:/etc/xray teddysun/xray

```

v2ray
```
sudo docker run -d --name v2ray -v $PWD/v2ray/config.json:/etc/v2ray/config.json --net host v2fly/v2fly-core:v4.31.0 
```