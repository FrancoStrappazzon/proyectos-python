# Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.


def esAnagrama(palabra1, palabra2):
    #ordeno las letras alfabeticamente
    palabra1_ordenada = sorted(palabra1.lower())
    palabra2_ordenada = sorted(palabra2.lower())
    
    #Si es la misma palabra retorno false
    if palabra1.lower() == palabra2.lower():
        return False
    else:
        
        if palabra1_ordenada == palabra2_ordenada:
            return True
        else:
            return False

    
print(esAnagrama("AmoR", "ROma"))