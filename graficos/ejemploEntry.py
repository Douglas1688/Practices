from tkinter import *
def codigoBoton():
    minombre.set("Juan")
raiz = Tk()
miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

minombre= StringVar()

cuadroNombre = Entry(miFrame,textvariable=minombre)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

cuadroNombre.config(fg="blue",justify="center")
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=10,pady=10)
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)
#comentarios
textoComentario=Text(miFrame,width=40,height=5)
textoComentario.grid(row=4,column=1,padx=10,pady=10)
#scroll
scrollVertical = Scrollbar(miFrame,command=textoComentario.yview)
scrollVertical.grid(row=4,column=2,sticky="nsew")


nLabel = Label(miFrame,text="Nombre:")
nLabel.grid(row=0,column=0,sticky="w",padx=10,pady=10)
pLabel = Label(miFrame,text="Contraseña:")
pLabel.grid(row=1,column=0,sticky="w",padx=10,pady=10)
aLabel = Label(miFrame,text="Apellido:")
aLabel.grid(row=2,column=0,sticky="w",padx=10,pady=10)
dLabel = Label(miFrame,text="Dirección:")
dLabel.grid(row=3,column=0,sticky="w",padx=10,pady=10)
comentarioLabel = Label(miFrame,text="Comentarios:")
comentarioLabel.grid(row=4,column=0,sticky="w",padx=10,pady=10)
btnEnvio = Button(raiz,text="Enviar",command=codigoBoton)
btnEnvio.pack()

raiz.mainloop()