# resize root filesystem if its tiny
```bash
# get the logical volume to increase
sudo lvs
# increase logical volume
sudo lvextend -L+46G /dev/mapper/ubuntu--vg-ubuntu--lv
# increase size of filesystem, this is done in current root fs, careful
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
# verify that it worked
df -h
```