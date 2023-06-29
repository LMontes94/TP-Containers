class GPSMock:

    def kmPorHora(self):
        #ejemplo de los km por hora que recorre el barco
        kmPorHora = 40
        return kmPorHora
    
    def calcularDistancia(self, origen, destino):
        distancia = destino - origen
        
        #Seteamos una distancia x
        distancia = 500
        return distancia
    
    def calcularTiempoDeViaje(self, origen, destino):
        #tiempo = distancia / velocidad

        tiempo = self.calcularDistancia(origen,destino) / self.kmPorHora()
        return tiempo