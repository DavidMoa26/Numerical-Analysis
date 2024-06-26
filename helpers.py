def PrintMatrix(matrix):
    for line in matrix:
        print('  '.join(map(str, line)))


def MaxNorm(matrix):
    max_norm = 0
    for i in range(len(matrix)):
        norm = 0
        for j in range(len(matrix)):
            # Sum of organs per line with absolute value
            norm += abs(matrix[i][j])
        # Maximum row amount
        if norm > max_norm:
            max_norm = norm

    return max_norm


def Determinant(matrix, mul):
    width = len(matrix)
    # Stop Conditions
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        det = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            # Change the sign of the multiply number
            sign *= -1
            #  Recursive call for determinant calculation
            det = det + mul * Determinant(m, sign * matrix[0][i])
    return det


def MakeIMatrix(cols, rows):
    # Initialize a identity matrix
    return [[1 if x == y else 0 for y in range(cols)] for x in range(rows)]


def MultiplyMatrix(matrixA, matrixB):
    # result matrix initialized as singularity matrix
    result = [[0 for y in range(len(matrixB[0]))] for x in range(len(matrixA))]
    for i in range(len(matrixA)):
        # iterate through columns of Y
        for j in range(len(matrixB[0])):
            # iterate through rows of Y
            for k in range(len(matrixB)):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result


