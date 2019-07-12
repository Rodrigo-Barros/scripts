#!/usr/bin/python
#! _*_ encoding:utf-8 _*_

from os import system, listdir, popen, stat
from time import strftime, localtime, sleep

return_code = system('sudo mount /dev/sda3 /media/rodrigo/88CC5795CC577C7E')
if return_code == 16 or return_code == 4096:
	#volume já mountado
	print (system('cp -r "/home/rodrigo/Documentos/Planilhas" "/media/rodrigo/88CC5795CC577C7E/Exchange Data"'))
	print (system('sudo umount -l /media/rodrigo/88CC5795CC577C7E'))
else:
	#pasta nao existente e volume nao montado
	system('mkdir /home/rodrigo/88CC5795CC577C7E')
	system('sudo mount /dev/sda3 /home/rodrigo/88CC5795CC577C7E')
	system('cp -r "/home/rodrigo/Documentos/Planilhas/" "/home/rodrigo/88CC5795CC577C7E/Exchange Data"')
	print (system('sudo umount -l /home/rodrigo/88CC5795CC577C7E'))
	system('rmdir /home/rodrigo/88CC5795CC577C7E')

