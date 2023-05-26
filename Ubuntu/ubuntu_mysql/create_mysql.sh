#!/bin/bash



# 设置变量
NEW_USER="mysql"
NEW_UID="212047"
NEW_GROUP="mysql"
NEW_GID="212000"

# 创建新组
groupadd -g $NEW_GID $NEW_GROUP

# 创建新用户
useradd -u $NEW_UID -g $NEW_GID -G $NEW_GROUP $NEW_USER

# 安装MySQL
apt-get update
apt-get install -y mysql-server

# 设置root用户可以从任何IP访问MySQL
sed -i 's/127\.0\.0\.1/0\.0\.0\.0/g' /etc/mysql/mysql.conf.d/mysqld.cnf

# 重启MySQL
service mysql restart

# 设置mysql用户root密码为156354
mysql -uroot -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '156354'; FLUSH PRIVILEGES;"
