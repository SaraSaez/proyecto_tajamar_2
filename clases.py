"""
class Persona:
    def __init__(self, nombre, apellido_1, apellido_2, edad: int):
        self.nombre = nombre
        self.apellido_1 = apellido_1
        self.apellido_2 = apellido_2
        self.edad = edad
    @property 
    #Decorador para converir el método en una propiedad de
    #la clase y asi poder llamarlo sin parentesis
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido_1} {self.apellido_2}"
    
    @property #recuperacion del atributo
    def edad(self):
        return f"{self.edad} años"
    @edad.setter #generacion del atributo privado
    def edad(self, valor:int):
        if valor < 0:
            raise ValueError("La edad no puede ser un número negativo")
        self.edad = valor #aqui setteamos el valor de la edad, es decir, 
        #lo guardamos en el atriuto privado _edad para que luego podamos
        #acceder a él con el método edad() que es una propiedad de la clase
if __name__ == "__main__":
    Joa = Persona("Joa", "Iglesias", "Ramos", -20)
    print(Joa.edad)
    #___________________________________________________________

class CuentaBancaria:
        def __init__(self, nombre_titular):
            self.nombre_titular = nombre_titular
            self._balance = 0

        @property
        def balance(self):
            if self._balance < 0:
                return f"{abs(self._balance)} euros en negativo"
            else:
                return f"{self._balance} euros"

        def añadir_dinero(self, cantidad: int):
            self._balance += cantidad

        def retirar_dinero(self, cantidad: int):
            self._balance -= cantidad

"""

#______________________________________________________-
#GETTERS

class Persona:
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @property #qué pasa cuando lo establezco
    def nombre(self) -> str | None:
        return self._nombre

    @nombre.setter #qué pasa cuando lo modifico
    def nombre(self, valor: str) -> None:
        self._nombre = valor

    @nombre.deleter #qué pasa cuando lo elimino
    def nombre(self): 
        print("Has eliminado el nombre!")
        #del self._nombre
        self._nombre = None

    def __str__(self) -> str:
        return self.nombre

joa = Persona("Joaquin")
print(joa)
print(joa.nombre)
joa.nombre = "Ana"
print(joa.nombre)
del joa.nombre
print(joa.nombre)
    