import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

#Establezco la conexion con la base de datos
db_conn = sqlite3.connect("productos.db")
db_cursor = db_conn.cursor()

#Creo la tabla productos si es que no existe
db_cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            price REAL NOT NULL,
                            quantity INTEGER NOT NULL
                        )''')

db_conn.commit()

#Con BaseModel valido los datos de entrada y salida de los endpoints
class Products(BaseModel):
    name : str
    price : float
    quantity : int


#Objeto de la clase Fastapi
app = FastAPI()

#Ruta raiz
@app.get('/')
def root():
    return "Bienvenido a la API de gestion de productos"

#ruta para agregar productos
@app.post('/products')
def crear_producto(name: str, ):
    return "Producto creado exitosamente"

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