from unittest import TestCase 
from unittest.mock import Mock

from Clases.Barco.SistemaPropulsion.Motor import Motor
from Clases.Barco.SistemaPropulsion.Vela import Vela
from Clases.Barco.BarcoBasico import BarcoBasico
from Clases.Barco.SistemaPropulsion.SistemaPropulsion import SistemaPropulsion
from Clases.Contenedores.ManejadorContenedores import ManejadorContenedores
from Clases.Viaje.Viaje import Viaje


class SistemaPropulsion(TestCase):
    
    def test_gastar_combustible_Vela(self):
        
        vela=Vela()
        tiempo=10

        barco=BarcoBasico()

        barco.set_sistema_Propulsion(vela)
        resultado=barco.get_sistema_Propulsion().gastar_combustible(tiempo)

        self.assertEqual(resultado,0)


    def test_gastar_combustible_Motor(self):
        
        motor = Motor()
        tiempo = 10

        barco = BarcoBasico()
        barco.set_sistema_Propulsion(motor)

        resultado = barco.get_sistema_Propulsion().gastar_combustible(tiempo)
        
        self.assertEqual(resultado,60)

    def test_viajar(self):

        barco = BarcoBasico()

        viaje = Viaje()

        gps = Mock()
        gps.calcularDistancia.return_value = 500 #distancia entre sede y sede en km
        gps.calcularTiempoDeViaje.return_value = 12 #hrs de viaje TOTALES --> probar con numero > 16 para la excepcion

        viaje.set_sede_inicial("sedeNro1")
        viaje.set_sede_final("sedeDestinoNro2")
        viaje.set_km_Recorridos(gps.calcularDistancia())
        viaje.set_horas(gps.calcularTiempoDeViaje())

        barco.set_viaje(viaje)
        #self.assertEquals(barco.get_viaje().get_horas(), 12) me da que el barco tiene una clase viaje con un tiempo de 12 hrs
        
        vela = Vela()
        motor = Motor()
        
        barco.set_sistema_Propulsion(motor)
        
        barco.viajar()
        self.assertEqual(barco.get_combustible_Actual(), 28) #compruebo que se gasto y actualizo el combustible 



