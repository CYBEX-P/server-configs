
# LVM Storage
Volume Group: `dev-vg`
Physical Storage (100GiB): `storage`   
Physical Storage (2TiB): `cache-db-storage`   

```bash
sudo lvcreate -L 2T -n cache-db-storage dev-vg
mkfs.xfs /dev/mapper/dev--vg-cache--db--storage

```

Use `sudo blkid` to get drive's UUID, then mount to `/storage/cache-db` with:   

```bash
sudo mount -t xfs -U 52618327-d305-4e28-82f4-25daddf98df5  /storage/cache-db
```


# Users and Groups
These users can not login. `uid` is of type `system`. `Shell` is `nologin`.

## User: cybexp-input
This user is used to run the plugin manager module, which will spawn input plugins. 

## User/group: cybexp-api
Api should be run as this user. `cybex-api` is part. This user is part of the `cache-db` group.   
```bash
adduser --system --no-create-home --disabled-login --shell /bin/nologin cybexp-api
```

## System Group: cybexp-module
This group has write access most of things cybexp, mainly used to access python virtual environment `/opt/cybexp/env` and logs at `/storage/logs`.   

# Modules in this serevr


## MongoDB cache-db (docker)
MongoDB is bound to a local UDS not a IP:PORT interface.    
Worth checking out https://stackoverflow.com/a/30657374     

Server: `cici-dev`   
Service: `cachedb.service`   
IP: `localhost`   
Port: `27017`   

## API
For now API is not hook up to an nginx instance, but can be done easily.

UWSGI config: `/etc/cybexp/api/api-uwsgi.ini`   
Service: `cybexp-api.service`   
Bind: `127.0.0.1:5000`   
Protocol: `HTTP`   

## Input
Server: `cici-dev`   
Location: `/opt/cybexp/input`   
logs: `/storage/logs`
Service: `inputManager.service`   