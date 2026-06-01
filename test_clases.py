from clases import Persona#, #CuentaBancaria
import pytest
from dataclasses import dataclass


persona = Persona("Ana", "Juan", "Rodriguez", 32)

def test_nombre_completo():
   
    persona_nombre = persona.nombre_completo() #Atributo de la clase Persona
    assert persona_nombre.nombre_completo() == "Ana Juan Rodriguez"
    assert persona.edad()== "32 años"

    def test_persona_edad_negativa() -> None:
        with pytest.raises(ValueError):
            Persona("Joa", "Iglesias", "Ramos", -20)

    #__________________________________________________________

def funcion_de_prueba():
    # Todo esto lleva 4 espacios (un Tabulador) de sangría porque está DENTRO de la función
    cuenta = CuentaBancaria("Ana")
    cuenta.añadir_dinero(100)
    print(cuenta._balance)
    print(cuenta.retirar_dinero(120))
    print(cuenta._balance)
    print("¡El archivo se está ejecutando correctamente y las clases se importaron!")

# Esto va PEGADO al margen izquierdo (sin ningún espacio) porque está FUERA de la función
funcion_de_prueba()


#__________________________________________________________

class Producto():
    def __init__(self, nombre: str, precio: float, cantidad: int = 1, ) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, valor: float):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        else:
            self._precio = valor

    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self, valor: int):
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa")
        else:
            self._cantidad = valor
    
    def __str__(self) -> str:
        return f"{self.nombre} | {self.precio} | {self.cantidad}"

p = Producto("galletas", 10.20)
print(p)

#_____________________________________________________________

@dataclass
class Archivo:
    filename: str

    @property
    def extension(self):
        return self.filename.split(".")[-1]
    
    @property
    def raiz(self):
        return self.filename.split(".")[0]
    
f = Archivo("base_datos.sql")
print(f.filename)
print(f.raiz)
print(f.extension)
f.filename = "test_clases.py"
print(f.filename)
print(f.raiz)
print(f.extension)


