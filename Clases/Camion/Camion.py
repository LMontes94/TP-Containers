from Clases.Contenedores.Contenedor import Contenedor
from Clases.Excepciones.CamionCargadoException import CamionCargadoException
from Clases.Excepciones.ContenedorVacioException import ContenedorVacioException
from Clases.Excepciones.NoMercaderiaException import NoMercaderiaException
from Clases.Excepciones.NoPuedeCargarContenedorException import NoPuedeCargarContenedorException
from Clases.Despacho.ContenedorManejador import ContenedorManejador
from Clases.Mercaderia.Mercaderia import Mercaderia

class Camion:
#Constructor
    def __init__(self, patente):
        self.patente = patente
        self.costoFijo = 20000.0
        self.contenedor = None
        

#Getters & Setters
    def getPatente(self):
        return self.patente
    def setPatente(self, patente):
        self.patente = patente

    def getCostoFijo(self):
        return self.costoFijo

    def getContenedor(self):
        return self.contenedor
    def setContenedor(self, contenedor : Contenedor):
        self.contenedor = contenedor

    def llevaContenedor(self):
        return self.contenedor is not None
    
    def verificarCargaContenedor(self):
        return self.getContenedor().get_es_especial()
    
    def cargarCamion(self,contenedor):

        if not self.llevaContenedor():
            raise CamionCargadoException("El camion ya se encuentra cargado!!")
        if not self.verificarCargaContenedor():
            raise NoPuedeCargarContenedorException("Este contenedor no puede ser cargado por el camion!!")
        self.setContenedor(contenedor)
    
    def descargarMercaderia(self, cliente):
       mercaderia = self.getContenedor().getMercaderia()
       mercaderia_cliente = []
       for item in mercaderia:
         if item.getCliente() == cliente:
            mercaderia_cliente.append(item)
        
       return mercaderia_cliente

    def sinMercaderiaCliente(self,mercaderia_cliente,cliente):
          if len(mercaderia_cliente) == 0:
            raise NoMercaderiaException(f"No hay mercadería para el cliente {cliente} en el camión.") 
          
            
    def entregarMercaderia(self, cliente):        
       
       try:
          self.getContenedor().contenedor_vacio()
          mercaderia_cliente = self.descargarMercaderia()
          self.sinMercaderiaCliente(mercaderia_cliente,cliente)

          # Entregar la mercadería al cliente
          for item in mercaderia_cliente:
            cliente.recibirMercaderia(item)
            self.getContenedor().getMercaderia().remove(item)

          # Actualizar la lista de mercadería en el contenedor
          self.getContenedor().setMercaderia(self.getContenedor().getMercaderia())

       except (ContenedorVacioException, NoMercaderiaException) as e:
          print(f"Error {e.get_code()} / {e.get_mensaje}")   

        

       

        
