
from unittest import TestCase
from Clases.Barco.Barco import Barco
from Clases.Contenedores.Basico import Basico
from Clases.Contenedores.BasicoHC import BasicoHC
from Clases.Contenedores.Contenedor import Contenedor
from Clases.Contenedores.FlatRack import FlatRack
from Clases.Contenedores.OpenTop import OpenTop
from Clases.Contenedores.Ventilado import Ventilado
from Clases.Excepciones.NoListaBarcosException import NoListaBarcosException
from Clases.Despacho.Despacho import Despacho
from Clases.Cliente.Cliente import Cliente
from Clases.Barco.BarcoBasico import BarcoBasico
from Clases.Despacho.ContenedorManejador import ContenedorManejador
from Clases.Contenedores.ManejadorContenedores import ManejadorContenedores
from Clases.Mercaderia.Mercaderia import Mercaderia
from Clases.Mercaderia.MercaderiaAlimenticia import MercaderiaAlimenticia
from Clases.Mercaderia.MercaderiaNormal import MercaderiaNormal
from Clases.Mercaderia.MercaderiaToxica import MercaderiaToxica


class DespachoTest(TestCase):
    
    def test_buscar_contenedor(self):
        despacho = Despacho()
        basico = Basico(103)
        basicoHC = BasicoHC(1055)
        flatrack = FlatRack(203)
        
        despacho.agregar_container(basico)
        despacho.agregar_container(basicoHC)
        despacho.agregar_container(flatrack)
        
        assert despacho.buscarContenedor(basicoHC) > -1 
        
    def test_cargar_contenedor(self):
        despacho = Despacho()
        basico = Basico(103)
        basicoHC = BasicoHC(1055)
        flatrack = FlatRack(203)
        open_top= OpenTop(675)
        ventilado = Ventilado(785)
        
        despacho.agregar_container(basico)
        despacho.agregar_container(basicoHC)
        despacho.agregar_container(flatrack)
        despacho.agregar_container(open_top)
        despacho.agregar_container(ventilado)
        
        mercaderia1 = Mercaderia(102,"Silla",3.0,5.0,1.0,2.0,5.0)
        mercaderia2 = Mercaderia(102,"Silla",3.0,5.0,1.0,2.0,5.0)
        mercaderia3 = Mercaderia(102,"Silla",3.0,5.0,1.0,2.0,5.0)
        mercaderia4 = Mercaderia(102,"Silla",3.0,5.0,1.0,2.0,5.0)
        mercaderia5 = Mercaderia(102,"Silla",3.0,5.0,1.0,2.0,5.0)
        
        cliente = Cliente("Lucas",38211156,102365)
        cliente.agregarMercaderia(mercaderia1)
        cliente.agregarMercaderia(mercaderia2)
        cliente.agregarMercaderia(mercaderia3)
        cliente.agregarMercaderia(mercaderia4)
        cliente.agregarMercaderia(mercaderia5)
        
        despacho.cargarContenedor(basico,cliente)
        self.assertIn(mercaderia1, basico.mercaderia)
        self.assertIn(mercaderia2, basico.mercaderia)
        self.assertIn(mercaderia3, basico.mercaderia)
        self.assertIn(mercaderia4, basico.mercaderia)
        self.assertIn(mercaderia5, basico.mercaderia)

    def test_menorbarcoKm (self):
          despacho = Despacho()  # Crear una instancia de la clase Despacho  
    
          b=BarcoBasico()
          
          b.id=10
          b.max_Containers=60
          b.set_max_Peso(90002.0)
          b.get_viaje().set_sede_inicial('AFR-002') 
          b.get_viaje().set_sede_final('AME-003')  
          b.get_viaje().set_km_Recorridos(10900.0)       
          b.km_Total=b.get_viaje().get_km_Recorridos()
          b.es_Especial=False
          b.peso_Actual=10980.0
          

          ba=BarcoBasico()
          ba.id=10
          ba.max_Containers=90
          ba.set_max_Peso(100000.0)
          ba.get_viaje().set_sede_inicial('AFR-002') 
          ba.get_viaje().set_sede_final('AME-003')
          ba.get_viaje().set_km_Recorridos(900200.0)  
          ba.km_Total=ba.get_viaje().get_km_Recorridos()
          ba.es_Especial=False
          ba.peso_Actual=12980.0

          despacho.agregar_barcos(b)    # Agrego los barcos a la lista
          despacho.agregar_barcos(ba)

          auxBarco=BarcoBasico()                 # creo el auxiliar donde se guardara el mayorbarcoKm
          auxBarco=despacho.barcos[0] 

          
          for barco in despacho.get_barcos():
            if barco.km_Total < auxBarco.km_Total:
                auxBarco=barco

          self.assertEqual(auxBarco,b)
         
        
    def test_mayorbarcoKm (self):
          
          despacho = Despacho()  # Crear una instancia de la clase Despacho  
    
          b=BarcoBasico()          
          b.id=10
          b.max_Containers=60
          b.set_max_Peso(90002.0)          
          b.get_viaje().set_sede_inicial('AFR-002') 
          b.get_viaje().set_sede_final('AME-003')  
          b.get_viaje().set_km_Recorridos(10900.0)       
          b.km_Total=b.get_viaje().get_km_Recorridos()
          b.es_Especial=False
          b.peso_Actual=10980.0
          

          ba=BarcoBasico()
          ba.id=10
          ba.max_Containers=90
          ba.set_max_Peso(100000.0)
          ba.get_viaje().set_sede_inicial('AFR-002') 
          ba.get_viaje().set_sede_final('AME-003')
          ba.get_viaje().set_km_Recorridos(900200.0)  
          ba.km_Total=ba.get_viaje().get_km_Recorridos()
          ba.es_Especial=False
          ba.peso_Actual=12980.0
         
          despacho.agregar_barcos(b)    # Agrego los barcos a la lista
          despacho.agregar_barcos(ba)

          auxBarco=BarcoBasico()                 # creo el auxiliar donde se guardara el mayorbarcoKm
          auxBarco=despacho.barcos[0] 

          

          for barco in despacho.get_barcos():
            if barco.km_Total > auxBarco.km_Total:
                auxBarco=barco

          self.assertEqual(auxBarco,ba)


    def test_No_hay_Barcos(self):
        despacho = Despacho()  # Crear una instancia de la clase Despacho
    
        with self.assertRaises(NoListaBarcosException):
          despacho.menorbarcoKm(despacho.get_barcos())  # Llamar al método menorbarcokm() en la instancia de Despacho

              
             
                


           
