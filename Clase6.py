'''
Crea una clase "Estudiante" con propiedades para el nombre, la edad y la carrera, 
y métodos para obtener y establecer estas propiedades, así como un método para 
calcular la nota media de un conjunto de exámenes.

'''
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []  
        
    def obtener_nombre(self):
        return self.nombre
        
    def obtener_edad(self):
        return self.edad
        
    def obtener_carrera(self):
        return self.carrera
        
    def obtener_notas(self):
        return self.notas

    def establecer_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def establecer_edad(self, nueva_edad):
        self.edad = nueva_edad
        
    def establecer_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera


    def agregar_nota(self, nota):
        self.notas.append(nota)
        
    def calcular_media(self):

        if len(self.notas) == 0:
            return 0
    
        promedio = sum(self.notas) / len(self.notas)
        return promedio
    

# Si profe use ia para el ejemplo ok me dio paja.

if __name__ == "__main__":
    

    estudiante1 = Estudiante("Lionel", 19, "Ingeniería en Sistemas")
    
    print("--- DATOS INICIALES ---")
    print(f"Alumno: {estudiante1.obtener_nombre()}")
    print(f"Edad: {estudiante1.obtener_edad()}")
    print(f"Carrera: {estudiante1.obtener_carrera()}")
    
    print("\n--- ACTUALIZANDO DATOS ---")
 
    estudiante1.establecer_edad(20)
    print(f"¡Feliz cumpleaños! Nueva edad: {estudiante1.obtener_edad()}")
    
    print("\n--- CARGA DE EXÁMENES ---")
    estudiante1.agregar_nota(8)
    estudiante1.agregar_nota(9)
    estudiante1.agregar_nota(7)
    
    print("\n--- RESULTADO FINAL ---")
    media_final = estudiante1.calcular_media()
    print(f"La nota media de {estudiante1.obtener_nombre()} es: {round(media_final, 2)}")