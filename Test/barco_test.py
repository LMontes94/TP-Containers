from unittest import TestCase

from Clases.Barco.Barco import Barco


class BarcoTest(TestCase):
    def obtener_Km_Recorridos_Test(self,inicio,final):
        #km_Recorridos=GPS(inicio,final) No se como se hace el mock de GPS por eso paso los km directos.
        barcoT=Barco()
        km_Recorridos=18903.9
        barcoT.set_km_Total+=km_Recorridos

        


        

