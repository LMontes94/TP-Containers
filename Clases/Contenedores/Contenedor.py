from abc import ABC
import Medida

class Contenedor:

    id=0
    interior=Medida
    exterior=Medida
    pies=0
    max_Peso=0.0
    max_Volumen=0.0
    precio_Base=0.0
    hay_Espacio=False
    es_Especial=False

#------------Getters & setters------------

#Getters & setters id

    def get_id(self):
        return self.id
    def set_id(self,valor):
        self.id=valor
    id=property(get_id,set_id)

#Getters & setters interior
    
    def get_interior(self):
        return self.interior
    def set_interior(self,valor):
        self.interior=valor
    interior=property(get_interior,set_interior)

#Getters & setters exterior
    
    def get_exterior(self):
        return self.exterior
    def set_exterior(self,valor):
        self.exterior=valor
    exterior=property(get_exterior,set_exterior)

#Getters & setters pies
    
    def get_pies(self):
        return self.pies
    def set_pies(self,valor):
        self.pies=valor
    pies=property(get_pies,set_pies)

#Getters & setters maxPeso
    
    def get_max_Peso(self):
        return self.max_Peso
    def set_max_Peso(self,valor):
        self.max_Peso=valor
    max_Peso=property(get_max_Peso,set_max_Peso)

#Getters & setters maxVolumen
    
    def get_max_Volumen(self):
        return self.max_Volumen
    def set_max_Volumen(self,valor):
        self.max_Volumen=valor
    max_Volumen=property(get_max_Volumen,set_max_Volumen)

#Getters & setters precioBase
    
    def get_precio_Base(self):
        return self.precio_Base
    def set_precio_Base(self,valor):
        self.precio_Base=valor
    precio_Base=property(get_precio_Base,set_precio_Base)    

#Getters & setters hayEspacio

    def get_hay_Espacio(self):
        return self.hay_Espacio
    def set_hay_Espacio(self,valor):
        self.hay_Espacio=valor
    hay_Espacio=property(get_hay_Espacio,set_hay_Espacio)

#Getters & setters esEspecial

    def get_es_Especial(self):
        return self.es_Especial
    def set_es_Especial(self,valor):
        self.es_Especial=valor
    es_Especial=property(get_es_Especial,set_es_Especial)     

#------------Getters & setters------------
#............................................
#------------Funciones------------

    @abstractmethod
    def calcularPrecio(self):
        return 0.0
    
    @abstractmethod
    def calcularEspacio(self):
        pass
    
