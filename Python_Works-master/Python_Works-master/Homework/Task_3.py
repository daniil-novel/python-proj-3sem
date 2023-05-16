import math


def main(b, n, x, a, z):
    sum1 = 0.0
    sum2 = 0.0
    for i in range(1, n+1, 1):
        for k in range(1, b+1, 1):
            sum1 += 48 * (math.log2(i) ** 7) - math.log2(89 * x) - \
                    (math.cos(k ** 2) ** 6)
            print(sum1,i,k)
    for i in range(1, b+1, 1):
        for j in range(1, a+1, 1):
            for k in range(1, n+1, 1):
                sum2 += (abs(z) ** 2) + 31 * (j ** 3) - k - 56 * (i ** 2)
                print(sum2,i,j,k)
    return sum1 - sum2


print(main(4, 3, 0.35, 2, -0.81))
