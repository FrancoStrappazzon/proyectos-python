import sqlite3

#base de datos en sqlite
DATABASE = "productos.db"

# Función para conectar a la base de datos SQLite
def connect_to_database():
    conn = sqlite3.connect(DATABASE)
    return conn

# Función para desconectar de la base de datos SQLite
def close_database_connection(conn):
    conn.close()