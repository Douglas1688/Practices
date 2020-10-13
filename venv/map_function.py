class Empleado :
    def __init__(self, nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)

lstEmpleado = [
Empleado("Juan", "Director", 7500),
Empleado("Ana", "Presidente", 8500),
Empleado("Douglas", "Administrador", 2500),
Empleado("Mario", "Jefe", 100),
Empleado("Paula", "Contadora", 300),
]

def calculo_comision(empleado):
    if empleado.salario<=3000:
        empleado.salario = empleado.salario*1.03
    return empleado
listaEmpleado = map(calculo_comision,lstEmpleado)

for emp in listaEmpleado:
    print(emp)