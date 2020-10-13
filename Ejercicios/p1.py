"""Realizar un programa que conste de una clase llamada alumno
que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos, imprimirlos y
mostrar un mensaje con el resultado de la nota y mostrar si aprobó o no"""

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("nota: ",self.nota)

    def resultado(self):

        if self.nota >7:
            print("Aprobado")
        else:
            print("Reprobado")



objAlumno = Alumno("Douglas Vásquez",7)

objAlumno.imprimir()
objAlumno.resultado()
