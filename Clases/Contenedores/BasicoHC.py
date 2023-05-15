
from Clases.Contenedores.Contenedor import Contenedor


class BasicoHC(Contenedor):
    def __init__(self, id):
        super().__init__(id, 2.35, 2.3, 12.0, 2.45, 2.6, 12.1)

    def __init__(self, id, precio_base):
        super().__init__(self, id, 2.35, 2.3, 12.0, 2.45, 2.6, 12.1,
                         40, 32500.0, 67.7, precio_base)
