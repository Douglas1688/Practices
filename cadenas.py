from random import randint
Alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
         'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
         '7', '8', '9']
def generaClave():
   global Alpha
   try:
       caracteres = int(input("Ingrese el valor de caracteres que desea en su clave:"))
       if caracteres <= 42:
           print("Clave generada con éxito: ",end="")
           for x in range(caracteres):
               print(Alpha[randint(0, len(Alpha))],end="")
           print("\nLa clave tiene %d %s"%(caracteres,'caracteres'))
       else:
           print("Warning: Valor de caracteres fuera de rango.")
           generaClave()
   except:
       print("VALORES ERRÓNEOS.")
       generaClave()
generaClave()
