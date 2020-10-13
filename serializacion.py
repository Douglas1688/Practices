import pickle
"""lst_nombres=["Pedro","Ana","María","Douglas"]
fichero_binario = open("lista_nombres","wb")
pickle.dump(lst_nombres,fichero_binario)
fichero_binario.close()
del(fichero_binario)"""

fichero = open("lista_nombres","rb")
lst=pickle.load(fichero)
fichero.close()
for name in lst:
    print(name,end=" ")
