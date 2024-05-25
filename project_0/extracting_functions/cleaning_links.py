import os
import re                       # regular expressions operations


def htmls_folders(folderdate):

    ruta = '/home/ion/Documentos/albertjimrod/ScraperETL-EDA-ML-Personal/project_0/{}'.format(folderdate)
    print(f"Ruta del directorio formada: {ruta}")

    if os.path.exists(ruta):
        try:
            os.chdir(ruta)
            return ruta
        except OSError:
            print(f"El directorio {ruta} existe.")

    if not os.path.exists(ruta):
        try:
            os.makedirs(ruta)
            print(f"Directorio '{ruta}' creado.")
            os.chdir(ruta)
            return ruta

        except PermissionError:
            print(f"No tienes permisos para acceder al directorio {ruta}")

        except Exception as e:
            print(f"Se produjo un error al cambiar el directorio: {e}")




def dictionary_filter(listado_enlaces):
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

    return diccionario_enlaces
