# 可选(直接docker运行)

# 官方

```
docker run --name kenger_zerotier -d \
--cap-add=NET_ADMIN \
--cap-add=SYS_ADMIN \
--net=host \
--device /dev/net/tun \
-v $PWD/zerotier-one:/var/lib/zerotier-one \
zerotier/zerotier:latest xxx

```



## it测试

```
docker run --name kenger_zerotier -it \
--cap-add=NET_ADMIN \
--cap-add=SYS_ADMIN \
--net=host \
--device /dev/net/tun \
-v $PWD/zerotier-one:/var/lib/zerotier-one \
zerotier/zerotier:latest bash

```











# 纯ubuntu执行

```
NET_ID=52b337794f7ead9d

# download
curl https://install.zerotier.com/ | bash

# run zerotier
/usr/sbin/zerotier-one -d

# join target network
/usr/sbin/zerotier-cli join $NET_ID

/usr/sbin/zerotier-cli listnetworks 
```





# ref-truenas

https://www.gurenkai.com/archives/1676560532122