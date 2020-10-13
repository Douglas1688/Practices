import sqlite3

miconexion = sqlite3.connect("primerabase")
miCursor = miconexion.cursor()
"""miCursor.execute("CREATE TABLE PRODUCTO ("
                 "nombre_articulo varchar(50),precio integer,"
                 "seccion varchar(20) )")
"""
#miCursor.execute("INSERT INTO PRODUCTO VALUES ('BALÓN',15,'DEPORTES')")

"""variosProductos=[
("Camiseta",10,"Deportes"),
("Jarrón",90,"Cerámica"),
("Camión",20,"Juguetería"),
("Pantalón",30,"Casual")
]
miCursor.executemany("INSERT INTO PRODUCTO VALUES (?,?,?)",variosProductos)
"""

miCursor.execute("SELECT *FROM PRODUCTO")
variosProductos = miCursor.fetchall()
for x in variosProductos:
    print("Nombre Artículo:",x[0])
miconexion.commit()

miconexion.close()