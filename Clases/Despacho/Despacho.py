
from Clases.Excepciones.ContenedorNoEncontradoException import ContenedorNoEncontradoExcpetion
from Clases.Excepciones.ContenerdorLlenoException import ContenedorLlenoException
from Clases.Excepciones.ExcesoMedidasException import ExcesoMedidasException
from Clases.Excepciones.NoListaBarcosException import NoListaBarcosException
from Clases.Cliente.Cliente import Cliente
from Clases.Contenedores.Contenedor import Contenedor
from Clases.Barco.Barco import Barco
from Clases.Camion.Camion import Camion
from Clases.Excepciones.SinUnicaCargaException import SinUnicaCargaExcpetion
from Clases.Mercaderia.Mercaderia import Mercaderia

class Despacho:

    MAX_CAMIONES = 5

    def __init__(self):
        self.__cliente = []
        self.__retiro = False  # revisar!!
        self.__conteiner_Completo = False
        self.__containers = []
        self.__barcos = []
        self.__camiones = []


# ------------Getters & setters------------

# Getters & setters cliente


    def get_cliente(self):
        return self.__cliente

    def agregar_cliente(self, valor):
        self.__cliente.append(valor)
    cliente = property(get_cliente, agregar_cliente)

# Getters & setters retiro

    def get_retiro(self):
        return self.__retiro

    def set_retiro(self, valor):
        self.__retiro = valor
    retiro = property(get_retiro, set_retiro)

# Getters & setters conteinerCompleto

    def get_conteiner_Completo(self):
        return self.__conteiner_Completo

    def set_conteiner_Completo(self, valor):
        self.__conteiner_Completo = valor
    conteiner_Completo = property(
        get_conteiner_Completo, set_conteiner_Completo)

# Getters & setters conteiner
    def get_containers(self):
        return self.__containers

    def agregar_container(self, valor):
        self.__containers.append(valor)
    containers = property(get_containers, agregar_container)

# Getters & setters Barco :Lista

    def get_barcos(self):
        return self.__barcos

    def agregar_barcos(self, valor):
        self.__barcos.append(valor) 
    barcos = property(get_barcos,agregar_barcos)

# Getters & setters camiones:Lista

    def get_camiones(self):
        return self.__camiones

    def agregar_camiones(self, valor):
        self.__camiones.append(valor)
    camiones = property(get_camiones, agregar_camiones)


# ------------Getters & setters------------
# ............................................
# ------------Funciones---------------------


    def buscarContenedor(self, contenedor):
        pos =  self.__containers.index(contenedor)
        if pos > -1:
            return pos 
        raise ContenedorNoEncontradoExcpetion("El contenedor no se encuentra en nuesta lista de contenedores!!")                
        
    def cargarContenedor(self, contenedor,cliente):
        try:
            posContenedor = self.buscarContenedor(contenedor)
            for mercaderia in cliente.mercaderia:
                self.__containers[posContenedor].validarCargaMercaderia(mercaderia) 
        except ContenedorNoEncontradoExcpetion as e:
               print(f"Error {e.get_code()} / {e.get_mensaje}")
        except ContenedorLlenoException as e:
              print(f"Error {e.get_code()} / {e.get_mensaje()}")
        except ExcesoMedidasException as e:
               print(f"Error {e.get_code()} / {e.get_mensaje()}")       


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


    
    def verificarCargaBarco (self,conteiner):  
            
      flag=False
      i=0

      while self.barcos() and flag!=True:
         
         if conteiner.__es_especial ==True and self.barcos[i].es_Especial == True:

            if ((conteiner.__peso_actual+self.barcos[i].peso_Actual) <= self.barcos[i].max_Peso) and len(self.barcos[i].get_conteiner()) < self.barcos[i].max_Containers :


                self.barcos[i].cargar_contenedor(conteiner)
                flag=True

         elif conteiner.__es_especial == False and  self.barcos[i].es_Especial == False: 

             if ((conteiner.__peso_actual+self.barcos[i].peso_Actual) <= self.barcos[i].max_Peso) and len(self.barcos[i].get_conteiner()) < self.barcos[i].max_Containers :


                self.barcos[i].cargar_contenedor(conteiner)
                flag=True

         i=i+1


      











