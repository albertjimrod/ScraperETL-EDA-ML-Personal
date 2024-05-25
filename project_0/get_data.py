# Comentario o docstring del módulo

# Importaciones de la librería estándar de Python
import os                       # A versatile way to use operating system-dependent functionality.
import sys

# Importaciones de terceros (si tienes alguna)

#import requests                 # Is an elegant and simple HTTP library for Python

#import pandas as pd             # A fast, powerful, flexible and easy to use open source data analysis tool


# Importaciones de módulos locales
from extracting_functions.server_response import response
from extracting_functions.date_for_folders import datefolder
from extracting_functions.extracting_page_number import extracting_content
from extracting_functions.extracting_page_number import extractMax
from extracting_functions.gathering_adlinks import adlinks
from extracting_functions.cleaning_links import htmls_folders
from extracting_functions.cleaning_links import dictionary_filter
from extracting_functions.downloading_ads import download_ads

#from brand_functions.manufacturers import sintes
#from brand_functions.cleaning_manufacturers import cleaning_names



local_path = '/home/ion/Documentos/albertjimrod/hispaok/htmls/'

url = "https://www.hispasonic.com/anuncios/teclados-sintetizadores"
main_url='https://www.hispasonic.com'


accion = ["compro","cambio","vendo","regalo","busco","busca",'reparar','piezas']


def main():
    page = response(url)
    print(page)

    html_folder = datefolder()

    test = extracting_content(page)
    print(test)

    print(extractMax(test)) # visualizo el numero de paginas que hay en la web
    page = extractMax(test)
    print(page)

    local_path = htmls_folders(html_folder)
    print(local_path)

    listado_enlaces = adlinks(page, url)
    print(listado_enlaces)

    diccionario_enlaces=dictionary_filter(listado_enlaces)
    print(diccionario_enlaces)

    download_ads(main_url, diccionario_enlaces)

    # lista_sintes = cleaning_names(sintes)


if __name__ == "__main__":
    main()
