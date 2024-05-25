from managing_manufacturers_brands.manufacturer_brand import *
from managing_manufacturers_brands.action_functions import * 


df = pd.DataFrame({'urgent':list_urgente,
                   'buy':list_compro,
                   'change':list_cambio,
                   'sell':list_vendo,
                   'price':list_price,
                   'gift':list_regalo,
                   'search':list_busco,
                   'repair':list_reparar,
                   'parts':list_piezas,
                   'synt_brand':list_brand,
                   'description':texto_descriptivo_salida,
                   'city':list_city,
                   'published':list_published,
                   'expire':list_expire,
                   'date_scrapped':date_scrapped,
                   'seen':list_times_seen
                  },index = list(range(1,len(texto_descriptivo_salida)+1)))