
from bs4 import BeautifulSoup   # library for pulling data out of HTML and XML files
import requests                 # Is an elegant and simple HTTP library for Python
import re                       # regular expressions operations


def adlinks(page_numbers, direccion):

    links_ads = []        # lista que almacena los enlaces a los anuncios
    listado_enlaces = []  # lista que almacena los enlaces a las paginas de los anuncios

    pattern="([0-9]{4,9})" # filtering all links with number, that mean choosing the page number related to and ad.

    for pagina in range(page_numbers, 0, -1): 
        url = "{direccion}/pagina{pagina}".format(pagina=pagina, direccion=direccion)
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        

        for link in soup.find_all('a'):             # filter everything that is a link on soup variable
            links_ads.append(link.get('href'))      # append links into links_ads
            fecha = soup.find_all('span', class_='miniicon miniicon-date')

        
        #  Los anuncios tienen un numero asociado, con 'pattern'
        
        for link_ad in links_ads:                   
            if re.search(pattern, link_ad):
                #print(link_ad)
                listado_enlaces.append(link_ad)

    return listado_enlaces