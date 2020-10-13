from tkinter import *


acceso = input("ingrese su clave: ")

while acceso != "Douglas1688*":
    print("Acceso denegado!!!")
    acceso = input("ingrese su clave: ")

else:
    root = Tk()
    miFrame = Frame(root)
    miFrame.pack()
    root.mainloop()
