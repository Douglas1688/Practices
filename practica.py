class Coche():
    def __init__(self):
        self.__largo=250
        self.__ancho=120
        self.__ruedas=4
        self.__enmarcha = False

    def arrancar(self,arrancamos):
        self.__enmarcha= arrancamos

        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif (self.__enmarcha and chequeo== False):
            return "Algo ha ido mal en el chequeo. No se puede arrancar"
        else:
            return "El coche está detenido"

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__ancho,"y un largo de ",self.__largo)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puerta="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puerta=="cerradas"):
            return True
        else:
            return False

c1 = Coche()
print(c1.arrancar(True))
c1.estado()
#print(c1.__chequeo_interno())
print("------------------ A continuación creamos el segundo objeto--------------")
c2 = Coche()
print(c2.arrancar(False))
c2.estado()