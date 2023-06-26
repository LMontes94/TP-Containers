from Clases.Contenedores.Contenedor import Contenedor
from Clases.Barco.Vela import Vela
from Clases.Barco.Motor import Motor
from abc import ABC , abstractmethod

class Barco(ABC):

    def __init__(self):
        self.__id=''
        self.__max_Containers= ''
        self.__max_Peso=''

        self.__conteiner = list()
        self.__sede_Inicial=''
        self.__sede_Final=''
        self.__km_Total=0.0
        self.__es_Especial=False
        self.__peso_Actual=0.0
        self.__combustible_Actual = 100
        self.__sistema_Propulsion = None


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

    
    #getters y setters sedeInicial
    def get_sede_Inicial(self):
        return self.__sede_Inicial
    
    def set_sede_Inicial(self,valor):
        self.__sede_Inicial=valor

    sede_Inicial= property(get_sede_Inicial,set_sede_Inicial)

    #getters y setters sedeFinal
    def get_sede_Final(self):
        return self.__sede_Final
    
    def set_sede_Final(self,valor):
        self.__sede_Final=valor

    sede_Final= property(get_sede_Final,set_sede_Final)
    
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
  
#--------Getters & Setters-----------------   
#  ...........................
#-----------Funciones-----------


    #funcion para los Sistemas_Propulsion

    def viajar(self, tiempo):
        combustible_Gastado = self.__sistema_Propulsion.gastar_combustible(tiempo)
        self.set_combustible_Actual(combustible_Gastado) #actualizo el combustible del barco
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

