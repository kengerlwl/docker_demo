```
docker run -d \
--name frpc_lwl \
-v $PWD/frpc.ini:/etc/frp/frpc.ini \
--net host \
snowdreamtech/frpc



docker run -d \
--name frps_lwl \
-v $PWD/frps.ini:/etc/frp/frps.ini \
--net host \
snowdreamtech/frps

```