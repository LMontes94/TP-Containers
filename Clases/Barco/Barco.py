from Clases.Contenedores.Contenedor import Contenedor
from abc import ABC , abstractmethod

class Barco(ABC):

    def __init__(self):
        self.id=0
        self.max_Containers=0
        self.max_Peso=0.0
        self.conteiner = list (Contenedor())
        self.sede_Inicial=''
        self.sede_Final=''
        self.km_Total=0.0
        self.es_Especial=False
        self.peso_Actual=0.0



#--------Getters & Setters-----------------
    #getters y setters id
    def get_id(self):
        return self.id
    
    def set_id(self,valor):
        self.id=valor
    
    id= property(get_id,set_id)

    #getters y setters maxContainers
    def get_max_Containers(self):
        return self.max_Containers
    
    def set_max_Containers(self,valor):
        self.max_Containers=valor

    max_Containers= property(get_max_Containers,set_max_Containers)


    #getters y setters maxPeso
    def get_max_Peso(self):
        return self.max_Peso
    
    def set_max_Peso(self,valor):
        self.max_Containers=valor

    max_Containers= property(get_max_Peso,set_max_Peso)

    
    #getters y setters conteiner
    def get_conteiner(self):
        return self.conteiner
    
    def set_conteiner(self,valor):
        self.conteiner=valor

    conteiner= property(get_conteiner,set_conteiner)

    
    #getters y setters sedeInicial
    def get_sede_Inicial(self):
        return self.sede_Inicial
    
    def set_sede_Inicial(self,valor):
        self.sede_Inicial=valor

    sede_Inicial= property(get_sede_Inicial,set_sede_Inicial)

    #getters y setters sedeFinal
    def get_sede_Final(self):
        return self.sede_Final
    
    def set_sede_Final(self,valor):
        self.sede_Final=valor

    sede_Final= property(get_sede_Final,set_sede_Final)
    
#getters y setters kmsTotal
    def get_km_Total(self):
        return self.km_Total
    
    def set_km_Total(self,valor):
        self.km_Total=valor

    km_Total= property(get_km_Total,set_km_Total)    

#getters y setters es_Especial
    def get_es_Especial(self):
        return self.es_Especial
    
    def set_es_Especial(self,valor):
        self.es_Especial=valor

    es_Especial= property(get_es_Especial,set_es_Especial)    

    #getters y setters pesoActual

    def get_peso_Actual(self):
        return self.peso_Actual
    def set_peso_Actual(self,valor):
        self.peso_Actual=valor
    peso_Actual=property(get_peso_Actual,set_peso_Actual)    


#--------Getters & Setters-----------------   
#  ...........................
#-----------Funciones-----------

    @abstractmethod
    def descargar(self):
        pass

    @abstractmethod
    def obtenerKmRecorridos(self):
        pass

