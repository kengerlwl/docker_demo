

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
# 以root权限登录
mysql -u root -p 

# 以普通用户登录，例如用户kenger
mysql -u kenger -p
关键来了，由于权限分离，导致普通用户是不能看到root用户的表的


```



手动连接到mysql数据库中去。修改host。

```
 mysql -u root -p update mysql.user set host='%' where user='root' and host = 'localhost'; flush privileges; # 设置访问权限
```



如何新建用户并新增权限，以及新建数据库

```
# user:kenger
# pwd:156354

# 新建数据库
CREATE DATABASE 数据库名;


#创建账户
create user 'kenger'@'%' identified by '156354';

#赋予权限
grant all privileges on *.* to 'kenger'@'%' with grant option;

#刷新
flush privileges;
```


更改root用户的登录域名限制
```
DROP USER 'root'@'%'; # 可以有多个root用户，host不一样，要注意修改host
CREATE USER 'root'@'localhost' IDENTIFIED BY 'WKcqDgd8k5WgF2Xp2koj';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
update mysql.user set host='%' where user='root' and host = 'localhost'; flush privileges; # 设置访问权限
FLUSH PRIVILEGES;

```
