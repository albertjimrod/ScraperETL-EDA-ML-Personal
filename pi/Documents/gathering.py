import requests               # Is an elegant and simple HTTP library for Python
from bs4 import BeautifulSoup # library for pulling data out of HTML and XML files
import re                     # regular expressions operations
#import pandas as pd           # A fast, powerful, flexible and easy to use open source data analysis tool
import os                     # A versatile way to use operating system-dependent functionality.
import datetime as dt         # module for manipulating dates and times.
import time                   # This module provides various time-related functions.
import random       

# Enter the address and see the response from the server.

url = "https://www.hispasonic.com/anuncios/teclados-sintetizadores"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
# soup <- all site is stored in this variable

unordered_list = soup.find('ul', class_='pagination') # into variable unordered_list

unordered_list = unordered_list.contents # tag's children available in a list called .content. from variable to list

test = str(unordered_list[-2])

def extractMax(input):
     # get a list of all numbers separated by
     # lower case characters
     # \d+ is a regular expression which means
     # one or more digit
     # output will be like ['100','564','365']
    numbers = re.findall(r'\d+',input)
     # now we need to convert each number into integer
     # int(string) converts string into integer
     # we will map int() function onto all elements
     # of numbers list
    numbers = map(int,numbers)
    return max(numbers) # returns a int number


page_numbers = extractMax(test)


links_ads = []        # all the ads on the page
listado_enlaces = []  # all the links on the page

pattern="([0-9]{4,9})" # filtering all links with number, that mean choosing the page number related to and ad.

for pagina in range(page_numbers, 0, -1):
    url = "https://www.hispasonic.com/anuncios/teclados-sintetizadores/pagina{pagina}".format(pagina=pagina)
    #print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')


    for link in soup.find_all('a'):       # filter everything that is a link on soup variable
        links_ads.append(link.get('href'))
        fecha = soup.find_all('span', class_='miniicon miniicon-date')


    for link_ad in links_ads:                   # of those links what I do is stay with what ends in number
        if re.search(pattern, link_ad):
            listado_enlaces.append(link_ad)



# Obtener la fecha actual
fecha_actual = dt.datetime.now()


nombre_directorio = fecha_actual.strftime("%Y-%m-%d")  # Formato: Año-Mes-Día

# Crear el directorio si no existe
if not os.path.exists(nombre_directorio):
    os.makedirs(nombre_directorio)
    print(f"Directorio '{nombre_directorio}' creado.")



diccionario_enlaces = {} # dict
listado_marcas = []      # synth_brand

brand_pattern = r"((?<=anuncios\/)[1-9][a-z]{1,})|((?<=anuncios\/)[a-z]{1,})" # filter brand regex

for enlace in listado_enlaces:
    if enlace not in diccionario_enlaces:
        try:
            marca = re.search(brand_pattern, enlace).group()
            diccionario_enlaces[enlace] = marca
        except AttributeError:
            #marca = re.search(brand_pattern, enlace)
            pass # voy a ver si funciona, lo que aprendi del try except



main_path='https://www.hispasonic.com'
#local_path = '/home/ion/Documentos/albertjimrod/hispaok/htmls/'


for enlace in diccionario_enlaces:
    # sampling interval
    time.sleep(random.uniform(1, 4))
    page = requests.get(main_path + enlace) # https://www.hispasonic.com/anuncios/polyend-tracker/1057403.html
    # filter for extracting
    enlace = enlace.split("/")
    # name ad
    enlace= enlace[2]
    # Open a file in write mode ("w+"). If the file doesn't exist, it's created. If it already exists, it is overwritten
    with open(nombre_directorio + '/' + enlace + '.html',"w+") as f:
        #Write to the file that was opened earlier (f). page.text
        f.write(page.text)

    #print(nombre_directorio + '/' + enlace)




