
class ContenedorLlenoException(Exception):
    def __init__(self, msj):
        self.mensaje = msj

    def get_mensaje(self):
        return self.mensaje
