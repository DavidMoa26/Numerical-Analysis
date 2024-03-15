import numpy as np
from colors import bcolors
from jacobi import jacobi_iterative
from gauss_seidel import gauss_seidel
from is_diagonally_dominant import is_diagonally_dominant

if __name__ == '__main__':
    A = np.array([
        [3, -1, 1],
        [0, 1, -1], 
        [1, 1, -2]
        ])
    b = np.array([4, -1, -3])
    x = np.zeros_like(b, dtype=np.double)

    
    try:
        if not is_diagonally_dominant(A):
            print("The matrix does not have diagonally dominant")
        else:
            print("======== Jacobi Method ===========")
            solution = jacobi_iterative(A,b,x)
            print(bcolors.OKBLUE,"\nApproximate solution:", solution)

            print("======== Gauss seidel Method ===========")
            solution = gauss_seidel(A, b, x)
            print(bcolors.OKBLUE,"\nApproximate solution:", solution)
            

    except ValueError as e:
        print(str(e))


