#A script with all the functions necessary to run simulations of the mathematical model of the Tree Consensus Algorithm
#For a more step by step explanation, please refer to math_model.ipynb and the paper of this work available on ArXiv soon.

import sympy as sp
#we will manipulate the generating function symbolically to compute the probability of success in a single depth level for a single parent
import math
import numpy as np

def generating_function(x:sp.Symbol, p_a:sp.Symbol, p_r:sp.Symbol, p_i:sp.Symbol, n:sp.Symbol)->sp.Expr:
    """Generating function to keep track of the probability that an approval is either accept(1), reject(-1) or ignore(0).
    The probability that the approval is each one of these values is the coefficient of the x term. For more info check the paper.
    
    Inputs: 
    x: symbolic variable, later we substitue x = 1 to evaluate probability of success of a parent.

    n: exponent of the generating function (this is the number of times a parent asks for an approval, which == number of children parent has.)
    
    p_a: symbolic variable representing the probability that an agent accepts the parent's claim
    p_r: symbolic variable representing the probability that an agent rejects the parent's claim
    p_i: symbolic variable representing the probability that an agent ignores the parent's claim

    All inputs are symbolic objects.
    """
    g = (p_a*(x**1) + p_r*(x**-1) + p_i*(x**0))**n
    return g


#Here we will sub into n the number of neighbours a parent has at depth d
def sub_neighbours_into_g(g:sp.Expr, n_symbolic:sp.Symbol, n:int):
    """Expands the generating function and substitues the integer value into the exponent of the generating function.
    The exponent n is the number of children a parent has at that depth level, n_d.
    
    Returns expanded generating function with substituted value for the exponent n.
    
    inputs:
    g: generating function
    n_symbolic: the symbolic variable that is the exponent of the generating function
    n: the integer value to substitute into n_symbolic"""
    gn = g.subs(n_symbolic, n)
    expanded_gn = sp.expand(gn)
    return expanded_gn

def coefficients_g(expanded_generating_function:sp.Expr, x:sp.Symbol)-> dict:
    """extracting coefficients of x from the expanded generating function.

    Inputs:
    expanded_generating_function: expanded generating function: sympy expression
    x: variable to extract coefficients from. 

    returns: dict:{power: coefficient}
    """
    # Dictionary to hold coefficients by power
    coeff_dict = {}

    # Break the expression into terms and analyze powers
    for term in expanded_generating_function.as_ordered_terms():
        term = sp.expand(term)
        coeff, power = term.as_coeff_exponent(x)
        coeff_dict[power] = coeff_dict.get(power, 0) + coeff

    return coeff_dict

def prob_success_single_parent_at_depth_d(coeff_dict:dict, n:int, k:int, p_a:sp.Symbol, p_r:sp.Symbol, p_i:sp.Symbol, x:sp.Symbol, p_accept:float, p_reject:float, p_ignore:float):
    """Returns: probability of a single parent receiving enough approvals at a given depth level d.

    Here we evaluate the symbolic coefficients of the expanded generating function by inputing the actual values of 
    p_accept, p_reject, p_ignore.
    
    inputs:
    coeff_dict: dictionary with the coefficients of each term of x from the generating function. 
    The keys are the x exponent, and the values are the coefficient of that x^exponent term

    n: branching factor at that depth level. (i.e: number of children the parent has at depth level d)
    k: minimum number of children that need to approve the parent so it is considered valid.

    p_a: symbolic variable representing the probability that an agent accepts the parent's claim
    p_r: symbolic variable representing the probability that an agent rejects the parent's claim
    p_i: symbolic variable representing the probability that an agent ignores the parent's claim

    p_accept: probability that a single child accepts its parent (response = 1)
    p_reject: probability that a single child rejects its parent (response = -1)
    p_ignore: probability that a single child ignores its parent (response = 0)
    """
    #range(np.ceil(n_d*t), n_d +1)
    prob_success = 0
    for exponent in range(k, n+1):

        prob_success += coeff_dict[exponent].subs({p_a: p_accept, p_r: p_reject, p_i: p_ignore, x: 1})
    return prob_success

