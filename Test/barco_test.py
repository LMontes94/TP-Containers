from unittest import TestCase 
from unittest.mock import Mock
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


class BarcoTest(TestCase):

    def test_obtener_Km_Recorridos(self):
        gps = Mock()
        gps.obtenerKmRecorridos.return_value = 500 
        km_Recorridos=GPSMock().calcularDistancia(100,290)
        barcoT=BarcoBasico()
        basico=Basico(189)
        barcoT.cargar_conteiner(basico)
        barcoT.set_km_Total(100)

        
        barcoT.set_km_Total(barcoT.get_km_Total()+km_Recorridos)
        resultado=barcoT.get_km_Total()

        self.assertEqual(resultado,600) 

        
        
    def test_descargar(self):

      conteiner=Basico(910)      
      conteiner2=BasicoHC(700)   
      conteiner3=Basico(799)     
      

      listPrueba=list()
      listPrueba.append(conteiner)
      listPrueba.append(conteiner2)  
      listPrueba.append(conteiner3)   

      listAux=list()

      while listPrueba:
          contAux=listPrueba.pop(0)
          listAux.append(contAux)

          
          self.peso_Actual=0.0    
      
    
      self.assertIn(conteiner,listAux)
      self.assertIn(conteiner2,listAux)
      self.assertIn(conteiner3,listAux)


    #def test_viajar_Alcanza_Combustible(self):
        
    
    
    



        

