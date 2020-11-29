# Consumer-Producer

DockerImageLink

Consumer: https://hub.docker.com/repository/docker/3006199908/server

Producer: https://hub.docker.com/repository/docker/3006199908/client
Commands to run the docker container - Linux Termial

sudo docker network create client_server_network
sudo docker run --network-alias server --network client_server_network -it server:05
sudo docker run --network client_server_network -it client:05

Video Demo: https://www.youtube.com/watch?v=HE_bwkWnBH0