def binomial_probability(p_success:float, n:int, k:int)-> float:
        """your good old binomial probability formula."""
        n_choice_k = math.factorial(n)/(math.factorial(k) * math.factorial(n-k))
        binomial_prob = n_choice_k * ((p_success ** k) * ((1-p_success) ** (n-k)))
        return binomial_prob

def probability_of_success_at_depth_d(p_success:float, N:int, t:float)->float:
    """p_s: probability of ENOUGH parents receiving enough approvals from their n_d children
    N: number of parents in that depth level
    t: threshold parameter, float (percentage) between 0,1 dictating minimum number of approvals necessary
    
    returns: probability of enough PARENTS succeeding at depth level d"""
    k = int(np.ceil(N*t))


    # Calculate the binomial probability
    prob_sucess_depth = 0

    #summing over all the possible valid outcomes. (ie: from getting k approvals, to k+1, k+2, ... n)
    for i in range(k, N+1):
        #print(i)
        binomial_prob= binomial_probability(p_success, N, i)
        prob_sucess_depth += binomial_prob
    return prob_sucess_depth

def parent_array(height:int, branching_factor:list):
    """Returns list where each element is the number of parents at its index's depth level.
    e.g: N_d_array[0] = 1 means there is one parent at depth level 0.
    
    inputs: 
    height: height of the tree
    branching_factor: list where each element is the branching factor of its index's depth level. 
    branching_factor[height] must always = 0, as leaves of tree should have no children."""

    assert len(branching_factor) -1 == height
    assert branching_factor[height] == 0
    N_d_array = []
    for d in range(len(branching_factor)):
        #print(branching_factor[:d])
        
        ancestor_branching_factors = branching_factor[:d]
        N_d = 1
        for n in ancestor_branching_factors:
            N_d = N_d * n
            #print(N_d)
        N_d_array.append(N_d)
    return N_d_array


def prob_TCA_True(height:int, branching_factor:list, threshold:float,
                x:sp.Symbol, p_a:sp.Symbol, p_r:sp.Symbol, p_i:sp.Symbol, symbolic_n:sp.Symbol, 
                probabilities_response_kwargs:dict):
    """
    Inputs:
    height: height of the tree
    branching_factor: list where each element is the branching factor of its index's depth level.
    t: threshold parameter, float (percentage) between 0,1 dictating minimum number of approvals necessary

    x: symbolic variable, we substitue x = 1 to evaluate probability of success of a parent.
    
    n: symbolic variable representing the exponent of the generating function.
    
    p_a: symbolic variable representing the probability that an agent accepts the parent's claim
    p_r: symbolic variable representing the probability that an agent rejects the parent's claim
    p_i: symbolic variable representing the probability that an agent ignores the parent's claim

    probabilities_response_kwargs = dict with keys 'p_accept', 'p_reject', 'p_ignore', all mapped to float values.
    # Example: {'p_accept': 0.7, 'p_reject': 0.2, 'p_ignore': 0.1}. These are the values substituted into p_a, p_r and p_i.
    """

    #number of parents per depth level
    N_d = parent_array(height, branching_factor)
    total_probability = 1

    #we start from lowest depth level in the tree
    for d in range(height-1, -1, -1):
            n = branching_factor[d]
            k = int(np.ceil(branching_factor[d] * threshold))
            #print(d, n, N_d[d])

            #NOTE here p_a, p_r, p_i are symbolic sympy variables
            g = generating_function(x, p_a, p_r, p_i, symbolic_n)
            expanded_g = sub_neighbours_into_g(g, symbolic_n, n)
            coeffs_dict = coefficients_g(expanded_g, x)


            #we compute the probability of a single parent remaining in the tree at that depth level
            #NOTE here prob_accept, prob_reject, prob_ignore are literal float values
            p_parent_success = prob_success_single_parent_at_depth_d(coeffs_dict, n, k, p_a, p_r, p_i, x, **probabilities_response_kwargs)

            #probability of enough parents at depth level d succeeding (i.e: remaining in the tree)
            p_A_d = probability_of_success_at_depth_d(p_parent_success, N_d[d], threshold)
            #print(p_A_d)

            #we take the product of this across all depth levels to compute the total probability of enough parents remaining in the whole tree.
            total_probability *= p_A_d
    return total_probability