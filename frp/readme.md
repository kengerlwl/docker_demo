docker run -d \
--name frpc_lwl \
-v $PWD/frpc.ini:/etc/frp/frpc.ini \
--net host \
snowdreamtech/frpc
