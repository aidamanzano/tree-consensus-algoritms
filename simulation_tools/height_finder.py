import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Define ranges
h = np.arange(0, 10, .1)
rho = np.arange(0, 1, 0.01)

# Create meshgrid
RHO, H = np.meshgrid(rho, h)

# Compute rho^h

Z = RHO ** H


# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(RHO, H, Z, cmap='viridis', vmin=0, vmax=1, shade=False)


# Add labels and title
ax.set_xlabel(r'$\rho$')
ax.set_ylabel(r'Height ($h$)')
ax.set_zlabel(r'$\rho^h$')
#ax.set_title(r'3D Surface Plot of $\rho^h$')






# Add color bar
cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
cbar.set_label(r'$\rho^h$')

# Force consistent tick marks including 1.0
cbar.set_ticks(np.linspace(0, 1, 6))  # [0. , 0.2, 0.4, 0.6, 0.8, 1.0]

plt.tight_layout()
plt.show()



