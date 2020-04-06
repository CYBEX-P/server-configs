# TODO
[TODO.md](TODO.md)   

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
|logs|/var/logs/cybexp/|LVM raid TODO|
|configs / module configs|/etc/cybexp/|locally main drive|  