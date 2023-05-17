class ContenedorNoEncontradoExcpetion(Exception):
    def __init__(self, msj):
        self.mensaje = msj
        self.code = 304

    def get_mensaje(self):
        return self.mensaje
    
    def get_code(self):
        return self.code