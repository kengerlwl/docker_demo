
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