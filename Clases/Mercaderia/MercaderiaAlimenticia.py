from Clases.Mercaderia.Mercaderia import Mercaderia

class MercaderiaAlimenticia(Mercaderia):
    def __init__(self, id, n, p, v, ancho, alto, largo):
        super().__init__(id, n, p, v, ancho, alto, largo)

    def __eq__(self, otro):
        if isinstance(otro, self.__class__):
            return self.get_id() == otro.get_id()
        return False