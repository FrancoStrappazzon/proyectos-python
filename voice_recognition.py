#Instalo speechRecognition con pip install SpeechRecognition
#instalo pyttsx3 con pip install pyttsx3

import speech_recognition as sr
import webbrowser   #Libreria para abrir el navegador web
import pyttsx3  #Sirve para obtener la interfaz de sintesis de voz a texto

recognizer = sr.Recognizer()

maquina = pyttsx3.init()


def talk():
    mic = sr.Microphone()
    
    with mic as source:
        
        audio = recognizer.listen(source)   #variable para escuchar el microfono
        
    text = recognizer.recognize_google(audio, language ='ES')

    print(f'Has dicho: {text}')
    return text.lower()

if 'amazon' in talk():    #Si yo dije amazon hablando
    maquina.say('Que quieres comprar en amazon?')
    maquina.runAndWait()
    text = talk()
    #abro el navegador
    webbrowser.open(f'https://www.amazon.es/s?k={text}')
    
# if 'MercadoLibre' in talk():
#     maquina.say('Que quieres comprar en mercado libre?')
#     maquina.runAndWait()
#     text = talk()
#     webbrowser.open(f'https://listado.mercadolibre.com.ar/{text}')