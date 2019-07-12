#!/usr/bin/python

# -*- encoding:utf-8 -*-
import os
from time import localtime, strftime, time, sleep,localtime

class Utils:
    def sorcepath(self, spath):
        return spath

    def destpath(self, dpath):
        return dpath

    def horaFormatada(self):
        move_file_time=localtime(time())
        return strftime("%m/%d/%Y %H:%M:%S", move_file_time)


trinta_dias = 2505600
utils = Utils()
current_time = time()
trash_path = utils.sorcepath("/home/rodrigo/.local/share/Trash/files")
dest_path = utils.destpath("/home/rodrigo/88CC5795CC577C7E/Exchange Data/Backup Files")
files_trash = os.listdir(trash_path)
files_dest = os.listdir(dest_path)
files_gt_30_days = []

for i in range(0, len(files_trash)):
    create_time = os.stat(trash_path + "/" +files_trash[i]).st_ctime
    diff_times = current_time - create_time
    if diff_times > trinta_dias:
        files_gt_30_days.append(files_trash[i])

for i in files_dest:
    for j in files_gt_30_days:
        if i == j:
            files_gt_30_days.remove(j)

if len(files_gt_30_days) > 0:
    for i in files_gt_30_days:
        date_and_hour = strftime('%d/%m/%Y %H:%M:%S',localtime())
        os.system('echo "%s %s" >>  "%s/log"' % (date_and_hour, i, dest_path))
        copy_result = os.system("cp -r '%s/%s' '%s' " % (trash_path, i,dest_path))
        if(copy_result != 0):
            os.system("notify-send 'Trash-Backup:' 'erro ao copiar o arquivo: %s'" % i)
        else:
            continue
else:
    exit(0)

