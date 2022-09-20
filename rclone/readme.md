# rclone

```
docker run -d --name=rclonebrowser \
--cap-add SYS_ADMIN \
--device /dev/fuse \
--security-opt apparmor=unconfined \
-p 5801:5800 \
-p 5901:5900 \
-v /volume1/docker/rclone/config:/config \
-v /volume1/docker/rclone/media:/media:shared \
-e GROUP_ID=0 \
-e USER_ID=0 \
-e TZ=Asia/Shanghai \
-e VNC_PASSWORD=123456 \
-e ENABLE_CJK_FONT=1 \
romancin/rclonebrowser:latest


```




# mac 不支持
fuse搞不定
