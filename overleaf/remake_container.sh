container_name=kenger_container
image_name=kenger_image

docker stop $container_name
docker rm $container_name  #

# rebuild
docker build -t ${image_name}:v1 . 

# run
docker run --privileged=true -it \
--name=$container_name \
--net=host \
-v /etc/config:/var/app/config_file \
${image_name} bash  
