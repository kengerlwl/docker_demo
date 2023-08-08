```
docker run -d --restart=always -v $PWD/alist_data:/opt/alist/data -p 5244:5244 --name="alist" xhofe/alist:latest
```


默认用户是admin

密码是随机生成的，查看方式为
`docker logs alist`

```
(base) kenger@hw-ubuntu:~$ docker logs alist
INFO[2023-07-06 03:21:56] reading config file: data/config.json        
INFO[2023-07-06 03:21:56] config file not exists, creating default config file 
INFO[2023-07-06 03:21:56] load config from env with prefix:            
INFO[2023-07-06 03:21:56] init logrus...                               
INFO[2023-07-06 03:21:56] Successfully created the admin user and the initial password is: ANn4yLf7 
INFO[2023-07-06 03:21:57] start HTTP server @ 0.0.0.0:5244             
INFO[2023-07-06 03:21:57] qbittorrent not ready.                       
INFO[2023-07-06 03:21:57] Aria2 not ready. 
```