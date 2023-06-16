
# demo
```
version: "2.1"
services:
  healthchecks:
    image: lscr.io/linuxserver/healthchecks:latest
    container_name: healthchecks
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - SITE_ROOT=
      - SITE_NAME=
      - DEFAULT_FROM_EMAIL=
      - EMAIL_HOST=
      - EMAIL_PORT=
      - EMAIL_HOST_USER=
      - EMAIL_HOST_PASSWORD=
      - EMAIL_USE_TLS=
      - SUPERUSER_EMAIL=
      - SUPERUSER_PASSWORD=
      - REGENERATE_SETTINGS= #optional
      - ALLOWED_HOSTS= #optional
      - APPRISE_ENABLED= #optional
      - DEBUG= #optional
      - INTEGRATIONS_ALLOW_PRIVATE_IPS= #optional
      - PING_EMAIL_DOMAIN= #optional
      - SECRET_KEY= #optional
      - SITE_LOGO_URL= #optional
    volumes:
      - /path/to/data:/config
    ports:
      - 8000:8000
      - 2525:2525 #optional
    restart: unless-stopped
```

# 注意：这个管理员密码对强密码支持性不太好，我输入太长的长密码，直接不work，就是登录不了

# 使用
Mychecks侦听来自您的 cron 作业和计划任务的 HTTP 请求（“ping”）。
只要 ping 准时到达，它就会保持沉默。
一旦 ping 未按时到达，它就会发出警报。