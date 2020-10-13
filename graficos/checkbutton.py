from tkinter import *
root = Tk()
root.title("Ejemplo")
playa = IntVar()
montagna=IntVar()
turismo_rural=IntVar()

def opcionViaje():
    opcionEscogida =""
    if playa.get()==1:
        opcionEscogida+=" playa"
    if montagna.get() ==2:
        opcionEscogida+= " montaña"
    if turismo_rural.get()==3:
        opcionEscogida+= " turismo rural"
    textoFinal.config(text="La ooción escogida es: "+opcionEscogida)

miFrame = Frame(root)
miFrame.pack()
etiqueta = Label(miFrame)
etiqueta.config(text="Elige destinos:",width=50)
etiqueta.pack()
Checkbutton(miFrame,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcionViaje).pack()
Checkbutton(miFrame,text="Montaña",variable=montagna,onvalue=2,offvalue=0,command=opcionViaje).pack()
Checkbutton(miFrame,text="Turismo rural",variable=turismo_rural,onvalue=3,offvalue=0,command=opcionViaje).pack()
textoFinal =Label(miFrame)
textoFinal.pack()



mainloop()