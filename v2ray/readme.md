```
docker run -d --net host --name xray --restart=always -v $PWD/xray:/etc/xray teddysun/xray

```

```
sudo docker run -d --name v2ray -v $PWD/v2ray:/etc/v2ray --net host v2ray/official  v2ray -config=/etc/v2ray/config.json
```