import numpy as np
import matplotlib.pyplot as plt
from pylab import  *
x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

figure()
plt.plot(x,y)
plt.title("Prueba 1")
plt.show()