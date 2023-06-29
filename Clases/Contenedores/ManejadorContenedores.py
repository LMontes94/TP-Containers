from abc import ABC, abstractmethod

class ManejadorContenedores(ABC):
    def __init__(self):
        self.siguiente = None

    def set_siguiente(self, manejador):
        self.siguiente = manejador

    @abstractmethod
    def manejar(self, mercaderia):
        pass