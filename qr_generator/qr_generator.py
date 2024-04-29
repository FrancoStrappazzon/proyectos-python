#Obtengo el QR que corresponde a una URL y creo una pagina web

import qrcode
import streamlit as st

#path en donde se va a almacenar el QR
filename = "E:\\FRANCO\\Proyectos_PYTHON\\nuevo_repo\\proyectos-python\\qr_generator\\qr_code.png"

def generate_qr_code(url,filename):
    #creo el objero
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L ,
        box_size = 10,
        border = 4
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    #genero la imagen y la guardo
    img = qr.make_image(fill_color ="black", back_color = "white")
    img.save(filename)
    
#Creo la aplicacion web
st.set_page_config(page_title = "QR Code Generator", page_icon = "E:\\FRANCO\\Proyectos_PYTHON\\nuevo_repo\\proyectos-python\\qr_generator\\qr_icono.png", layout= "centered")
st.image("E:\\FRANCO\\Proyectos_PYTHON\\nuevo_repo\\proyectos-python\\qr_generator\\qr_icono.png",use_column_width=True)
st.title("QR Code Generator")
    
url = st.text_input("Enter the URL: ")
    
if st.button("Generate QR Code"):
     #llamo a la funcion
    generate_qr_code(url,filename)
    st.image(filename,use_column_width=True)
    #abro la imagen y doy la posibilidad de descargarla
    with open(filename,"rb") as f: 
        image_data = f.read()
    download = st.download_button(label = "Download QR", data = image_data, file_name="qr_generated.png")
    
#Para correr el programa: streamlit run qr_generator\\qr_generator.py