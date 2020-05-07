# info
Setup infomation is pretty much identical to how `cici-dev` was setup, so look [there](../cici-dev/README.md)   


# Modules
Under `/opt/cybexp/`:   
- archive
- analytics

# Users
- system: cybexp-proc, system user that runs the above modules


# Groups 
- cybexp-admin, for real users to be able to access thigs easily
- cybexp-proc, same as cybexp-proc user
- cybexp-module, group that can access cybexp respurces, liel python3 venv at `/opt/cybexp/env`
	- cybexp-proc user is part of this


- 
