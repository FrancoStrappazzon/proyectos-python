# Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
#   - Los signos de puntuación no forman parte de la palabra.
#  - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#   - No se pueden utilizar funciones propias del lenguaje que
#     lo resuelvan automáticamente.
import re

texto = "Hola como estas titan, yo bien aca ando todo bien por suerte."
def cuento_palabra():
    texto_limpio = re.sub(r'[^\w\s]', '', texto)    #Tomo solo los caracteres especiales
    palabras = texto_limpio.lower().split() #minusculas y saco los espacios creando una lista
    
    # Contar ocurrencias de cada palabra con un diccionario
    recuento = {}
    
    for palabra in palabras:
        recuento[palabra] = recuento.get(palabra, 0) + 1
    
    # Imprimir recuento final de palabras
    for palabra, ocurrencias in recuento.items():
        print(f'La palabra "{palabra}" aparece {ocurrencias} veces')
        
cuento_palabra()