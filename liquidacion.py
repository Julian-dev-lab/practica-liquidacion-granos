# liquidacion.py - Versión Inicial
def calcular_neto(toneladas, precio_por_tonelada, comision_porcentaje):
    bruto = toneladas * precio_por_tonelada
    comision = bruto * (comision_porcentaje / 100)
    neto = bruto - comision
    return neto

# Datos de prueba
tons = 100
precio = 250  # USD
comision_ref = 2 # %

resultado = calcular_neto(tons, precio, comision_ref)
print(f"Liquidación Total: USD {resultado}")