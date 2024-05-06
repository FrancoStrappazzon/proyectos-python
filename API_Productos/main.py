from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import connect_to_database, close_database_connection
import sqlite3


#Con BaseModel valido los datos de entrada y salida de los endpoints
class Product(BaseModel):
    name : str
    price : float
    quantity : int


#Objeto de la clase Fastapi
app = FastAPI()


#Dependencia para obtener la conexion con la base de datos
def get_db_connection():
    db_conn = connect_to_database()
    try:
        yield db_conn   #uso yield como generador
        #finally se ejecuta siempre
    finally:
        close_database_connection(db_conn)


#Ruta raiz
@app.get('/')
def root():
    return "Bienvenido a la API de gestion de productos"


#ruta para agregar productos
@app.post('/products', status_code=201) #devuelve el codigo 201 cuando es exitoso
def crear_producto(product: Product, db_conn: sqlite3.Connection= Depends(get_db_connection)):
    try:
        cursor = db_conn.cursor()
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?,?,?)", (product.name, product.price, product.quantity))
        db_conn.commit()
        return {"mensaje:":"Producto creado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el producto: {str(e)}")


#mostrar todos los productos
@app.get('/products')
def obtener_productos():
    return ""


#Mostrar producto por su id
@app.get('/products/{product_id}')
def mostrar_producto(product_id):
    return "producto"


#Actualizar un producto
@app.put('/products/{product_id}')
def actualizar_producto(product_id):
    return "producto actualizado"


#Borrar un producto
@app.delete('/products/{product_id}')
def borrar_producto(product_id):
    return "Producto borrado"




#PARA EJECUTAR LA API uvicorn main:app --reload