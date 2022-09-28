## 下载镜像

```bash
docker pull sameersbn/bind:9.16.1-20200524
```

## 启动容器

参数说明：

| 参数                      | 说明                                                         |
| :------------------------ | :----------------------------------------------------------- |
| WEBMIN_INIT_SSL_ENABLED   | 是否应通过SSL服务Webmin。默认为true。如果您在较早的阶段执行SSL终止，请将其设置为false。 |
| WEBMIN_INIT_REDIRECT_PORT | 从端口提供Webmin。将此设置为反向代理端口，例如443。默认为10000。 |
| ROOT_PASSWORD             | 设置web登录密码                                              |

启动命令：

```
docker run --name='bind' -d -p 53:53/udp -p 53:53/tcp -p 10000:10000/tcp   -e WEBMIN_ENABLED=true -e ROOT_PASSWORD=root -v ~/bind:/data   sameersbn/bind:latest
```



访问Webmin界面：用户名密码：root/root，如果没有设置–env ROOT_PASSWORD=root，默认的用户名密码：root/password
**（注意：一定要用https，不然访问不了界面）** chrome 如何提示不安全。直接命令行输入`thisisunsafe`

```bash
https://192.168.56.200:10000/
```





## linux/Mac 临时修改dns服务器

```
echo nameserver 110.40.204.239 > /etc/resolv.conf
echo nameserver 10.10.1.48 > /etc/resolv.conf
echo nameserver 192.168.1.114 > /etc/resolv.conf
```



### 国内常见dns

```
119.29.29.29 腾讯
```

### mac 删除dns上的缓存

```
sudo killall -HUP mDNSResponder
```

**linux**

```
service nscd reload
```





# bind dns 的webmin使用



把界面改成中文：
![在这里插入图片描述](https://img-bc.icode.best/20210318140703659.png)

## 设置dns域名配置

### 1）删除自带全部主域名配置：

![在这里插入图片描述](https://img-bc.icode.best/20210318140721926.png)
删除成功
![在这里插入图片描述](https://img-bc.icode.best/2021031814085639.png)

### 2）创建视图

![在这里插入图片描述](https://img-bc.icode.best/20210318140910237.png)
填写信息：（我这边写两个网卡的配置）
1：视图的名称
2：就是写网段信息
3：确认
![在这里插入图片描述](https://img-bc.icode.best/20210318140925538.png)
再新建一个132网段的视图
![在这里插入图片描述](https://img-bc.icode.best/20210318140939805.png)
注：几个网卡就是配置这个视图

### 3）开始创建主区域

点击创建新的主区域
![在这里插入图片描述](https://img-bc.icode.best/20210318140956403.png)
输入信息：
1：输入自己的主域名
2：选择视图
3：初始化时容器的id，改成对应视图网段的ip：192.168.56.200
4：邮箱地址（自定义）
5：新建确认
![在这里插入图片描述](https://img-bc.icode.best/2021031814100958.png)
再新建一个132网段的
![在这里插入图片描述](https://img-bc.icode.best/20210318141021758.png)
创建成功：
![在这里插入图片描述](https://img-bc.icode.best/20210318141032405.png)

### 4）开始创建正向区域记录地址

点击主区域：
![在这里插入图片描述](https://img-bc.icode.best/20210318141044233.png)
点击地址：
![在这里插入图片描述](https://img-bc.icode.best/20210318141558176.png)

填写内容：
1：输入名称，比如：ttt，后面访问的时候会自动加上主区域名称，域名全称变成：ttt.binggoling.com
2：域名要映射的主机地址
3：确认
![在这里插入图片描述](https://img-bc.icode.best/20210318141153716.png)
点击右上角的应用，把配置生效：
![在这里插入图片描述](https://img-bc.icode.best/2021031814121725.png)

注意，有多个ip映射，就多配置几个

### 5）132网段的设置也是一样的

在视图132的主区域上设置，IP是192.168.132.121
![在这里插入图片描述](https://img-bc.icode.best/20210318141250211.png)



然后就可以通过ttt.binggoling.com访问到ip192.168.132.121。



# 如何设置内网dns

做这个的目的是为了在内网搭建一套dns系统。

可以通过路由器设置dhcp的信息。将主路由设置为自建dns的ip。辅路由设置成一个公网的dns ip。

这样就可以即访问外网也能访问内网。

一个比较成熟的设计方案是搞一个nginx作为代理。将所有的域名请求都转发到该代理主机ip上。通过80端口监听所有的请求服务。

然后根据不同的访问域名做分发，映射到不同的服务上去。



# ref

https://icode.best/i/04829639391675
