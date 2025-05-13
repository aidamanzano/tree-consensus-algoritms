import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define binomial probability using math.comb
def binomial_probability(p_a, n, k):
    if k > n:
        return 0
    return math.comb(n, k) * (p_a ** k) * ((1 - p_a) ** (n - k))

# Calculate the nested probability of success
def probability_of_success(p_a, n_d, t):
    total_prob_success = 1.0
    for d in range(len(n_d) - 1, -1, -1):
        n = n_d[d]
        k = int(np.ceil(n * t))
        prob = sum(binomial_probability(p_a, n, i) for i in range(k, n + 1))
        total_prob_success *= prob
    return total_prob_success

# Define grid
p_a_vals = np.arange(0.1, 1.1, 0.1)
t_vals = np.arange(0.1, 1.1, 0.1)
P, T = np.meshgrid(p_a_vals, t_vals)

# Setup figure
fig, ax = plt.subplots()
levels = np.linspace(0, 1, 11)
contour = ax.contourf(P, T, np.zeros_like(P), levels=levels, cmap='viridis')
cbar = fig.colorbar(contour)
ax.set_xlabel('p_a')
ax.set_ylabel('t')

# Update function for animation
def update(frame):
    
    n_d = [2] * (frame + 1)
    Z = np.zeros_like(P)

    for i in range(P.shape[0]):
        for j in range(P.shape[1]):
            Z[i, j] = probability_of_success(P[i, j], n_d, T[i, j])

    contour = ax.contourf(P, T, Z, levels=levels, cmap='viridis')
    ax.set_title(f'Probability of Success\nn_d = {n_d}')
    ax.set_xlabel('p_a')
    ax.set_ylabel('t')
    return contour.collections


# Create animation
anim = FuncAnimation(fig, update, frames=4, interval=1500, blit=False, repeat=True)

plt.tight_layout()
plt.show()
