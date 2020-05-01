# ssh tunnel service
Used to access mongodb backend on cici-dev, example:   
```bash
systemctl start ssh-tunnel@3001:localhost:27017.service
```   
will which uses:   
```bash
ssh -N -R localhost:%i cici-dev
```
so it ends up like:   
```bash
ssh -N -R localhost:3001:localhost:27017 cici-dev
```
which binds cicidev `3001` to `localhost` (mogno1 or 2) to port `27017`,
connecting to `3001` connects to one node on the backed db replica set.    
this is only available to cici-dev for security reasons   

# services names/options
`systemctl <action> ssh-tunnel@<option>.service`   
|option|execute from|
|-|-|
|3001:localhost:27017|cici-mongo1|
|3002:localhost:27017|cici-mongo2|
|3003:localhost:27020|cici-mongo2|


# resources
https://askubuntu.com/questions/48129/how-to-create-a-restricted-ssh-user-for-port-forwarding