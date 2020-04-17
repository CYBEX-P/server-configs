
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

## User: cybexp-input
This user is used to run the plugin manager module, which will spawn input plugins. This user can not login. `uid` is of type `system`. `Shell` is `nologin`.

## User: cybexp-api
Api should be run as this user. `cybex-api` is part. This user is part of the `cache-db` group.   
```bash
adduser --system --no-create-home --disabled-login --shell /bin/nologin cybexp-api
```

## System Group: cybexp-log
This group has write access the log folder, things writings logs should be in this group.   
```bash
addgroup --system cache-db
```

# Modules in this serevr
## Input
Location: ` `
Service: ` `

## MongoDB cache-db (docker)
MongoDB is bound to a local UDS not a IP:PORT interface.   
Worth checking out https://stackoverflow.com/a/30657374   

Server: `cici-dev`
Service: ` `
IP: `localhost`
Port: `27017`

