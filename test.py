import gastos

def test_agregar_gasto(gestor_vacio):
    # Comprobar que devuelve True al añadir bien
    resultado = gestor_vacio.agregar_gasto("Cine", 15.0)
    assert resultado is True
    assert len(gestor_vacio.obtener_gastos()) == 1

def test_agregar_gasto_incorrecto(gestor_vacio):
    # Usar el objeto que nos da la fixture
    resultado = gestor_vacio.agregar_gasto("Error", -5.0)
    assert resultado is False

def test_calcular_total(gestor_vacio):
    gestor_vacio.agregar_gasto("Pan", 1.50)
    gestor_vacio.agregar_gasto("Agua", 2.00)
    
def test_calcular_total(gestor_vacio):
    gestor_vacio.agregar_gasto("Pan", 1.50)
    gestor_vacio.agregar_gasto("Agua", 2.00)

    assert gestor_vacio.calcular_total() == 3.50
    print("¡Todos los tests han pasado con éxito!")