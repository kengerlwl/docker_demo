由于bitwarden要ssl才能使用，我懒得配置docker容器内部的ssl访问。
所以直接使用nginx反向代理实现https加密

```
mkdir ./data
docker run  -d \
            --rm \
            --name bitwarden \
            -p 8080:80 \
            -p 3012:3012 \
            -e SIGNUPS_ALLOWED=true \
            -e WEB_VAULT_ENABLED=true \
            -e DOMAIN=https://mydomain.cn \
            -v $PWD/data:/data \
            vaultwarden/server:latest
```
上面命令的各个参数含义如下：
-d 在后台运行
--rm 容器停止运行后，自动删除容器文件
--name bitwarden容器的名字为bitwarden
-p 8080:80 容器的端口80映射到8080，在Nginx配置
-p 3012:3012 容器的端口3012映射到3012
-e SIGNUPS_ALLOWED=true 设置环境变量SIGNUPS_ALLOWED=true允许用户注册
-e WBE_VAULT_ENABLE=true 设置环境变量WBE_VAULT_ENABLE=true
-e DOMAIN=https://mydomain.cn设置域名,需要替换成自己申请的域名
-v /data/bitwarden:/data 容器的/data/目录映射到宿主机的/data/bitwarden目录

解析一个域名到你的服务器上，

配置反向代理
server
{
    listen 80;
    server_name password.imcharon.com;
    index index.php index.html index.htm default.php default.htm default.html;
    root /www/wwwroot/password.imcahron.com;
    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Range $http_range;
        proxy_set_header If-Range $http_if_range;
        proxy_redirect off;
        proxy_pass http://127.0.0.1:8080;
    }
    #禁止访问的文件或目录
    location ~ ^/(\.user.ini|\.htaccess|\.git|\.svn|\.project|LICENSE|README.md)
    {
        return 404;
    }
    #一键申请SSL证书验证目录相关设置
    location ~ \.well-known{
        allow all;
    }
    access_log  /www/wwwlogs/password.imcahron.com.log;
    error_log  /www/wwwlogs/password.imcahron.com.error.log;
}
因为我用的cloudflare，所以没有https的设置，你们在宝塔配置完直接把我的反代贴上去就行。

# ref
https://www.imcharon.com/1125/