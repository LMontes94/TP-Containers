
from Clases.Contenedores.Contenedor import Contenedor


class FlatRack(Contenedor):
    def __init__(self, id):
        super().__init__(id, None, 2.3, 6.0, None, 2.3, 6.1)

    def __init__(self, id, pies, precio_base):
        super().__init__(self, id, None, 2.3, 6.0, None, 2.3, 6.1,
                         pies, 45000.0, 33.0, precio_base)
