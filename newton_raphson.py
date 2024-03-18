def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        if abs(fxn) < tol:
            return xn
        f_prime_xn = f_prime(xn)
        if f_prime_xn == 0:
            print("Zero derivative. No solution found.")
            return None
        xn = xn - fxn / f_prime_xn
    print("Exceeded maximum iterations. No solution found.")
    return None

