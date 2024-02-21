import subprocess
import datetime

# Obtener la configuración de crontab
crontab_output = subprocess.check_output("crontab -l", shell=True).decode()

# Cálculo del tiempo hasta la próxima ejecución
# Aquí necesitarás analizar la salida de crontab para obtener la configuración

# Supongamos que la configuración es "*/5 * * * *", lo que significa cada 5 minutos
# Puedes calcular el tiempo restante hasta la siguiente ejecución así:
delta = 1  # En este caso, la tarea se ejecuta cada 5 minutos
now = datetime.datetime.now()
next_run = now + datetime.timedelta(minutes=(delta - now.minute % delta))
time_remaining = next_run - now

print(f'Tiempo restante para la próxima ejecución: {time_remaining}')

