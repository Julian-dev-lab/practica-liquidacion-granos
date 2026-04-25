def calcular_neto(toneladas, precio_por_tonelada, comision_porcentaje, retencion_porcentaje):
    # Lógica del Bono: Si supera las 500 toneladas, bajamos la comisión
    if toneladas > 500:
        print("--- Aplicando Bono por Gran Productor (-0.5% comisión) ---")
        comision_porcentaje = comision_porcentaje - 0.5
    
    bruto = toneladas * precio_por_tonelada
    comision = bruto * (comision_porcentaje / 100)
    retencion = bruto * (retencion_porcentaje / 100)
    neto = bruto - comision - retencion
    return neto

# Datos de prueba (Probemos con 600 toneladas para activar el bono)
tons = 600 
precio = 250 
comision_ref = 2 
retencion_ref = 3

resultado = calcular_neto(tons, precio, comision_ref, retencion_ref)
print(f"Liquidación Final: USD {resultado}")