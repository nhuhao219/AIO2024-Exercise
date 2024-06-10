# factorial(n)
def factorial(n):
    if n == 0:
        factorial = 1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial * i
    return factorial

# sin(x)
def approx_sin(x, n):
    approx_sin = 0
    for i in range(n + 1):
        fac = factorial(2 * i + 1)
        approx_sin = approx_sin + (-1) ** i * x ** (2 * i + 1) / fac
    return approx_sin

# cos(x)
def approx_cos(x, n):
    approx_cos = 0
    for i in range(n + 1):
        fac = factorial(2 * i)
        approx_cos = approx_cos + (-1) ** i * x ** (2 * i) / fac
    return approx_cos

# sinh(x)
def approx_sinh(x, n):
    approx_sinh = 0
    for i in range(n + 1):
        fac = factorial(2 * i + 1)
        approx_sinh = approx_sinh + x ** (2 * i + 1) / fac
    return approx_sinh

# cosh(x)
def approx_cosh(x, n):
    approx_cosh = 0
    for i in range(n + 1):
        fac = factorial(2 * i)
        approx_cosh =  approx_cosh + x ** (2 * i) / fac
    return approx_cosh

if __name__ == "__main__":
    x = float(input("Nhap vao gia tri cua x: "))
    n = int(input("Nhap vao gia tri cua n: "))

    print("approx_sin(x={}, n={}) = {}".format(x, n, approx_sin(x, n)))
    print("approx_cos(x={}, n={}) = {}".format(x, n, approx_cos(x, n)))
    print("approx_sinh(x={}, n={}) = {}".format(x, n, approx_sinh(x, n)))
    print("approx_cosh(x={}, n={}) = {}".format(x, n, approx_cosh(x, n)))
