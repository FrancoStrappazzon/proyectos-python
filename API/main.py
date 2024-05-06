from fastapi import FastAPI
from pydantic import BaseModel  #Sireve para manipular y validar datos

#Creo un objeto de la clase FastAPI
app = FastAPI()

#Con BaseModel valido que los atributos (titulo,autor,pagina y editorial) sean del tipo de dato que especifico
class Libro(BaseModel):
    titulo : str
    autor : str
    pagina : int
    editorial : str
    

#ruta para la API
#http://127.0.0.1:8000  ruta raiz

@app.get('/')   #Cuando alguien llame un get a esa ruta se ejecuta la funcion de abajo
def index():
    return {"message":"Hola como andas?"}

#Agrego una nueva ruta para otra funcion
@app.get('/Libros/{id}')
def mostrar_libro(id: int):
    return {"data":id}


#Creo una nueva ruta para la validacion de datos
@app.post('/Libros')
def insertar_libro(libro : Libro): 
    return {"message": f'Libro {libro.titulo} ha sido insertado'}



#PARA EJECUTAR LA API uvicorn main:app --reload