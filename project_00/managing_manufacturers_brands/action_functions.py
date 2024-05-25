

def func_compro(clave_func_dict): 
    if list_compro[-1] == "0":
        list_vendo.pop(-1)
        list_vendo.append("0")
        list_compro.pop(-1)
        list_compro.append("1")
    else:
        pass
    
def func_cambio(clave_func_dict):
    if list_cambio[-1] == "0":
        list_vendo.pop(-1)
        list_vendo.append("0")
        list_cambio.pop(-1)
        list_cambio.append("1")
        #list_price.append("0")
    else:
        pass

def func_vendo(clave_func_dict):
    if list_vendo[-1] == "0":
        list_vendo.pop(-1)
        list_vendo.append("1")
    else:
        pass

def func_regalo(clave_func_dict): 
    if list_regalo[-1] == "0":
        list_vendo.pop(-1)
        list_vendo.append("0")
        list_regalo.pop(-1)
        list_regalo.append("1")
    else:
        pass

def func_busco(clave_func_dict):  # if looking for, then is not a sell...
    if list_busco[-1] == "0":
        list_vendo.pop(-1)
        list_vendo.append("0")
        list_busco.pop(-1)
        list_busco.append("1")
    else:
        pass

def func_reparar(clave_func_dict):
    if list_busco[-1] == "0":
        list_reparar.pop(-1)
        list_reparar.append("1")
    else:
        pass

def func_piezas(clave_func_dict):
    if list_busco[-1] == "0":
        list_piezas.pop(-1)
        list_piezas.append("1")
    else:
        pass

def func_rebaja(clave_func_dict):
    if list_rebaja[-1] == "0":
        list_vendo.pop(-1)
        list_vendo.append("0")
        list_rebaja.pop(-1)
        list_rebaja.append("1")
    else:
        pass

def func_oferta(clave_func_dict):
    if list_oferta[-1] == "0":
        list_oferta.pop(-1)
        list_oferta.append("1")
    else:
        pass

func_dict = {                                                        # function dictionary
    "compro":func_compro,
    "cambio":func_cambio,
    "vendo":func_vendo,
    "vende":func_vendo,
    "regalo":func_regalo,
    "busco":func_busco,
    "busca":func_busco,
    "reparar":func_reparar,
    "piezas":func_piezas,
    "rebajado":func_rebaja,
    "rebaja":func_rebaja,
    "oferta":func_oferta
}

def remove_compro(clave_func_dict):
    #list_compro.append(clave_func_dict
    list_compro.remove(clave_func_dict)

#rmv_func = {"compro":remove_compro}


def urgente():                                                       # if some "accion" word is repeated on description, means urgency
    list_urgente.remove('0')
    list_urgente.append("1")

def eliminar_signos(txt): 
    # cleaning text
    txt = txt.lower()
    description = txt.replace(":"," ")
    descripcion = description.replace(";"," ")
    descripcion_1 = descripcion.replace("("," ")
    descripcion_2 = descripcion_1.replace(")"," ")
    descripcion_3 = descripcion_2.replace("/"," ")
    descripcion_4 = descripcion_3.replace("."," ")
    descripcion_5 = descripcion_4.split()
    return descripcion_5



def default_atributes():                                            # default actions, means all is selling, if not then function will be called.
    """
    Añade el contenido por defecto a las diferentes listas con las que se trabaja en cada fila.
    """
    list_cambio.append("0")
    list_compro.append("0")
    list_urgente.append("0")
    list_vendo.append("1")
    list_regalo.append("0")
    list_reparar.append("0")
    list_piezas.append("0")
    list_busco.append("0")
    list_brand.append("-")




def synt_brand(descripcion, accion,lista_palabras_para_eliminar, compare, list_brand,list_descripcion ):
    for word_1 in descripcion:                                  
        if word_1 in accion:                                     
            func_dict[word_1](word_1)                           
            return lista_palabras_para_eliminar.append(word_1)

        elif word_1 in compare:   
            list_temp.append(word_1)                            

            for marca_sinte in list_temp:                       
                marca_del_sinte += marca_sinte + ' '             
                return lista_palabras_para_eliminar.append(marca_sinte) 

            list_brand.pop(-1)
            return list_brand.append(marca_del_sinte)

            compare = '' 

        elif word_1 in dict_marca:                        
            size_brand = len(dict_marca[word_1])

            if ((size_brand == 1) and (list_brand != "-")) :
                list_brand.pop(-1)
                return list_brand.append(word_1)
                break

            elif ((size_brand == 1) and (list_brand == "-")) :
                return list_descripcion.append(word_1)

            if ((size_brand >= 1) and (list_brand == "-") and (size_brand != 0)) :  
                list_descripcion.append(word_1) 
                list_brand.pop(-1) 
                x = dict_marca[word_1]
                return list_brand.append(x)
                break

            elif size_brand >= 1:                               
                compare = dict_marca[word_1]                    
                list_temp.append(word_1)                         

            elif list_brand != "-":                              
                return list_descripcion.append(word_1)

        marca_del_sinte = ''
    list_temp.clear()


