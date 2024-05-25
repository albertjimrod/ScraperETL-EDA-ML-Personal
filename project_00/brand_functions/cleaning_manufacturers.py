

# cleaning names in sintes list.

def cleaning_names(sintes):

    lista_criba = []

    for marca in sintes:
        # Switch to lowercase
        marca = marca.lower()
        if marca not in lista_criba:
            # Filter out the repeated names and put them in another list
            lista_criba.append(marca)


    # split double names in sintes list

    lista_sintes= []

    for marca in lista_criba:
        marca = marca.lower()
        if marca not in lista_sintes:
            marca = marca.split()
            lista_sintes.append(marca)
    
    return lista_sintes

