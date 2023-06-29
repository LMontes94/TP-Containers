from unittest import TestCase 
from Clases.Contenedores.Contenedor import Contenedor
from Clases.Contenedores.FlatRack import FlatRack
from Clases.Contenedores.Ventilado import Ventilado
from Clases.Mercaderia.MercaderiaAlimenticia import MercaderiaAlimenticia
from Clases.Mercaderia.MercaderiaNormal import MercaderiaNormal
from Clases.Mercaderia.MercaderiaToxica import MercaderiaToxica
from Clases.Excepciones.MercaderiaInvalidaException import MercaderiaInvalidaException
from Clases.Excepciones.NoHayContenedorException import NoHayContenedorException

class TestContenedor(TestCase):
    def test_cargar_mercaderia_alimenticia(self):
        mercaderia_alimenticia = MercaderiaAlimenticia(9541,"Cocos",5,15,10,4,6)
        contenedor = Ventilado(136)
        
        contenedor.cargar_mercaderia(mercaderia_alimenticia)  

        # Verifica que la mercadería haya sido cargada por el ventilado
        self.assertEqual(len(contenedor.get_mercaderia()), 1)
        self.assertIsInstance(contenedor.get_mercaderia()[0], MercaderiaAlimenticia)

    def test_not_cargar_mercaderia_alimenticia(self):
        mercaderia_alimenticia = MercaderiaAlimenticia(9541,"Bananas",5,15,10,4,6)
        contenedor = FlatRack(156)
        
        contenedor.cargar_mercaderia(mercaderia_alimenticia)  

        # Verifica que la mercadería no haya sido cargada por el que no es ventilado
        self.assertRaises(MercaderiaInvalidaException, contenedor.validarCargaMercaderia, mercaderia_alimenticia)

    def test_cargar_mercaderia_normal(self):
        contenedor1 = FlatRack(322)
        contenedor2 = FlatRack(681)
    
        mercaderia_normal = MercaderiaNormal(12, "Armario", 20, 10, 9, 4, 6)

        contenedor1.siguiente = contenedor2

        contenedor1.manejar(contenedor1.siguiente, mercaderia_normal)

        #Verifica que el primer contenedor no haya sido cargado y el segundo sí por la MercaderíaNormal
        self.assertEqual(len(contenedor1.get_mercaderia()), 0)
        self.assertEqual(len(contenedor2.get_mercaderia()), 1)
        self.assertIsInstance(contenedor2.get_mercaderia()[0], MercaderiaNormal)
    
    def test_cargar_mercaderia_toxica(self):
        contenedor1 = Ventilado(953)
        contenedor2 = Ventilado(954)
        alimento = MercaderiaAlimenticia(3, "Manzanas", 2, 4, 2, 3, 1)

        contenedor1.cargar_mercaderia(alimento)  #Colocamos una mercadería alimenticia para levantar el error

        mercaderia_toxica = MercaderiaToxica(9, "Residuos", 2, 3, 4, 5, 6)

        self.assertRaises(MercaderiaInvalidaException, contenedor1.manejar, contenedor2, mercaderia_toxica)

    def test_no_hay_contenedores(self):
        contenedor = Ventilado(631)
        mercaderia = MercaderiaNormal(3, "Mueble", 2, 4, 2, 3, 1)

        self.assertRaises(NoHayContenedorException,contenedor.manejar, None, mercaderia)