
class GestorGastos:
    def __init__(self):
        self.lista_gastos = []

    def agregar_gasto(self, concepto, cantidad):
        if cantidad <= 0:
            return False
    
    # Crear un diccionario para el gasto
        nuevo_gasto = {"concepto": concepto, "cantidad": cantidad}
        self.lista_gastos.append(nuevo_gasto)
        return True

    def obtener_gastos(self):
        return self.lista_gastos

    def calcular_total(self):
        total = 0
        for gasto in self.lista_gastos:
            total += gasto["cantidad"]
        return total

    def borrar_gastos(self):
    #Función auxiliar para limpiar  la lista
        self.lista_gastos.clear()