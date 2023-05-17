
from Clases.Contenedores.Contenedor import Contenedor


class Basico(Contenedor):
    def __init__(self, id):
        super().__init__(id, 2.35, 2.3, 6.0, 2.45, 2.6, 6.1)
        self.set_pies(20)
        self.set_max_Peso(24000.0)
        self.set_max_Volumen(32.6)
