class Medida:

    ancho=0.0
    alto=0.0
    largo=0.0


#---------- Getters & Setters ----------

#Getters & setters de ancho
    def get_ancho(self):
        return self.ancho
    def set_ancho(self,valor):
        self.ancho=valor
    ancho=property(get_ancho,set_ancho)

#Getters & setters de alto
    def get_alto(self):
        return self.alto
    def set_alto(self,valor):
        self.alto=valor
    alto=property(get_alto,set_alto)

#Getters & setters de largo
    def get_largo(self):
        return self.largo
    def set_largo(self,valor):
        self.largo=valor
    largo=property(get_largo,set_largo)

#---------- Getters & Setters ----------