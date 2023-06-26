from abc import ABC , abstractmethod
class SistemaPropulsion(ABC):

    def gastar_combustible(self, tiempo):
        pass

    def get_nombre(self):
        pass