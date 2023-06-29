class CalculadorPrecio:

    def __init__(self):
        self.precio_conteiner_completo = {
            100: 200000, 1000: 210000, 9999: 230000, 10000: 250000
        }

        self.precio_conteiner_incompleto = {
            100: 1000, 1000: 1100, 9999: 1150, 10000: 1500
        }

    def obtener_precio_container_completo(self, distancia: int) -> int:
        for d, precio in self.precio_conteiner_completo.items():
            if distancia < d:
                return precio
        # Si la distancia es mayor a 10000 Km
        return self.precio_conteiner_completo[10000]

    def obtener_precio_container_incompleto(self, distancia: int) -> int:
        for d, precio_base in self.precio_conteiner_incompleto.items():
            if distancia < d:
                return precio_base
        # Si la distancia es mayor a 10000 Km
        return self.precio_conteiner_incompleto[10000]

    def obtenerPrecio(self, container, idC, idB, distancia):
        container = self.__containers[idC]
        distancia = self.__barcos[idB].get_km_Total()

        if not self.__barcos:
            raise NoListaBarcosException(
                "No hay una lista de barcos para realizar la operacion", 123)

        if container.hayEspacio() == False:
            precio_base = self.__calcularPrecioBase(distancia)
        else:
            peso_total = container.get_peso_actual()
            precio_base = self.__calcularPrecioBase(distancia, peso_total)

        if self.__retiro == True:
            precio_base += 20000

        return precio_base
