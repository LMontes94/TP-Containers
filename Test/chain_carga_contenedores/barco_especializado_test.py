from unittest import TestCase
from Clases.Contenedores.FlatRack import FlatRack
from Clases.Barco.BarcoEspecializado import BarcoEspecializado
from Clases.Excepciones.NoHayBarcoException import NoHayBarcoException
from Clases.Barco.BarcoBasico import BarcoBasico 
from Clases.Contenedores.Basico import Basico
from Clases.Despacho.ContenedorManejador import ContenedorManejador
from Clases.Contenedores.ManejadorContenedores import ManejadorContenedores
from Clases.Mercaderia.Mercaderia import Mercaderia
from Clases.Mercaderia.MercaderiaAlimenticia import MercaderiaAlimenticia
from Clases.Mercaderia.MercaderiaNormal import MercaderiaNormal
from Clases.Mercaderia.MercaderiaToxica import MercaderiaToxica

class BarcoEspecializadoTest(TestCase):
    
    def test_set_max_peso(self):
        barco = BarcoEspecializado()
        barco.set_max_Peso(120000.0)
        self.assertEqual(barco.get_max_Peso(), 120000.0)
        
    def test_verifica_carga_contenedor(self):
    # Crear una instancia de BarcoEspecializado
      barco = BarcoEspecializado()
      barco.set_max_Peso(120000)
      barco.set_max_Containers(10)

    # Crear un contenedor que puede ser cargado por el barco
      contenedor = FlatRack(1)

    # Verificar que el contenedor puede ser cargado por el barco
      self.assertTrue(barco.verificar_carga_contenedor(contenedor))

    def test_puede_cargar_contenedor(self):
         # Crear una instancia de BarcoEspecializado
      barco = BarcoEspecializado()
      barco.set_max_Peso(120000)
      barco.set_max_Containers(10)

    # Crear un contenedor que puede ser cargado por el barco
      contenedor = FlatRack(1)
      
      self.assertTrue(barco.puede_cargar_contenedor(contenedor))
   
    def test_manejar_contenedor(self):
     # Crear una instancia de BarcoEspecializado
      barco = BarcoEspecializado()
      barco.set_max_Peso(120000)
      barco.set_max_Containers(10)

    # Crear un contenedor que puede ser cargado por el barco
      contenedor = FlatRack(1)
      barco.manejar(contenedor)
      self.assertIn(contenedor,barco.get_conteiner())
      
    def test_hay_siguiente(self):
        barco = BarcoEspecializado()
        barcoBasico = BarcoEspecializado()
        
        barco.set_siguiente(barcoBasico)
        self.assertTrue(barco.noHaySiguiente())
        
    def test_no_hay_siguiente(self):
        barco = BarcoEspecializado()
        with self.assertRaises(NoHayBarcoException):          
          barco.noHaySiguiente()
          
    def test_pasar_contenedor_al_siguiente(self):
     # Crear una instancia de BarcoEspecializado
      barco = BarcoEspecializado()
      barco.set_max_Peso(120000)
      barco.set_max_Containers(10)
      
      barco1 = BarcoBasico()
      barco1.set_max_Peso(100000)
      barco1.set_max_Containers(8)
      
      contenedor = Basico(1)
      
      barco.set_siguiente(barco1)
      barco.manejar(contenedor)
      
      
      self.assertIn(contenedor,barco1.get_conteiner())
      