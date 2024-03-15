import numpy as np

def gauss(A_b):
    n = len(A_b)
    elementary_matrices = []
    matrix_states = []
    
    print("Starting Augmented Matrix [A|b]:")
    print(A_b)
    print()  # Print a blank line for readability

    for i in range(n):
        # Pivot selection by finding the maximum in the current column
        pivot_row = np.argmax(np.abs(A_b[i:, i])) + i
        if A_b[pivot_row, i] == 0:
            raise ValueError("Matrix is singular; cannot proceed.")

        # Swap if necessary
        if pivot_row != i:
            E_swap = np.identity(n)
            E_swap[[i, pivot_row]] = E_swap[[pivot_row, i]]
            A_b[[i, pivot_row]] = A_b[[pivot_row, i]]
            # print(f"Elementary Matrix for Swapping rows {i} and {pivot_row}:")
            elementary_matrices.append(E_swap)
            # print(E_swap)
            # print("Matrix after swapping:")
            matrix_states.append(A_b.copy())
            # print(A_b)

        # Scale the pivot row to make the pivot 1
        pivot = A_b[i, i]
        if pivot != 1:
            E_scale = np.identity(n)
            E_scale[i, i] = 1 / pivot
            A_b[i] = A_b[i] / pivot
            # print(f"Elementary Matrix for Scaling row {i}:")
            elementary_matrices.append(E_scale)
            # print(E_scale)
            # print("Matrix after scaling:")
            matrix_states.append(A_b.copy())
            # print(A_b)

        # Eliminate elements below the pivot
        for j in range(i + 1, n):
            if A_b[j, i] != 0:
                factor = -A_b[j, i] / A_b[i, i]
                E_eliminate = np.identity(n)
                E_eliminate[j, i] = factor
                A_b[j] += factor * A_b[i]
                # print(f"Elementary Matrix for Eliminating element at row {j}, column {i}:")
                elementary_matrices.append(E_eliminate)
                # print(E_eliminate)
                # print("Matrix after elimination:")
                matrix_states.append(A_b.copy())
                # print(A_b)

    # Backward Substitution
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = -A_b[j, i] / A_b[i, i]
            E_eliminate = np.identity(n)
            E_eliminate[j, i] = factor
            A_b[j] += factor * A_b[i]
            # print(f"Elementary Matrix: ")
            elementary_matrices.append(E_eliminate)
            # print(E_eliminate)
            # print("Matrix after backward elimination:")
            matrix_states.append(A_b.copy())
            # print(A_b)
    
    x = A_b[:, -1]
    return x, elementary_matrices, matrix_states

if __name__ == '__main__':
    print("X")
