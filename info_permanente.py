import pickle
class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de : "+self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
    personas=[]
    def __init__(self):
        listaPersona=open("ficheroExterno","ab+")
        listaPersona.seek(0)
        try:
            self.personas= pickle.load(listaPersona)
            print("Se ha cargaron {} personas del fichero externo ".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaPersona.close()
            del(listaPersona)
    def agregarPersonas(self,obj):
        self.personas.append(obj)
        self.guardarPersonaEnFicheroExterno()
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    def guardarPersonaEnFicheroExterno(self):
        listaPersonas = open("ficheroExterno","wb")
        pickle.dump(self.personas,listaPersonas)
        listaPersonas.close()
        del(listaPersonas)
    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)
miLst= ListaPersonas()
persona=Persona("Jessenia","Femenino",27)
miLst.agregarPersonas(persona)
miLst.mostrarInfoFicheroExterno()


"""objPersona1 = Persona("Douglas","Masculino",31)
objPersona2 = Persona("Jessenia","Femenino",27)
objPersona3 = Persona("Gladys","Femenino",72)
miLst.agregarPersonas(objPersona1)
miLst.agregarPersonas(objPersona2)
miLst.agregarPersonas(objPersona3)

miLst.mostrarPersonas()"""
