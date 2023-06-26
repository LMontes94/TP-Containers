from unittest import TestCase 
from unittest.mock import Mock

from Clases.Barco.Motor import Motor
from Clases.Barco.Vela import Vela
from Clases.Barco.BarcoBasico import BarcoBasico


class SistemaPropulsionTest(TestCase):

    def test_probando_Motor(self):

        barcoBasico = BarcoBasico()

        assert barcoBasico.get_combustible_Actual() == 100 #comprobamos que el barco se inicializa con 100 litros de combustible

        motor = Motor() # gasta 6 litros por hora
        vela = Vela() # gasta 0 litros cuando es usada

        barcoBasico.set_sistema_Propulsion(motor)

        barcoBasico.viajar(6) # le pasamos 6 horas de viaje, va a modificar el combustibleActual del barco

        assert barcoBasico.get_combustible_Actual() == 64
        assert barcoBasico.get_sistema_Propulsion() == "Motor"

        barcoBasico.set_sistema_Propulsion(vela)

        barcoBasico.viajar(4) #viaja cuatro horas mas pero con el sistema de vela

        assert barcoBasico.get_combustible_Actual() == 64
        assert barcoBasico.get_sistema_Propulsion() == "Vela"
