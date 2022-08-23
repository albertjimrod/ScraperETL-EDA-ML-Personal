import requests               # Is an elegant and simple HTTP library for Python
from bs4 import BeautifulSoup # library for pulling data out of HTML and XML files
import re                     # regular expressions operations
import pandas as pd           # A fast, powerful, flexible and easy to use open source data analysis tool
import os                     # A versatile way to use operating system-dependent functionality.
import datetime as dt         # module for manipulating dates and times.
import time


os.chdir('/home/ion/Documentos/albertjimrod/personal_projects/hispasonic/htmls')

os.getcwd() # checking path

# por defecto todo se vende a menos que alguna de estas acciones esten en el titular

accion = ["compro","cambio","vendo","regalo","busco","busca",'reparar','piezas']

accesorios = ["maleta","flightcase","sonidos","rack","enracado","enrackado","racks"]

instrumento = ['sintetizador','piano','teclado','modulo']
                

sintes = {'000': ['000'], '2hp': ['2hp'], '4ms': ['4ms'], 'acces': ['acces'], 'access': ['access'], 'acidlab': ['acidlab'], 'acl': ['acl'], 'akai': ['akai'], 'alembic': ['alembic'], 'alesis': ['alesis'], 'allen&heath': ['allen&heath'], 'analogaudio1': ['analogaudio1'], 'arp': ['arp'], 'arturia': ['arturia'], 'asm': ['asm'], 'atomosynth': ['atomosynth'], 'axoloty': ['axoloty'], 'balaguer': ['balaguer'], 'baloran': ['baloran'], 'befaco': ['befaco'], 'behringer': ['behringer'], 'bitbox': ['bitbox'], 'boss': ['boss'], 'bubblesound': ['bubblesound', 'instruments'], 'buchla': ['buchla'], 'böhm': ['böhm'], 'casio': ['casio'], 'charvel': ['charvel'], 'chronograf': ['chronograf'], 'clavia': ['clavia', 'electro', 'lead', '3', '4', 'micro', 'modular', 'rack', 'stage', 'wave'], 'coast': ['coast'], 'corsynth': ['corsynth'], 'cosmotronic': ['cosmotronic'], 'cre8audio': ['cre8audio'], 'crumar': ['crumar'], 'cyclone': ['cyclone', 'analogic'], 'deepmind': ['deepmind', '12', '6'], 'delptronics': ['delptronics'], 'dexibell': ['dexibell'], 'digitack': ['digitack'], 'divkid': ['divkid'], 'doepfer': ['doepfer'], 'dreadbox': ['dreadbox'], 'dubreq': ['dubreq'], 'dynacord': ['dynacord'], 'e-mu': ['e-mu'], 'e-rm': ['e-rm'], 'e:m:c': ['e:m:c'], 'electribe': ['electribe'], 'electrosmith': ['electrosmith'], 'electrovoice': ['electrovoice'], 'elektron': ['elektron'], 'elka': ['elka'], 'emc': ['emc'], 'emu': ['emu'], 'endorphin': ['endorphin.es'], 'endorphines': ['endorphin.es'], 'ensoniq': ['ensoniq'], 'eowave': ['eowave'], 'epiphone': ['epiphone'], 'eurorack': ['eurorack'], 'eventide': ['eventide'], 'evh': ['evh'], 'evolver': ['evolver'], 'farfisa': ['farfisa'], 'fender': ['fender'], 'fishman': ['fishman'], 'five12': ['five12'], 'fodera': ['fodera'], 'formanta': ['formanta'], 'fretlight': ['fretlight'], 'friedman': ['friedman'], 'futuresonus': ['futuresonus'], 'gator': ['gator'], 'gemini': ['gemini'], 'generalmusic': ['generalmusic'], 'gibson': ['gibson'], 'gieskes': ['gieskes'], 'godin': ['godin'], 'gotharman': ['gotharman'], 'grayscale': ['grayscale'], 'gretsch': ['gretsch'], 'guild': ['guild'], 'hammond': ['hammond'], 'hartmann': ['hartmann'], 'hexinverter': ['hexinverter'], 'hofner': ['hofner'], 'hypersynth': ['hypersynth'], 'höfner': ['höfner'], 'ibanez': ['ibanez'], 'ik': ['ik'], 'instruo': ['instruo'], 'intellijel': ['intellijel', 'designs'], 'iomega': ['iomega'], 'isla': ['isla'], 'jackson': ['jackson'], 'jaspers': ['jaspers'], 'jomox': ['jomox'], 'joranalogue': ['joranalogue'], 'kawai': ['kawai'], 'kenton': ['kenton'], 'ketron': ['ketron'], 'klavis': ['klavis'], 'knobula': ['knobula'], 'komplete': ['komplete'], 'korg': ['korg'], 'kramer': ['kramer'], 'kurzweil': ['kurzweil'], 'l-1': ['l-1'], 'lakland': ['lakland'], 'livid': ['livid'], 'lmntl': ['lmntl'], 'm-audio': ['m-audio'], 'make': ['make', 'noise'], 'malekko': ['malekko', 'heavy', 'industry'], 'maschine': ['maschine'], 'mellotron': ['mellotron'], 'mfb': ['mfb'], 'miditech': ['miditech'], 'modal': ['modal', 'electronics'], 'models': ['models'], 'modor': ['modor'], 'modular': ['modular'], 'modulus': ['modulus'], 'monome': ['monome'], 'moog': ['moog'], 'mordax': ['mordax'], 'mosaic': ['mosaic'], 'mpc': ['mpc'], 'mrseri': ['mrseri'], 'mutant': ['mutant'], 'neutron': ['neutron'], 'nord': ['2', 'electro', 'lead', '3', '4', 'micro', 'modular', 'rack', 'stage', 'wave'], 'novation': ['novation'], 'numark': ['numark'], 'oberheim': ['oberheim'], 'octatrack': ['octatrack'], 'paratek': ['paratek'], 'pearl': ['pearl'], 'peavey': ['peavey'], 'percussa': ['percussa'], 'polyend': ['polyend'], 'polygraf': ['polygraf'], 'prs': ['prs'], 'qu-bit': ['qu-bit', 'electronix'], 'quasimidi': ['quasimidi'], 'qubit': ['qubit'], 'quiklok': ['quiklok'], 'rhodes': ['rhodes'], 'rickenbacker': ['rickenbacker'], 'roland': ['roland'], 'roli': ['roli'], 'rossum': ['rossum'], 'sanson': ['sanson'], 'schecter': ['schecter'], 'sensel': ['sensel'], 'sequentix': ['sequentix'], 'shakmat': ['shakmat', 'modular'], 'simmons': ['simmons'], 'soma': ['soma'], 'sonicware': ['sonicware'], 'soundforce': ['soundforce'], 'soundmachines': ['soundmachines'], 'spector': ['spector'], 'sputnik': ['sputnik'], 'squarp': ['squarp'], 'squier': ['squier'], 'ssff': ['ssff'], 'stanton': ['stanton'], 'steinberger': ['steinberger'], 'sterling': ['sterling'], 'strymon': ['strymon'], 'studiologic': ['studiologic', 'music'], 'supercritical': ['supercritical'], 'swissonic': ['swissonic'], 'synamodec': ['synamodec'], 'synthrotek': ['synthrotek'], 'synthstrom': ['synthstrom'], 'synthtech': ['synthtech'], 'tascam': ['tascam'], 'taylor': ['taylor'], 'technos': ['technos'], 'transient': ['transient'], 'trogotronic': ['trogotronic'], 'tubbutec': ['tubbutec'], 'u-he': ['u-he'], 'vermona': ['vermona'], 'virus': ['virus'], 'viscount': ['viscount'], 'voicas': ['voicas'], 'volca': ['volca'], 'vox': ['vox'], 'vpme.de': ['vpme.de'], 'waldorf': ['waldorf'], 'warwick': ['warwick'], 'washburn': ['washburn'], 'wurlitzer': ['wurlitzer'], 'yamaha': ['yamaha'], 'yocto': ['yocto'], 'zoom': ['zoom'], '0': ['coast'], '1010': ['music'], 'a-v-p': ['synth'], 'acid': ['rain'], 'addac': ['system'], 'after': ['later'], 'aion': ['modular'], 'ajh': ['synth'], 'allen': ['&'], 'alm': ['busy'], 'alright': ['devices'], 'analogue': ['solutions', 'systems'], 'atomo': ['synth'], 'audio': ['damage'], 'audiophile': ['circuits'], 'bastl': ['instruments'], 'black': ['corporation'], 'blackhole': ['cases'], 'blue': ['lantern'], 'boredbrain': ['music'], 'charlie': ['lab'], 'circuit': ['abbey'], 'club': ['of'], 'custom': ['made'], 'dave': ['jones', 'smith', 'instruments'], 'delta': ['music'], 'denon': ['dj'], 'dnipro': ['modular'], 'e': ['mu'], 'elby': ['designs'], 'electronic': ['music'], 'emblematic': ['systems'], 'empress': ['effects'], 'erica': ['synths'], 'ernie': ['ball'], 'erogenous': ['tones'], 'eskatonic': ['modular'], 'esp': ['ltd'], 'exodus': ['digital'], 'frap': ['tool', 'tools'], 'frequency': ['central'], 'future': ['retro', 'sound'], 'graph': ['tech'], 'hinton': ['instruments'], 'industrial': ['music'], 'io': ['instruments'], 'john': ['bowen'], 'kilpatrick': ['audio'], 'koma': ['elektronik'], 'line': ['6'], 'linn': ['electronics'], 'logan': ['electronics'], 'low-gain': ['electronics'], 'lzx': ['industries'], 'macbeth': ['studio'], 'manhattan': ['analog'], 'manikin': ['electronic'], 'meng': ['qi'], 'michigan': ['synth'], 'micro': ['modular'], 'modbap': ['modular'], 'mutable': ['instruments'], 'nano': ['modules'], 'native': ['instruments'], 'noise': ['engineering'], 'orthogonal': ['devices'], 'patching': ['panda'], 'pioneer': ['dj'], 'pittsburgh': ['modular'], 'plankton': ['electronics'], 'poly': ['effects'], 'ppg': ['ppg'], 'qu': ['bit'], 'radikal': ['technologies'], 'random': ['source'], 'ritual': ['electronics'], 'schlappi': ['engineering'], 'sequential': ['circuits'], 'special': ['waves'], 'spectral': ['audio'], 'steady': ['state'], 'studio': ['electronics'], 'synthesis': ['technology'], 'system': ['80'], 'tall': ['dog'], 'tasty': ['chips'], 'teenage': ['engineering'], 'tenderfoot': ['electronics'], 'tesseract': ['modular'], 'tiptop': ['audio'], 'traveler': ['guitar'], 'udo': ['audio'], 'uno': ['synth'], 'verbos': ['electronics'], 'waves': ['grendel'], 'wersi': ['music'], 'winter': ['modular'], 'wmd': ['ssf'], 'worng': ['electronics'], 'xaoc': ['devices'], 'xor': ['electronics'], 'zeppelin': ['design'], 'zlob': ['modular']}


