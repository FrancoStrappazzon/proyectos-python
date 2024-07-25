# Crea un programa que invierta el orden de una cadena de texto
#  sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def invertir_cadena(cadena):
    longitud = len(cadena)
    texto_invertido = ''
    for i in range(longitud -1, -1, -1):
        texto_invertido += cadena[i]
        
    return texto_invertido

print(invertir_cadena("Como estas?"))