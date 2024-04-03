import numpy as np

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    I = h * (0.5*y[0] + 0.5*y[-1] + sum(y[1:-1]))
    return I

def calculate_error(a, b, n):
    E = -((b-a)**3) / (12*n**2) * 1 
    return E



if __name__ == "__main__":
    f = np.sin
    a = 0
    b = np.pi
    n = 4

    I_approx = trapezoidal_rule(f, a, b, n)
    E_approx = calculate_error(a, b, n)

    print(f"The approximated integral value is: {I_approx}")
    print(f"The theoretical error estimate is: {E_approx}")