os.chdir('/home/ion/Documentos/albertjimrod/personal_projects/hispasonic/htmls') # working directory mapping

compare = ''
texto_marca_compuesta =''
texto_descriptivo = ''
list_temp = []

list_compro = []
list_cambio = []
list_vendo = []


list_regalo = []
list_busco = []
list_busca = []
list_reparar = []
list_piezas = []
list_urgente = []



list_brand = []
list_descripcion = []    
texto_descriptivo_salida = []                                      # esto es lo que se vera como contenido del anuncio

lista_palabras_para_eliminar = []



def func_compro(clave_func_dict):

    if list_compro[-1] == "0":
        list_compro.remove('0')
        list_compro.append("1")
    else:
        pass


def func_cambio(clave_func_dict):
    if list_cambio[-1] == "0":
        list_cambio.remove('0')
        list_cambio.append("1")

    else:
        pass

def func_vendo(clave_func_dict):
    if list_vendo[-1] == "0":
        list_vendo.remove('0')
        list_vendo.append("1")
    else:
        pass


func_dict = {
    "compro":func_compro,
    "cambio":func_cambio,
    "vendo":func_vendo,
    "vende":func_vendo,

    
}

def remove_compro(clave_func_dict):
    #list_compro.append(clave_func_dict
    list_compro.remove(clave_func_dict)


