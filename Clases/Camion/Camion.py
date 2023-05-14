from Contenedores import Contenedor

class Camion:
#Constructor
    def __init__(self, patente):
        self.patente = patente
        self.costoFijo = 20000.0
        self.contenedor = None
        self.ocupado = False

#Getters & Setters
    def getPatente(self):
        return self.patente
    def setPatente(self, patente):
        self.patente = patente

    def getCostoFijo(self):
        return self.costoFijo

    def getContenedor(self):
        return self.contenedor
    def setContenedor(self, contenedor : Contenedor):
        self.contenedor = contenedor

    def llevaContenedor(self):
        return self.contenedor is not None