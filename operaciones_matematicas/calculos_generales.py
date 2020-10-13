"""Este módulo permite realizar operaciones matemáticas"""
def sumar(x,y):
    print("El resultado de la suma es: ",x+y)
def restar(x,y):
    print("El resultado de la suma es: ",x-y)
def multiplicar(x,y):
    print("El resultado de la suma es: ",x*y)
def dividir(x,y):
    print("El resultado de la suma es: ",x//y)
def potencia(x,y):
    print("El resultado de la suma es: ",x**y)
def raiz_cuadrada(x,y):
    print("El resultado de la suma es: ",x**(1/2))
def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)