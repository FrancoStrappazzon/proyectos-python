#  Escribe un programa que se encargue de comprobar si un número es o no primo.
#  Hecho esto, imprime los números primos entre 1 y 100.

def es_primo(num):
    #si se puede dividir por un num entre 2 y el mismo numero significa que no es primo
    for i in range(2,num-1):
        if num %i ==0:
            return False
    return True
        
def numeros_primos():
    lista_numeros =[]
    for i in range(2,101):
        if es_primo(i):
            lista_numeros.append(i)
    return lista_numeros

print(numeros_primos())