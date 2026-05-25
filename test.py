import gastos

def test_agregar_gasto():
    # Comprobamos que devuelve True al añadir bien
    resultado = gastos.agregar_gasto("Cine", 15.0)
    assert resultado is True
    assert len(gastos.obtener_gastos()) == 1

def test_agregar_gasto_incorrecto():
    # Comprobamos que no deja añadir números negativos
    resultado = gastos.agregar_gasto("Error", -5.0)
    assert resultado is False

def test_calcular_total():
    gastos.agregar_gasto("Pan", 1.50)
    gastos.agregar_gasto("Agua", 2.00)
    
    assert gastos.calcular_total() == 3.50
    if __name__ == "__main__":
        print("Ejecutando pruebas a mano...")
    test_agregar_gasto()
    test_agregar_gasto_incorrecto()
    test_calcular_total()
    print("¡Todos los tests han pasado con éxito! 🎉")