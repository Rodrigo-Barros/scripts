#!/usr/bin/python

# -*- encoding:utf-8 -*-
from os import system, popen, listdir
from time import sleep
from my_extensions import desmontar, montar

ntfs_partition = "/home/rodrigo/88CC5795CC577C7E"
# Recovery_folder = "%s/Exchange Data/Backup Files" % ntfs_partition
check_if_path_exists = system('ls %s' % ntfs_partition)
if check_if_path_exists == 0:
	montar()
	system("python date.py")
	desmontar()
	exit(0)
else:
	montar()
	system("python date.py")
	desmontar()
	exit(0)