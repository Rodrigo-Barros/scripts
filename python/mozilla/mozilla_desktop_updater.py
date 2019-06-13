#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
# esse script se destina a atualizar o arquivo firefox.desktop sempre que o mesmo é atualizado para
# para quando clicar com o botão direito do mouse em cima do ícone aparecer o texto "nova janela anônima"

import os
root_dir="/home/rodrigo/.config/scripts/python/mozilla"
cur_firefox_version = os.popen('firefox -v').read().split(" ").pop()
file_old_version=open(root_dir+"/version.txt","rw")
old_firefox_version=file_old_version.read()
file_old_version.close()

if(cur_firefox_version != old_firefox_version):
    print "versão atual do FF:" + cur_firefox_version
    print "versão Anterior do FF:" + old_firefox_version
    print "versões diferentes"
    file_new_version=open(root_dir +"/version.txt","w")
    file_new_version.write(cur_firefox_version)
    file_new_version.close()
    os.system ("cp %s/firefox.desktop /home/rodrigo/.local/share/applications" % (root_dir))
else:
    print "versões iguais saindo do script..."

print "\nfinalizando mozilla-desktop-updater"
exit(0)
