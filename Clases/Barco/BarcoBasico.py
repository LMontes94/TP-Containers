import Barco
from Contenedores.Contenedor import Contenedor

class BarcoBasico(Barco):
  

  def sumaKmRecorridos(self):
         self.km_Recorridos=GPS(self.sedeInicial,self.sedeFinal)
         self.km_Total+=self.km_Recorridos 
         super().sumaKmRecorridos()
  
  def descargar(self):
       
      contAux=Contenedor()
      listAux=list()
      for ind in self.conteiner:
           contAux=self.conteiner().remove
           listAux.append(contAux)

      self.peso_Actual=0.0    
      return listAux


            
          

