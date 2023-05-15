class Medida:

    def __init__(self, ancho, alto, largo):
        self.ancho = ancho
        self.alto = alto
        self.largo = largo


# ---------- Getters & Setters ----------

# Getters & setters de ancho


    def get_ancho(self):
        return self.ancho

    def set_ancho(self, valor):
        self.ancho = valor


# Getters & setters de alto


    def get_alto(self):
        return self.alto

    def set_alto(self, valor):
        self.alto = valor


# Getters & setters de largo


    def get_largo(self):
        return self.largo

    def set_largo(self, valor):
        self.largo = valor

    largo = property(get_largo, set_largo)
    alto = property(get_alto, set_alto)
    ancho = property(get_ancho, set_ancho)
# ---------- Getters & Setters ----------
