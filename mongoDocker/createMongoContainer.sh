#!/usr/bin/env bash


MONGO_NAME="backend-mongo-rs0"
ARBITER_NAME="backend-mongo-arb-rs0"
STORAGE_LOCATION=/storage/backend

# MONGO_TYPE="Dockerfile-standalone"
MONGO_TYPE="Dockerfile-replicaSet"

docker build --tag mongodb $MONGO_TYPE




mkdir -p ${STORAGE_LOCATION}/{db,configdb,logs}
docker run -d -p 27017:27017 --name $MONGO_NAME -v ${STORAGE_LOCATION}/db:/data/db -v ${STORAGE_LOCATION}/configdb:/data/configdb  -v ${STORAGE_LOCATION}/logs:/var/log/mongodb

mkdir -p ${STORAGE_LOCATION}/arbiter/{db,configdb,logs}
docker run -d -p 27020:27017 --name $ARBITER_NAME -v ${STORAGE_LOCATION}/arbiter/db:/data/db -v ${STORAGE_LOCATION}/arbiter/configdb:/data/configdb  -v ${STORAGE_LOCATION}/arbiter/logs:/var/log/mongodb
