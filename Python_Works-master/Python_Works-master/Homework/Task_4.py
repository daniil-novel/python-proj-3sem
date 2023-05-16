import math


def main(n):
    if n == 0:
        return 0.83
    elif n == 1:
        return -0.83
    elif n >= 2:
        return (math.atan(main(n - 1)) / 92) + 4 * main(n - 2) ** 2


print(main(4))
