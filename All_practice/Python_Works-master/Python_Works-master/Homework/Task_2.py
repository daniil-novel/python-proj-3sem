import math


def main(z):
    if z < 0:
        return 16 * (math.ceil(26 * z + z ** 3) ** 5
                     - z ** 7 - 49 * math.sin(68 * z ** 3) * 4)
    elif 0 <= z < 29:
        return ((z ** 2 - 50 * z) ** 0.5) ** 3 - z ** 2
    elif 29 <= z < 118:
        return 23 * z + 1
    elif 118 <= z < 186:
        return (24 * z ** 2) ** 2 + 8 * z ** 3 + 96 * z ** 4
    else:
        return 1 - 46 * (abs(92 * z ** 2)) ** 4
