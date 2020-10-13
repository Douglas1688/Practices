def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args,**kwargs):
        #Acciones adicionales que decoran
        print("Vamos a realizar un cálculo: ")
        funcion_parametro(*args,**kwargs)
        #Acciones adicionales que decoran

        print("Hemos terminado el cálculo")
    return funcion_interior

@funcion_decoradora
def potencia(base, exp):
    print(pow(base, exp))



@funcion_decoradora
def suma (n1,n2,n3):
    print(n1+n2+n3)

@funcion_decoradora
def resta(n1,n2):
    print(n1-n2)

suma(7,5,8)
print("*****************************")
resta(12,10)
print("*****************************")
potencia(base=2,exp=5)

