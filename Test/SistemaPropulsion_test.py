from unittest import TestCase 
from unittest.mock import Mock

from Clases.Barco.SistemaPropulsion.Motor import Motor
from Clases.Barco.SistemaPropulsion.Vela import Vela
from Clases.Barco.BarcoBasico import BarcoBasico
from Clases.Barco.SistemaPropulsion.SistemaPropulsion import SistemaPropulsion


class SistemaPropulsion(TestCase):
    
    def test_gastar_combustible_Vela(self):
        
        vela=Vela()
        tiempo=10

        barco=BarcoBasico()

        barco.set_sistema_Propulsion(vela)
        resultado=barco.get_sistema_Propulsion().gastar_combustible(tiempo)

        self.assertEqual(resultado,0)


    def test_gastar_combustible_Motor(self):

        motor=Motor()
        tiempo=10

        barco=BarcoBasico()

        barco.set_sistema_Propulsion(motor)
        resultado=barco.get_sistema_Propulsion().gastar_combustible(tiempo)

        self.assertEqual(resultado,60)



