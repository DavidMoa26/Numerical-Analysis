import numpy as np


def linear_interpolation(points, x):
    points.sort(key=lambda point: point[0]) 
    for i in range(len(points) - 1):
        if points[i][0] <= x <= points[i + 1][0]:
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return None

def polynomial_interpolation(points, x):
    x_vals, y_vals = zip(*points)
    coefficients = np.polyfit(x_vals, y_vals, len(points) - 1)
    poly = np.poly1d(coefficients)
    return poly(x)

def lagrange_interpolation(points, x):
    total = 0
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        pi = yi
        for j in range(n):
            if i != j:
                xj, _ = points[j]
                pi *= (x - xj) / (xi - xj)
        total += pi
    return total

if __name__ == "__main__":
    x_data = np.array([0.2, 0.35, 0.45, 0.6, 0.75])
    y_data = np.array([3.7241, 3.9776, 4.0625, 2.9776, 3.7241]) 
    points = [(0.2,3.7241) , (0.35,3.9776) , (0.45,4.0625),(0.6,2.9776),(0.75,3.7241)]
    x_value = 0.65
    # method = input("Choose the interpolation method : \n1.linear\n2.polynomial\n3.lagrange\n").lower()
    
    # if method == "1":
    #     y_value = linear_interpolation(points, x_value)
    # elif method == "2":
    #     y_value = polynomial_interpolation(points, x_value)
    # elif method == "3":
    #     y_value = lagrange_interpolation(points, x_value)
    # else:
    #     print("Invalid method chosen.")
    #     y_value = None

    # if y_value is not None:
    #     print(f"The approximated y value for x = {x_value} is: {y_value}")
    # else:
    #     print("Could not find an approximated y value.")

    res = polynomial_interpolation(points, x_value)
    print(res)
    