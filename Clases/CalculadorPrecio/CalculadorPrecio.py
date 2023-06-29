
class CalculadorPrecio:

    def __init__(self):
        self.precio_conteiner_completo = {
            (100, 200000), (1000, 210000), (9999, 230000), (10000, 250000)
        }

        self.precio_conteiner_incompleto = {
            (100, 1000), (1000, 1100), (9999, 1150), (10000, 1500)
        }

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

    def calcularPrecioBase(self, distancia, contenedor):
        if distancia < 100:
            if contenedor.contenedor_lleno():
                return 200000
            else:
                return 1000 * (peso_total // 100)
        elif distancia < 1000:

            if peso_total is None:
                return 210000
            else:
                return 1100 * (peso_total // 100)
        elif distancia < 10000:
            if peso_total is None:
                return 230000
            else:
                return 1150 * (peso_total // 100)
        else:
            if peso_total is None:
                return 250000
            else:
                return 1500 * (peso_total // 100)
