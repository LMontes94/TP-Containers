from Clases.Barco.SistemaPropulsion import SistemaPropulsion

class Motor(SistemaPropulsion):

    def __init__(self):

        self.__nombre = "Motor"

    def gastar_combustible(self, tiempo):
        return 6 * tiempo
    
    def get_nombre(self):
        return self.__nombre
