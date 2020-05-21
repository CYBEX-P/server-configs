# TODO

- [ ] do [this](https://unix.stackexchange.com/a/503064) to the input manager 

## All servers (where aplicable)

- [ ] make log stored in LVM instead of local drive
   - [ ] cic-dev
- [x] settup fstab
- [x] mount log partition under `/storage//cybexp/`
- [x] change permissions to allow group `cybexp` to write 
- [ ] settup email config `/etc/cybexp/email.conf`



## cici-dev 

- [ ] deploy input:
   - [x] put code in `opt` 
   - [ ] settup email config
   - [x] plugin configs:   
      - [x] setup local config file unser `/etc/cybex/input/static-config.conf`
      - [ ] setup backend config module `rs0`
   - [x] setup socket location `/run/cybexp/inputs/`
   - [x] setup api key `/etc/cybexp/input/api-config.conf`
      -[x] set read only by system user `cybexp-input`
   - [x] install service unit file 
   - [x] enable service 
   - [x] setup api key `/etc/cybexp/input/api-config.conf`

- [x] deploy API
   - [x] enable `raw` endpoint
   - [x] add backend db URI
   - [x] enable commented endpoints

- [x] deploy cache db
   - [x] deploy docker mongo standalone
   - [x] configure
   - [ ] enable autehntication
      - [ ] add admin user
      - [ ] add other users
         - [ ] API
         - [ ] archive

## mongo 1-2 and arbiter(on mongo2)

- [x] LVM
- [x] fstab automount
- [x] install docker
- [x] create container
   - [x] arbiter
- [x] install service unit file
- [x] install port forwarding unit files
- [ ] configure `rs0`
- authentication
   - [ ] add admin user 
   - [ ] add other users
      - [ ] api
      - [ ] archive
      - [ ] analitics
   - [ ] enable set memeber authentication
      - [ ] https://docs.mongodb.com/manual/core/security-internal-authentication/#inter-process-auth
      - [ ] https://docs.mongodb.com/manual/tutorial/deploy-replica-set-with-keyfile-access-control/
      - [ ] add key auth to mongo config file
         - [ ] 1
         - [ ] 2
         - [ ] 2A
   - enable auth in mongo configuration file
      - [ ] 1
      - [ ] 2
      - [ ] 2A
