import numpy as np

def is_diagonally_dominant(mat):
    if mat is None:
        return False

    d = np.diag(np.abs(mat))
    s = np.sum(np.abs(mat), axis=1) - d 
    return np.all(d >= s)