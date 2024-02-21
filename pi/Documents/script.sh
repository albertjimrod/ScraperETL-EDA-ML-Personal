#!/bin/bash

python3 ~/Documents/gathering.py & proceso_id=$!

#wait $proceso_id

# Obtener el último directorio creado en el directorio actual
ultimo_directorio=$(ls -td -- */ | head -n 1)

# Contar los elementos dentro del último directorio
cantidad_elementos=$(ls -l "$ultimo_directorio" | grep -v '^total' | wc -l)


# Crear un archivo temporal con el contenido del directorio
archivo_temporal="/tmp/contenido_directorio.txt"
ls -l "$ultimo_directorio" > "$archivo_temporal"
cantidad_elementos >> "$archivo_temporal"

echo "La cantidad de elementos en el último directorio ($ultimo_directorio) es: $cantidad_elementos"

# Enviar el archivo por correo electrónico
mail -s "Contenido del último directorio" -a "$archivo_temporal" albert@datablogcafe.com

