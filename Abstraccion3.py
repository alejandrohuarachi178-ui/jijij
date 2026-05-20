from abc import ABC
from abc import abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self):
        self.radio = 0
    def calcular_area(self):
        return 3.1416 * self.radio * self.radio

class Rectangulo(Figura):
    def __init__(self):
        self.base = 0
        self.altura = 0
    def calcular_area(self):
        return self.base * self.altura
