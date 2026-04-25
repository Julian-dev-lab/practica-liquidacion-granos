def generar_recibo_liquidacion(productor, toneladas, precio_por_ton, producto):
    # Definimos el diccionario de comisiones
    comisiones = {
        "soja": 2.0,
        "maiz": 1.5,
        "trigo": 1.8,
        "girasol": 2.5
    }
    
    producto = producto.lower()
    
    comision_nativa = comisiones.get(producto, 2.5)

    # Cálculos de Negocio
    if toneladas > 500:
        comision_nativa -= 0.5

    bruto = toneladas * precio_por_ton
    comision_monto = bruto * (comision_nativa / 100)
    retencion_monto = bruto * 0.03
    neto = bruto - comision_monto - retencion_monto

    # 2. Construcción del Recibo (Visual)
    print("\n" + "="*30)
    print("   DETALLE DE LIQUIDACIÓN")
    print(f"VENDEDOR: {productor.upper()}")
    print(f"PRODUCTO: {producto.upper()}")
    print("="*30)
    print(f"Toneladas:          {toneladas:>10}")
    print(f"Precio x Ton:       USD {precio_por_ton:>6.2f}")
    print("-" * 30)
    print(f"Subtotal Bruto:     USD {bruto:>10.2f}")
    print(f"Comisión ({comision_nativa}%):    -USD {comision_monto:>10.2f}")
    print(f"Retenciones (3%):   -USD {retencion_monto:>10.2f}")
    print("-" * 30)
    print(f"TOTAL NETO A PAGAR: USD {neto:>10.2f}")
    print("="*30 + "\n")


generar_recibo_liquidacion("Juan Perez", 600, 250, "Soja")
generar_recibo_liquidacion("Ana Lopez", 600, 240, "Sorgo") # Probará el valor default