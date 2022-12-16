# 不清空文件夹那么会创建失败
rm -rf mysql/data

mkdir mysql/data

# 后台运行compose文件
docker-compose -f docker-compose.yml up -d


