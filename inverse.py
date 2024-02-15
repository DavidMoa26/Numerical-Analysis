from colors import bcolors
from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix,swap_row
import numpy as np

def swap_row_elementary_matrix(n, i, j):
    """Creates an elementary matrix for swapping rows i and j in an n x n matrix."""
    E = np.identity(n)
    E[[i, j], :] = E[[j, i], :]
    return E

def inverse(matrix):
    print(bcolors.OKBLUE + f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n {matrix}\n" + bcolors.ENDC)
    rows, cols = matrix.shape
    if(cols == rows):
        pass
    elif(cols == rows + 1):
        matrix = matrix[:, :-1]
    else:
        raise ValueError("Matrix must be square")
    
    n = matrix.shape[0]
    identity = np.identity(n)
    elementary_matrix_array = []
    matrix_after_elementary_array= []

    for i in range(n):
        # Find the row with the maximum absolute value in the current column from i down
        max_row_index = i + np.argmax(np.abs(matrix[i:, i]))
        
        # Swap if the max absolute value is not in the current pivot row
        if max_row_index != i:
            elementary_matrix = swap_row_elementary_matrix(n, i, max_row_index)
            matrix = np.dot(elementary_matrix, matrix)
            print(f"Elementary matrix to swap row {i} with row {max_row_index} (making pivot maximum):\n{elementary_matrix}\n")
            print(f"The matrix after elementary operation \n {matrix}")
            identity = np.dot(elementary_matrix, identity)
            elementary_matrix_array.append(elementary_matrix)
            matrix_after_elementary_array.append(matrix)
            
        
        # Scale the pivot row to make the diagonal element 1
        if matrix[i, i] != 1:
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            matrix = np.dot(elementary_matrix, matrix)
            print(f"Elementary matrix to make the diagonal element 1:\n{elementary_matrix}\n")
            print(f"The matrix after elementary operation \n {matrix}")
            identity = np.dot(elementary_matrix, identity)
            elementary_matrix_array.append(elementary_matrix)
            matrix_after_elementary_array.append(matrix)

        # Zero out the other elements in the column
        for j in range(n):
            if i != j:
                scalar = -matrix[j, i] / matrix[i, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                matrix = np.dot(elementary_matrix, matrix)
                print(f"Elementary matrix for R{j+1} = R{j+1} + ({scalar}R{i+1}):\n{elementary_matrix}\n")
                print(f"The matrix after elementary operation \n {matrix}")
                identity = np.dot(elementary_matrix, identity)
                elementary_matrix_array.append(elementary_matrix)
                matrix_after_elementary_array.append(matrix)

    return identity, elementary_matrix_array,matrix_after_elementary_array



if __name__ == '__main__':

    A = np.array([[1, 2, 3],
    [2, 3, 4],
    [3, 4, 6]])

    try:
        A_inverse,elementary_matrix_array,matrix_after_elementary_array = inverse(A)
        print(bcolors.OKBLUE, "\nInverse of matrix A: \n", A_inverse)
        print("=====================================================================================================================", bcolors.ENDC)
        # print(bcolors.OKBLUE, "Elementary matrix array: \n", np.array(elementary_matrix_array), bcolors.ENDC)
        # print(bcolors.OKBLUE, "Elementary matrix array: \n", np.array(matrix_after_elementary_array), bcolors.ENDC)

    except ValueError as e:
        print(str(e))


