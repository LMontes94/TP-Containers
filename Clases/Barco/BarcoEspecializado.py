from Clases.Contenedores.Contenedor import Contenedor
from Clases.Barco.Barco import Barco
from abc import ABC,abstractmethod


class BarcoEspecializado(Barco):
     
     def __init__(self):
         super().__init__()
         self.es_Especial=True
        

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

                