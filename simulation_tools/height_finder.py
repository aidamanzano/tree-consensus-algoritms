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

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define ranges
h = np.arange(0, 10, .1)
rho = np.arange(0, 1, 0.01)

# Create meshgrid
RHO, H = np.meshgrid(rho, h)

# Compute Z = rho^h
Z = RHO ** H

# Compute partial derivative dZ/dh (gradient w.r.t. h)
# We use the analytical derivative: d/dh (rho^h) = rho^h * ln(rho)
# Note: log(0) = -inf, so we handle it carefully
with np.errstate(divide='ignore', invalid='ignore'):
    dZ_dh = Z * np.log(RHO)
    dZ_dh[np.isnan(dZ_dh)] = 0  # remove NaNs from log(0)
    dZ_dh[np.isinf(dZ_dh)] = 0  # remove infs from log(0)

# Plot the gradient surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot surface of the gradient
surf = ax.plot_surface(RHO, H, dZ_dh, cmap='plasma', edgecolor='none')

# Labels and title
ax.set_xlabel(r'$\rho$')
ax.set_ylabel(r'Height ($h$)')
ax.set_zlabel(r'$\frac{\partial}{\partial h} \rho^h$')
ax.set_title(r'Gradient of $\rho^h$ with respect to $h$')

# Add color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

plt.tight_layout()
plt.show()
