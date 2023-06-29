from unittest import TestCase

from mock import Mock
from Clases.Barco.BarcoBasico import BarcoBasico

from Clases.CalculadorPrecio.CalculadorPrecio import CalculadorPrecio
from Clases.Cliente.Cliente import Cliente
from Clases.Contenedores.Ventilado import Ventilado
from Clases.Mercaderia.MercaderiaAlimenticia import MercaderiaAlimenticia
from Clases.Viaje.Viaje import Viaje


class CalculadorPrecioTest(TestCase):

      def test_obtener_precio_completo(self):
            
           
            gps = Mock() 
            gps.calcularkmrecorridos.return_value = 1200

            calculadora = CalculadorPrecio()            
            precio = calculadora.obtener_precio_container_completo(gps.calcularkmrecorridos())

            self.assertEqual(precio,230000)

      def test_obtener_precio_incompleto(self):
            gps = Mock() 
            gps.calcularkmrecorridos.return_value = 12000

            calculadora = CalculadorPrecio()            
            precio = calculadora.obtener_precio_container_incompleto(gps.calcularkmrecorridos())

            self.assertEqual(precio,1500)

      def test_calcular_precio_conteiner_completo(self):
            
            gps = Mock() 
            gps.calcularkmrecorridos.return_value = 12000
            mercaderia_alimenticia = MercaderiaAlimenticia(9541,"Cocos",24000.0,15,10,4,6)
            contenedor = Ventilado(136)
            lucas = Cliente("Lucas",12345678,159)
            lucas.agregarMercaderia(mercaderia_alimenticia)
            contenedor.cargar_mercaderia(lucas.descargarMercaderia())
            
            calculadora = CalculadorPrecio()    
            precio = calculadora.calcularPrecio(contenedor,lucas,gps.calcularkmrecorridos())
            self.assertEqual(precio,250000)

      def test_calcular_precio_conteiner_completo_servicio_puerta(self):
            
            gps = Mock() 
            gps.calcularkmrecorridos.return_value = 12000
            mercaderia_alimenticia = MercaderiaAlimenticia(9541,"Cocos",24000.0,15,10,4,6)
            contenedor = Ventilado(136)
            lucas = Cliente("Lucas",12345678,159)
            lucas.agregarMercaderia(mercaderia_alimenticia)
            lucas.setServicioAPuerta(True)

            contenedor.cargar_mercaderia(lucas.descargarMercaderia())
            
            calculadora = CalculadorPrecio()    
            precio = calculadora.calcularPrecio(contenedor,lucas,gps.calcularkmrecorridos())
            self.assertEqual(precio,270000)

      def test_calcular_precio_conteiner_incompleto(self):
            gps = Mock() 
            gps.calcularkmrecorridos.return_value = 12000
            mercaderia_alimenticia = MercaderiaAlimenticia(9541,"Cocos",5,15,10,4,6)
            contenedor = Ventilado(136)
            lucas = Cliente("Lucas",12345678,159)
            lucas.agregarMercaderia(mercaderia_alimenticia)
            contenedor.cargar_mercaderia(lucas.descargarMercaderia())
            
            calculadora = CalculadorPrecio()  
            precio = calculadora.calcularPrecio(contenedor,lucas,gps.calcularkmrecorridos())

            self.assertEqual(precio,1575)