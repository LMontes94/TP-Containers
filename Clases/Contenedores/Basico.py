
from Clases.Contenedores.Contenedor import Contenedor


class Basico(Contenedor):
    def __init__(self, id):
        super().__init__(id, 2.35, 2.3, 6.0, 2.45, 2.6, 6.1)

    def __init__(self, id, precio_base):
        super().__init__(self, id, 2.35, 2.3, 6.0, 2.45, 2.6, 6.1,
                         20, 24000.0, 32.6, precio_base)
