import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define ranges
h = np.arange(0, 10, 1)
rho = np.arange(0, 1, 0.1)

# Create meshgrid
RHO, H = np.meshgrid(rho, h)

# Compute rho^h

Z = RHO ** H

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(RHO, H, Z, cmap='viridis', edgecolor='none')

# Add labels and title
ax.set_xlabel(r'$\rho$')
ax.set_ylabel(r'Height ($h$)')
ax.set_zlabel(r'$\rho^h$')
ax.set_title(r'3D Surface Plot of $\rho^h$')

# Add color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

plt.tight_layout()
plt.show()

