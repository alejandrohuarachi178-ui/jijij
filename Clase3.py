'''

Crea una clase "Producto" con propiedades para el nombre, 
el precio y el stock disponible, y métodos para aumentar o 
disminuir el stock.


'''
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def AumentarStock(self, stockAumentar):
        self.stock += stockAumentar
        return self.stock
        
    def DisminuirStock(self, StockDisminir):
        self.stock -= StockDisminir
        return self.stock

if __name__ == "__main__":
    
    Producto1 = Producto("Papeada Termonuclear", 9999.99, 5)
    print(f"1. {Producto1.nombre} | Precio: ${Producto1.precio} | Stock: {Producto1.stock}")
    
    Producto1.AumentarStock(60)
    print(Producto1.stock)
    
    Producto1.DisminuirStock(20)
    print(Producto1.stock)