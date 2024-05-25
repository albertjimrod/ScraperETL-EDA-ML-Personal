import time                     # This module provides various time-related functions.
import random                   # This module implements pseudo-random number generators for various distributions.
import requests                 # Is an elegant and simple HTTP library for Python


main_url='https://www.hispasonic.com'



def download_ads(main_url, diccionario_enlaces):

    for enlace in diccionario_enlaces:

        # sampling interval
        time.sleep(random.uniform(1, 4))       
        page = requests.get(main_url + enlace) # https://www.hispasonic.com/anuncios/polyend-tracker/1057403.html

        # filter for extracting
        enlace = enlace.split("/")  

        # name ad
        enlace = enlace[2]         

        # Open a file in write mode ("w+"). If the file doesn't exist, it's created. If it already exists, it is overwritten
        with open(enlace + '.html',"w+") as f: 
            #Write to the file that was opened earlier (f). page.text
            f.write(page.text)
        
        print(enlace)