from z3 import *

def find_valid_combination(rho, h_max=3, value_min=4, value_max=6, n_bound=5):
    for h in range(1, h_max + 1):
        #we create a Solver instance
        s = Solver()
        # Create integer variables n1, n2, ..., nh, that are called n_{i+1} (i.e: branching factor)
        n = [Int(f"n{i+1}") for i in range(h)]
        print(n)

        # bound the search space, n_i's need to have a maximum value limit,
        # and be positive integers.
        for ni in n:
            s.add(ni > 0, ni <= n_bound)

        # Build the expression v = sum of product terms with rho powers
        # v = n1 * rho + (n1 * n2 * rho^2) + ... + ((\prod_{i = 1}^{d} n_i) * rho^h)
        v = RealVal(0)
        product = RealVal(1)
        for d in range(1, h + 1):
            #d-1 index because python is 0-indexed, so n_1 is n[0].
            product *= n[d - 1]
            term = product * (rho ** d)
            v += term

        s.add(v >= value_min, v <= value_max)

        if s.check() == sat:
            model = s.model()
            #.as_long() converts the Z3 integer to a python int
            #values are the valid n_i's that satisfy the constraints.
            values = [model.evaluate(ni).as_long() for ni in n]
            #
            final_v = sum(
                #values[:d] are the n_i's from 1 to d, and we need to multiply them
                #by rho^d.
                #list comprehension creates list of the following terms:
                #[n_1 * rho,  (n_1 * n_2 * rho^2),  ... , ((\prod_{i = 1}^{d} n_i) * rho^h)]
                eval_product(values[:d]) * (rho ** d) for d in range(1, h + 1)
            )
            #the sum of the elements of the list is:
            #v = n1 * rho + (n1 * n2 * rho^2) + ... + ((\prod_{i = 1}^{d} n_i) * rho^h)
            return {
                "h": h,
                "n_values": values,
                "v": round(final_v, 5)
            }

    return None

def eval_product(lst):
    result = 1
    for x in lst:
        result *= x
    return result

# example: use p_a = 0.7, p_r = 0.4 => rho = 0.3
rho = 0.3
result = find_valid_combination(rho)

if result:
    print(f"Found valid solution:")
    print(f"Height h = {result['h']}")
    print(f"n values = {result['n_values']}")
    print(f"v ≈ {result['v']}")
else:
    print("No solution found up to max height.")
