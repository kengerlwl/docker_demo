# 不清空文件夹那么会创建失败
rm mysql/data/*

# 后台运行compose文件
docker-compose -f docker-compose.yml up -d

# 再把文件建立回去
touch mysql/data/test



