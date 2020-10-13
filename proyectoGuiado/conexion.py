import sqlite3
from tkinter import messagebox

def conexion():
    try:
        conexion = sqlite3.connect("guiaBD")
        miCursor = conexion.cursor()
        miCursor.execute('''
        CREATE TABLE datosusuarios(
        id integer primary key autoincrement,
        nombre_usuario varchar(50),
        password varchar(50),
        apellido varchar(10),
        direccion varchar(50),
        comentarios varchar(100)
        )''')

        messagebox.showwarning("BBDD", "BBDD creada con éxito!!!")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe!!!")

    miCursor.close()

