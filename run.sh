#!/bin/bash

#cd "$(dirname "$0")";
#CWD="$(pwd)"
#echo $CWD

cd /home/vineeth/configs/prefixes/
/usr/bin/python3 prefix_update.py
/usr/sbin/service bird6 reload
