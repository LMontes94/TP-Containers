
from Clases.Contenedores.Medida import Medida


class Mercaderia:
    def __init__(self,id,n,p,v,ancho,alto,largo):
        self.__id = id
        self.__nombre = n
        self.__peso = p 
        self.__volumen = v 
        self.__medida = Medida(ancho,alto,largo)
        self.__es_especial = False 

    def get_id(self):
        return self.__id 
    
    def set_id(self,id):
        self.__id = id 

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,n):
        self.__nombre = n 

    def get_peso(self):
        return self.__peso
    
    def set_peso(self,p):
        self.__peso = p 

    def get_volumen(self):
        return self.__volumen
    
    def set_volumen(self,v):
        self.__volumen = v 

    def get_medida(self):
        return self.__medida
    
    def set_medida(self,ancho,alto,largo):
        self.__medida.set_ancho(ancho)
        self.__medida.set_alto(alto)
        self.__medida.set_largo(largo)

    def get_es_especial(self):
        return self.__es_especial
    
    def is_especial(self,especial):
        self.__es_especial = especial

    id = property(get_id,set_id)
    nombre = property(get_nombre,set_nombre)
    peso = property(get_peso,set_peso)
    volumen = property(get_volumen,set_volumen)
    medida = property(get_medida,set_medida)
    es_especial = property(get_es_especial,is_especial)

    
