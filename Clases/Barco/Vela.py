from Clases.Barco.SistemaPropulsion import SistemaPropulsion
class Vela(SistemaPropulsion):

    def __init__(self):

        self.__nombre = "Vela"

    def gastar_combustible(self, tiempo):
        return 0 * tiempo
    
    def get_nombre(self):
        return self.__nombre   
