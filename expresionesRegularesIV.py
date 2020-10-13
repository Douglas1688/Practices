import re

lst= ["Douglas Vásquez","douglas Loor","Jessenia Loor",
      "Patricio Estrella","Bob Esponja"]
cad = input("Ingrese expresión a buscar: ")

for elem in lst:
    if re.search(cad,elem):
        print(elem)
