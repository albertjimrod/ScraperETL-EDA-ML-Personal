"""
En la identificacion de los nombres de los sintetizadores suceden varias cosas:

- la primera es que el nombre de la maquina sea unico por lo que eso no es un problema
- la segunda es que el nombre sea compuesto, por ejemplo: "Dave Smith". 
    
    La solucion que he encontrado para este caso ha sido el uso de un diccionario, en el que se han introducido el mayor numero de sintetizadores
    Asi cuando la variable que estamos leyendo del texto coincide con llave del diccionario lo que sucede es que obtenemos el nombre completo del sintetizador

- la tercera cosa que puede darse es que el nombre sea un nombre compuesto, y que la primera parte sea compartida por otro fabricante:
    Analogue Solutions y Analogue Systems.

    Se puede apreciar que la tecnica anterior no es suficiente.
    La solución propuesta es de nuevo la utilización del diccionario pero teniendo en cuenta que la palabra que es comun a los dos fabricantes sea la clave del diccionario
    y que lo que corresponde a valor sea un lista, con las variaciones pertinentes.

    cuando el for para por el texto que queremos analizar, este identifica si la longitud que devuelve el diccionariom es superior a 1, 
    En caso de ser asi lo que sucede es que el contenido 
    asigna a una variable llamada "compare" y cuando el for vuelve a leer el texto que a nosotros nos interesa comprueba si existe o no coincidencia con lo que contiene la 
    variable "compare" y a una lista temporal, si es asi. la palabra coincidente se introduce en una lista temporal
"""




sint1 = {"analogue":"systems",
    "analogue":"solutions"}

sint2 = {"systems":"analogue",
    "solutions":"analogue"}

sint3 = {"analogue":["solutions","systems"]}

descrip = ['analogue', 'systems', 'woggeblug', '+', 'morphagene', '+', 'optomix']

#print(sint["make"])
texto_marca_compuesta =''
compare = ''

list_temp = []
list_brand = []

for idx in descrip:                                 # 1. empieza el for / 7. el indice ya tiene el segundo nombre del sinte
    if idx in compare:                              # 2. si el indice del for coincide con una variable llamada compare que de inicio vale '', pasa al elif
                                                    # 8. al comparar el indice con la variable que contiene la coincidencia 
        list_temp.append(idx)                       # 9. Guardo la segunda coincidencia en la lista temporal
        for palabritas in list_temp:                # 10. Convierto los elementos de la lista en una cadena de texto
            texto_descriptivo += ' '+ palabritas

        list_brand.append(texto_marca_compuesta)    # 11 asigno la cadena a la marca del sinte
        compare = ''                                # 12. limpio el valor de la variable compare y texto_marca_compuesta
        list_temp.clear()                           # 13. limpio el contenido de la lista temporal

        
            
    elif idx in sint3:                              # 3. si el indice esta contenido en el diccionario sint3
        if len(sint3[idx]) > 1:                     # 4. y la longitud del valor de la clave del diccionario es mayor que 1, significa que tengo dos posibles marcas
            list_temp.append(idx)                   # 5. meto esa primer coincidencia en una lista temporal

            print(sint3[idx])
            compare = sint3[idx]                    # 6. guardo la lista de posibles coincidencias en una variable, la que inicialmente valia '' 
        

        
print(texto_descriptivo)


