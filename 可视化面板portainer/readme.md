# 命令
docker run -d -p 8090:9000 \
--restart=always -v /var/run/docker.sock:/var/run/docker.sock --privileged=true  portainer/portainer


# 然后就可以通过8088这个端口去访问了