
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




        def menorbarcoKm (self):
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

          if not barcos:
                raise NoListaBarcosException("No hay una lista de barcos para realizar la operacion",123)   
          
          auxBarco=Barco()                
          auxBarco=barcos[0]

          for barco in barcos:
            if barco.km_Total < auxBarco.km_Total:
                auxBarco=barco

        
          print(f"El barco que menor Km Recorrio fue el barco con id: {auxBarco.id} con {auxBarco.km_Total} kms")


        def mayorbarcoKm (self,barcos):
          
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
          if not barcos:
            raise NoListaBarcosException("No hay una lista de barcos para realizar la operacion",123)  
          auxBarco=Barco()                
          auxBarco=barcos[0]

          for barco in barcos:
            if barco.km_Recorridos > auxBarco.km_Recorridos:
                auxBarco=barco

        
          print(f"El barco que mayor Km Recorrio fue el barco con id: {auxBarco.id} con {auxBarco.km_Recorridos} kms")


    def test_verificarCargaBarco (self):  
      conteiner=Basico(980)                   
      flag=False
      i=0

       while i < len(self.barcos) and flag == False:
         
         if conteiner.__es_especial ==True and self.barcos[i].es_Especial == True:

            if ((conteiner.__peso_actual+self.barcos[i].peso_Actual) <= self.barcos[i].max_Peso) and len(self.barcos[i].get_conteiner()) < self.barcos[i].max_Containers :


                self.barcos[i].cargar_contenedor(conteiner)
                flag=True

         elif conteiner.__es_especial == False and  self.barcos[i].es_Especial == False: 

             if ((conteiner.__peso_actual+self.barcos[i].peso_Actual) <= self.barcos[i].max_Peso) and len(self.barcos[i].get_conteiner()) < self.barcos[i].max_Containers :


                self.barcos[i].cargar_contenedor(conteiner)
                flag=True

         i=i+1