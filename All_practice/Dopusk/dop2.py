import math

import math


def main(z):
    if z < 65:
        return z ** 6 - z ** 4 / 9 - (9 * z ** 2 - 76 * z)
    elif 65 <= z < 136:
        return (18 * z) ** 6 - 81 * math.atan(z) ** 7
    elif z >= 136:
        return 99 * z ** 5 - 1 - 13 * (math.sqrt(z ** 3 / 50 - 68 * z - 56) ** 3)


print('{:.2e}'.format(main(156)))

print('{:.2e}'.format(main(73)))

print('{:.2e}'.format(main(150)))

print('{:.2e}'.format(main(55)))

