
from unittest import TestCase

from Clases.Contenedores.Basico import Basico
from Clases.Contenedores.BasicoHC import BasicoHC
from Clases.Contenedores.FlatRack import FlatRack
from Clases.Mercaderia.Mercaderia import Mercaderia
from Clases.Despacho.ContenedorManejador import ContenedorManejador
from Clases.Contenedores.ManejadorContenedores import ManejadorContenedores
from Clases.Mercaderia.MercaderiaAlimenticia import MercaderiaAlimenticia
from Clases.Mercaderia.MercaderiaNormal import MercaderiaNormal
from Clases.Mercaderia.MercaderiaToxica import MercaderiaToxica


class ContenedorTest(TestCase):

    def test_actualizar_espacio_basico(self):
        basico = Basico(1023)
        mercaderia = Mercaderia(102, "Silla", 3.0, 5.0, 25.0, 100.0, 50.0)

        basico.actualizarEspacio(mercaderia)
        assert basico.get_peso_actual() > 0.0 and basico.get_volumen_actual() > 0.0

    def test_actualizar_espacio_basicohc(self):
        basico = BasicoHC(1023)
        mercaderia = Mercaderia(102, "Silla", 3.0, 5.0, 25.0, 100.0, 50.0)

        basico.actualizarEspacio(mercaderia)
        assert basico.get_peso_actual() > 0.0 and basico.get_volumen_actual() > 0.0

    def test_actualizar_espacio_flatrack(self):
        basico = FlatRack(1023)
        mercaderia = Mercaderia(102, "Silla", 3.0, 5.0, 25.0, 100.0, 50.0)

        basico.actualizarEspacio(mercaderia)

        assert basico.get_peso_actual() > 0.0 and basico.get_volumen_actual() > 0.0

    def test_validar_carga_mercaderia_basico(self):
        basico = Basico(1023)
        mercaderia = Mercaderia(102, "Silla", 3.0, 5.0, 1.0, 2.0, 5.0)

        # Verificamos que no se lance ninguna excepción
        try:
            basico.validarCargaMercaderia(mercaderia)
        except Exception as e:
            self.fail(f"Hubo una excepción: {e}")

    def test_validar_carga_mercaderia_basicohc(self):
        basico = BasicoHC(1023)
        mercaderia = Mercaderia(102, "Silla", 3.0, 5.0, 1.0, 2.0, 5.0)

        # Verificamos que no se lance ninguna excepción
        try:
            basico.validarCargaMercaderia(mercaderia)
        except Exception as e:
            self.fail(f"Hubo una excepción: {e}")

    def test_validar_carga_mercaderia_flatrack(self):
        basico = FlatRack(1023)
        mercaderia = Mercaderia(102, "Silla", 3.0, 5.0, 1.0, 2.0, 5.0)

        # Verificamos que no se lance ninguna excepción
        try:
            basico.validarCargaMercaderia(mercaderia)
        except Exception as e:
            self.fail(f"Hubo una excepción: {e}")

    def test_validar_unica_cargaok(self):
        basico = Basico(1023)
        mercaderia1 = Mercaderia(102, "Silla", 3.0, 5.0, 1.0, 2.0, 5.0)
        mercaderia2 = Mercaderia(102, "Silla", 3.0, 5.0, 1.0, 2.0, 5.0)
        mercaderia3 = Mercaderia(102, "Silla", 3.0, 5.0, 1.0, 2.0, 5.0)

        basico.cargar_mercaderia(mercaderia1)
        basico.cargar_mercaderia(mercaderia2)
        basico.cargar_mercaderia(mercaderia3)

        assert basico.validarUnicaCarga

    def test_not_validar_unica_carga(self):
        basico = FlatRack(1023)
        mercaderia1 = Mercaderia(102, "Silla", 3.0, 5.0, 1.0, 2.0, 5.0)
        mercaderia2 = Mercaderia(100, "Mesa", 3.0, 5.0, 1.0, 2.0, 5.0)
        mercaderia3 = Mercaderia(10010, "Pelota", 3.0, 5.0, 1.0, 2.0, 5.0)

        basico.validarCargaMercaderia(mercaderia1)
        basico.validarCargaMercaderia(mercaderia2)
        basico.validarCargaMercaderia(mercaderia3)

        assert not basico.validarUnicaCarga()
