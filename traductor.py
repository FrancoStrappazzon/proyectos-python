from deep_translator import GoogleTranslator

idiomas_permitidos = ["ingles", "portugues", "italiano"]

while True:
    seleccion = input("Seleccione el idioma en el cual quiere su traducción: Inglés, Portugués o Italiano: \n").lower()
    
    if seleccion in idiomas_permitidos:
    
        texto = input("¿Qué quieres traducir?: \n")
    
        try:
            if seleccion == "ingles":
                respuesta = GoogleTranslator(source="spanish", target="english").translate(texto)
            elif seleccion == "portugues":
                respuesta = GoogleTranslator(source="spanish", target="portuguese").translate(texto)
            elif seleccion == "italiano":
                respuesta = GoogleTranslator(source="spanish", target="italian").translate(texto)
        
            print("Texto traducido: ", respuesta)
    
        except Exception as e:
            print("Ocurrió un error durante la traducción:", e)

    elif seleccion not in idiomas_permitidos: 
        print("ERROR, por favor seleccione uno de los idiomas disponibles")
        continue

