FROM rclone/rclone

WORKDIR /app

VOLUME ["./data","/data"]
VOLUME ["./conf","config/rclone"]



CMD ["rclone" , "/data/main.sh"]