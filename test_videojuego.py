#Test videojuego
from videojuego import Item, Inventory
# Test 1: Crear un ítem
pocion = Item("Poción", "Bebible", 0.5, 10)
assert pocion.nombre == "Poción"
espada = Item("Espada victoriosa", "Arma", 3.0, 100)
assert espada.nombre == "Espada victoriosa"

# Test 2: Inventario vacío
mochila = Inventory()
assert len(mochila.items) == 0

# Test 3: Añadir objeto
mochila.añadir_item(pocion)
mochila.añadir_item(espada)
assert len(mochila.items) == 2
assert mochila.peso_total == 3.5
assert mochila.valor_total == 110

# Test 4: Eliminar objeto
mochila.eliminar_item(pocion)

# Ahora queda 1 objeto (la espada)
assert len(mochila.items) == 1  
# El peso de la espada es 3.0 y su valor es 100
assert mochila.peso_total == 3.0
assert mochila.valor_total == 100

# Test 5: Verificar los métodos de mostrar 
mochila.mostrar_inventario()
mochila.mostrar_peso_valor()

print("¡Todos los tests han pasado con éxito!")