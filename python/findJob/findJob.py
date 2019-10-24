# encoding: utf-8
import urllib 
from bs4 import BeautifulSoup
from time import sleep
import re

base_url='https://www.indeed.com.br'
print('Digite as informações a seguir para fazer a sua consulta')
job = input('Digite o cargo desejado (Padrão Programador PHP): ')
city = input('Digite a cidade desajada (Padrão São Paulo): ')
number_of_pages_to_look_resuts = int(input('Digite quantas páginas você deseja vasculhar no site (Padrão 10 páginas): ') or 10)
timeout_between_pages = int(input('Digite uma valor em segundos para esperar entre uma página e outra (Padrão 5 segundos): ') or 5)
filters = open("filters.txt","r").readlines()


page_index = 0

if job == '':
    job = 'Programador PHP'
if city == '':
    city = 'São Paulo'
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
            filters = '/jobs?q=%s&l=%s' % (job.replace(' ','+').lower(), urllib.parse.quote_plus(city))
        else:
            page_index = i*10
            filters = '/jobs?q=%s&l=%s&start=%s' % (job.replace(' ','+').lower(), urllib.parse.quote_plus(city),page_index)

        request_url = base_url + filters

        query_url = urllib.request.urlopen(request_url)

        soup = BeautifulSoup(query_url, 'html.parser')

        resultados = soup.find(id='resultsCol')
        
        #test = soup.find(id='resultsCol')
        for info in resultados.find_all('div',{'class':'jobsearch-SerpJobCard'}):
            empresa=info.span.text.strip()
            print('empresa')
            print(info.span.text)

            emprego=info.find('div',{'class':'title'}).text.strip()
            print('emprego')
            print (emprego)
            
            link=('%s%s' % (base_url,info.div.a['href']))
            print('link')
            print(link)

            desc = info.find('div',{'class':'summary'}).text.strip()
            print ("descrição")
            print(desc)            

            if ( check_regex(desc) and check_regex(emprego) ):
                f = open('vagas.txt','a+')
                f.write('Vaga: %s \nEmpresa: %s \nDescrição: %s \nLink: %s \n\n' % (emprego,empresa,desc,link))
                f.close()
            else:
                f = open('vagas_excluidas.txt','a+')
                f.write('Vaga: %s \nEmpresa:%s \nDescrição: %s\ \nLink: %s \n\n' % (emprego,empresa,desc,link))
                f.close()
            

        page_index = 1 if page_index == 0 else (page_index/10)+1
        print('página %s' % int(page_index))

        sleep(timeout_between_pages)

get_job(number_of_pages_to_look_resuts)
