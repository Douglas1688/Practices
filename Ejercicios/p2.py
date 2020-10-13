from io import open
counter = 0
fichero = open("archivo.txt","r")
ar = fichero.read()
print(len(ar))
print(ar[10:20])

for linea in fichero:
    print(linea)
    counter+=1
print("Contador de líneas: ",counter)



fichero.close()
