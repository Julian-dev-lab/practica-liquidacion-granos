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

if __name__ == "__main__":
    generar_datos_prueba()