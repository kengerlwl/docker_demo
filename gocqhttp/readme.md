# 用docker安装 gocqhttp

## 扫码登录生成配置文件

universal: ws://127.0.0.1:8082/onebot/v11/ws/

```
## 启动gocq
docker run --rm -d --name="gocq" --network host -v $PWD/gocqhttp_data:/data xzsk2/gocqhttp-docker:latest
```





然后把config.yml移动到挂载文件夹里面