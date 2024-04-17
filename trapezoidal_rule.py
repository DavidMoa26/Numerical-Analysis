import numpy as np
import math

# Define the lambda function for sin using numpy
f = lambda x: np.sin(x)

# Trapezoidal Rule function
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    I = (h/2) * (y[0] + 2 * sum(y[1:n]) + y[n])
    return I

# Calculate the theoretical error (assuming exact error formula for sin(x) integral)
def calculate_error(a, b, n):
    # The maximum value of the second derivative of sin(x) over [0, pi] is 1
    h = (b - a) / n
    return (b - a) * (h**2) / 12



f = lambda x : np.sin(x)
a = 0
b = np.pi
n = 4

I_approx = trapezoidal_rule(f, a, b, n)
E_approx = calculate_error(a, b, n)

print(f"The approximated integral value is: {I_approx}")
print(f"The theoretical error estimate is: {E_approx}")

