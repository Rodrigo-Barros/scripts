#!/usr/bin/python

# -*- encoding:utf-8 -*-
from os import system, popen, listdir
from time import sleep
from my_extensions import desmontar, montar, symbolic_link_to_disc

ntfs_partition = "/home/rodrigo/88CC5795CC577C7E"
# Recovery_folder = "%s/Exchange Data/Backup Files" % ntfs_partition
check_if_path_exists = system('ls %s' % ntfs_partition)
if check_if_path_exists == 0:
	#montar()
	system("python /home/rodrigo/.config/scripts/python/backup-files/date.py")
	desmontar()
	exit(0)
else:
	system('sudo ntfsfix %s' % symbolic_link_to_disc)
	montar()
	system("python /home/rodrigo/.config/scripts/python/backup-files/date.py")
	desmontar()
	exit(0)