def urgente(lista_palabras_para_eliminar):
    duplicates = [element for element in lista_palabras_para_eliminar if lista_palabras_para_eliminar.count(element) > 1] # Detecta caracteres repetidos dentro de 'lista_de_palabras_para_eliminar' siempre que el tamaño de la lista sea superior a 1
    unique_duplicates = list(set(duplicates))                                                                             # Muestra el elemento duplicado
    size_unique_duplicates = len(duplicates)                                                                              # Muestra la longitud de esos dos elementos sumados 'size_unique_duplicates'
    if size_unique_duplicates > 3:                                                                                        # Si la longitud 'size_unique_duplicates' es superior a 3 entonces llama a la función urgente.
        urgente()                                                                                                         # Pinta un 1 en la columna urgente

    for eliminar in lista_palabras_para_eliminar:
        try:
            descripcion.remove(eliminar)                # As actions are identified, and the synth's name is removed from the ad description
        except:
            pass

        
    for palabras in descripcion:                       # The description is traversed after it has been deleted and what remains is entered into a variable 'texto_descriptivo'
        texto_descriptivo += palabras + ' '

    texto_descriptivo_salida.append(texto_descriptivo) # The variable with the content of 'texto_descriptivo' will be the text that will finally remain as a description in the final csv

    texto_descriptivo =''                              # I write the content of the variable 'texto_descriptivo' on top of it by way of a reset.

    return texto_descriptivo

def price(soup,list_price):
    try:
        # Try to find the element with the 'ad-price' class and extract the text
        price = soup.find('div', class_='ad-price').text
        # Quita el símbolo € del texto del precio
        price = price.replace("€", "")
        
    except AttributeError:
        # If the item is missing, assign "N/A" to the price variable
        price = 0
        # Delete the last item in list_price if it exists (there may be an error if the list is empty)

    finally:
        # Add the price value (either the found price or "N/A") to list_price
        return list_price.append(price)


def user_name(soup, list_user):
    user = soup.find('div',class_='col-lg-7').a.text
    return list_user.append(user)


def city(soup, list_city):
    city = soup.find('div',class_='col-lg-7').div.strong.text
    return list_city.append(city)


def published(soup,list_original ):
    publish = ' '
    try:
        # Find the div element with the class 'col-lg-7' and extract the text from the inner div
        published = soup.find('div', class_='col-lg-7').div.text.split()[-5:-2]

        for indx in published:
            list_original.append(indx)  # Add indx to the list list_original

            # Check to see if there's a forward slash on the item
            if '/' in indx:
                # indx = indx.replace("/", "-")  # Reemplaza "/" por "-"
                DD = indx[0:2]  # Extract the first two characters (day)
                MM = indx[3:5]  # Extract the next two characters (month)
                YYYY = indx[6:]  # Extract the remaining characters (year)
                publish = f'{YYYY}/{MM}/{DD}'  # Create the date string in YYYY-MM-DD format
                #print("YYYY", publish)
            

            # If "hace" is in the element, it means that it is no longer a date that is extracted, but the reference to how long ago.
            elif 'hace' in indx:
                #indx = indx.replace("/", "-")  # Replace "/" por "-"
                a = published.index(indx)  # Gets the index of the current item

                # Combine the numerical value and the unit of time (2 hours ago, 5 days ago, 2 weeks ago...)
                publish = published[a + 1] + ' ' + published[a + 2] # <- With this I get the format of: 1 week ago or 19 hours ago...
                #  I put the Publish content into the dataframe, later I'll modify that annoying format
                #print("publish", publish)

    except (AttributeError, IndexError):
                # If exceptions occur due to attribute or index issues, assign "N/A" to the publish variable
                publish = " "
                
    finally:
            # Add the final value of "publish" to the list list_published
            return list_published.append(publish)



def expire():
        expire = soup.find('div',class_="expira").text.split()[1]
        #expire = expire.replace("/","-")
        DD = expire[0:2]
        MM = expire[3:5]
        YYYY = expire[6:]
        date_corrected = f'{YYYY}-{MM}-{DD}'
        return list_expire.append(date_corrected)


def times_seen(soup,list_times_seen, lista_palabras_para_eliminar ):
    seen = soup.find('div',class_="expira").text.split()[4]
    return list_times_seen.append(seen), lista_palabras_para_eliminar.clear()