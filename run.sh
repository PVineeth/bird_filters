#!/bin/bash

cd $1
/usr/bin/python3 prefix_update_v6.py
/usr/sbin/service bird6 reload
