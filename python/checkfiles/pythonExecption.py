# -*- coding: utf-8 -*-

import urllib2
error=0
provider = "http://localhost/"
cliente  = "bichobrasil"
fullUrl  = ("%s%s" % (provider,cliente))
apiUrl   = ("%s/goupsistema/assets/js" % (fullUrl))
url = {
    "consumers":"%s/consumers.js" % apiUrl,
    "application":"%s/application.js" % apiUrl,
    "artigo":"%s/artigo.js" % apiUrl,
    "produto":"%s/produto.js" % apiUrl,
    "produtos":"%s/produtos.js" % apiUrl
}

for x in url:
    try:
        urllib2.urlopen(url[x])
    except urllib2.HTTPError:
        error=1
        print("Arquivo não encotrado:" + url[x])
    except urllib2.URLError as e:
        if provider.find("https") != (-1):
            print ("Problemas Com o certificado SSL")
            error=1
            break
        else:
            print("Servidor Fora de Alcance")
            error=1
            break
if error==1:
    exit(1)
else:
    exit(0)