def InverseMatrix(matrix, vector):
    # Unveri reversible matrix
    if Determinant(matrix, 1) == 0:
        print("Error,Singular Matrix\n")
        return
    # result matrix initialized as singularity matrix
    result = MakeIMatrix(len(matrix), len(matrix))
    # loop for each row
    for i in range(len(matrix[0])):
        # turn the pivot into 1 (make elementary matrix and multiply with the result matrix )
        # pivoting process
        matrix, vector = RowXchange(matrix, vector)
        elementary = MakeIMatrix(len(matrix[0]), len(matrix))
        elementary[i][i] = 1 / matrix[i][i]
        result = MultiplyMatrix(elementary, result)
        matrix = MultiplyMatrix(elementary, matrix)
        # make elementary loop to iterate for each row and subtracrt the number below (specific) pivot to zero  (make
        # elementary matrix and multiply with the result matrix )
        for j in range(i + 1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            elementary[j][i] = -(matrix[j][i])
            matrix = MultiplyMatrix(elementary, matrix)
            result = MultiplyMatrix(elementary, result)

    # after finishing with the lower part of the matrix subtract the numbers above the pivot with elementary for loop
    # (make elementary matrix and multiply with the result matrix )
    for i in range(len(matrix[0]) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            elementary[j][i] = -(matrix[j][i])
            matrix = MultiplyMatrix(elementary, matrix)
            result = MultiplyMatrix(elementary, result)

    return result


def InverseMatrix(matrix):
    vector=[0]*len(matrix)
    # Unveri reversible matrix
    if Determinant(matrix, 1) == 0:
        print("Error,Singular Matrix\n")
        return
    # result matrix initialized as singularity matrix
    result = MakeIMatrix(len(matrix), len(matrix))
    # loop for each row
    for i in range(len(matrix[0])):
        # turn the pivot into 1 (make elementary matrix and multiply with the result matrix )
        # pivoting process
        matrix, vector = RowXchange(matrix, vector)
        elementary = MakeIMatrix(len(matrix[0]), len(matrix))
        elementary[i][i] = 1 / matrix[i][i]
        result = MultiplyMatrix(elementary, result)
        matrix = MultiplyMatrix(elementary, matrix)
        # make elementary loop to iterate for each row and subtracrt the number below (specific) pivot to zero  (make
        # elementary matrix and multiply with the result matrix )
        for j in range(i + 1, len(matrix)):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            elementary[j][i] = -(matrix[j][i])
            matrix = MultiplyMatrix(elementary, matrix)
            result = MultiplyMatrix(elementary, result)

    # after finishing with the lower part of the matrix subtract the numbers above the pivot with elementary for loop
    # (make elementary matrix and multiply with the result matrix )
    for i in range(len(matrix[0]) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            elementary = MakeIMatrix(len(matrix[0]), len(matrix))
            elementary[j][i] = -(matrix[j][i])
            matrix = MultiplyMatrix(elementary, matrix)
            result = MultiplyMatrix(elementary, result)

    return matrix


def RowXchange(matrix, vector):
    for i in range(len(matrix)):
        max = abs(matrix[i][i])
        for j in range(i, len(matrix)):
            # The pivot member is the maximum in each column
            if abs(matrix[j][i]) > max:
                temp = matrix[j]
                temp_b = vector[j]
                matrix[j] = matrix[i]
                vector[j] = vector[i]
                matrix[i] = temp
                vector[i] = temp_b
                max = abs(matrix[i][i])

    return [matrix, vector]


def CheckDominantDiagonal(matrix):
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            if i != j:
                # Sum of line member without pivot
                sum += abs(matrix[i][j])
        # If the pivot is less than the sum of the rest of the line
        if abs(matrix[i][i]) < sum:
            return False
    return True


def dominant_diagonal_fix(matrix):
    #Check if we have a dominant for each column
    dom = [0]*len(matrix)
    result = list()
   # Find the largest organ in a row
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] > sum(map(abs,map(int,matrix[i])))-matrix[i][j]) :
                dom[i]=j
    for i in range(len(matrix)):
        result.append([])
        # Cannot dominant diagonal
        if i not in dom:
            print("Couldn't find dominant diagonal.")
            return matrix
    # Change the matrix to a dominant diagonal
    for i,j in enumerate(dom):
        result[j]=(matrix[i])
    return result


def minusMatrix(matrix):
    return [[-i for i in j] for j in matrix]


def matrixAddition(matrixA, matrixB):
    return [[a + b for (a, b) in zip(i, j)] for (i, j) in zip(matrixA, matrixB)]


def matrixDLUdissasembly(matrix):
    D, L, U = list(), list(), list()
    for x, row in enumerate(matrix):
        D.append(list()), L.append(list()), U.append(list())
        for y, value in enumerate(row):
            # Diagonal with zeros
            if x == y:
                D[x].append(value), L[x].append(0), U[x].append(0)
            # Zeros below diagonal
            elif x < y:
                D[x].append(0), L[x].append(0), U[x].append(value)
            # Zeros above diagonal
            elif x > y:
                D[x].append(0), L[x].append(value), U[x].append(0)
    return D, L, U


def JacobiG(matrix):
    """
    :param matrix: Matrix nxn
    :return: G matrix
    """
    D, L, U = matrixDLUdissasembly(matrix)
    return MultiplyMatrix(minusMatrix(InverseMatrix(D)), InverseMatrix(matrixAddition(L, U)))


def JacobiH(matrix):
    """
        :param matrix: Matrix nxn
        :return: H matrix
        """
    D, L, U = matrixDLUdissasembly(matrix)
    return InverseMatrix(D)


def GaussSeidelG(matrix):
    """
            :param matrix: Matrix nxn
            :return: G matrix
            """
    D, L, U = matrixDLUdissasembly(matrix)
    return MultiplyMatrix(minusMatrix(InverseMatrix(matrixAddition(L, D))), U)


def GaussSeidelH(matrix):
    """
            :param matrix: Matrix nxn
            :return: H matrix
            """
    D, L, U = matrixDLUdissasembly(matrix)
    return InverseMatrix(matrixAddition(L, D))



def CheckJacobiGnorm(matrix):
    return 1 > MaxNorm(JacobiG(matrix))



def CheckGaussSeidelGnorm(matrix):
    return 1 > MaxNorm(GaussSeidelG(matrix))


def InitVector(size):
    return [0 for index in range(size)]


def CopyVector(vector):
    copy = []
    for i in range(len(vector)):
        copy.append(vector[i])

    return copy


def JacobiMethod(matrix, vector, epsilon, previous, counter):

    NextGuess = []
    for i in range(len(matrix)):
        ins = 0
        for j in range(len(matrix)):
            if i != j:
                # Insulating variables
                ins = ins + matrix[i][j]*previous[j]
        # Calculate the next iteration
        newGuess = 1/matrix[i][i]*(vector[i]-ins)
        # Result vector insertion
        NextGuess.append(newGuess)

    # Result vector insertion
    print("Iteration no. "+str(counter)+" " +str(NextGuess))

    # Check stop conditions
    for i in range(len(matrix)):
        if abs(NextGuess[i] - previous[i]) < epsilon:
            return

    # Recursive call
    JacobiMethod(matrix, vector, epsilon,NextGuess,counter+1)


def GaussSeidelMethod(matrix, vector, epsilon, previous, counter):
    """
     Function for solving a set of equations according to the GaussSeidel method
     :param matrix: Matrix nxn
     :param vector: Vector n
     :param epsilon: Stop Conditions
     :param previous: Result vector
     :param counter: Number of iterations
     """

    NextGuess = []
    ImprovedGuess = CopyVector(previous)
    for i in range(len(matrix)):
        ins = 0
        for j in range(len(matrix)):
            if i != j:
                # Insulating variables
                ins = ins + matrix[i][j]*ImprovedGuess[j]
        newGuess = 1/matrix[i][i]*(vector[i]-ins)
        # Using calculated results
        ImprovedGuess[i] = newGuess
        NextGuess.append(newGuess)

    # Result vector insertion
    print("Iteration no. "+str(counter)+" " +str(NextGuess))

    # Check stop conditions
    for i in range(len(matrix)):
        if abs(NextGuess[i] - previous[i]) < epsilon:
            return

    # Recursive call
    GaussSeidelMethod(matrix, vector, epsilon,NextGuess,counter+1)
