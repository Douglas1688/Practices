import numpy as np
"""
a = np.array([0,{"uno":"número uno"},2,3,4])
x = np.zeros((2,3,4))
print(a.size)
print(a.ndim)
print(a.shape)
print(x.ndim)
print(x)

c = np.array([20,1,2,3,4])
print(c)
c[0]=100
print(c)
c[4]=0
print(c)
d = c[1:4]
print(d)
c[3:5]= 300,400
print(c)"""

u = np.array([1,0])
v=np.array([0,1])
z = u-(2*v)
print(z)
u = np.array([1,2])
v=np.array([3,2])
z = u*v
print(z)
u=np.array([1,2])
v=np.array([3,1])
result =np.dot(u,v) #Producto entre 2 vectores
print(result)

a = np.array([3,3,3,3])
mean_a = a.mean() #Media aritmética
print(mean_a)

b = np.array([1,-2,3,4,5])
max_b = b.max() #Muestra el valor mayor del arreglo
print(max_b)

x =np.array([0,np.pi/2,np.pi])
y = np.sin(x)
print(y)

print(np.linspace(-2,2,num=4))# realiza una lista con un intervalo de números







