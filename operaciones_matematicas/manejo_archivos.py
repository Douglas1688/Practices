from io import open
"""
archivo_texto =open("archivo.txt", "a",encoding="utf-8")#Lectura y escritura
lst_txt=archivo_texto.readlines()
lst_txt.insert(1,"Esta línea ha sido incluida desde el exterior\n")
archivo_texto.seek(0)
archivo_texto.writelines(lst_txt)
archivo_texto.close()"""
archivo_texto = open("archivo.txt","a",encoding="utf-8")
archivo_texto.writelines("Esto es lo último que he escrito ")
archivo_texto.close()

