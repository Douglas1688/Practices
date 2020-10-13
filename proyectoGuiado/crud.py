from tkinter import *
from proyectoGuiado.conexion import *

root =Tk()
root.title("Proyecto Guíado")
root.geometry("300x400")
def salirAplicacion():
    valor = messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    if valor == "yes":
        root.destroy()


def borrarCampos():
    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    txtComentario.delete(1.0,END)




miFrame = Frame(root)
miFrame.pack()
#################Cuadros de texto##################

miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion =StringVar()

def insertar():
    valor = messagebox.askquestion("Insertar","¿Guardar datos?")
    if valor == "yes":
        miConexion = sqlite3.connect("guiaBD")
        miCursor = miConexion.cursor()
        miCursor.execute('''INSERT INTO datosusuarios values (NULL,?,?,?,?,?)''',(miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),txtComentario.get(1.0,END)))

        miConexion.commit()
        messagebox.showinfo("BBDD","Registro insertado con éxito!")
        miConexion.close()
        borrarCampos()


def leerRegistro():
    n =miId.get()
    if n.isdigit():
        miConexion = sqlite3.connect("guiaBD")
        miCursor=miConexion.cursor()
        miCursor.execute("SELECT * FROM datosusuarios WHERE id = "+n+"")
        registro = miCursor.fetchall()

        for x in registro:
            miId.set(x[0])
            miNombre.set(x[1])
            miPass.set(x[2])
            miApellido.set(x[3])
            miDireccion.set(x[4])
            txtComentario.insert(1.0,x[5])
            miConexion.commit()
    else:
        messagebox.showwarning("Advertencia","Por favor, ingrese id en el campo correspondiente")



    #miNombre.set(registro[1])


def modificarRegistro():
    sqlquery = """UPDATE datosusuarios SET nombre_usuario=?,password=?,apellido=?,direccion=?,comentarios=? where id= ?"""
    inputs=(miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),txtComentario.get(1.0,END),miId.get())
    miConexion= sqlite3.connect("guiaBD")
    miCursor = miConexion.cursor()
    miCursor.execute(sqlquery,inputs)
    #miCursor.execute('''UPDATE datosusuarios SET nombre_usuario = ? , password=? , apellido=?, direccion=?, comentarios=? where id = ?''',(miNombre.get(),
     #                miPass.get(),miApellido.get(),miDireccion.get(),txtComentario.get(1.0,END),miId.get()))
    miConexion.commit()
    miConexion.close()
    messagebox.showinfo("ACTUALIZAR","Registro modificado con éxito!")

def eliminaRegistro():
    sqlquery = """DELETE FROM datosusuarios where id= ?"""
    num = miId.get()
    valor = messagebox.askquestion("Eliminar Registro","¿Desea eliminar registro?")
    if valor == "yes":
        miConexion = sqlite3.connect("guiaBD")
        miCursor = miConexion.cursor()
        miCursor.execute(sqlquery, num)
        miConexion.commit()
        miConexion.close()
        borrarCampos()
        messagebox.showinfo("Eliminar", "Registro eliminado con éxito!")




#--------------ID-----------------------
txtId = Entry(miFrame,textvariable=miId)
txtId.grid(row=0,column=1,padx=10,pady=10)
lblId = Label(miFrame,text="id")
lblId.grid(row=0,column=0)
#-------------NOMBRE---------------------
txtNombre = Entry(miFrame,textvariable= miNombre)
txtNombre.grid(row=1,column=1,padx=10,pady=10)
lblNombre = Label(miFrame,text="Nombre")
lblNombre.grid(row=1,column=0)

#-------------CLAVE---------------------
txtClave = Entry(miFrame,textvariable = miPass)
txtClave.grid(row=2,column=1,padx=10,pady=10)
lblClave = Label(miFrame,text="Clave")
lblClave.grid(row=2,column=0)
txtClave.config(show="*")

#-------------APELLIDO---------------------
txtApellido = Entry(miFrame,textvariable=miApellido)
txtApellido.grid(row=3,column=1,padx=10,pady=10)
lblApellido = Label(miFrame,text="Apellido")
lblApellido.grid(row=3,column=0)

#-------------DIRECCIÓN---------------------
txtDireccion = Entry(miFrame,textvariable=miDireccion)
txtDireccion.grid(row=4,column=1,padx=10,pady=10)
lblDireccion = Label(miFrame,text="Dirección")
lblDireccion.grid(row=4,column=0)

#-------------COMENTARIOS---------------------
txtComentario = Text(miFrame,width=20,height=5)
txtComentario.grid(row=5,column=1,padx=10,pady=10)
lblComentario = Label(miFrame,text="Comentarios")
lblComentario.grid(row=5,column=0)




barra_menu = Menu(root)
root.config(menu=barra_menu)

################MENÚ##########################
#---------------menú BBDD------------------
archivo_BBDD=Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="BBDD",menu=archivo_BBDD)
archivo_BBDD.add_command(label="Conexión",command=conexion)
archivo_BBDD.add_command(label="Salir",command=salirAplicacion)

#--------------menú Borrar------------------
archivo_Borrar=Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="Borrar",menu=archivo_Borrar)
archivo_Borrar.add_command(label="Borrar campos",command=borrarCampos)

#-------------menú CRUD--------------------
archivo_CRUD=Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="CRUD",menu=archivo_CRUD)
archivo_CRUD.add_command(label="Insertar",command=insertar)
archivo_CRUD.add_command(label="Mostrar",command=leerRegistro)
archivo_CRUD.add_command(label="Actualizar")
archivo_CRUD.add_command(label="Eliminar")
#-------------menú ayuda
archivo_ayuda=Menu(barra_menu,tearoff=0)
barra_menu.add_cascade(label="Ayuda",menu=archivo_ayuda)
archivo_ayuda.add_command(label="Licencia")
archivo_ayuda.add_command(label="Acerca de")


###############BOTONES########################
miFrame2 = Frame(root)
miFrame2.pack()
btnInsertar = Button(miFrame2, text="Insertar",command=insertar)
btnInsertar.grid(row=1,column=0,sticky="e",padx=10,pady=10)

btnMostrar = Button(miFrame2, text="Mostrar",command=leerRegistro)
btnMostrar.grid(row=1,column=1,sticky="e",padx=10,pady=10)

btnActualizar = Button(miFrame2, text="Actualizar",command=modificarRegistro)
btnActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

btnEliminar = Button(miFrame2, text="Eliminar",command=eliminaRegistro)
btnEliminar.grid(row=1,column=3,sticky="e",padx=10,pady=10)





root.mainloop()