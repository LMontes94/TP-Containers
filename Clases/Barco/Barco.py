from Clases.Contenedores.Contenedor import Contenedor
from Clases.Barco.SistemaPropulsion.SistemaPropulsion import SistemaPropulsion
from Clases.Viaje.Viaje import Viaje
from Clases.Excepciones.NoCombustibleSuficiente import NoCombustibleSuficiente
from abc import ABC , abstractmethod

class Barco(ABC):

    def __init__(self):
        self.__id=''
        self.__max_Containers= ''
        self.__max_Peso=''
        self.__conteiner = list()
        self.__viaje = Viaje()
        self.__km_Total=0.0
        self.__es_Especial=False
        self.__peso_Actual=0.0
        self.__combustible_Max=100
        self.__combustible_Actual = self.__combustible_Max
        self.__sistema_Propulsion = SistemaPropulsion()


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
        self.__max_Containers=valor

    max_Containers= property(get_max_Peso,set_max_Peso)

    
    #getters y setters conteiner
    def get_conteiner(self):
        return self.__conteiner
    
    def cargar_conteiner(self,valor):
        self.__conteiner.append(valor)

    conteiner= property(get_conteiner,cargar_conteiner)


    #getters y setters Viaje
    def get_viaje(self):
        return self.__viaje
    
    def set_viaje(self,valor):
        self.__viaje=valor

    km_Total= property(get_viaje,set_viaje)    
    
   
   
    
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
        return self.__sistema_Propulsion.get_nombre()

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


    def viajar(self):

        combustible_Gastado = self.__sistema_Propulsion.gastar_combustible(self.__viaje.get_horas())
        if combustible_Gastado > self.get_combustible_Actual():
            raise NoCombustibleSuficiente("No hay combustible suficiente para realizar el viaje a motor, cambiar a vela si es que se tiene una",912)  
        self.set_combustible_Actual(self.get_combustible_Actual()- combustible_Gastado) #actualizo el combustible del barco
        self.combustible_Restante()
        
        '''Maia: aca tengo que actualizar los datos de la clase Viaje() que tiene el
            combustible que se utilizó aun no le agregue este atributo porque tengo que ver
            la mejor manera de organizarlo para que interactue con el Módulo Contable
        '''

    @abstractmethod
    def descargar(self):
        pass

    @abstractmethod
    def obtenerKmRecorridos(self):
        pass

