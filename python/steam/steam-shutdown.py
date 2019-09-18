#!/usr/bin/env python3

from time import sleep
from steamfiles import acf
import os
import glob

# diretorio steam apps alterar conforme o necessário
steamAppsDir = "/home/rodrigo/.steam/steam/steamapps/"
os.chdir(steamAppsDir)
gamefiles = []

def getData(f,m):
    arquivo = open(f,m)
    return acf.load(arquivo)
timeout = int(input("\ninforme a quantidade de tempo em segundos para desligar o computador apos a conclusao dos downloads, \nse não \
quiser informar um valor, aperte enter para continuar: ") or 60)
for file in glob.glob("*.acf"):
    openedFile = getData(steamAppsDir + file,'r')
    baixado = openedFile['AppState']['BytesDownloaded']
    total = openedFile['AppState']['BytesToDownload']
    if(baixado != total):
        gamefiles.append(file)

for x in range(len(gamefiles)):
    while True:
        try:
            opened = getData(steamAppsDir + gamefiles[x],'r')
            baixado = int(opened['AppState']['BytesDownloaded'])
            total = int (opened['AppState']['BytesToDownload'])
            jogo = opened['AppState']['name']
            if(total == baixado and total > 0):
                break
            elif (total == 0 and baixado == 0):
                print("Inicio do download")
                sleep(1)
                continue
            else:
                porcentagem = (baixado / total) * 100
                print("Download do titulo %s, %.2f%% %.2f MB de %.2f MB" % (jogo,porcentagem,baixado/1000000,total/1000000))
                sleep(1)
        except KeyError:
            continue
if not gamefiles:
    print("nenhum Download em andamento saindo do script")
    exit(0)
print (timeout)
sleep(timeout)
os.system("poweroff")
exit()
