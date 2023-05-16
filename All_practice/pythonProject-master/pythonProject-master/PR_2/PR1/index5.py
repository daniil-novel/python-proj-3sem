from functools import cache


def ham_dist(x, y):
    dist = 0
    while x > 0 or y > 0:
        if x % 2 != y % 2:
            dist += 1
        x //= 2
        y //= 2
    return dist

def ham_dist_str(x, y):
    return sum([1 for i in range(32) if (x >> i) & 1 != (y >> i) & 1])

def split_bits(val):
    return [(0b111 if (val >> i) & 1 else 0b000) for i in range(7, -1, -1)]

@cache
def lev_dist(s1, s2):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    if s1[0] == s2[0]:
        return lev_dist(s1[1:], s2[1:])
    else:
        add = lev_dist(s1, s2[1:])
        delete = lev_dist(s1[1:], s2)
        replace = lev_dist(s1[1:], s2[1:])
        return 1 + min(add, delete, replace)


def lev_dist_ops(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    ops = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j
                ops[i][j] = 'вставка'
            elif j == 0:
                dp[i][j] = i
                ops[i][j] = 'удаление'
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                ops[i][j] = 'совпадение'
            else:
                insert = dp[i][j - 1]
                delete = dp[i - 1][j]
                replace = dp[i - 1][j - 1]
                min_ops = min(insert, delete, replace)
                dp[i][j] = min_ops + 1
                if min_ops == insert:
                    ops[i][j] = 'вставка'
                elif min_ops == delete:
                    ops[i][j] = 'удаление'
                else:
                    ops[i][j] = 'замена'
    i, j = n, m
    result = []
    while i > 0 or j > 0:
        op = ops[i][j]
        result.append(op)
        if op == 'совпадение':
            i, j = i - 1, j - 1
        elif op == 'вставка':
            j -= 1
        elif op == 'удаление':
            i -= 1
        else:
            i, j = i - 1, j - 1
    return result[::-1]

if __name__ == "__main__":
    print(ham_dist(0b1011,0b0111))
    print(ham_dist_str(0b1100,0b0011))

    print(lev_dist('столб', 'слон'))
    print(lev_dist('кот', 'скот'))
    print(lev_dist('дом', 'кот'))

    print(lev_dist_ops('столб', 'слон'))
    print(lev_dist_ops('кот', 'скот'))
    print(lev_dist_ops('дом', 'кот'))