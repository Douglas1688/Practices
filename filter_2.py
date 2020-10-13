class Empleado :
    def __init__(self, nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)

lstEmpleado = [
Empleado("Juan", "Director", 75000),
Empleado("Ana", "Presidente", 85000),
Empleado("Douglas", "Administrador", 25000),
Empleado("Mario", "Jefe", 10000),
Empleado("Paula", "Contadora", 3000),
]

salarios_altos = filter(lambda empleado: empleado.salario>50000,lstEmpleado)

for empleado_salario in salarios_altos:
    print(empleado_salario)