# -*- coding:utf-8 -*-

from os import system, listdir, getcwd, chdir

partition = "/home/rodrigo/88CC5795CC577C7E"
symbolic_link_to_disc = "/dev/sda3"

def desmontar():
	system("sudo umount -l %s" % partition)
	system("rmdir %s" % partition)
		# system("notify-send 'Trash-Backup:' 'ainda existem arquivos na pasta %s tome uma atitude \nsaindo do script...' " % partition)
		# system("nemo %s" %partition)

def montar():
	system("mkdir -p %s" % partition)
	error_code = system("sudo mount %s %s" % (symbolic_link_to_disc, partition))
	#if error_code == 10 or error_code == 21:
		#system('ntfsfix %s' % symbolic_link_to_disc)
