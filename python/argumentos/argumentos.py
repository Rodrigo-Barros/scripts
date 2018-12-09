#i *-* coding: utf-8 *-*
import argparse
import os
from termcolor import colored
import urllib2

# -------------------------- functions -----------------------------
def mkStructure(cliente):

    try:
        os.makedirs("%s/%s/goupsistema/assets/js" % (siteroot,cliente))
        for i in range(2):
            file = open(siteroot + "/"+ cliente +"/goupsistema/assets/js/" + files[i]['name'], "w")
            file.write(files[i]['content'].encode('utf-8'))
            file.close()
    except OSError as e:
        print("Houveram erros ao construir a estrutura " + str(e))


def checkFiles():
    print("[status] [file]")
    for i in range(len(files)):
        try:
            url=urllib2.urlopen("%s/%s" % (apiJSPath, files[i]['name']))
            if(url.code == 200):
                print(" " + colored("[ Ok ]","white","on_green")+ "  %s/%s \t\t %s" % (apiJSPath,files[i]['name'],url.code))
            else:
                print(" " + colored("[ Error ]","white","on_red")+ "  %s/%s \t %s" % (apiJSPath,files[i]['name'],url.code))
        except urllib2.HTTPError:
            error = 1
            print (" "+colored("[Erro]", "white", "on_red") + "  %s/%s Arquivo não Encontrado" % (apiJSPath, files[i]['name']))
        except urllib2.URLError:
            if provider.find("https") != (-1):
                print (" " + colored("[Erro]", "white", "on_red") + " O site informado tem problemas com o certificado SSL")
                error = 1
                break
            else:
                print(" "+colored("[Erro]", "white", "on_red") + "  Servidor Fora de Alcance")
                error = 1
                break
# ----------------------------------------------------------------

siteroot = "/var/www/html"
files = [
    {
        "name":"consumers.js",
        "content":"urlBase=\"http://177.234.151.251/~ecosand\""
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
apiPath = "%s/goupsistema/assets/js" % siteroot
provider = "http://177.234.151.251/~"

parser = argparse.ArgumentParser(description='sum the integers at the command line')
parser.add_argument('--check', help='Verifica os arquivos javascript', action='store_true')
parser.add_argument('-C', help='Especifica o nome do cliente para criar as pastas locais')
parser.add_argument('-a', help='Verifica se artigo.php e artigo.js estão criados se não estiverem os cria', action = 'store_true')
parser.add_argument('-c', help='Verifica se categoria.php e categoria.js estão criados se não estiverem os cria', action = 'store_true')
parser.add_argument('-p', help='Verifica se produto.php e produto.js estão criados se não estiverem os cria', action = 'store_true')
parser.add_argument('-host', help='Especifica o site do cliente para verificar se os arquivos da api estão sendo carregados')
parser.add_argument('--config', help='Espefica um arquivo de configuração para o site, ainda em desenvolvimento')
parser.add_argument('--build',help='cria uma pasta para o projeto em: /var/www/html/nomedapasta')

# get all args
args = parser.parse_args()
apiJSPath = "%s%s/goupsistema/assets/js" % (provider, args.C)

if args.check and args.C:
    checkFiles()
elif args.check or args.C:
    print "Informe o comando da seguinte maneira --check -C cliente"

mkStructure(args.build)
