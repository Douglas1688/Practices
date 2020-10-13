class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera = False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena = True
    def estado(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",
              self.enmarcha,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena)

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:",
              self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena,"\nCaballito: ",self.hcaballito)


class V_electricos(Vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
    def cargarEnergía(self):
        self.cargando = True


"""
moto1=Moto("Honda","CBR")
moto1.caballito()
moto1.estado()
miFurgo = Furgoneta("Renault","Kangoo")
miFurgo.arrancar()
miFurgo.estado()
print(miFurgo.carga(True))

class BicicletaElectrica(V_electricos,Vehiculos):
    pass

miBici=BicicletaElectrica("Yamaha","Atigua")
miBici.estado()
"""