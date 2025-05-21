import sympy as sp

def generating_function(x:sp.Symbol, p_a:sp.Symbol, p_r:sp.Symbol, p_i:sp.Symbol, n:sp.Symbol)->sp.Expr:

    g = (p_a*(x**1) + p_r*(x**-1) + p_i*(x**0))**n
    return g

def derivative_generating_function(g:sp.Expr, x:sp.Symbol):
    # Calculate the derivative of the generating function
    dg = sp.diff(g, x).doit()
    
    return dg

def exp_generating_function(g:sp.Function):

    gn = sp.expand(g)
    return gn

x, n = sp.symbols('x, n')
p_a, p_r, p_i = sp.symbols('p_a, p_r, p_i')


g = generating_function(x, p_a, p_r, p_i, n)

eg = g.subs(n, 2)
eg = sp.expand(eg)
print('EXPANDED G: ', eg)



# Dictionary to hold coefficients by power
coeff_dict = {}

# Break the expression into terms and analyze powers
for term in eg.as_ordered_terms():
    term = sp.expand(term)
    coeff, power = term.as_coeff_exponent(x)
    coeff_dict[power] = coeff_dict.get(power, 0) + coeff

# Sort and display coefficients by power of x
for power in sorted(coeff_dict):
    print(f"Coefficient of x^{power}: {coeff_dict[power]}")

#-----------------------------------------------
#range(np.ceil(n_d*t), n_d +1)
prob_success_at_level_d = 0
for exponent in range(-2, 3):
    #print('coefficient', coeff_dict[exponent])
    print('subbed in coefficient', coeff_dict[exponent].subs({p_a: 0.5, p_r: 0.3, p_i: 0.2, x: 1}))
    prob_success_at_level_d += coeff_dict[exponent].subs({p_a: 0.5, p_r: 0.3, p_i: 0.2, x: 1})
print('SUCCESS AT DEPTH LEVEL D', prob_success_at_level_d)

#-------------------------------------------------
g1_psub = g.subs({p_a: 0.5, p_r: 0.3, p_i: 0.2, n:1})
g1 = g.subs(n, 1)
print("Generating Function:", g, type(g))
print("Substituted Generating Function with probabilities:", g1_psub)
print("Substituted Generating Function:", g1)
dg = derivative_generating_function(g, x)
print("Derivative of Generating Function:", dg)
print("Substituted Derivative of Generating Function:", dg.subs({p_a: 0.5, p_r: 0.3, p_i: 0.2, n:2, x: 1}))



g3 = g.subs(n, 3)
dg3 = derivative_generating_function(g3, x)

print('diff of g(x)^3', dg3)

expanded_dg3 = sp.expand(dg3)
print("Expanded Derivative of g(x)^3:", expanded_dg3)
#print("Exponential Generating Function:", eg)
