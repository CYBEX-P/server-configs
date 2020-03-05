
# Initial settup on mongoX servers (not done yet)

Install `docker`:   
```bash
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
# the following was skiped for security reasons
# sudo usermod -aG docker $USER # add user so that it does not need to use sudo to modify machines
```   
# hostnames for mongo replica set
|Hostname|Internal IP|External IP | 
|:------:|:---------:|:----------:|
|cici-mongo1|172.16.1.|134.197.20.18:3333|
|cici-mongo2|172.16.1.14|134.197.20.18:4444|
||172.16.1.|134.197.20.18:|

# Storage LVM on Mongo1,2 servers (one time setup)
Each server should have a RAID drive of 4TB which is ~3.3.TB. Usually located at `/dev/sdb`
There is a LVM Physical volume of 100% of this drive.   
`/dev/sdb1` is `db-storage` Physical volume.   
`db-storage-vg` is the database storage volumen group.   
`backend-storage` is the name of the logical volume used in the DAM/Tahoe,Users,Archive,Report modules.   
`cache-storage` is the name of the logical volume used for the cache data, this is a temporary location. This should be migrated to an external server(maybe cici-dev).  
`backend-storage` and `cache-storage` use filesystem `ext4`.   
   
The following was done on `cici-mongo1` and `cici-mongo2`(independently):   
```bash
parted -s /dev/sdb 'mklabel gpt'
parted -s /dev/sdb 'mkpart db-storagre 1Mb 100%'
pvcreate /dev/sdb1
vgcreate db-storage-vg /dev/sdb1
lvcreate -L 2T -n backend-storage db-storage-vg
lvcreate -L 1T -n cache-storage db-storage-vg
mkfs.ext4 /dev/mapper/db--storage--vg-backend--storage
mkfs.ext4 /dev/mapper/db--storage--vg-cache--storage
```

## Mount points (fstab) (one time setup)
Use `sudo blkid` to get UUID for each disk.   

`/etc/fstab`:   
```
UUID=<uuid> /storage/backend ext4 defaults 0 0
UUID=<uuid> /storage/cache ext4 defaults 0 0
```

# Container Volumnes 

# Container settup
One `mongo` container in each server. There are `cici-mongo1`, `cici-mongo2`, `mongo3`, where they are primary, secondary and arbiter architechture. The arbiter will live on server `name` since it does not hold any data. 
The name of the replica set is `rs0`.   

Use `mongodb://cici-mongo1,cici-mongo2,<host3>/?replicaSet=rs0` to access the replica set.

## Settup/update procedure
The `docker run` command will create new instance, so if you already have an instance please refer to start/stop section
```bash
docker pull mongo
docker stop <mongoX>
docker rm <mongoX>
docker run -p 27017:27017 --name <mongoX> mongo mongod --replSet rs0
```   
## List instances
```bash
docker container --all
```

## Start/Stop an instance 
```bash
docker start <mongoX>
docker stop <mongoX>
```


# Mongo authentication

## Replicate ser internal/membership authentication
When using DB autehntication internal.membership authentication is mandatory.    
<deatails here>


