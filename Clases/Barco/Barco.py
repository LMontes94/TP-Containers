from Clases.Contenedores.Contenedor import Contenedor
from Clases.Barco.SistemaPropulsion.SistemaPropulsion import SistemaPropulsion
from Clases.Despacho.ContenedorManejador import ContenedorManejador
from Clases.Viaje.Viaje import Viaje
from Clases.Excepciones.NoCombustibleSuficiente import NoCombustibleSuficiente
from Clases.Mercaderia.Mercaderia import Mercaderia

from abc import ABC , abstractmethod

class Barco(ContenedorManejador):

    def __init__(self):
        self.__id=''
        self.__max_Containers=0.0
        self.__max_Peso=0.0
        self.__conteiner = [self.get_max_Containers()]
        self.__viaje = Viaje()
        self.__km_Total=0.0
        self.__es_Especial=False
        self.__peso_Actual=0.0
        self.__combustible_Max=100
        self.__combustible_Actual = self.__combustible_Max
        self.__sistema_Propulsion = None
        self.__siguiente = None


#--------Getters & Setters-----------------
    #getters y setters id
    def get_id(self):
        return self.__id
    
    def set_id(self,valor):
        self.__id=valor
    
    id= property(get_id,set_id)

    #getters y setters maxContainers
    def get_max_Containers(self):
        return self.__max_Containers
    
    def set_max_Containers(self,valor):
        self.__max_Containers=valor

    max_Containers= property(get_max_Containers,set_max_Containers)


    #getters y setters maxPeso
    def get_max_Peso(self):
        return self.__max_Peso
    
    def set_max_Peso(self,valor):
        self.__max_Peso=valor

    max_Containers= property(get_max_Peso,set_max_Peso)

    
    #getters y setters conteiner
    def get_conteiner(self):
        return self.__conteiner
    
    def cargar_conteiner(self,valor):
        self.__conteiner.append(valor)
        self.peso_Actual += valor.get_peso_actual()

    conteiner= property(get_conteiner,cargar_conteiner)


    #getters y setters Viaje
    def get_viaje(self):
        return self.__viaje
    
    def set_viaje(self,valor):
        self.__viaje=valor

    viaje= property(get_viaje,set_viaje)    
    
   
   
    
#getters y setters kmsTotal
    def get_km_Total(self):
        return self.__km_Total
    
    def set_km_Total(self,valor):
        self.__km_Total=valor

    km_Total= property(get_km_Total,set_km_Total)    

#getters y setters es_Especial
    def get_es_Especial(self):
        return self.__es_Especial
    
    def set_es_Especial(self,valor):
        self.__es_Especial=valor

    es_Especial= property(get_es_Especial,set_es_Especial)    

    #getters y setters pesoActual

    def get_peso_Actual(self):
        return self.__peso_Actual
    def set_peso_Actual(self,valor):
        self.__peso_Actual=valor
    peso_Actual=property(get_peso_Actual,set_peso_Actual)    

    #getters y setters Sistema_Propulsion
    def get_sistema_Propulsion(self):
        return self.__sistema_Propulsion

    def set_sistema_Propulsion(self, sistema_Propulsion):
        self.__sistema_Propulsion = sistema_Propulsion

    sistema_Propulsion = property(get_sistema_Propulsion, set_sistema_Propulsion)    

    # getters y setters de combustible_Actual 
    def get_combustible_Actual(self):
        return self.__combustible_Actual 
    
    def set_combustible_Actual(self, restarCombustible):
        self.__combustible_Actual -= restarCombustible


    # getters y setters de combustible_Max
    def get_combustible_Max(self):
        return self.__combustible_Max
    
    def set_combustible_Actual(self, Max):
        self.__combustible_Max=Max
        
    def get_siguiente(self):
        return self.__siguiente
    
    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente
        
    siguiente = property(get_siguiente,set_siguiente)
  
#--------Getters & Setters-----------------   
#  ...........................
#-----------Funciones-----------


    #funcion para los Sistemas_Propulsion

    def activar(self):
        return self.__sistema_Propulsion.avanzar()
    
    def sistema_Propulsion_Actual(self):
        print(f"El barco esta trabajando con el sistema de Propulsion a {self.__sistema_Propulsion.get_nombre()}") 

    def combustible_Restante(self):
        print("::::CALCULANDO COMBUSTIBLE RESTANTE ::::::")  
        print(f"Combustible Restante: {self.get_combustible_Actual}")

    
    def combustible_suficiente(self,combustible_Gastado):
        if combustible_Gastado > self.get_combustible_Actual():
            raise NoCombustibleSuficiente("No hay combustible suficiente para realizar el viaje a motor, cambiar a vela si es que se tiene una",912)  
        return True
    
    def viajar(self):
        
        try:
           combustible_Gastado = self.get_sistema_Propulsion().gastar_combustible(self.__viaje.get_horas())
           self.combustible_suficiente(combustible_Gastado)
           self.set_combustible_Actual(self.get_combustible_Actual()- combustible_Gastado) #actualizo el combustible del barco
           self.combustible_Restante()
        except NoCombustibleSuficiente as e:
            print(f"Error {e.get_code()} / {e.get_mensaje()}")
            
        '''Maia: aca tengo que actualizar los datos de la clase Viaje() que tiene el
            combustible que se utilizó aun no le agregue este atributo porque tengo que ver
            la mejor manera de organizarlo para que interactue con el Módulo Contable
        '''
    
    def verificar_carga_contenedor(self, contenedor):
       return contenedor.get_max_Peso() < self.get_max_Peso() and len(
            self.get_conteiner()) < self.get_max_Containers()
    
    @abstractmethod
    def descargar(self):
        pass

    @abstractmethod
    def obtenerKmRecorridos(self):
        pass

    @abstractmethod
    def manejar(self, contenedor):
        pass