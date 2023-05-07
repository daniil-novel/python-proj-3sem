import random
import string
import itertools


def f1(s):
    return list(map(int, s))

def f2(s):
    return len(set(s))

def f3(s):
    s = s[::-1]
    return s

def f4(s, x):
    indices = [i for i in range(len(s)) if s[i] == x]
    return indices

def f5(s):
    sum_even_indices = sum(s[::2])
    return sum_even_indices

def f6(s):
    longest_string = max(s, key=len)
    return longest_string

def f7(num):
    is_harshad = num % sum(map(int, str(num))) == 0
    return is_harshad

def f8(max_size):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=max_size))
    return random_string

def f9():
    rle_encode = lambda s: [(k, len(list(g))) for k, g in itertools.groupby(s)]
    return rle_encode


if __name__ == "__main__":
    x = 0