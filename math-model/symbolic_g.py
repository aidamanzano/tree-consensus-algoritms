import sympy as sp

def generating_function(x:sp.Symbol, p_a:sp.Symbol, p_r:sp.Symbol, p_i:sp.Symbol)->sp.Expr:

    g = (p_a*(x**1) + p_r*(x**-1) + p_i*(x**0))**n
    return g

def derivative_generating_function(g:sp.Expr, x:sp.Symbol):
    # Calculate the derivative of the generating function
    dg = sp.diff(g, x).doit()
    
    return dg

def exp_generating_function(g:sp.Function, n:sp.Symbol):

    eg = g**n
    eg = sp.expand(eg)
    return eg

x, n = sp.symbols('x, n')
p_a, p_r, p_i = sp.symbols('p_a, p_r, p_i')


g = generating_function(x, p_a, p_r, p_i)
g1_psub = g.subs({p_a: 0.5, p_r: 0.3, p_i: 0.2, n:1})
g1 = g.subs(n, 1)
print("Generating Function:", g, type(g))
print("Substituted Generating Function with probabilities:", g1_psub)
print("Substituted Generating Function:", g1)
dg = derivative_generating_function(g, x)
print("Derivative of Generating Function:", dg)
print("Substituted Derivative of Generating Function:", dg.subs({p_a: 0.5, p_r: 0.3, p_i: 0.2, n:2, x: 1}))


#eg = exp_generating_function(g, n)

#print("Exponential Generating Function:", eg)
