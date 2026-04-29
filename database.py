from pymongo import MongoClient
import sys

def conectar_db():
    try:
        # Cadena de conexión (la misma que usamos en Compass)
        client = MongoClient("mongodb://localhost:27017/")
        
        # Seleccionamos la base de datos
        db = client["corredora_db"]
        
        # Probamos la conexión
        client.admin.command('ping')
        print("✅ Conexión exitosa a MongoDB")
        
        return db
    except Exception as e:
        print(f"❌ Error al conectar a MongoDB: {e}")
        sys.exit()

# Definimos la colección para usarla en otros scripts
db = conectar_db()
coleccion_liquidaciones = db["liquidaciones"]