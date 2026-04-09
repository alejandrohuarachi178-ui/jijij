'''
Crea una clase "Tienda" con propiedades para el nombre de la tienda y una 
lista de productos disponibles, y métodos para añadir o eliminar productos 
de la lista y para obtener la lista completa de productos.
'''

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    
    def ObtenerProductos(self):
        return self.productos
    
    def AgregarProductos(self, producto):
        self.productos.append(producto)
        return producto
        
    def RemoverProducto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print(f"El producto '{producto}' no se encuentra en la tienda.")

if __name__ == "__main__":
    kiosko = Tienda("Kiosko skibidi phonk")
    
    kiosko.AgregarProductos("Manaos")
    kiosko.AgregarProductos("Tussi")
    kiosko.AgregarProductos("Enrqiue")
    
    print("Productos:")
    print(f"{kiosko.ObtenerProductos()}")
    
    print("Tussi eliminado:")
    kiosko.RemoverProducto("Tussi")
    print(f"{kiosko.ObtenerProductos()}")
    