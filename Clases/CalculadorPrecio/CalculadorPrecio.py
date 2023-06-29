class CalculadorPrecio:

    def __init__(self):
        self.precio_conteiner_completo = {
            100: 200000, 1000: 210000, 9999: 230000, 10000: 250000
        }

        self.precio_conteiner_incompleto = {
            100: 1000, 1000: 1100, 9999: 1150, 10000: 1500
        }
        self.km_base = 100

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

    def calcularPrecio(self, container, cliente, distancia):

        if container.contenedor_lleno():
            precio_base = self.obtener_precio_container_completo(distancia)
        else:
            # o deberia buscar dentro del contenedor mercaderia del cliente e ir sumando el peso
            peso_total = container.get_peso_actual()
            precio_base = self.obtener_precio_container_incompleto(distancia)
            precio_base += (peso_total//self.km_base)

        if cliente.tieneServicioAPuerta:
            precio_base += 20000

        return precio_base
