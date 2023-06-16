# 青龙定时执行面板
```
# curl -sSL get.docker.com | sh

# 确认文件夹是否存在
if [ ! -d "data" ]; then
    mkdir data
fi

docker run -dit \
  -v $PWD/data:/data \
  -p 5700:5700 \
  -e QlBaseUrl="/" \
  --name qinglong \
  --hostname qinglong \
  --restart unless-stopped \
  whyour/qinglong:latest
```