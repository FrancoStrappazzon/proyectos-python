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
        #Me conecto con la db
        cursor = db_conn.cursor()
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?,?,?)", (product.name, product.price, product.quantity))
        db_conn.commit()
        return {"mensaje:":"Producto creado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el producto: {str(e)}")


#mostrar todos los productos
@app.get('/products')
def obtener_productos(db_conn : sqlite3.Connection = Depends(get_db_connection)):
    
    try:
        #Me conecto con la db
        cursor = db_conn.cursor()
        #obtengo las filas de la db
        cursor.execute("SELECT name,price,quantity FROM products")
        #devuelve las filas como una lista de tuplas
        rows = cursor.fetchall()
    
    # Transformo las filas en una lista de diccionarios (para devolver como JSON)
        products = []
    
        for row in rows:
            products_dict = {
                "name": row[0],
                "quantity": row[1],
                "price": row[2]
            }
            products.append(products_dict)
    
        return {"products":products}    #Devuelvo el resultado como JSON
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los productos: {str(e)}")


#Mostrar producto por su id
@app.get('/products/{product_id}')
def mostrar_producto(product_id,db_conn : sqlite3.Connection = Depends(get_db_connection)):
    try:
        #Me conecto con la db
        cursor = db_conn.cursor()
        #obtengo las filas de la db
        cursor.execute("SELECT name,price,quantity FROM products WHERE id = ?", (product_id,))
        # Obtengo el resultado de la consulta
        producto= cursor.fetchone()
        
        if producto:
            #Transformo el resultado en un diccionario
            product_dict ={
                "name": producto[0],
                "price": producto[1],
                "quantity": producto[2]
            }
            
        return {"producto":product_dict}    #Devuelvo el resultado como JSON
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los el producto con id: {product_id}: {str(e)}")

#Actualizar un producto
@app.put('/products/{product_id}')
def actualizar_producto(product_id):
    return "producto actualizado"


#Borrar un producto
@app.delete('/products/{product_id}')
def borrar_producto(product_id):
    return "Producto borrado"




#PARA EJECUTAR LA API uvicorn main:app --reload