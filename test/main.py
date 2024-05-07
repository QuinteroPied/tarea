def suma(a,b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def es_mayor_de_edad(edad):
    return edad >= 18


class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_adulto(self):
        return self.edad >= 18
