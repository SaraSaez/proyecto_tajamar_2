import pytest
import gastos

@pytest.fixture(autouse=True)
def limpiar_datos():
    #Borra los gastos antes de cada test para que empiecen de cero
    gastos.borrar_gastos()