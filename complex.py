import numpy as np
from matplotlib import pyplot as plt
l =([-2+2j,-1+2j,0+2j,1+2j,2+2j,-1+4j,0+4j,1+4j])
x = [x.real for x in l]
y = [y.imag for y in l]
plt.plot(x,y,'o')
plt.xlabel('Real values')
plt.ylabel('imaginary values')
plt.title('Graph of Complex number')
plt.grid(True)
plt.show()