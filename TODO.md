# TODO

- [ ] do [this](https://unix.stackexchange.com/a/503064) to the input manager 


## All servers (where aplicable)

- [ ] make log stored in LVM instead of local drive
   - [ ] cic-dev
- [ ] settup fstab
- [ ] mount log partition under `/var/log/cybexp/`
- [ ] change permissions to allow group `cybexp` to write 
- [ ] settup email config `/etc/cybexp/email.conf`



## cici-dev 

- [ ] deploy input:
   - [ ] put code in `opt` 
   - [ ] settup email config
   - [ ] plugin configs:   
      - [ ] setup local config file unser `/etc/cybex/input/static-config.conf`
      - [ ] setup backend config module `rs0`
   - [ ] setup socket location `/run/cybexp/inputs/`
   - [ ] setup api key `/etc/cybexp/input/api-config.conf`
      -[ ] set read only by system user `cybexp-input`

   - [ ] install service unit file 
   - [ ] enable service 
   - [x] setup api key `/etc/cybexp/input/api-config.conf`

- [x] deploy API


## mongo 1-2 and arbiter(on mongo2)

- [ ] LVM
- [ ] fstab automount
- [ ] install docker
- [ ] create container
   - [ ] arbiter
- [ ] install service unit file
- [ ] install port forwarding unit files
- [ ] configure `rs0`
