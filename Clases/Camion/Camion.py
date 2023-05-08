from Contenedores import Contenedor
class Camion:
    
    patente=''
    costo_Fijo=20000.00
    conteiner=Contenedor

#---------- Getters & Setters ----------

#Getters & setters de Patente 
    def get_patente(self):
        return self.patente
    def set_patente(self,valor):
        self.patente=valor
    patente=property (get_patente,set_patente)

#Getters & setters de costoFijo
    def get_costo_Fijo(self):
        return self.costo_Fijo
    def set_costo_Fijo(self,valor):
        self.costo_Fijo=valor
    costo_Fijo=property (get_costo_Fijo,set_costo_Fijo)

#Getters & setters de conteiner
    def get_conteiner(self):
        return self.conteiner
    def set_conteiner(self,valor):
        self.conteiner=valor
    conteiner=property (get_conteiner,set_conteiner)

#---------- Getters & Setters ----------
#...................................................
#---------- Funciones ----------
    
    def llevaConteiner(self):
        return True
    
    
    def calcularMonto(self):
        return 0.0