from deep_translator import GoogleTranslator

try:
    texto = input("¿Qué quieres traducir?: ")
    respuesta = GoogleTranslator(source="spanish", target = "english").translate(texto)
    print("Texto traducido: ", respuesta)
except Exception as e:
    print("Ocurrió un error durante la traducción:", e)
