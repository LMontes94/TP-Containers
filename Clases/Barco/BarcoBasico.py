from Clases.Barco.Barco import Barco
from Clases.Contenedores.Contenedor import Contenedor
from Clases.Excepciones.NoHayBarcoException import NoHayBarcoException
from Clases.Despacho.ContenedorManejador import ContenedorManejador
from Clases.Mercaderia.Mercaderia import Mercaderia
from Clases.Mercaderia.MercaderiaAlimenticia import MercaderiaAlimenticia
from Clases.Mercaderia.MercaderiaNormal import MercaderiaNormal
from Clases.Mercaderia.MercaderiaToxica import MercaderiaToxica

class BarcoBasico(Barco):
  
  def __init__(self):
      super().__init__() 

  def obtenerKmRecorridos(self,viaje):
      kmRecorridos=viaje.get_km_Recorridos()
          
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

  def manejar(self, contenedor):

        try:
            if self.puede_cargar_contenedor(contenedor):
                self.cargar_conteiner(contenedor)
            elif self.noHaySiguiente():
                self.get_siguiente().manejar(contenedor)
        except NoHayBarcoException as e:
            print(f"Error {e.get_code()} / {e.get_mensaje()}")

  def puede_cargar_contenedor(self, contenedor):
           return self.verificar_carga_contenedor(contenedor)
            
          

