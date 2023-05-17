
from Clases.Contenedores.Contenedor import Contenedor


class FlatRack(Contenedor):
    def __init__(self, id):
        super().__init__(id, None, 2.3, 6.0, None, 2.3, 6.1)
        self.set_max_Peso(45000.0)
        self.set_max_Volumen(33.0)
