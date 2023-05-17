
from Clases.Contenedores.Contenedor import Contenedor


class BasicoHC(Contenedor):
    def __init__(self, id):
        super().__init__(id, 235.0, 230.0, 1200.0, 245.0, 260.0, 1210.0)
        self.set_pies(40)
        self.set_max_Peso(32500.0)
        self.set_max_Volumen(67.7)

