import numpy as np
from numpy import matlib
from numpy import lib
from matplotlib import pyplot as plt
# https://www.yiibai.com/numpy



x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
y1=np.cos(x)

plt.subplot(2,1,1)
plt.title("sin")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.subplot(2,1,2)
plt.title("cos")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y1)
plt.show()
