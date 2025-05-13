import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define binomial probability
def binomial_probability(p_a, n, k):
    if k > n:
        return 0
    return math.comb(n, k) * (p_a ** k) * ((1 - p_a) ** (n - k))

# Define tree success probability
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
p_a_values = np.linspace(0.1, 1.0, 100)
n_base = [1, 2, 3, 4, 5]  # base branching structure

# Animation setup
fig, ax = plt.subplots(figsize=(8, 5))
line, = ax.plot([], [], lw=2)
title = ax.text(0.5, 1.05, '', transform=ax.transAxes, ha='center', fontsize=12)

ax.set_xlim(0.1, 1.0)
ax.set_ylim(0, 1.05)
ax.set_xlabel("p_a (Approval Probability)")
ax.set_ylabel("Success Probability")
ax.grid(True)

def update(frame):
    height = frame + 1
    n_d = n_base[:height]
    probs = [probability_of_success(p_a, n_d, t) for p_a in p_a_values]

    line.set_data(p_a_values, probs)
    title.set_text(f"Tree Structure: n_d = {n_d}")
    return line, title

# Animate through 4 tree structures
ani = FuncAnimation(fig, update, frames=4, interval=1500, repeat=True)

plt.tight_layout()
plt.show()
