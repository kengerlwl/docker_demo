

# 运行
```
docker-compose -f docker-compose.yml up -d
```





# docker run 启动mysql

```
docker run --name=mysql_lwl -v /data/DataLACP/liuwenlong:/tmp/test -it -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql/mysql-server:5.7.26 /bin/bash
```





# mysql

宿主主机不能访问问题。

**进入mysql**

```
mysql -u root -p 
```



手动连接到mysql数据库中去。修改host。

```
 mysql -u root -p update mysql.user set host='%' where user='root' and host = 'localhost'; flush privileges; # 设置访问权限
```



如何新建用户并新增权限

```
# user:kenger
# pwd:156354
#创建账户
create user 'kenger'@'%' identified by '156354';

#赋予权限
grant all privileges on *.* to 'kenger'@'%' with grant option;

#刷新
flush privileges;
```

