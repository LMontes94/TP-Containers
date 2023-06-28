from Clases.Barco.SistemaPropulsion.SistemaPropulsion import SistemaPropulsion

class Motor(SistemaPropulsion):

    def __init__(self):
        super().__init__()
        self.__nombre = "Motor"

    def gastar_combustible(self, tiempo):
        return 6 * tiempo
    
    def get_nombre(self):
        return self.__nombre


    def avanzar(self):
        print(f"Ha activado el sistema de propulsion {self.get_nombre()}")