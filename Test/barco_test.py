from unittest import TestCase
from unittest.mock import Mock
from Clases.Barco.SistemaPropulsion.Motor import Motor
from Clases.Excepciones.NoCombustibleSuficiente import NoCombustibleSuficiente
from Test.GPSMock import GPSMock

from Clases.Barco.BarcoBasico import BarcoBasico
from Clases.Contenedores.Basico import Basico
from Clases.Contenedores.BasicoHC import BasicoHC
from Clases.Contenedores.Contenedor import Contenedor
from Clases.Contenedores.Medida import Medida
from Clases.Despacho.ContenedorManejador import ContenedorManejador
from Clases.Contenedores.ManejadorContenedores import ManejadorContenedores
from Clases.Mercaderia.Mercaderia import Mercaderia
from Clases.Mercaderia.MercaderiaAlimenticia import MercaderiaAlimenticia
from Clases.Mercaderia.MercaderiaNormal import MercaderiaNormal
from Clases.Mercaderia.MercaderiaToxica import MercaderiaToxica
from Clases.Viaje.Viaje import Viaje


class BarcoTest(TestCase):

    def test_obtener_Km_Recorridos(self):
        barcoT = BarcoBasico()
        basico = Basico(189)
        gps = Mock()
        gps.calcularDistancia.return_value = 500  # distancia entre sede y sede en km
        # hrs de viaje TOTALES --> probar con numero > 16 para la excepcion
        gps.calcularTiempoDeViaje.return_value = 12
        
        barcoT.get_viaje().set_km_Recorridos(gps.calcularDistancia())
        km_Recorridos = barcoT.get_viaje().get_km_Recorridos()
        barcoT.cargar_conteiner(basico)
        barcoT.set_km_Total(100)

        barcoT.set_km_Total(barcoT.get_km_Total()+km_Recorridos)
        resultado = barcoT.get_km_Total()

        self.assertEqual(resultado, 600)

    def test_descargar(self):

        conteiner = Basico(910)
        conteiner2 = BasicoHC(700)
        conteiner3 = Basico(799)

        listPrueba = list()
        listPrueba.append(conteiner)
        listPrueba.append(conteiner2)
        listPrueba.append(conteiner3)

        listAux = list()

        while listPrueba:
            contAux = listPrueba.pop(0)
            listAux.append(contAux)

            self.peso_Actual = 0.0

        self.assertIn(conteiner, listAux)
        self.assertIn(conteiner2, listAux)
        self.assertIn(conteiner3, listAux)

    def test_viajar_Alcanza_Combustible(self):
        gps = Mock()  
        gps.calcularTiempoDeViaje.return_value = 120

        barco = BarcoBasico()
        basico = Basico(189)
        barco.cargar_conteiner(basico)
        barco.set_combustible_Actual(10000)
        motor = Motor()
        barco.set_sistema_Propulsion(motor)
        barco.get_viaje().set_horas(gps.calcularTiempoDeViaje())
        horas = barco.get_viaje().get_horas()
        combustible_Gastado = barco.get_sistema_Propulsion().gastar_combustible(horas)
        barco.set_combustible_Actual(barco.get_combustible_Actual(
        ) - combustible_Gastado)  # actualizo el combustible del barco

        self.assertEqual(barco.get_combustible_Actual(),9280)


    def test_no_Combustible_Suficiente(self):
        barco=BarcoBasico()
        barco.set_combustible_Actual(1300)
        motor = Motor()
        barco.set_sistema_Propulsion(motor)
        gps = Mock()  
        gps.calcularTiempoDeViaje.return_value = 1200
        barco.get_viaje().set_horas(gps.calcularTiempoDeViaje())
        horas = barco.get_viaje().get_horas()
        combustible_Gastado = barco.get_sistema_Propulsion().gastar_combustible(horas)
        with self.assertRaises(NoCombustibleSuficiente):
            barco.combustible_suficiente(combustible_Gastado)


    def test_combustible_Restante(self):
        barco=BarcoBasico()
        barco.set_combustible_Actual(13000)
        motor = Motor()
        barco.set_sistema_Propulsion(motor)
        gps = Mock()  
        gps.calcularTiempoDeViaje.return_value = 1200
        barco.get_viaje().set_horas(gps.calcularTiempoDeViaje())
        horas = barco.get_viaje().get_horas()
        combustible_Gastado = barco.get_sistema_Propulsion().gastar_combustible(horas)
        barco.set_combustible_Actual(barco.get_combustible_Actual(
        ) - combustible_Gastado)
        resultado=barco.get_combustible_Actual()


        self.assertEqual(resultado,5800)