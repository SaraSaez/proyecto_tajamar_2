
# Esta lista guardará los gastos en memoria
lista_gastos = []

def agregar_gasto(concepto, cantidad):
    if cantidad <= 0:
        return False
    
    # Creamos un diccionario simple para el gasto
    nuevo_gasto = {"concepto": concepto, "cantidad": cantidad}
    lista_gastos.append(nuevo_gasto)
    return True

def obtener_gastos():
    return lista_gastos

def calcular_total():
    total = 0
    for gasto in lista_gastos:
        total += gasto["cantidad"]
    return total

def borrar_gastos():
    """Función auxiliar para vaciar la lista en los tests"""
    lista_gastos.clear()