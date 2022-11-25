```
docker run --name syncthing -d -p 8384:8384 -p 22000:22000 -v /Users/lwl/file_station:/var/syncthing syncthing/syncthing
```

参数解释：

-d：后台运行
-p 8384:8384： 暴露 8384 端口，8384 是 Web 界面端口
-p 22000:22000：暴露 22000 端口，22000 是通讯端口
-v /data/syncthing:/var/syncthing：映射文件夹，将备份的文件映射至宿主机的/data/syncthing 目录下
–restart=always：容器随着 Docker 的启动而启动
syncthing/syncthing:latest：镜像版本

如果你购买的服务器有控制面板，需要在控制面板开放8384（TCP）和22000（TCP 和 UDP 都要开）

至此，syncthing 已经部署到了服务器上，下一步我们只需要在本地也启动一个 syncthing，与服务器进行实时同步即可。



注意，docker启动后，使用动态解析ip是解析不出来的，添加设备时要手动设置
