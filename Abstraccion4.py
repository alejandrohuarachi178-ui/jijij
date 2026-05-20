from abc import ABC
from abc import abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self):
        pass

class Email(Notificacion):
    def enviar(self):
        return "Notificacion enviada por email"

class SMS(Notificacion):
    def enviar(self):
        return "Notificacion enviada por SMS"
