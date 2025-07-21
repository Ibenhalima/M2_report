from scipy.stats import poisson
from scipy.optimize import root_scalar

p_list = [1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
epsilon = 0.05

def solve_for_n(p, k, epsilon):
    def f(lambd):
        return  epsilon - poisson.cdf(k - 1, lambd)
    
    sol = root_scalar(f, bracket=[0, 1e5], method="bisect")
    if sol.converged:
        n = sol.root / p
        return n
    else:
        return None

print("Résultats pour k=10 et k=100 avec epsilon=0.05 :\n")

for k in [10, 100]:
    print(f"Pour k = {k} :")
    for p in p_list:
        n = solve_for_n(p, k, epsilon)
        if n is not None:
            print(f"  p = {p:.0e}  =>  n = {n:.3e}")
        else:
            print(f"  p = {p:.0e}  =>  pas de converge :sadfaceemoji:")
    print()
