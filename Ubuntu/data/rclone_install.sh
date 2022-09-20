apt-get install -y unzip fuse

curl https://rclone.org/install.sh | bash

rclone mount one: /data1 --allow-other --allow-non-empty --vfs-cache-mode writes