# Describe request IP

## Build docker image
`docker build -t flask_myip:1.0 .`

## run docker
`docker-compose up -d`

## Create network docker
`docker network create --attachable --driver bridge --ipam-driver default --subnet 192.168.255.0/24 ce_frontend`
