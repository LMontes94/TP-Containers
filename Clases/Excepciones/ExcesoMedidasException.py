class ExcesoMedidasException(Exception):
    def __init__(self, msj,code):
        self.mensaje = msj
        self.code = code 

    def get_mensaje(self):
        return self.mensaje
    
    def get_code(self):
        return self.code