container_name=selenium_chrome_1

sudo docker stop $container_name
sudo docker rm $container_name

container_name=selenium-hub

sudo docker stop $container_name
sudo docker rm $container_name

sudo docker-compose -f docker_compose.yml up -d