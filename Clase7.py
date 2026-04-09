'''

Crea una clase "Banco" con propiedades para el nombre del banco y la tasa de interés
, y métodos para calcular el interés que se obtendría en una cantidad determinada de 
dinero y el tiempo que se tardaría en duplicar esa cantidad.


'''
class Banco:
    def __init__(self, nombre, tasainteres):
        self.nombre = nombre
        self.tasainteres = tasainteres
    
    def CalcularInteres(self, CantidadDinero, Dias):
        return CantidadDinero * self.tasainteres * (Dias / 365)
        
    def TiempoParaDuplicar(self):
        return 1 / self.tasainteres

if __name__ == "__main__":
    MiBanco = Banco("BBVA", 0.63)
    print("Ingresa dinero y dias | tasa de interes BBVA: %0.63")
    DineroIngresar = float(input())
    DiasIngresar = int(input())
    
    print(f"Interes Calculado: {round(MiBanco.CalcularInteres(DineroIngresar, DiasIngresar))} ")
    print(f"Tiempo para duplicar {(MiBanco.TiempoParaDuplicar())}")