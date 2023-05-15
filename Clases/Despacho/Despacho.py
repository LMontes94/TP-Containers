
from Cliente import Cliente
from Contenedores import Contenedor
from Barco import Barco
from Camion import Camion


class Despacho:

    MAX_CAMIONES = 5

    def __init__(self):
        self.cliente = []
        self.retiro = False  # revisar!!
        self.conteiner_Completo = False
        self.containers = []
        self.barcos = []
        self.camiones = [Camion() for _ in range(Despacho.MAX_CAMIONES)]


# ------------Getters & setters------------

# Getters & setters cliente


    def get_cliente(self):
        return self.cliente

    def set_cliente(self, valor):
        self.cliente = valor
    cliente = property(get_cliente, set_cliente)

# Getters & setters retiro

    def get_retiro(self):
        return self.retiro

    def set_retiro(self, valor):
        self.retiro = valor
    retiro = property(get_retiro, set_retiro)

# Getters & setters conteinerCompleto

    def get_conteiner_Completo(self):
        return self.conteiner_Completo

    def set_conteiner_Completo(self, valor):
        self.conteiner_Completo = valor
    conteiner_Completo = property(
        get_conteiner_Completo, set_conteiner_Completo)

# Getters & setters conteiner
    def get_container(self):
        return self.container

    def set_container(self, valor):
        self.container = valor
    container = property(get_container, set_container)

# Getters & setters Barco :Lista

    def get_barcos(self):
        return self.barcos

    def set_barcos(self, valor):
        self.barcos = valor
    barcos = property(get_barcos, set_barcos)

# Getters & setters camiones:Lista

    def get_camiones(self):
        return self.camiones

    def set_camiones(self, valor):
        self.camiones = valor
    camiones = property(get_camiones, set_camiones)


# ------------Getters & setters------------
# ............................................
# ------------Funciones---------------------


    def buscarContenedor(self, contenedor):
        return self.containers.index(contenedor)

    def cargarContenedor(self, contenedor):

        posContenedor = self.buscarContenedor(contenedor)
