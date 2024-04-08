# Personal git : https://github.com/DavidMoa26/Numerical-Analysis.git
# Group git : https://github.com/danielbogus99/Numaric.git
# Date: 08/04/2024
# Group : Eytan Stryzhack 336244959 , Daniel Boguslavsky 209412317, Shifra Avigdor 207067125, David Moalem 203387337
# Name : David Moalem 203387337

import numpy as np
import sympy as sp
from cubic_spline import evaluate_natural_cubic_spline
from trapezoidal_rule import trapezoidal_rule, calculate_error
from Romberg_method import romberg_integration
from interpolation_methods import polynomial_interpolation
import math



if __name__ == '__main__':
   # Data points
    x_data = np.array([0.2, 0.35, 0.45, 0.6, 0.75])
    y_data = np.array([3.7241, 3.9776, 4.0625, 2.9776, 3.7241]) 

    # Points to evaluate the spline
    x_vals = [0.4, 0.65]
    res1,res2 = evaluate_natural_cubic_spline(x_data, y_data, x_vals)
    print(res1,res2)

    def f(x):
        return np.sin(x**3 + x**2 - 6) / (2 * np.exp(-2*x))
    
    integral = romberg_integration(f, res1, res2, 5)
    print(integral)



   



