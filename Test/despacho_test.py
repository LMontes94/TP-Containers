
from unittest import TestCase
from Clases.Barco.Barco import Barco
from Clases.Contenedores.Basico import Basico
from Clases.Contenedores.BasicoHC import BasicoHC
from Clases.Contenedores.Contenedor import Contenedor
from Clases.Contenedores.FlatRack import FlatRack
from Clases.Excepciones.NoListaBarcosException import NoListaBarcosException
from Clases.Mercaderia.Mercaderia import Mercaderia
from Clases.Despacho.Despacho import Despacho
from Clases.Cliente.Cliente import Cliente
from Clases.Barco.BarcoBasico import BarcoBasico
from Clases.Barco.BarcoEspecializado import BarcoEspecializado

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
        
        despacho.agregar_container(basico)
        despacho.agregar_container(basicoHC)
        despacho.agregar_container(flatrack)
        
        mercaderia1 = Mercaderia(102,"Silla",3.0,5.0,1.0,2.0,5.0)
        mercaderia2 = Mercaderia(102,"Silla",3.0,5.0,1.0,2.0,5.0)
        mercaderia3 = Mercaderia(102,"Silla",3.0,5.0,1.0,2.0,5.0)
        
        cliente = Cliente("Lucas",38211156,102365)
        cliente.agregarMercaderia(mercaderia1)
        cliente.agregarMercaderia(mercaderia2)
        cliente.agregarMercaderia(mercaderia3)
        
        despacho.cargarContenedor(basico,cliente)
        self.assertIn(mercaderia1, basico.mercaderia)
        self.assertIn(mercaderia2, basico.mercaderia)
        self.assertIn(mercaderia3, basico.mercaderia)
        #assert len(despacho.get_containers()) > 0

    def test_menorbarcoKm (self):
          barcos=list(Barco)  
          b=Barco()
          b.id=10
          b.max_Containers=60
          b.max_Peso=90002.0
          b.conteiner = list (Contenedor())
          b.sede_Inicial='AFR-002'
          b.sede_Final='AME-003'
          b.km_Total=10900.0
          b.es_Especial=False
          b.peso_Actual=10980.0

          ba=Barco()
          ba.id=10
          ba.max_Containers=90
          ba.max_Peso=12932.0
          ba.conteiner = list (Contenedor())
          ba.sede_Inicial='AME-001'
          ba.sede_Final='EUR-003'
          ba.km_Total=900200.0
          ba.es_Especial=False
          ba.peso_Actual=112980.0

          barcos.append(b)
          barcos.append(ba)  

          
          for barco in barcos:
            if barco.km_Total < auxBarco.km_Total:
                auxBarco=barco

          self.assertEqual(auxBarco,ba)
         
        
    def test_mayorbarcoKm (self,barcos):
          
          barcos=list(Barco)  
          b=Barco()
          b.id=10
          b.max_Containers=60
          b.max_Peso=90002.0
          b.get_viaje().set_sede_inicial('AFR-002') 
          b.get_viaje().get_sede_final('AME-003')
          b.km_Total=10900.0
          b.es_Especial=False
          b.peso_Actual=10980.0

          ba=Barco()
          ba.id=10
          ba.max_Containers=90
          ba.max_Peso=12932.0
          ba.conteiner = list (Contenedor())
          ba.sede_Inicial='AME-001'
          ba.sede_Final='EUR-003'
          ba.km_Total=900200.0
          ba.es_Especial=False
          ba.peso_Actual=112980.0

          barcos.append(b)
          barcos.append(ba)  

          auxBarco=Barco()                
          auxBarco=barcos[0]

          for barco in barcos:
            if barco.km_Recorridos > auxBarco.km_Recorridos:
                auxBarco=barco

          self.assertEqual(auxBarco,b)


def test_No_hay_Barcos(self):
    despacho = Despacho()  # Crear una instancia de la clase Despacho
    
    with self.assertRaises(NoListaBarcosException):
        despacho.menorbarcokm(despacho.get_barcos())  # Llamar al método menorbarcokm() en la instancia de Despacho

              
             
                


           
