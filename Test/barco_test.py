from unittest import TestCase
from Test.GPSMock import GPSMock

from Clases.Barco.BarcoBasico import BarcoBasico
from Clases.Contenedores.Basico import Basico
from Clases.Contenedores.BasicoHC import BasicoHC
from Clases.Contenedores.Contenedor import Contenedor
from Clases.Contenedores.Medida import Medida


class BarcoTest(TestCase):
    def test_obtener_Km_Recorridos(self):
        km_Recorridos=GPSMock()
        barcoT=BarcoBasico()
        basico=Basico(189)
        barcoT.cargar_conteiner(basico)

        km_Recorridos=18903.9
        barcoT.set_km_Total(barcoT.get_km_Total()+km_Recorridos)

        assert km_Recorridos > 0

        print(f"Km recorridos {km_Recorridos}")
        
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

    
    
    



        

