import math


def main(x, z):
    if len(z) == 1:
        return math.acos(z[0] ** 3 - z[0] - 84 * x[0] ** 2) ** 2
    else:
        index = len(x) - 1 - math.ceil(len(z) / 2)
        if index < 0:
            return 0
        else:
            return (math.acos(z[0] ** 3 - z[0] - 84 * x[index] ** 2) ** 2 +
                    main(x[:-1], z[1:]))


args = ([0.98, -0.04], [-0.76, 0.26])
result = main(*args)
print(result)
