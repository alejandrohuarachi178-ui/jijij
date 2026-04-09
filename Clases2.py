'''

Crea una clase "Coche" con propiedades para la marca, el modelo y el 
año de fabricación, y un método para obtener el número de años que ha 
pasado desde que se fabricó el coche. gascon307 argentina velez

'''
class Auto:
    def __init__(self, anio_fabricacion, modelo, marca):
        self.marca = marca
        self.modelo = modelo
        self.anio_fabricacion = anio_fabricacion
    
    def FabricationDate(self):
        return 2026 - self.anio_fabricacion

if __name__ == "__main__":
    mi_auto = Auto(1990, "Skibidi", "Bugggati")
    
    print(f"Mi Auto {mi_auto.marca} {mi_auto.modelo}, creado en: {mi_auto.anio_fabricacion}")
    print(f"Creado hace {mi_auto.FabricationDate()} años")
