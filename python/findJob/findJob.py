# -*- coding: utf-8 -*-
import urllib 
from urllib import parse
from urllib import request
from bs4 import BeautifulSoup
from time import sleep
import re
import sys
import os

help = 'Ajuda:\n\n'
help += '--clear limpa os arquivos vagas.txt e vagas_excluidas.txt\n'
help += '--exit  pode ser usuado com qualquer comando para finalizar a execução do script\n'
help += '--show  Mostra as vagas incluidas com base no filtro após a busca do script'
show_in_editor=False
# arguments
if len(sys.argv) > 1:
    for arg in sys.argv:
        if arg == '--clear':
            os.system('rm vagas.txt vagas_excluidas.txt')
        if arg == '--help':
            print(help)
            exit(0)
        if arg == '--exit':
            exit(0)
        if arg == '--show':
            show_in_editor=True

# main program
base_url='https://www.indeed.com.br'
print('Digite as informações a seguir para fazer a sua consulta')
job = input('Digite o cargo desejado (Padrão Programador PHP): ') or 'Programador PHP'
city = input('Digite a cidade desajada (Padrão São Paulo, SP): ') or 'São Paulo, SP'
number_of_pages_to_look_resuts = int(input('Digite quantas páginas você deseja vasculhar no site (Padrão 10 páginas): ') or 10)
timeout_between_pages = int(input('Digite uma valor em segundos para esperar entre uma página e outra (Padrão 5 segundos): ') or 5)
filters = open("filters.txt","r").readlines()

page_index = 0

print('cargo selecionado %s' % job)
print('cidade escolhida %s' % city)

def check_regex(response_array):
    found_filters=0
    for word in filters:
        regex = re.search(word.strip(),response_array,re.IGNORECASE)
        if hasattr(regex,'pos'):
            #print('a palavra %s foi encontrada' % word)
            found_filters+=1

    if found_filters > 0:
        return False
    else:
        return True

def get_job(page_number):
    global page_index 
    for i in range(0, page_number):
        if i == 0:
            filters = '/jobs?q=%s&l=%s' % (job.replace(' ','+').lower(), parse.quote_plus(city))
        else:
            page_index = i*10
            filters = '/jobs?q=%s&l=%s&start=%s' % (job.replace(' ','+').lower(), parse.quote_plus(city),page_index)

        request_url = base_url + filters

        query_url = urllib.request.urlopen(request_url)

        soup = BeautifulSoup(query_url, 'html.parser')

        resultados = soup.find(id='resultsCol')
        
        #test = soup.find(id='resultsCol')
        for info in resultados.find_all('div',{'class':'jobsearch-SerpJobCard'}):

            empresa=info.span.text.strip()
            print( 'Empresa: %s' % empresa )

            cidade = info.find('span',{'class':'location'})
            if hasattr(cidade,'text') == False:
                cidade = info.find('div',{ 'class':'location' })
            cidade = cidade.text.strip()

            print( 'Cidade: %s' % cidade )

            emprego=info.find('h2',{'class':'title'}).text.strip()
            print( 'Emprego: %s' % emprego )
            
            link=('%s%s' % (base_url,info.h2.a['href']))
            print( 'link %s' % link )

            desc = info.find('div',{'class':'summary'}).text.strip()
            print ( "Descrição: %s" % desc )


            print('\n')

            if ( check_regex(desc) and check_regex(emprego) and check_regex(empresa) and check_regex(link) and check_regex(cidade) ):
                f = open('vagas.txt','a+')
                f.write('Vaga: %s \nEmpresa: %s \nCidade: %s \nDescrição: %s \nLink: %s \n\n' % (emprego,empresa,cidade,desc,link))
                f.close()
            else:
                f = open('vagas_excluidas.txt','a+')
                f.write('Vaga: %s \nEmpresa:%s \nCidade: %s \nDescrição: %s\ \nLink: %s \n\n' % (emprego,empresa,cidade,desc,link))
                f.close()
            

        page_index = 1 if page_index == 0 else (page_index/10)+1
        print('página %s' % int(page_index))

        if page_index == page_number and show_in_editor:
            os.system('less vagas.txt')
            exit(0)
        sleep(timeout_between_pages)

get_job(number_of_pages_to_look_resuts)
