class Cliente:

    nombre=''
    dni=0
    nro_Cliente=0


#---------- Getters & Setters ----------

#Getters & setters de nombre

    def get_nombre(self):
        return self.nombre
    def set_nombre(self,valor):
        self.nombre=valor
    nombre=property(get_nombre,set_nombre)

#Getters & setters de dni

    def get_dni(self):
        return self.dni
    def set_dni(self,valor):
        self.dni=valor
    dni=property(get_dni,set_dni)

#Getters & setters de nroCliente

    def get_nro_Cliente(self):
        return self.nro_Cliente
    def set_nro_Cliente(self,valor):
        self.nro_Cliente=valor
    nro_Cliente=property(get_nro_Cliente,set_nro_Cliente)

#---------- Getters & Setters ----------