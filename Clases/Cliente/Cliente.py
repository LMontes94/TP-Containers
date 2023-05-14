from Mercaderia import Mercaderia

class Cliente:
    #Constructor
    def __init__(self, nombre, dni, nroCliente):
        self.nombre = nombre
        self.dni = dni
        self.nroCliente = nroCliente
        self.mercaderia = []
        self.servicioAPuerta = False
    #Getters && Setters
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getDni(self):
        return self.dni
    def setDni(self, dni):
        self.dni = dni

    def getNroCliente(self):
        return self.nroCliente
    def setNroCliente(self, nroCliente):
        self.nroCliente = nroCliente

    def getMercaderia(self):
        return self.mercaderia
    def agregarMercaderia(self, mercaderia: Mercaderia):
        self.mercaderia.append(mercaderia)

    def tieneServicioAPuerta(self):
        return self.servicioAPuerta
    def setServicioAPuerta(self, servicioAPuerta):
        self.servicioAPuerta = servicioAPuerta