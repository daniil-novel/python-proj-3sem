import math


def main(x, z):
    return (math.log2(z**3 + 1) ** 3 - (math.asin(1 + x + x ** 2) ** 5) / (49 * (z ** 3) - 63 * (x ** 5)) - (z ** 6 - (x + 60 * (x ** 3) + 20 * (z ** 2)) ** 5) / (x ** 5 + x ** 7)


print(main(-0.24, -0.45))
'''
print(main(-0.7, 0.17), "/n")
print(main(-0.2, 0.42), "/n")
print(main(-0.19, -0.11), "/n")
print(main(-0.76, 0.83), "/n")
'''