class Item():
    def __init__(self, nombre, tipo, peso, valor):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso
        self.valor = valor

class Inventory():
    def __init__(self):
        self.items= []
        self.peso_total = 0.0
        self.valor_total = 0

    def añadir_item(self, item):
        self.items.append(item)
        self.peso_total += item.peso
        self.valor_total += item.valor

    def eliminar_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.peso_total -= item.peso
            self.valor_total -= item.valor

