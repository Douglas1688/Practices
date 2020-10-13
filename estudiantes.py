
cal_estudiantes=[]
acum=0
cant = int(input("Ingrese cantidad de estudiantes:"))
for i in range(cant):
    name = input("Ingrese nombre: ")
    cal= int(input("Ingrese nota 0-100"))
    acum = cal+acum
    nota_est=[name,cal]
    cal_estudiantes.append(nota_est)

prom=acum/cant

for i in range(len(cal_estudiantes)):
    if cal_estudiantes[i][1]>prom:
        print("",cal_estudiantes[i]," * ")
    else:
        print("", cal_estudiantes[i])
