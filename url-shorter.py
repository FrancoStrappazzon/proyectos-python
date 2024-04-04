#Este codigo sirve para acortar una direccion de URL y crea una aplicacion web 

import pyshorteners
import streamlit as st  #Libreria para crear la pagina web

def acortar_url(url):
    #Creo un objeto y le llamo a la funcion para acortar la url
    s = pyshorteners.Shortener()
    #invoco al metodo para acortar la url
    url_acortada = s.tinyurl.short(url)
    return url_acortada

#Creamos la app web con streamlit
st.set_page_config(page_title= "Acortador de URL", layout="centered")
st.image("Imágenes\url_imagen.jpg",use_column_width=True)
st.title("Acortador de URL")
url=st.text_input("Ingrese la URL")
#Si se aprieta el boton llamo a la funcion para acortar la URL
if st.button("Generar nueva URL"):
    st.write("URL acortada: ", acortar_url(url))
