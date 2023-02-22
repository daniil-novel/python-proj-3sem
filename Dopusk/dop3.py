import math


def main(n, a, b, m, z):
    result = 0
    for i in range(1, a + 1):
        for j in range(1, n + 1):
            result += 36 * (12 * j) ** 6 - i ** 2

    for j in range(1, n + 1):
        for c in range(1, m + 1):
            for k in range(1, b + 1):
                result += 89 * (j ** 2 - z ** 3) ** 5 + 65 * \
                    math.exp(68 * c - 80 * k ** 3 - 1)

    return result


print('{:.2e}'.format(main(6, 8, 5, 7, -0.91)))

print('{:.2e}'.format(main(5, 4, 6, 6, -1.0)))

print('{:.2e}'.format(main(5, 7, 3, 7, 0.12)))
