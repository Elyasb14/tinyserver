#!/bin/bash

crontab -l > crontab_new 
echo "0 0 * * * python3 /home/ebianchi/tinyserver/server/sftp.py" >> crontab_new
crontab crontab_new
rm crontab_new