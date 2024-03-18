# Group git : https://github.com/danielbogus99/Numaric
# Date: 19.02.2024
# Group: Eytan Stryzhack 336244959, Daniel Boguslavsky 207915729, Shifra Avigdor 207067125, David Moalem 203387337
# Git: https://github.com/DavidMoa26/Numerical-Analysis
# Name: David Moalem 203387337


import numpy as np
from LU_factorization import lu_solve
from newton_raphson import newton_raphson

if __name__ == '__main__':

    def f(x):
     numerator = 1.545455*x**2 - 8.636364*x + 7.454545
     denominator = 3.454545*x**2 - 4.272727
     return numerator / denominator

    
    def f_prime(x):
     numerator_prime = 1.63422369300636*x**2 - 3.54459038821842*x + 2.02127680986873
     denominator_prime = 0.653689363667008*x**4 - 1.6170211670439*x**2 + 1.0
     return numerator_prime / denominator_prime



    A = np.array([
    [-1, 1, 3, -3, 1],
    [3, -3, -4, 2, 3],
    [2, 1, -5, -3, 5],
    [-5, -6, 4, 1, 3],
    [3, -2, -2, -3, 5]
])
    b = np.array([1, 18,6,22,10])
    mat = np.column_stack((A, b))
    print("Question 1 : ")
    lu_solve(mat)
    x0 = 1
    print("\n\n Question 2 : ")
    root = newton_raphson(f, f_prime, x0)
    print(root)      


