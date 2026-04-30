from database import coleccion_liquidaciones

def mostrar_top_productores(producto_buscado=None):
    # 1. Construimos el filtro base (siempre liquidados)
    filtro = { "estado": "liquidado" }
    
    # 2. Si el usuario pasó un producto, lo agregamos al filtro
    if producto_buscado:
        filtro["producto"] = producto_buscado.lower()
        titulo = f"RANKING TOP 3 PRODUCTORES ({producto_buscado.upper()})"
    else:
        titulo = "RANKING TOP 3 PRODUCTORES (GENERAL)"

    pipeline = [
        { "$match": filtro }, # Usamos nuestro diccionario dinámico
        { 
            "$group": { 
                "_id": "$productor", 
                "total_cobrado": { "$sum": "$neto_pagado" } 
            } 
        },
        { "$sort": { "total_cobrado": -1 } },
        { "$limit": 3 },
        {
            "$project": {
                "_id": 0,
                "Cliente": "$_id",
                "Monto_Total": "$total_cobrado"
            }
        }
    ]

    resultados = list(coleccion_liquidaciones.aggregate(pipeline))

    if not resultados:
        print(f"\n⚠️ No se encontraron liquidaciones para: {producto_buscado or 'General'}")
        return

    # Formateo estético
    print("\n" + "╔" + "═"*48 + "╗")
    print(f"║{titulo.center(48)}║")
    print("╠" + "═"*48 + "╣")
    print(f"║ {'PRODUCTOR':<28} | {'TOTAL COBRADO':<15} ║")
    print("╟" + "─"*48 + "╢")

    for res in resultados:
        print(f"║ {res['Cliente']:<28} | USD {res['Monto_Total']:>12,.2f} ║")

    print("╚" + "═"*48 + "╝\n")

def reporte_comisiones_promedio():

    pipeline = [
        {"$match": {"estado": "liquidado"}},
        {"$group": {"_id":"$producto", "promedio_comision": {"$avg":"$comision_aplicada"}}},
        {"$sort": {"promedio_comision": -1}}
    ]

    resultados = list(coleccion_liquidaciones.aggregate(pipeline))

    for res in resultados:
        print(f"Producto: {res['_id']} || Comision promedio: {res['promedio_comision']}")

    print(resultados)


reporte_comisiones_promedio()

### --- PRUEBAS ---
#if __name__ == "__main__":
#    mostrar_top_productores()         # Sin parámetros: General
#    mostrar_top_productores("soja")   # Con parámetro: Solo Soja

