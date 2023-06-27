from abc import ABC , abstractmethod
class SistemaPropulsion(ABC):

    @abstractmethod
    def gastar_combustible(self, tiempo):
        pass

    @abstractmethod    
    def get_nombre(self):
        pass

    @abstractmethod    
    def avanzar(self):
        pass