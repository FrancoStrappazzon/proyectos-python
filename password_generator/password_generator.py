#generador de contraseñas
#!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

import random

chars = '!#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
password = ''

lenght_pw = int(input("Que longitud quiere para su contraseña: "))

for char in range(lenght_pw):
    password += random.choice(chars)
    
print(password)