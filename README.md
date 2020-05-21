# TODO
[TODO.md](TODO.md)   

# Connecting to mongo backend instance rs0
## from inside firewall or in cici-dev
`monogodb://monog1,monog2,monog2:27020/?replicaSet=rs0`   
if using authentication:   
`monogodb://<user>:<pass>@monog1,monog2,monog2:27020/?replicaSet=rs0&authSource=admin`   

cici-dev its already configured, unlike outside of the network (see below).
## from outside of the firewall or cici-dev

to connect you need two things:
1. edit dns hosts file and add `cici-dev`, `mongo1` and `mongo2` to it, using the ips of the interfaces bound in previous step
2. make ssh tunnels and bind them to a different local interface

do the following:   

edit local `/etc/hosts` (windows has one on another location) and add the following:   
```
<cici-dev IP> cici-dev
127.0.0.5 mongo1
127.0.0.6 mongo2
```
then execute
```bash
ssh -L 27017:127.0.0.1:27017 \
   -L 127.0.0.5:27017:127.0.0.5:27017 \
   -L 127.0.0.6:27017:127.0.0.6:27017 \
   -L 127.0.0.6:27020:127.0.0.6:27020 \
   -L 5000:127.0.0.1:5000 \
   cici-dev
```
then use:
`monogodb://monog1,monog2,monog2:27020/?replicaSet=rs0`   
if using authentication:   
`monogodb://<user>:<pass>@monog1,monog2,monog2:27020/?replicaSet=rs0&authSource=admin`   



# Services
Systemctl have been setup to aid management   
Rememeber that some services have restart upon exiting, to stop use `systemctl stop <service name>`, else it will restart.

|server|service name|purpose|executable location|notes|-|
|:----:|:----------:|:-----:|:-----------------:|:---------------:|:-|
|cici-dev|cachedb.service|Stop/Starp cachedb mongodb instance|docker|-||
||inputManager.service|Stop/Start input manager service|/opt/cybexp/input/|will try to grafully stop input plugings upon systemctl stop request, else will always restart. SIGTERM will only stop inputmanager, SIGUSR1 will stop all the plugings+manager( may restart).||
||cybexp-api.service|Stop/Start API module|/opt/cybexp/api|||
|||||||
|Mongo1|backenddb.service|Stop/Start backend mongo instance(ps rs0)|docker|||
|Mongo2|backenddb.service|Stop/Start backend mongo instance(ps rs0)|docker|||
|Mongo2|backenddbA.service|Stop/Start backend mongo instance(a rs0)|docker|||   

   
### Services Location
`/etc/systemd/system/`
# Virtual ENVIRONMENT
Python3 virtual environgment is located at `/opt/cybexp/env`   


# Configs
ALL configs are under `/etc/cybexp`   


# Connectting to mongo-db instances
Mongo ports are only accesible via internal network, make ssh tunels to the following ports:   

|mongo instance|remote host|remote port|
|:------------:|:-----------:|:-------:|
|Cache DB (s)|127.0.0.1|27017|
|Mongo1 (PS)|127.0.0.1|27020|
|Mongo2 (PS)|127.0.0.1|27021|
|Mongo3 (s)|127.0.0.1|27022|   

Multiple `-L` can be used on one command:   
`ssh -L <local port>:<remote host>:<remote port> <user>@<cici-dev>`   
EX:   
`ssh -L 27017:127.0.0.1:27017 cici-dev`   

Then, connect to them via `localhost` or `127.0.0.1` using `local port`.





## Editing Mongo settings:
On the server that hosts the mongo instance:   
```bash
sudo docker ps --all # get the name of the docker container, not image
sudo docker exec -it <container name> mongo [args]

```
where `[args]` is either nothing for `cache-db` instance or `mongodb://mongo1,mongo2,mogno2:27020/?replicaSet=rs0` for the replica set mongo1-3, do not connect via mongo3 instance since it is not data bearing you can not autehnticate.   


## Storage
Look at how each server is setup in detail on the servers forder of this repo.   

|what|location|type|
|:--:|:------:|:--:|
|cache-db|/storage/cache-db|LVM raid|
|backend db|/storage/backend|LVM raid| 
|backend db arbiter|/storage/backend/arbiter|LVM raid| 
|logs|/storage/logs/|LVM RAID|
|configs / module configs|/etc/cybexp/|locally main drive|  
