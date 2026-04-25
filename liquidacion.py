def generar_recibo_liquidacion(toneladas, precio_por_tonelada, comision_porcentaje, retencion_porcentaje):
    # 1. Cálculos de Negocio
    if toneladas > 500:
        comision_porcentaje -= 0.5
    
    bruto = toneladas * precio_por_tonelada
    comision_monto = bruto * (comision_porcentaje / 100)
    retencion_monto = bruto * (retencion_porcentaje / 100)
    neto = bruto - comision_monto - retencion_monto

    # 2. Construcción del Recibo (Visual)
    print("\n" + "="*30)
    print("   DETALLE DE LIQUIDACIÓN")
    print("="*30)
    print(f"Toneladas:          {toneladas:>10}")
    print(f"Precio x Ton:       USD {precio_por_tonelada:>6.2f}")
    print("-" * 30)
    print(f"Subtotal Bruto:     USD {bruto:>10.2f}")
    print(f"Comisión ({comision_porcentaje}%):    -USD {comision_monto:>10.2f}")
    print(f"Retenciones (3%):   -USD {retencion_monto:>10.2f}")
    print("-" * 30)
    print(f"TOTAL NETO A PAGAR: USD {neto:>10.2f}")
    print("="*30 + "\n")

# Ejecución
generar_recibo_liquidacion(600, 250, 2, 3)