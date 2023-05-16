import math


def main(n):
    if n == 0:
        return 0.35
    elif n == 1:
        return 0.01
    else:
        return 71 * (1 + main(n - 2) / 97) ** 3 + \
            math.log2(main(n - 1)) / 26 + 1

    print((main(4)))
