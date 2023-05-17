class Medida:

    def __init__(self, ancho, alto, largo):
        self.__ancho = ancho
        self.__alto = alto
        self.__largo = largo


# ---------- Getters & Setters ----------

# Getters & setters de ancho


    def get_ancho(self):
        return self.__ancho

    def set_ancho(self, valor):
        self.__ancho = valor


# Getters & setters de alto


    def get_alto(self):
        return self.__alto

    def set_alto(self, valor):
        self.__alto = valor


# Getters & setters de largo


    def get_largo(self):
        return self.__largo

    def set_largo(self, valor):
        self.__largo = valor

    largo = property(get_largo, set_largo)
    alto = property(get_alto, set_alto)
    ancho = property(get_ancho, set_ancho)
# ---------- Getters & Setters ----------
