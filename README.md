# Proyecto personal hispasonic.

<img src="READ.jpeg" alt="README" style="width:200px;"/>

## Descripción del proyecto

Este proyecto es muy especial para mí, ya que combina dos de mis pasiones: la música electrónica, los instrumentos musicales y el análisis de datos.

Como apasionado de los instrumentos electrónicos pensé que sería interesante recopilar información de la venta de instrumentos de segunda mano de la web de hispasonic y ver que conocimiento era capáz de extraer a modo de reto personal, así que me puse manos a la obra: 


El proyecto se compone de varias partes:

- [from_web_to_csv](https://github.com/albertjimrod/personal_proj_hispasonic/blob/main/from_web_to_csv.ipynb) : Proceso que he seguí para la **captura** y **limpieza** de datos de la página web de hispasonic desde cero, fuí avanzando y comprendiendo que camino debía seguir, descubriendo que biblioteca de funciones y que estratégias que debía implementar para condensar esa información de los anuncios en un archivo `*.csv`.

- [from_csv_to_PostgreSQL](https://github.com/albertjimrod/personal_proj_hispasonic/blob/main/from_csv_to_PostgreSQL.ipynb) Este projecto surgió como la necesidad natural de gestionar los datos de manera mas "**real**". En el explico los pasos que van desde la instalación de la base de datos **PostgreSQL** en una máquina con sistema opertivo Linux hasta la carga de los archivos  `.csv` que había ido recopilando en la base de datos.
