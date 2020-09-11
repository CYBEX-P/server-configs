# resize root filesystem if its tiny
```bash
# check if we need to do this
# find the one that says ubuntu
# if it has a size of 4GB  you probably want to increase it
df -h

# get the logical volume to increase, get the path of the one that says ubuntu and replace on the next commands
sudo lvs
# increase logical volume(aka the logical disk size), by adding some gigs up to a total of 200GB(total possible)-4GB(current)= 
sudo lvextend -L+46G /dev/mapper/ubuntu--vg-ubuntu--lv

# increase size of filesystem, this is done in current root fs
# warning: this does it in the live system, failure here means loss of the OS and any data in this partition
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
# verify that it worked
df -h
```
