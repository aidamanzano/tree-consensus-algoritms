import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def binomial_probability(p_a, n, k):
    if k > n:
        return 0
    return math.comb(n, k) * (p_a ** k) * ((1 - p_a) ** (n - k))

def probability_of_success(p_a, n_d, t):
    total_prob_success = 1
    for d in range(len(n_d) - 1, -1, -1):
        n = n_d[d]
        k = int(np.ceil(n * t))
        prob_success_depth = sum(binomial_probability(p_a, n, i) for i in range(k, n + 1))
        total_prob_success *= prob_success_depth
    return total_prob_success

# Set t = 1 (full approval required)
t = 1.0
heights = [1, 2, 3, 4]
p_a_values = np.linspace(0.1, 1.0, 20)

# Create meshgrid
P, H = np.meshgrid(p_a_values, heights)
Z = np.zeros_like(P)

# Compute success probabilities
for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        height = int(H[i, j])
        p_a = P[i, j]
        n_d = [2] * height
        Z[i, j] = probability_of_success(p_a, n_d, t)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(P, H, Z, cmap='viridis')

ax.set_xlabel('p_a (Agent Approval Probability)')
ax.set_ylabel('Height')
ax.set_zlabel('Probability of Success')
ax.set_title('Success Probability vs p_a and Tree Height (t = 1.0)')

plt.show()

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Binomial probability function
def binomial_probability(p_a, n, k):
    if k > n:
        return 0
    return math.comb(n, k) * (p_a ** k) * ((1 - p_a) ** (n - k))

# Success probability across tree
def probability_of_success(p_a, n_d, t):
    total_prob_success = 1
    for d in range(len(n_d) - 1, -1, -1):
        n = n_d[d]
        k = int(np.ceil(n * t))
        prob_success_depth = sum(binomial_probability(p_a, n, i) for i in range(k, n + 1))
        total_prob_success *= prob_success_depth
    return total_prob_success

# Constants
t = 1.0
p_a_values = np.linspace(0.1, 1.0, 20)
heights = [1, 2, 3, 4]
P, H = np.meshgrid(p_a_values, heights)

# Animation setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = [None]  # placeholder

def update(num):
    ax.clear()
    n = num + 1  # num in [0, 1, 2, 3] → n in [1, 2, 3, 4]

    Z = np.zeros_like(P)
    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            height = int(H[i, j])
            p_a = P[i, j]
            n_d = [n] * height
            Z[i, j] = probability_of_success(p_a, n_d, t)

    surf[0] = ax.plot_surface(P, H, Z, cmap='viridis')
    ax.set_zlim(0, 1)
    ax.set_xlabel('p_a')
    ax.set_ylabel('Height')
    ax.set_zlabel('Probability of Success')
    ax.set_title(f'Branching Factor per Level = {n}')

# Create animation
ani = FuncAnimation(fig, update, frames=4, repeat=True, interval=1500)

plt.show()

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def binomial_probability(p_a, n, k):
    if k > n:
        return 0
    return math.comb(n, k) * (p_a ** k) * ((1 - p_a) ** (n - k))

def probability_of_success(p_a, n_d, t):
    total_prob_success = 1
    for d in range(len(n_d) - 1, -1, -1):
        n = n_d[d]
        k = int(np.ceil(n * t))
        prob_success_depth = sum(binomial_probability(p_a, n, i) for i in range(k, n + 1))
        total_prob_success *= prob_success_depth
    return total_prob_success

# Parameters
t = 1.0
p_a_values = np.linspace(0.1, 1.0, 20)
heights = np.arange(1, 11)
P, H = np.meshgrid(p_a_values, heights)

# This list will generate frames like:
# [1], [1,2], [1,2,3], [1,2,3,4]
n_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Animation setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = [None]

def update(frame):
    ax.clear()
    n_d_example = [n_base[i] for i in range(frame + 1)]

    Z = np.zeros_like(P)
    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            height = int(H[i, j])
            n_d = n_d_example[:height]
            p_a = P[i, j]
            Z[i, j] = probability_of_success(p_a, n_d, t)

    surf[0] = ax.plot_surface(P, H, Z, cmap='viridis')
    ax.set_zlim(0, 1)
    ax.set_xlabel('p_a')
    ax.set_ylabel('Height')
    ax.set_zlabel('Probability of Success')
    ax.set_title(f'n_d = {n_d_example}')

# Create animation: 4 frames, one for each growing n_d
ani = FuncAnimation(fig, update, frames=10, repeat=True, interval=1500)

plt.show()
