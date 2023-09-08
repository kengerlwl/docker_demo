```
docker run -d --net host --name xray --restart=always -v $PWD/xray:/etc/xray teddysun/xray

```

v2ray
```
sudo docker run -it --name v2ray -v $PWD/v2ray/config.json:/etc/v2ray/config.json -p 52333:52333 v2fly/v2fly-core:v4.31.0 
```





# 解释

```
{
  "log": {
    "loglevel": "info"
  },
  "inbounds": [
    {
      "listen": "0.0.0.0",
      "port": 52333,
      "protocol": "vmess",
      "settings": {
        "clients": [
          {
            "id": "8FF6627C-C247-44EB-A9AA-A7EAB8385D4A",
            "alterId": 0,
            "security": "auto"
          }
        ]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "blackhole",
      "settings": {
        "response": {
          "type": "none"
        }
      },
      "tag": "block"
    },
    {
      "protocol": "freedom",
      "settings": {},
      "tag": "proxy"
    }
  ],
  "routing": {
    "domainStrategy": "AsIs",
    "domainMatcher": "mph",
    "rules": [
      {
        "domainMatcher": "mph",
        "type": "field",
        "outboundTag": "proxy",
        "domain": [
          "com",
          "cn",
          "xyz",
          "work",
          "" // 匹配所有域名
        ]
      },
      {
        "domainMatcher": "mph",
        "type": "field",
        "outboundTag": "proxy",
        "ip": ["0.0.0.0/0"] // 匹配所有ip
      }
    ]
  }
}
```

