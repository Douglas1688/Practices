def convertidorFaC():
    try:
        far = float(input("Ingrese la temperatura en Fº: "))
        cel = (far-32.0)*5.0/9.0
        print("La temperatura es: ",round(cel,2),"ºC")

    except:
        print("Datos incorrectos!!!")
        convertidorFaC()

convertidorFaC()