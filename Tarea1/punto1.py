class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_año(self, año):
        self.__año = año

    def detalles(self):
        print(f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año}")

# Creo un objeto de la clase Vehiculo
mi_auto = Vehiculo("Toyota", "Corolla", 2022)

mi_auto.set_marca("Honda")
mi_auto.set_año(2023)

# método detalles para mostrar la información del vehículo
mi_auto.detalles()


