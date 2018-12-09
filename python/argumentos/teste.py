import urllib2
import os
from termcolor import colored
provider = "http://177.234.151.251/~"

apiJSPath = "%sbichobrasil/goupsistema/assets/js" % (provider)


files = [
    {
        "name":"consumers.js",
        "content":""
    },
    {
        "name":"application.js",
        "content":""
    },
    {
        "name":"artigo.js",
        "content":""
    },
    {
        "name":"categoria.js",
        "content":""
    },
    {
        "name":"produto.js",
        "content":""
    },
]

def checkFiles():
    for i in range(5):
        try:
            urllib2.urlopen("%s/%s" % (apiJSPath,files[i]['name']))
            print(colored("[Ok]","white","on_green"))
        except urllib2.URLError as e:
            print(e)

