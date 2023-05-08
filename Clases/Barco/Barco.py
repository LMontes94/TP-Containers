from Contenedores import Contenedor
from abc import ABC

class Barco:

    id=0
    max_Containers=0
    max_Peso=0.0
    conteiner = list (Contenedor())
    sede_Inicial=''
    sede_Final=''
    km_Recorridos=0.0



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

    #getters y setters kmsRecorridos
    def get_km_Recorridos(self):
        return self.km_Recorridos
    
    def set_km_Recorridos(self,valor):
        self.km_Recorridos=valor

    km_Recorridos= property(get_km_Recorridos,set_km_Recorridos)    

#--------Getters & Setters-----------------   
#  ...........................
#-----------Funciones-----------

    @abstractmethod
    def cargar(self):
        return 0

    @abstractmethod
    def descargar(self):
        return 0






