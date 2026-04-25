# liquidacion.py - Versión Inicial
def calcular_neto(toneladas, precio_por_tonelada, comision_porcentaje, retencion_porcentaje):
    bruto = toneladas * precio_por_tonelada
    comision = bruto * (comision_porcentaje / 100)
    retencion = bruto * (retencion_porcentaje / 100)
    neto = bruto - comision - retencion 
    return neto

# Datos de prueba
tons = 100
precio = 250  # USD
comision_ref = 2 # %
retencion_impositiva = 3 # %

resultado = calcular_neto(tons, precio, comision_ref, retencion_impositiva)
print(f"Liquidación Total: USD {resultado}")