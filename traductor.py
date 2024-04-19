from translate import Translator

try:
    translator = Translator(from_lang='spanish', to_lang='english')
    texto = input("¿Qué quieres traducir?: ")
    respuesta = translator.translate(texto)
    print("Texto traducido: ", respuesta)
except Exception as e:
    print("Ocurrió un error durante la traducción:", e)
