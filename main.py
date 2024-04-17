# Personal git : https://github.com/DavidMoa26/Numerical-Analysis.git
# Group git : https://github.com/danielbogus99/Numaric.git
# Date: 08/04/2024
# Group : Eytan Stryzhack 336244959 , Daniel Boguslavsky 209412317, Shifra Avigdor 207067125, David Moalem 203387337
# Name : David Moalem 203387337

import numpy as np
import sympy as sp
from trapezoidal_rule import trapezoidal_rule, calculate_error
from Romberg_method import romberg_integration
from interpolation_methods import polynomial_interpolation
import math
from scipy.interpolate import CubicSpline




if __name__ == '__main__':
   # Data points
    points = [(0.2,3.7241) , (0.35,3.9776) , (0.45,4.0625),(0.6,2.9776),(0.75,3.7241)]

    res1 = round(polynomial_interpolation(points, 0.65) , 1)
    res2 = round(polynomial_interpolation(points, 0.4) ,1)

    print(f"polynomial_interpolation :  value at x=0.65 is {res1}")
    print(f"polynomial_interpolation : value at x=0.4 is {res2}")

    def f(x):
        return np.sin(x**3 + x**2 - 6) / (2 * np.exp(-2*x))
    
    integral = round(romberg_integration(f, res1, res2, 10) ,5)
    print(f"romberg_integration : value of integral is {integral}")



   



