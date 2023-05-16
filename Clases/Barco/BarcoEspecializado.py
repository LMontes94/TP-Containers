from Contenedores import Contenedor
import Barco
from abc import ABC,abstractmethod


class BarcoEspecializado(Barco):
     
     def __init__(self):
        self.id=0
        self.max_Containers=0
        self.max_Peso=0.0
        self.conteiner = list (Contenedor())
        self.sede_Inicial=''
        self.sede_Final=''
        self.km_Recorridos=0.0
        self.km_Total=0.0
        self.es_Especial=False
        self.peso_Actual=0.0


        def sumaKmRecorridos(self):
            self.km_Recorridos=GPS(self.sedeInicial,self.sedeFinal)
            self.km_Total+=self.km_Recorridos
        super().sumaKmRecorridos()

        def descargar(self):
            contAux=Contenedor()
            listAux=list()
            while self.conteiner():
                contAux=self.conteiner.pop(0)
                listAux.append(contAux)
          
            self.peso_Actual=0.0    
            return listAux

                