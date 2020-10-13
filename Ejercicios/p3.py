from io import *

linea="Este es un nuevo archivo en python"
file = open("nuevo.txt","r")
for elem in file:
    print(elem)
file.close()