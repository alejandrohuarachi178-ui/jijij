from abc import ABC
from abc import abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass

class EmpleadoPorHora(Empleado):
    def __init__(self):
        self.horas = 0
        self.pago_por_hora = 0
    def calcular_sueldo(self):
        return self.horas * self.pago_por_hora

class EmpleadoFijo(Empleado):
    def __init__(self):
        self.sueldo_fijo = 0
    def calcular_sueldo(self):
        return self.sueldo_fijo
