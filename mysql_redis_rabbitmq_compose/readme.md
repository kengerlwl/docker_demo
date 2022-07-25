

# 运行
```
docker-compose -f docker-compose.yml up -d
```





# mysql 

宿主主机不能访问问题。



手动连接到mysql数据库中去。修改host。

```
 mysql -u root -p update mysql.user set host='%' where user='root' and host = 'localhost'; flush privileges; # 设置访问权限
```

