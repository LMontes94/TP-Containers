from Clases.Contenedores.Contenedor import Contenedor
from Clases.Contenedores.ManejadorContenedores import ManejadorContenedores
from Clases.Excepciones.ContenerdorLlenoException import ContenedorLlenoException
from Clases.Excepciones.ExcesoMedidasException import ExcesoMedidasException
from Clases.Excepciones.NoHayContenedorException import NoHayContenedorException
from Clases.Excepciones.MercaderiaInvalidaException import MercaderiaInvalidaException
from Clases.Mercaderia.Mercaderia import Mercaderia
from Clases.Mercaderia.MercaderiaAlimenticia import MercaderiaAlimenticia
from Clases.Mercaderia.MercaderiaNormal import MercaderiaNormal
from Clases.Mercaderia.MercaderiaToxica import MercaderiaToxica
from Clases.Despacho.ContenedorManejador import ContenedorManejador

class BasicoHC(Contenedor, ManejadorContenedores):
    
    #Variables específicas
    def __init__(self, id):
        super().__init__(id, 235.0, 230.0, 1200.0, 245.0, 260.0, 1210.0)
        self.set_pies(40)
        self.set_max_Peso(32500.0)
        self.set_max_Volumen(67.7)

    #Manejo con COR
    def manejar(self, mercaderia, contenedor):
        try:
            self.validarCargaMercaderia(mercaderia)
            contenedor.cargar_mercaderia(mercaderia)
        except ContenedorLlenoException as e:
            if self.siguiente is not None:
                self.siguiente.manejar(contenedor, mercaderia)
            else:
                raise NoHayContenedorException("No hay contenedores disponibles")
        except ExcesoMedidasException as e:
            if self.siguiente is not None:
                self.siguiente.manejar(contenedor, mercaderia)
            else:
                raise NoHayContenedorException("No hay contenedores disponibles")

    #Validación según especificaciones    
    def validarCargaMercaderia(self, mercaderia):
        if isinstance(mercaderia, MercaderiaAlimenticia):
            raise MercaderiaInvalidaException("No se puede cargar mercadería alimenticia en este tipo de contenedor.")
        elif self.get_hay_Espacio():
            raise ContenedorLlenoException("El contenedor está completo.")
        elif self.get_interior().alto < mercaderia.medida.alto or self.get_interior().largo < mercaderia.medida.largo:
            raise ExcesoMedidasException("Las medidas de la mercadería exceden el límite.")