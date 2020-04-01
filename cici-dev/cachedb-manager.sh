#!/usr/bin/bash

SOCKET_LOCATION=/some/location.sock
CONTAINER_NAME="cache-db"

VALID_COMMANDS=("start" "stop")

function startCacheDB {
	echo "cachedb-manager.sh: Starting $CONTAINER_NAME container."
	# docker start $CONTAINER_NAME
	# chmod :cache-db $SOCKET_LOCATION	
}



function stopCacheDB {
	echo "cachedb-manager.sh: Starting $CONTAINER_NAME container."
	# docker stop $CONTAINER_NAME	
}


if [[ " ${VALID_COMMANDS[@]} " =~ " ${1} " ]]; then # if valid command
	${1}CacheDB

else
	echo "Valid commands: ${VALID_COMMANDS[*]}"
fi

