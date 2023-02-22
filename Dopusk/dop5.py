import math


def main(x, z):
    if len(z) == 1:
        return math.acos(z[0] ** 3 - z[0] - 84 * x[0] ** 2) ** 2
    else:
        return math.acos(z[0] ** 3 - z[0] - 84 * x[len(x) - 1 -
                         math.ceil(len(z) / 2)] ** 2) ** 2 + main(x[:-1], z[1:])
