'''
Crea una clase "Empleado" con propiedades para el nombre, la edad, 
el salario y el cargo, y métodos para obtener y establecer estas propiedades, 
así como un método para calcular el salario anual.
'''

class Empleado:
    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario = salario
    
    # obtener
    def obtener_nombre(self):
        return self.nombre
        
    def obtener_edad(self):
        return self.edad
        
    def obtener_salario(self):
        return self.salario
        
    def obtener_cargo(self):
        return self.cargo

   # establecer
    def establecer_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def establecer_edad(self, nueva_edad):
        self.edad = nueva_edad
        
    def establecer_salario(self, nuevo_salario):
        self.salario = nuevo_salario
        
    def establecer_cargo(self, nuevo_cargo):
        self.cargo = nuevo_cargo
    
    
    def CalcularAnual(self):
        return self.salario * 12

if __name__ == "__main__":
    Momo = Empleado("Geronimo Benavides", 29, 30995, "Vende Humo")
    
    print(f"Empleado: {Momo.obtener_nombre()}")
    print(f"Cargo inicial: {Momo.obtener_cargo()}")
    
    Momo.establecer_cargo("Streamer del Año")
    print(f"Nuevo cargo: {Momo.obtener_cargo()}")
    print(f"Salario anual: ${Momo.CalcularAnual()}")