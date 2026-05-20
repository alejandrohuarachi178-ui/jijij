from abc import ABC
from abc import abstractmethod

class Pago(ABC):
    @abstractmethod
    def procesar_pago(self):
        pass

class TarjetaCredito(Pago):
    def procesar_pago(self):
        return "Pago procesado con tarjeta de credito"

class PayPal(Pago):
    def procesar_pago(self):
        return "Pago procesado con PayPal"
