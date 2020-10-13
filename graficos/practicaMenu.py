from tkinter import *
from tkinter import messagebox
root = Tk()
def infoAdicional():
    messagebox.showinfo("Procesador de Juan","Procesador de textos versión 2020")

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def salirAplicacion():
    #valor=messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
    valor = messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?")
    """if valor == "yes":
        root.destroy()"""
    if valor == True:
        root.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar, documento bloqueado")
    

root.title("Ejemplo de Menú")
barraMenu = Menu(root)
root.config(menu=barraMenu)
root.geometry("650x350")


#------------Archivo-------------------
archivoMenu = Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)


#-------------- Edición---------------------
archivoEdicion = Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")


#--------------Herramienta--------------------
archivoHerramienta = Menu(barraMenu,tearoff=0)

#---------------Ayuda---------------------
archivoAyuda = Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de",command=infoAdicional)


barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edición",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramienta)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

root.mainloop()