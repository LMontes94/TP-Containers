
from Clases.Contenedores.Contenedor import Contenedor
from Clases.Excepciones.ContenerdorLlenoException import ContenedorLlenoException
from Clases.Excepciones.ExcesoMedidasException import ExcesoMedidasException


class FlatRack(Contenedor):
    def __init__(self, id):
        super().__init__(id, None, 2.3, 6.0, None, 2.3, 6.1)
        self.set_max_Peso(45000.0)
        self.set_max_Volumen(33.0)
    
    def validarCargaMercaderia(self, mercaderia):
        if self.get_hay_Espacio() :
                raise ContenedorLlenoException("El contenedor esta lleno!!", 302)
        elif self.get_interior().alto < mercaderia.medida.alto or self.get_interior().largo < mercaderia.medida.largo:
                raise ExcesoMedidasException(f"Las medidas de la {mercaderia.nombre} exceden el limite!!",303)
        else:
                self.cargar_mercaderia(mercaderia)