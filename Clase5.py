'''
Crea una clase "Círculo" con propiedades para el radio y el diámetro, 
y métodos para calcular el área y la circunferencia del círculo.


'''
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.diametro = radio * 2
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
        
    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio

if __name__ == "__main__":
    mi_circulo = Circulo(5)
    
    print(f"Radio: {mi_circulo.radio}")
    print(f"daimetro calculado automáticamente: {mi_circulo.diametro}")
    
    area = mi_circulo.calcular_area()
    print(f"araea calculada: {round(area, 2)}")
    
    circunferencia = mi_circulo.calcular_circunferencia()
    print(f"circunferencia calculada: {round(circunferencia, 2)}")