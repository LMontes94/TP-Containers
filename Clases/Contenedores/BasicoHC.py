
from Clases.Contenedores.Contenedor import Contenedor


class BasicoHC(Contenedor):
    def __init__(self, id):
        super().__init__(id, 2.35, 2.3, 12.0, 2.45, 2.6, 12.1)
        self.set_pies(40)
        self.set_max_Peso(32500.0)
        self.set_max_Volumen(67.7)

