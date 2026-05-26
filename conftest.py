import pytest
from gastos import GestorGastos

@pytest.fixture
def gestor_vacio():
    #Devuelve una instancia nueva y limpia de GestorGastos 
    # para cada test
    return GestorGastos()