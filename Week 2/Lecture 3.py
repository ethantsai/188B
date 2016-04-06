import numpy as np
from matplotlib.pyplot import plot, show

x = np.linspace(0,2*np.pi,100)
for i in range(1,501):
    plot(x,np.sin(i*x))
show()