
from typing import Container
from unittest import TestCase

from Clases.Contenedores.Basico import Basico
from Clases.Contenedores.BasicoHC import BasicoHC
from Clases.Contenedores.FlatRack import FlatRack
from Clases.Mercaderia.Mercaderia import Mercaderia

class ContenedorTest(TestCase):

    def test_actualizar_espacio_basico(self):
        basico = Basico(1023)
        mercaderia = Mercaderia(102,"Silla",3.0,5.0,25.0,100.0,50.0)

        basico.actualizarEspacio(mercaderia)
        assert basico.get_peso_actual() > 0.0 and basico.get_volumen_actual() > 0.0

    def test_actualizar_espacio_basicohc(self):
        basico = BasicoHC(1023)
        mercaderia = Mercaderia(102,"Silla",3.0,5.0,25.0,100.0,50.0)

        basico.actualizarEspacio(mercaderia)
        assert basico.get_peso_actual() > 0.0 and basico.get_volumen_actual() > 0.0

    def test_actualizar_espacio_flatrack(self):
        basico = FlatRack(1023)
        mercaderia = Mercaderia(102,"Silla",3.0,5.0,25.0,100.0,50.0)

        basico.actualizarEspacio(mercaderia)
        assert basico.get_peso_actual() > 0.0 and basico.get_volumen_actual() > 0.0
