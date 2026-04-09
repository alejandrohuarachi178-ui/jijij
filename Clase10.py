'''
Crea una clase "Libro" con propiedades para el título, el autor, 
el género y el número de páginas, y métodos para obtener y establecer 
estas propiedades, así como un método para comprobar si el libro es de ficción o no.
'''
class Libro:
    def __init__(self, titulo, autor, genero, numPags):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.numPags = numPags
    
    # getters
    def obtener_titulo(self):
        return self.titulo
        
    def obtener_autor(self):
        return self.autor
        
    def obtener_genero(self):
        return self.genero
        
    def obtener_numPags(self):
        return self.numPags
    # setters
    def establecer_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
        
    def establecer_autor(self, nuevo_autor):
        self.autor = nuevo_autor
        
    def establecer_genero(self, nuevo_genero):
        self.genero = nuevo_genero
        
    def establecer_numPags(self, nuevo_numPags):
        self.numPags = nuevo_numPags
    # misc
    def ValidarFiccion(self):
        return self.genero.lower() == "ficción"

if __name__ == "__main__":
    libro1 = Libro("Harry Potter", "J.K. Rowling", "ficción", 340)
    
    print(f"{libro1.obtener_titulo()} de {libro1.obtener_autor()}")
    print(f"Es ciencia ficción: {libro1.ValidarFiccion()}")
    