rmv_func = {"compro":remove_compro
}


def urgente():
    list_urgente.remove('0')
    list_urgente.append("1")



def eliminar_signos(txt):
    descripcion = txt.replace(":"," ")
    descripcion_1 = descripcion.replace("("," ")
    descripcion_2 = descripcion_1.replace(")"," ")
    descripcion_3 = descripcion_2.replace("/"," ")
    descripcion_4 = descripcion_3.replace("."," ").lower()
    descripcion_5 = descripcion_4.split()                   # aqui es cuando descripcion_4 se convierte en una lista como descripcion_5
    return descripcion_5

marca_del_sinte = ''

### Inicio


for pagina_anuncio in os.listdir('.'):                                  # '.' hace referencia al directorio donde está apuntando en htmls
    if "cambio" in pagina_anuncio:                               #compro-cambio

        with open(pagina_anuncio, 'r') as pagina_bruto:

            pagina_analizar = pagina_bruto.read()
            soup = BeautifulSoup(pagina_analizar, 'html.parser')

            node = soup.find('h1') 

        if  node is not None:                                           # con esto evito que me salte un error relacionado con None
            descripcion = node.text 
            descripcion = eliminar_signos(descripcion)
            print(descripcion)

            list_cambio.append("0")
            list_compro.append("0")
            list_urgente.append('0')
            list_vendo.append('0')
            list_brand.append("-")
            
            for word_1 in descripcion:
                if word_1 in accion:
                    func_dict[word_1](word_1)
                    lista_palabras_para_eliminar.append(word_1)
                                                                        
                elif word_1 in compare:
                    list_temp.append(word_1)
                    
                    for marca_sinte in list_temp:
                        marca_del_sinte += marca_sinte + ' '
                        #list_brand.append(marca_del_sinte)
                        lista_palabras_para_eliminar.append(marca_sinte) # con esto borro el nombre compuesto del sinte en la descripcion.

                        
                    
                    #list_temp.clear()
                    
                    #if list_brand == "-":
                        
                    list_brand.remove("-")
                    list_brand.append(marca_del_sinte)

                    compare = '' # en esta variable estaria la segunda parte del nombre por eso la limpio aqui.
                   
                elif word_1 in sintes:
                    if len(sintes[word_1]) >= 2:
                        list_temp.append(word_1)
                        compare = sintes[word_1]
                        #lista_palabras_para_eliminar.append(compare)

                    #list_brand.append(marca_del_sinte)

                    elif (len(sintes[word_1]) == 1) and (len(list_brand) !="-"):
                        list_brand.remove("-")
                        list_brand.append(word_1)
                        

                        #else:
                            #lista_palabras_para_eliminar.append(word_1)
                            #list_brand.remove("-")


            duplicates = [element for element in lista_palabras_para_eliminar if lista_palabras_para_eliminar.count(element) > 1]
            unique_duplicates = set(duplicates)
            unique_duplicates = ''.join(unique_duplicates)

            print(unique_duplicates)

            if unique_duplicates:
                urgente()
                

            for eliminar in lista_palabras_para_eliminar:
                descripcion.remove(eliminar)

            for palabras in descripcion:
                texto_descriptivo += palabras + ' '

            
            texto_descriptivo_salida.append(texto_descriptivo)

            print(f"urgente: {list_urgente[-1]} compro: {list_compro[-1]} cambio: {list_cambio[-1]} vendo: {list_vendo[-1]} marca: {list_brand[-1]} descripcion: {texto_descriptivo_salida}")
            

            print("\t","\t",texto_descriptivo)
            texto_descriptivo =''

            lista_palabras_para_eliminar.clear()

            
df = pd.DataFrame({'urgente':list_urgente,
                   'compro':list_compro,
                   'cambio':list_cambio,
                   'vendo':list_vendo,
                   'marca':list_brand,
                   'descripcion':texto_descriptivo_salida
                  },index = list(range(1,len(texto_descriptivo_salida)+1)))

print(df)


