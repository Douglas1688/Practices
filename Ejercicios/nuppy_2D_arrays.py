import  numpy as np
a = [[11,12,13],[21,22,23],[31,32,33]]

A = np.array(a)

print(A.ndim) #Dimensión
print(A.shape)# Forma (3,3)
print(A.size)#Tamaño : 9

print(A[0:2,2])

b = np.array([[0,1,1],[1,0,1]])
c= np.array([[1,1],[1,1],[-1,1]])


print(np.dot(b,c))