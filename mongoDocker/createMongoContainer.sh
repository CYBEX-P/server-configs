#!/usr/bin/env bash


RESTART_POLICY=always
#RESTART_POLICY=on-failure

MONGO_NAME="backend-mongo-rs0"
ARBITER_NAME="backend-mongo-arb-rs0"
STORAGE_LOCATION=/storage/backend

# MONGO_TYPE="Dockerfile-standalone"
MONGO_TYPE="Dockerfile-replicaSet"

sudo docker build --tag mongodb-rs0 -f $MONGO_TYPE .




sudo mkdir -p ${STORAGE_LOCATION}/{db,configdb,logs}
sudo docker run -d --restart=$RESTART_POLICY -p 27017:27017 --name $MONGO_NAME -v ${STORAGE_LOCATION}/db:/data/db -v ${STORAGE_LOCATION}/configdb:/data/configdb  -v ${STORAGE_LOCATION}/logs:/var/log/mongodb mongodb-rs0

#sudo mkdir -p ${STORAGE_LOCATION}/arbiter/{db,configdb,logs}
#sudo docker run -d --restart=$RESTART_POLICY -p 27020:27017 --name $ARBITER_NAME -v ${STORAGE_LOCATION}/arbiter/db:/data/db -v ${STORAGE_LOCATION}/arbiter/configdb:/data/configdb  -v ${STORAGE_LOCATION}/arbiter/logs:/var/log/mongodb mongodb-rs0
