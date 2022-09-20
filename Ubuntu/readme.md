# nginx
```
apt-get install nginx

# conf
/etc/nginx/nginx.conf


# cmd
**nginx # 开启
nginx -s reload     #重新加载配置文件
nginx -s reopen     #重新打开log文件
nginx -s stop       #快速关闭nginx服务
nginx -s quit       #优雅的关闭nginx服务，等待工作进程处理完所有的请求



# 反向代理接口
    server {
        listen       51001;
        server_name  110.40.204.239;
        location / {
            add_header Access-Control-Allow-Origin '*' always;
            add_header Access-Control-Allow-Headers "Accept,Accept-Encoding,Accept-Language,Connection,Content-Length,Content-Type,Host,Origin,Referer,User-Agent";
            add_header Access-Control-Allow-Methods "GET, POST, PUT, OPTIONS";
            add_header Access-Control-Allow-Credentials true;
            if ($request_method = 'OPTIONS') {
                return 200;
            }
            
            proxy_pass  http://0.0.0.0:53682;
        }

    }
```


