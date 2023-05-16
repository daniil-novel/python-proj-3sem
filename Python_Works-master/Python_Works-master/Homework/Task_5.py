import math


def main(z, x, y):
    n = len(x)
    i = 1
    sum1 = 0.0
    while i <= n:
        sum1 += abs((x[n - math.ceil(i / 2)] ** 2)
                    + y[i - 1]
                    + 84 * (z[n - math.ceil(i / 3)] ** 3)) ** 5
        i += 1
    return sum1


print(main([0.4, 0.75, -0.06, 0.04, 0.04, 0.05, -0.36], [-0.01, -0.98, -0.02, -0.69, 0.74, -0.36, 0.95], [-0.74, -0.15, -0.8, -0.45, -0.05, 0.03, -0.55]))
