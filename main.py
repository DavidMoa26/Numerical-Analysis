# Group git : https://github.com/danielbogus99/Numaric
# Date: 19.02.2024
# Group: Eytan Stryzhack 336244959, Daniel Boguslavsky 207915729, Shifra Avigdor 207067125, David Moalem 203387337
# Git: https://github.com/DavidMoa26/Numerical-Analysis

# Name: David Moalem 203387337


import numpy as np
from colors import bcolors
from jacobi import jacobi_iterative
from gauss_seidel import gauss_seidel
from is_diagonally_dominant import is_diagonally_dominant
from gauss import gauss
from gaussian_elimination import gaussianElimination
from inverse_matrix import inverse
from cond import condition_number
from norm import norm

if __name__ == '__main__':
    A = np.array([
        [0.913, 0.659],
        [0.457, 0.330], 
        ])
    b = np.array([0.254, 0.127])
    mat = np.column_stack((A, b))

    
    try:
        # if not is_diagonally_dominant(A):
        #     print("The matrix does not have diagonally dominant")
        # else:
        #     print("======== Jacobi Method ===========")
        #     solution = jacobi_iterative(A,b,x)
        #     print(bcolors.OKBLUE,"\nApproximate solution:", solution)

        #     print("======== Gauss seidel Method ===========")
        #     solution = gauss_seidel(A, b, x)
        #     print(bcolors.OKBLUE,"\nApproximate solution:", solution)
        # res=gaussianElimination(mat)
        # print(res)
        # norm_A = norm(A)
        # cond = condition_number(A)
        # print("Condition number of A:", cond, "\n")
        res=gaussianElimination(mat)
        print(res)
            

    except ValueError as e:
        print(str(e))


