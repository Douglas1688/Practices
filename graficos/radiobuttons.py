from tkinter import *
raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()
varOpcion= IntVar()
def imprimir():
    #print(varOpcion.get())
    if varOpcion.get()==1:
        etiqueta.config(text="has elegido masculino")
    else:
        etiqueta.config(text="has elegido femenino")
Label(miFrame,text="Género:").pack()
Radiobutton(miFrame,text="Masculino",variable=varOpcion,value=1,command=imprimir).pack()
Radiobutton(miFrame,text="Femenino",variable=varOpcion,value=2,command=imprimir).pack()

etiqueta =Label(miFrame)
etiqueta.pack()


mainloop()