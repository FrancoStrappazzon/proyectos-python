#Unifico PDFs desde una pagina web

import streamlit as st 
import PyPDF2


def merge_pdfs(output_path, pdf_documents):
    #funcion de la libreria para unir los pdf
    pdf_merger = PyPDF2.PdfMerger()
    
    for pdf_document in pdf_documents:
        #Agrego cada uno de los pdf
        pdf_merger.append(pdf_document)
    
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)
        
        
    
def main():
    #Imagen para la pagina web
    st.image("E:\\FRANCO\Proyectos_PYTHON\\nuevo_repo\\proyectos-python\\merge_PDFs\\PDF_icono.png")
    st.header("Fusion de PDFs")
    st.subheader('Adjunte archivos PDF para combinar')
    
    attached_pdf = st.file_uploader(label ='', accept_multiple_files= True)
    
    merge_button =st.button(label = "Fusionar archivos PDF")
    
    if merge_button:
        if len(attached_pdf) <= 1:
            
            st.warning("Adjunte mas de un PDF para fusionarlos")
            
        else:
            #Ruta donde quiero que se mande el archivo final
            output_pdf = 'E:\\FRANCO\Proyectos_PYTHON\\nuevo_repo\\proyectos-python\\merge_PDFs\\pdf_final.pdf'
            merge_pdfs(output_pdf, attached_pdf)
            st.success("Los archivos PDF se fusionaron correctamente")
            
            with open(output_pdf, "rb") as file:
                pdf_data = file.read()
                st.download_button(label = 'Descargar PDF fusionado', data= pdf_data, file_name= 'pdf_final.pdf')
                
                
if __name__ == '__main__':
    main()

#Para correr el programa poner en el terminal streamlit run 'merge_PDFs\\merge_pdfs.py