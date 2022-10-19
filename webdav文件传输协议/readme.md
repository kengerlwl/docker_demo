# readme
```
docker run -d -v $PWD/data:/var/webdav -e USERNAME=kenger -e PASSWORD=156354 -p 8887:80 morrisjobke/webdav
```

访问，后缀不能省略

http://ip:8888/webdav

Finder -> 前往 -> 连接服务器，在对话框中输入: http://用户名:密码@IP:端口/webdav就可以将共享盘挂载到本地，然后像访问本地磁盘文件夹一样直接将需要共享的内容复制进去即可。



# ref
https://blog.devzeng.com/blog/build-webdav-server-in-docker.html


