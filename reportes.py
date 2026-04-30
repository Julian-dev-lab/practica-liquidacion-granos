from database import coleccion_liquidaciones

def mostrar_top_productores():
    # El Pipeline que armaste (con la optimización del $limit)
    pipeline = [
        { "$match": { "estado": "liquidado" } },
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

    # Ejecutamos la query
    # aggregate() devuelve un "cursor" (un iterador), por eso usamos un for
    resultados = list(coleccion_liquidaciones.aggregate(pipeline))

    if not resultados:
        print("\n⚠️ No hay datos suficientes para generar el ranking.")
        return

    # Formateo estético del reporte
    print("\n" + "╔" + "═"*45 + "╗")
    print("║" + " "*10 + "RANKING TOP 3 PRODUCTORES" + " "*10 + "║")
    print("╠" + "═"*45 + "╣")
    print(f"║ {'PRODUCTOR':<25} | {'TOTAL COBRADO':<15} ║")
    print("╟" + "─"*45 + "╢")

    for res in resultados:
        cliente = res['Cliente']
        monto = res['Monto_Total']
        print(f"║ {cliente:<25} | USD {monto:>12,.2f} ║")

    print("╚" + "═"*45 + "╝\n")

    print(resultados)

if __name__ == "__main__":
    mostrar_top_productores()