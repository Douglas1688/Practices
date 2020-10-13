class Persona():
    def __init__(self,nombre,edad,Lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia=Lugar_residencia

    def descripcion(self):
        print("Nombre: ",self.nombre,end=", ")
        print("Edad: ",self.edad,end=", ")
        print("Residencia: ",self.lugar_residencia,end=", ")
class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia):
        super().__init__(nombre_empleado,edad_empleado,residencia)
        self.salario = salario
        self.antiguedad = antiguedad
    def descripcion(self):
        super().descripcion()
        print("\nSalario: ",self.salario,", Antiguedad: ",self.antiguedad)

antonio = Empleado(400,"5 años","Manuel",55,"Colombia")
antonio.descripcion()
print(isinstance(antonio,Persona))