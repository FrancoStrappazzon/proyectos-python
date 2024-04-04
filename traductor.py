from translate import Translator

translator = Translator(from_lang='spanish', to_lang='english')

texto = input("Que quieres traducir? :")

respuesta = translator.translate(texto)

print(respuesta)