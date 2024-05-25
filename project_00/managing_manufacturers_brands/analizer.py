from managing_manufacturers_brands.manufacturer_brand import *
from managing_manufacturers_brands.action_functions import * 

accion = ["compro","cambio","vendo","regalo","busco","busca",'reparar','piezas']

### Inicio


for pagina_anuncio in os.listdir('.'): # Read the contents of the directory with a for in the current "." folder
    with open(pagina_anuncio, 'r') as pagina_bruto:
        pagina_analizar = pagina_bruto.read()                        # Converts to the 'pagina_analizar' object with python's read() method
        soup = BeautifulSoup(pagina_analizar, 'html.parser')         # With Beautifulsoup, the pagina_analizar is parsed with the 'html.parser' and a variable named soup is passed
        node = soup.find('h1')                                       # All the contents of the H1 tag are searched within SOUP, and that content is fed into the NODE variable.

    if  node is not None:                                            # avoiding skipping an error related to None. An if is used to check that "node" is not empty using the condition "if node is not None"
        descripcion = node.text                                      # Using the.text method, I extract the text from Node and pass it to the Description variable
        descripcion = eliminar_signos(descripcion)                   # function that removes punctuation ;,:,(,),/... and lowercase the text
                             
        default_atributes()                                          # Calling the function default_atributes().
        
        # --- synt_brand
        lista_palabras_para_eliminar, list_brand, list_descripcion = synt_brand(descripcion, accion,lista_palabras_para_eliminar, compare, list_brand,list_descripcion )
    
        # --- urgente
        texto_descriptivo = urgente(lista_palabras_para_eliminar)

        # --- price
        list_price = price(soup,list_price)
        
        # --- user name
        list_user = user_name(soup, list_user)
        
        # --- city
        city(soup, list_city)

        # --- published
        published(soup,list_original )

        # --- expire 
        expire(soup,list_expire)
    
        # --- times_seen
        times_seen(soup,list_times_seen, lista_palabras_para_eliminar )
