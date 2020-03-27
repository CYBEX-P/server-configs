
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

## User: plugin-runner
This user is used to run the plugin manager module, which will spawn input plugins. This user can not login. `uid` is of type `system`. `Shell` is `nologin`.

## User: cybex-api
Api should be run as this user. `cybex-api` is part. This user is part of the `cache-db` group.   
```bash
adduser --system --disabled-login --shell /bin/nologin cybex-api
```

## System Group: cache-db
This group has access to the mongodb cache-db Unix Domain Socket.   
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

Service: ` `
IP: `/some/location.sock`
Port: `N/A`
GID: `cache-db`

