import datetime as dt           # module for manipulating dates and times.
import os


def datefolder():
    fecha_actual = dt.datetime.now()

    nombre_directorio = fecha_actual.strftime('%Y-%m-%d')
    print(nombre_directorio)   
    return nombre_directorio
