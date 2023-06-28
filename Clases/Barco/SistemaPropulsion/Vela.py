from Clases.Barco.SistemaPropulsion.SistemaPropulsion import SistemaPropulsion
class Vela(SistemaPropulsion):

    def __init__(self):

        super().__init__()
        self.__nombre = "Vela"

    def gastar_combustible(self, tiempo):
        return 0 * tiempo
    
    def get_nombre(self):
        return self.__nombre   

    def avanzar(self):
        print(f"Ha activado el sistema de propulsion {self.get_nombre()}")