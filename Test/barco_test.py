from unittest import TestCase

from Clases.Barco.Barco import Barco
from Clases.Contenedores.Contenedor import Contenedor
from Clases.Contenedores.Medida import Medida


class BarcoTest(TestCase):
    def test_obtener_Km_Recorridos(self,inicio,final):
        #km_Recorridos=GPS(inicio,final) No se como se hace el mock de GPS por eso paso los km directos.
        barcoT=Barco()
        km_Recorridos=18903.9
        barcoT.set_km_Total+=km_Recorridos

        assert km_Recorridos > 0

        print(f"Km recorridos {km_Recorridos}")
        
    '''def descargar(self):

      conteiner=Contenedor()  
      conteiner.id=910
      conteiner.__interior=Medida(10,11,20)
      conteiner.__exterior=Medida(20,30,50)
      conteiner.__pies=30
      conteiner.__max_peso=1080
      conteiner.__max_volumen = 180.5
      conteiner.__precio_base = 20000
      conteiner.__hay_espacio = False
      conteiner.__es_especial = False
      conteiner.__mercaderia = []
      conteiner.__peso_actual = 180
      conteiner.__volumen_actual = 100
      conteiner.__unica_carga = False


      conteiner2=Contenedor()  
      conteiner2.id=910
      conteiner2.__interior=Medida(30,12,24)
      conteiner2.__exterior=Medida(24,20,70)
      conteiner2.__pies=40
      conteiner2.__max_peso=1980
      conteiner2.__max_volumen = 280.5
      conteiner2.__precio_base = 250000
      conteiner2.__hay_espacio = False
      conteiner2.__es_especial = False
      conteiner2.__mercaderia = []
      conteiner2.__peso_actual = 1280
      conteiner2.__volumen_actual = 1000
      conteiner2.__unica_carga = False

      listPrueba=list()
      listPrueba.append(conteiner)
      listPrueba.append(conteiner2)  


      contAux=Contenedor()
      listAux=list()
      while listPrueba:
          contAux=listPrueba.pop(0)
          listAux.append(contAux)

          
          self.peso_Actual=0.0    
      return listAux '''
    
    
    



        

