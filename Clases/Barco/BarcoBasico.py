import Barco
from Contenedores.Contenedor import Contenedor

class BarcoBasico(Barco):
  
  def __init__(self):
      super().__init__()
  
  def obtenerKmRecorridos(self,inicio,final):
      kmRecorridos=GPS(inicio,final)
          
      self.km_Total+=kmRecorridos 
      return kmRecorridos

  
  def descargar(self):

      contAux=Contenedor()
      listAux=list()
      while self.conteiner:
          contAux=self.conteiner.pop(0)
          listAux.append(contAux)

          
          self.peso_Actual=0.0    
      return listAux


            
          

