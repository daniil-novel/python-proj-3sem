import math


def main(z,x,y):
    result = 0
    n = len(z)
    for i in range(1,n+1):
        result += 47 * (13 * x[math.floor((i - 1) / 3)] ** 2 + y[i - 1] + 70 * z[n + 1 - i - 1] ** 3) ** 4
    return 98 * result

if __name__ == "__main__":
    print(main([-0.15, 0.71, 0.23, -0.41, -0.34], [-0.12, -0.37, 0.16, -0.02, -0.49], [0.75, 0.88, -0.29, 0.6, 0.72]))

