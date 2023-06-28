
from abc import ABC, abstractmethod
from Clases.Excepciones.NoHayBarcoException import NoHayBarcoException


class ContenedorManejador(ABC):
    def __init__(self):
        self.siguiente = None

    def setSiguiente(self, manejador):
        self.siguiente = manejador

    @abstractmethod
    def manejar(self, contenedor):
        pass

    def noHaySiguiente(self):
        if self.siguiente is None:
            raise NoHayBarcoException("Ningún barco disponible!!")
        return True