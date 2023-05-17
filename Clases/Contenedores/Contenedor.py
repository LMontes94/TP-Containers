from abc import ABC, abstractmethod

from Clases.Contenedores.Medida import Medida
from Clases.Excepciones.ContenerdorLlenoException import ContenedorLlenoException
from Clases.Excepciones.ExcesoMedidasException import ExcesoMedidasException
from Clases.Mercaderia.Mercaderia import Mercaderia


class Contenedor(ABC):

    def __init__(self, id, int_ancho, int_alto, int_largo, ext_ancho, ext_alto, ext_largo):
        self.__id = id
        self.__interior = Medida(int_ancho, int_alto, int_largo)
        self.__exterior = Medida(ext_ancho, ext_alto, ext_largo)
        self.__pies = 0
        self.__max_peso = 0.0
        self.__max_volumen = 0.0
        self.__precio_base = 0.0
        self.__hay_espacio = False
        self.__es_especial = False
        self.__mercaderia = []
        self.__peso_actual = 0.0
        self.__volumen_actual = 0.0
        self.__unica_carga = False



# ------------Getters & setters------------


    def get_id(self):
        return self.__id

    def set_id(self, valor):
        self.__id = valor

    def get_interior(self):
        return self.__interior

    def set_interior(self, valor):
        self.__interior = valor

    def get_exterior(self):
        return self.__exterior

    def set_exterior(self, valor):
        self.__exterior = valor

    def get_pies(self):
        return self.__pies

    def set_pies(self, valor):
        self.__pies = valor

    def get_max_Peso(self):
        return self.__max_peso

    def set_max_Peso(self, valor):
        self.__max_peso = valor

    def get_max_Volumen(self):
        return self.__max_volumen

    def set_max_Volumen(self, valor):
        self.__max_volumen = valor

    def get_precio_Base(self):
        return self.__precio_base

    def set_precio_Base(self, valor):
        self.__precio_base = valor

    def get_hay_Espacio(self):
        return self.__hay_espacio

    def is_space(self):
        return self.__peso_actual < self.__max_peso and self.__volumen_actual < self.__max_volumen

    def get_es_Especial(self):
        return self.__es_especial

    def es_Especial(self, valor):
        self.__es_especial = valor

    def get_mercaderia(self):
        return self.__mercaderia

    def cargar_mercaderia(self, mercaderia):
        self.__mercaderia.append(mercaderia)
        self.actualizarEspacio(mercaderia)

    def get_peso_actual(self):
        return self.__peso_actual

    def set_peso_actual(self, peso):
        self.__peso_actual = peso

    def get_volumen_actual(self):
        return self.__volumen_actual

    def set_volumen_actual(self, v):
        self.__volumen_actual = v

    def get_unica_carga(self):
        return self.__unica_carga

    def es_unica_carga(self):
        self.validarUnicaCarga()

    id = property(get_id, set_id)
    interior = property(get_interior, set_interior)
    exterior = property(get_exterior, set_exterior)
    max_Volumen = property(get_max_Volumen, set_max_Volumen)
    max_Peso = property(get_max_Peso, set_max_Peso)
    pies = property(get_pies, set_pies)
    hay_espacio = property(get_hay_Espacio, is_space)
    precio_base = property(get_precio_Base, set_precio_Base)
    es_especial = property(get_es_Especial, es_Especial)
    mercaderia = property(get_mercaderia, cargar_mercaderia)
    peso_actual = property(get_peso_actual, set_peso_actual)
    volumen_actual = property(get_peso_actual, set_peso_actual)
    unica_carga = property(get_unica_carga, es_unica_carga)

# ------------Getters & setters------------
# ............................................
# ------------Funciones------------

    def actualizarEspacio(self, mercaderia):
        self.__peso_actual += mercaderia.get_peso()
        self.__volumen_actual += mercaderia.get_volumen()

    def validarUnicaCarga(self):
        primer_cargado = self.__mercaderia[0]
        for mercaderia in self.__mercaderia:
            if not primer_cargado.id == mercaderia:
                return False
        return True
    
    def validarCargaMercaderia(self, mercaderia):
        if not self.get_hay_Espacio() :
            raise ContenedorLlenoException("El contenedor esta lleno!!", 302)
        elif self.__interior.ancho < mercaderia.ancho or self.__interior.alto < mercaderia.alto or self.__interio.largo < mercaderia.largo:
            raise ExcesoMedidasException(f"Las medidas de la {mercaderia.nombre} exceden el limite!!",303)
        else:
            self.cargar_mercaderia(mercaderia)
            