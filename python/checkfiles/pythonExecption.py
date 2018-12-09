# -*- coding: utf-8 -*-

import urllib2
from termcolor import colored
import os
error=0
provider = "http://localhost/"
cliente  = "bichobrasil"
siteroot  = "/var/www/html/%s" % cliente
apiFolder = "%s/goupsistema/assets/js" % siteroot
fullUrl  = ("%s%s" % (provider,cliente))
apiUrl   = ("%s/goupsistema/assets/js" % (fullUrl))
url = {
    "consumers":"%s/consumers.js" % apiUrl,
    "application":"%s/application.js" % apiUrl,
    "artigo":"%s/artigo.js" % apiUrl,
    "produto":"%s/produto.js" % apiUrl,
    "produtos":"%s/produtos.js" % apiUrl
}

files = {
    "consumers.js":{
        "content":""
    },
    "application.js":{
        "content":""
    }
}

def mkStructure():
    try:
        os.chdir("%s" % apiFolder)
    except os.OSError:
        os.makedirs("%s" % apiFolder)
        for i in files:
            file=open(apiFolder + "/" + files[x],"w")
            file.write(file[x]['content'])

for x in url:
    try:
        urllib2.urlopen(url[x])
        print colored("[Ok]","white","on_green") + " " + url[x]
    except urllib2.HTTPError:
        error=1
        print(colored("[Erro]","white","on_red") + url[x] + " Arquivo não encotrado")
    except urllib2.URLError as e:
        if provider.find("https") != (-1):
            print (colored("[Erro]","white","on_red")+" O site informado tem problemas com o certificado SSL")
            error=1
            break
        else:
            print(colored("Erro","white","on_red")+" Servidor Fora de Alcance")
            error=1
            break
if error==1:
    exit(1)
else:
    exit(0)
