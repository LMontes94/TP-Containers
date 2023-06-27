class Viaje:
    def __init__(self):
        self.__sede_inicial = ""
        self.__sede_final = ""
        self.__horas_totales = 0
        self.__km_Recorridos = 0

    def __init__(self, sede_inicial, sede_final, horas,km_Recorridos):
        self.__sede_inicial = sede_inicial
        self.__sede_final = sede_final
        self.__horas_totales = horas
        self.__km_Recorridos = km_Recorridos

    def get_sede_inicial(self):
        return self.__sede_inicial

    def set_sede_inicial(self, sede_inicial):
        self.__sede_inicial = sede_inicial

    def get_sede_final(self):
        return self.__sede_final

    def set_sede_final(self, sede_final):
        self.__sede_final = sede_final

    def get_horas(self): 
        return self.__horas_totales

    def set_horas(self, horas): #se lo setea el mock del gps.
        self.__horas_totales = horas

    def get_km_Recorridos(self):
        return self.__km_Recorridos

    def set_km_Recorridos(self, km):#se lo setea el mock del gps.
        self.__km_Recorridos = km
    

    sede_inicial = property(get_sede_inicial, set_sede_inicial)
    sede_final = property(get_sede_final, set_sede_final)
    horas_totales = property(get_horas, set_horas)
    km_Recorridos = property(get_km_Recorridos,set_km_Recorridos)