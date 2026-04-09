'''
Crea una clase "Rectángulo" con propiedades para la longitud y la anchura, 
y métodos para calcular el área y el perímetro del rectángulo.

'''
class Rectangulo:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura
    
    def CalcularArea(self):
        return self.longitud * self.anchura
        
    def CalcularPerimetro(self):
        return 2 * (self.longitud + self.anchura)

if __name__ == "__main__":

    mi_rectangulo = Rectangulo(10, 5)
    
    print(f"Longitud: {mi_rectangulo.longitud}")
    print(f"Anchura: {mi_rectangulo.anchura}")
    
    area = mi_rectangulo.CalcularArea()
    print(f"area calculada: {area}")
    
    perimetro = mi_rectangulo.CalcularPerimetro()
    print(f"perimetro calculado: {perimetro}")