#!/bin/bash

domain='serveo.net'
log_file_name='git_server.log'
interval=120

function baixarSites() {
 for i in /etc/apache2/sites-enabled/*;
 do
    IFS="/" read -a filename <<< "${i}"
    IFS="." read -a sitename <<< "${filename[4]}"
    echo ${sitename[0]}
    if [ ${filename[4]} = "000-default.conf" ];then
	echo "ola"
    else
      wget https://${sitename[0]}.$domain -O /dev/null
      if [ $? = 0 ];then
        date +"%d/%m/%Y ás %H:%M: Baixando site: $sitename" >> $log_file_name
      fi
    fi
 done
 #echo "listar sites ativos e enviar para o download"
}


while true;
do
 ps aux | grep "[s]erveo" >> /dev/null
 serveo_is_up=$?
 sleep $interval
 if [ $serveo_is_up = 0 ]
 then
    date +"%d/%m/%Y ás %H:%M: serveo está rodando" >> $log_file_name
    baixarSites >> $log_file_name
 else
    date +"%d/%m/%Y ás %H:%M: serveo não está rodando" >> $log_file_name
 fi
done

