import json

def cargar_configuracion():
    try:
        with open('comisiones.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Aquí lanzamos el alerta que mencionabas
        print("\n[ERROR CRÍTICO] No se encontró el archivo 'comisiones.json'.")
        print("La liquidación no puede procesarse sin las tasas vigentes.")
        exit() # Detiene la ejecución por completo

def generar_recibo_liquidacion(productor, toneladas, precio_por_ton, producto):
    #Cargamos el diccionario desde el archivo externo
    comisiones = cargar_configuracion()

    producto = producto.lower()

    # 1. Obtenemos el valor por defecto del JSON. 
    # Si ni siquiera está la clave "default" en el JSON, usamos 2.5 como último recurso
    tasa_defecto = comisiones.get("default", 2.5)

    # 2. Buscamos el producto, y si no está, usamos la tasa_defecto que leímos antes.
    comision_nativa = comisiones.get(producto, tasa_defecto)

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
generar_recibo_liquidacion("Ana Lopez", 300, 240, "Poroto") # Probará el valor default