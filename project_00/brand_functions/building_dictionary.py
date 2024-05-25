

marcas_nombres = []

def sint_word(sintex):
    marcas_nombres.append(sintex)
    return [marcas_nombres[-1]]

def sint_more_word_rep(sintex):
    marcas_nombres.append(sintex)
    return marcas_nombres[-1]


dict_funct = {"sint_word":sint_word,
            "sint_more_word_rep":sint_more_word_rep
}


def build_manufacturers_dictionary():
    dict_marca = {}
    tag_mark = ''

    for marcas in lista_sintes:
        if len(marcas) == 1:
            if marcas[0] not in dict_marca:
                tag_mark = 'sint_word'
                brand = marcas[0]
                ret = dict_funct[tag_mark](brand)
                
                dict_marca[brand] = ret
                return dict_marca
                #print("x")
                
        elif len(marcas) > 1:                           # aqui la marca tiene este formato: ['0', 'coast']
            if marcas[0] not in dict_marca:
                tag_mark = 'sint_word'
                #print(marcas[0])
                #print(marcas[1])

            
                ret = dict_funct[tag_mark](marcas[1])
                dict_marca[marcas[0]] = ret

            elif marcas[0] in dict_marca:
                tag_mark = 'sint_more_word_rep'
                ret = dict_funct[tag_mark](marcas[1])
                dict_marca[marcas[0]].append(ret)
                #print("x")