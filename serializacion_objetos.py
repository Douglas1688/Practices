import pickle
from Herencia import Vehiculos
"""coche1 = Vehiculos("Honda","001")
coche2= Vehiculos("Ford","F150")
coche3=Vehiculos("Mazda","C56")
lst_coches=[coche1,coche2,coche3]
fich_Obj = open("fichero_objeto","wb")
pickle.dump(lst_coches,fich_Obj)
fich_Obj.close()
del(fich_Obj)"""

fichero = open("fichero_objeto","rb")
lst_fichero_objeto = pickle.load(fichero)
fichero.close()
for c in lst_fichero_objeto:
    print(c.estado())
