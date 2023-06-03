import pandas as pd 
import datetime as dt

df = pd.read_csv("/home/ion/Documentos/albertjimrod/personal_proj_hispasonic/htmls/fixing_feliz_cumple_dataframe.csv")
print(df)

semanas = ['1 semana', '2 semanas', '3 semanas', '4 semanas']
dias = ['1 día', '2 días', '3 días', '4 días', '5 días', '6 días', '7 días']
horas = ['1 hora','2 horas', '3 horas', '4 horas', '5 horas', '6 horas',
        '7 horas','8 horas', '9 horas', '10 horas', '11 horas', '12 horas',
        '13 horas', '14 horas','15 horas', '16 horas', '17 horas', '18 horas',
        '19 horas', '20 horas', '21 horas', '22 horas','23 horas', '24 horas']

minutes=[]
for mint in range(1,61):
    if mint < 2:
        texto = str(mint) + ' minuto'
        minutes.append(texto)
    else:
        texto = str(mint) + ' minutos'
        minutes.append(texto)

def alehop(parameter):
    #https://www.timeanddate.com/date/dateadded.html?d1=12&m1=12&y1=2021&type=sub&ay=&am=&aw=03&ad=&rec=
    
    days_inweek = 7
    
    hoy = dt.datetime.now()
    year=str(hoy.year)
    month=str(hoy.month)
    day=str(hoy.day)

    date_scrapped = day + '/' + month + '/' + year
    #date_scrapped =  '29/05/2022' #str(date_scrapped)
    
    
    current_datetime = dt.datetime.strptime(date_scrapped,"%d/%m/%Y") 
    
    if parameter in semanas:
        num_semana = parameter.split()
        num_semana = int(num_semana[0])
        cambio_semana = semanas[num_semana-1]
        
        dias_semana = (num_semana * days_inweek)
        
        fecha_real_semana = current_datetime - dt.timedelta(dias_semana)
        fecha_real_semana = fecha_real_semana.strftime("%d/%m/%Y")
                
        return df['published'].replace( to_replace = cambio_semana,value = fecha_real_semana) #+ ' semana'

    
    elif parameter in dias:
        num_dia = parameter.split()
        num_dias = int(num_dia[0])
        cambio_dia = dias[num_dias-1]

        fecha_real_dia = current_datetime - dt.timedelta(num_dias)
        fecha_real_dia = fecha_real_dia.strftime("%d/%m/%Y")
        
        a =  df['published'].replace( to_replace = cambio_dia,
                                                    value = fecha_real_dia) #+ ' semana'
        return a

    elif parameter in horas:
        num_hora = parameter.split()
        num_hora = int(num_hora[0]) #print(num_hora)

        
        if parameter != '24 horas':
            hora_real = current_datetime
            hora_real = hora_real.strftime("%d/%m/%Y")
            
            b =  df['published'].replace(to_replace = parameter,value = hora_real)
            return b

        
        elif parameter == '24 horas':
            horas_24 = 1
            hora_real = current_datetime - dt.timedelta(horas_24)
            hora_real = hora_real.strftime("%d/%m/%Y")
            
            c =  df['published'].replace( to_replace = parameter,value = hora_real ) #+ ' semana'
            return c
    
        elif parameter in minutes:
            horas_24 = 1
            hora_real = current_datetime - dt.timedelta(horas_24)
            hora_real = hora_real.strftime("%d/%m/%Y")
                
            d = df['published'].replace( to_replace = parameter,value = hora_real ) #+ ' semana'
            return d
    



df['published'].apply(alehop)

df['published'] = df['published'].apply(alehop)

print(df['published'])