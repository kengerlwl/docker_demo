rm -rf ./data/ldap_db/*
rm -rf ./data/ldap_config/*

docker_name="openldap"
docker image prune -f
docker stop ${docker_name}
docker rm ${docker_name}

docker_name="phpldapadmin"
docker image prune -f
docker stop ${docker_name}
docker rm ${docker_name}

echo -e "\033[5;36mOrz 旧容器(镜像)已清理\033[0m"


docker-compose -f docker-compose.yml up -d
sleep 1
docker ps -a