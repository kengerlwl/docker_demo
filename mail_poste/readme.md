```
docker run -d \

    -p 880:80 -p 8443:443 -p 25:25 -p 110:110 -p 143:143 -p 465:465 -p 587:587 -p 993:993 -p 995:995 -p 4190:4190 \

    -e TZ=Asia/Shanghai \

    -v /data:/data \

    --name "mailserver" \

    -h "mail.kengerbirthday.xyz" \

    --restart=always \

    -t analogic/poste.io
```

- 880/8443是WEB访问端口，为了避免和本地已有WEB服务（nginx等）冲突，所以这里使用的880/8443作为WEB端口
- TZ=Asia/Shanghai：设置容器为上海时区
- /data/mail-data：本地数据目录，根据实际情况修改为服务器目录
- mail.xxx.com：改成你自己的域名
- --restart=always：容器异常时自动拉起