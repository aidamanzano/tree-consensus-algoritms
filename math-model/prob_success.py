import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n_d = [1, 2, 3, 4] # base branching structure


height = len(n_d)

#Question: should we make t*n_d[d] an integer and use factorial, or keep it float and use gamma function?
def binomial_probability(p_a, n, k):
        n_choice_k = math.factorial(n)/(math.factorial(k) * math.factorial(n-k))
        binomial_prob = n_choice_k * ((p_a ** k) * ((1-p_a) ** (n-k)))
        return binomial_prob


def probability_of_success(p_a, n_d, t, height = len(n_d)):
#TODO: note that this is already taking the product over depth levels.
#remember to change it and split the sum and the product operand, since p_success changes
#at each depth level.
    total_prob_sucess = 1
    for d in range(height-1, -1, -1):
        n = n_d[d]
        k = n_d[d] * t
        
        #TODO: change this later maybe to float and gamma function.
        k = int(np.ceil(k))
        #print(f"n: {n}, k:{k}, depth: {d}")

        # Calculate the binomial probability

        prob_sucess_depth = 0

        #summing over all the possible valid outcomes. (ie: from getting k approvals, to k+1, k+2, ... n)
        for i in range(k, n+1):
            #print(i)
            binomial_prob= binomial_probability(p_a, n, i)
            prob_sucess_depth += binomial_prob
        #print(f"prob_sucess: {prob_sucess_depth}")
        total_prob_sucess *= prob_sucess_depth
    #print(f"total_prob_sucess: {total_prob_sucess}")
    return total_prob_sucess


# Create grid
p_a_values = np.arange(0.1, 1.1, 0.1)
t_values = np.arange(0.1, 1.1, 0.1)
P, T = np.meshgrid(p_a_values, t_values)

Z = np.zeros_like(P)

# Compute Z values
for i in range(P.shape[0]):
    for j in range(P.shape[1]):
        p_a = P[i, j]
        
        t = T[i, j]
        
        Z[i, j] = probability_of_success( p_a, n_d, t)
        print(f"p_a: {p_a}, t: {t}, Z: {Z[i, j]}")


# Plot
fig, ax = plt.subplots()
contour = ax.contourf(P, T, Z, levels=10, cmap='plasma')
fig.colorbar(contour)
ax.set_xlabel(r'$p_a$')
ax.set_ylabel(r'$t$')
#ax.set_title('Contour Plot of Probability of Success')
plt.show()

#total_prob_sucess = probability_of_success(n_d, t)
#print(f"total_prob_sucess: {total_prob_sucess}")


