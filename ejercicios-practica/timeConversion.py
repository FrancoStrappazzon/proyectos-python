#Dado un string en formato de 12 horas hh:mm:ssAM/PM , convertirlo a uno de formato 24 hs.
#ej : s='08:15:20PM a s='20:15:20' 

from datetime import datetime

def timeConversion(s):
    #analizo el string dado en formato 12 horas. %I es formato 12 horas, %p es AM/PM
    time_obj = datetime.strptime(s, '%I:%M:%S%p')
    #formateo a 24 horas
    return time_obj.strftime('%H:%M:%S')

s= "11:15:22PM"

print(timeConversion(s))