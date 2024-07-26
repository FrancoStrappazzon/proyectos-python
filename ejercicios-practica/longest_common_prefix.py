#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

def longCommonPrefix(palabras):
    prefijo = ""
    resultado = ""
    for letra in palabras[0]:
        prefijo += letra
        for palabra in palabras:
            if palabra.startswith(prefijo):
                continue
            else:
                return resultado
        resultado =prefijo
        
    return resultado

palabras = ["flower", "flow","flight"]
palabras2 = ["perro", "gato", "elefante"]
print(longCommonPrefix(palabras))