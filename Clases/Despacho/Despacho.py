
from Excepciones.ContenerdorLlenoException import ContenedorLlenoException
from Excepciones.ExcesoMedidasException import ExcesoMedidasException
from Excepciones.NoListaBarcosException import NoListaBarcosException
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
        self.containers = [Contenedor()]
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
        return self.containers

    def set_container(self, valor):
        self.containers = valor
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

    def cargarContenedor(self, contenedor,cliente):
        posContenedor = self.buscarContenedor(contenedor)
        
        try:
            for mercaderia in cliente.mercaderia:
                self.containers[posContenedor].validarCargaMercaderia(mercaderia) 
        except ContenedorLlenoException as e:
              print(f"Error {e.get_code} / {e.get_mensaje}")
        except ExcesoMedidasException as e:
               print(f"Error {e.get_code} / {e.get_mensaje}")       


    def mayorbarcoKm (self,barcos):
        
        if not barcos:
            raise NoListaBarcosException("No hay una lista de barcos para realizar la operacion",123)  
        auxBarco=Barco()                
        auxBarco=barcos[0]

        for barco in barcos:
            if barco.km_Recorridos > auxBarco.km_Recorridos:
                auxBarco=barco

        
        print(f"El barco que mayor Km Recorrio fue el barco con id: {auxBarco.id} con {auxBarco.km_Recorridos} kms")




    def menorbarcoKm (self,barcos):
        if not barcos:
            raise NoListaBarcosException("No hay una lista de barcos para realizar la operacion",123)   
          
        auxBarco=Barco()                
        auxBarco=barcos[0]

        for barco in barcos:
            if barco.km_Recorridos < auxBarco.km_Recorridos:
                auxBarco=barco

        
        print(f"El barco que menor Km Recorrio fue el barco con id: {auxBarco.id} con {auxBarco.km_Recorridos} kms")

