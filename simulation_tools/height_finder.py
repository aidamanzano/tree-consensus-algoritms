import numpy as np
import matplotlib.pyplot as plt

d = np.arange(0, 10, 1)
rho = np.arange(0, 1, 0.1)
y = rho * np.exp(d)
print(len(rho))
print(len(d))
print(len(y))
plt.plot(d, y, label='rho=0')
plt.title(r'Height vs. $\rho^d$')
plt.xlabel(r'Height ($h$)')
plt.ylabel(r'$\rho ^d$')
plt.show()