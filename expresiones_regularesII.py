import re
lista_nombres=[
'Ana Gómez',
'María Martín',
'Sandra López',
'Santiago Vásquez'
]
cad = input("Ingrese expresión: ")
long = len(lista_nombres)
cont=1
for elemento in lista_nombres:

    if re.findall(cad+'$',elemento) or re.findall('^'+cad,elemento):
        print(elemento)
    else:
        cont +=1

if cont == (long-1):
    print("No se han encontrado coincidencias")

