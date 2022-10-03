# 用docker安装 gocqhttp

## 扫码登录生成配置文件

universal: ws://127.0.0.1:8082/onebot/v11/ws/

```
## 启动gocq
docker run --rm -d --name="gocq" --network host -v $PWD/gocqhttp_data:/data xzsk2/gocqhttp-docker:latest
```

-d 是后台启动的意义，-i代表了交互式
第一次启动用下面的命令

```
docker run --rm -i --name="gocq"  \
-p 5700:5700 \
--platform linux/amd64 \
-p 8082:8082 \
-v $PWD/gocqhttp_data:/data \
xzsk2/gocqhttp-docker:latest
```


注意，不能python项目和gocq同时绑定一个端口。只能一个绑定，一个用host
```
docker run --rm -i --name="gocq" \
--net host \
--platform linux/amd64 \
-v $PWD/gocqhttp_data:/data \
xzsk2/gocqhttp-docker:latest
```



然后把config.yml移动到挂载文件夹里面

