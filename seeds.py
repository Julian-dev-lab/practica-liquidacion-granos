from database import coleccion_liquidaciones
from datetime import datetime, timedelta
import random

def generar_datos_prueba():
    productores = ["AgroS.A.", "López Hnos", "Establecimiento El Sol", "La Posta S.R.L."]
    productos = ["soja", "maiz", "trigo", "girasol"]
    
    documentos = []
    
    for i in range(1, 21):
        prod = random.choice(productores)
        grano = random.choice(productos)
        tons = random.randint(100, 800)
        precio = random.randint(200, 300)
        
        # Lógica de negocio simplificada
        bruto = tons * precio
        neto = bruto * 0.95 # Estimado rápido
        
        doc = {
            "nro_comprobante": f"0001-{i:08d}",
            "fecha_emision": datetime.now() - timedelta(days=random.randint(0, 30)),
            "productor": prod,
            "producto": grano,
            "toneladas": tons,
            "neto_pagado": round(neto, 2),
            "estado": random.choice(["pendiente", "liquidado", "anulado"])
        }
        documentos.append(doc)
    
    # Limpiamos e insertamos
    coleccion_liquidaciones.delete_many({}) # Borra lo anterior para no duplicar
    coleccion_liquidaciones.insert_many(documentos)
    print(f"✅ Se insertaron {len(documentos)} documentos de prueba.")

from database import coleccion_liquidaciones
import random

def actualizar_comisiones_faltantes():
    # Buscamos todos los documentos
    liquidaciones = coleccion_liquidaciones.find({})
    
    for liq in liquidaciones:
        # Generamos una comisión aleatoria entre 1.0 y 3.0
        comision_random = round(random.uniform(1.0, 3.0), 2)
        
        # Actualizamos el documento usando su _id
        coleccion_liquidaciones.update_one(
            {"_id": liq["_id"]},
            {"$set": {"comision_aplicada": comision_random}}
        )
    
    print("✅ Base de datos actualizada con el campo 'comision_aplicada'.")



if __name__ == "__main__":
    generar_datos_prueba()

if __name__ == "__main__":
    actualizar_comisiones_faltantes()