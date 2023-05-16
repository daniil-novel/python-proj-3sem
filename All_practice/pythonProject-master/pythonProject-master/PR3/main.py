import math
import random
def function1(x):
    x = x + x
    x = x + x
    result = x + x
    result = result + x
    return result

def function2(x):
    for i in range(0,4,1):
        x = x + x
    return x

def function3(x):
    y = x + x
    y = y + y
    y = y + y
    z = x - y
    z = y - z
    return z

def naive_mul(x, y):
    r = x
    for i in range(0, y - 1):
        r = x + r
    return r

def fast_mul(x, y):
    if x == 0 or y == 0:
        return 0
    x_str = bin(x)[2:]
    y_str = bin(y)[2:]
    x_str = x_str[::-1]
    y_str = y_str[::-1]
    result = 0
    for i, y_bit in enumerate(y_str):
        if y_bit == '1':
            shifted_x = x << i
            result += shifted_x
    return result

def fast_pow(x, y):
    if y == 0:
        return 1
    if x == 0:
        return 0
    y_str = bin(y)[2:]
    y_str = y_str[::-1]
    result = 1
    factor = x
    for i, y_bit in enumerate(y_str):
        if y_bit == '1':
            result *= factor
        factor *= factor
    return result


def mul16(x,y):
    x1 = x & 65280
    y1 = y & 65280
    x2 = x & 255
    y2 = y & 255
    result1 = x1 * y1
    result2 = x2 * y2
    result3 = x1 * x2
    result4 = y1 * y2
    return result1 + result2 + result3 + result4

def fn(x,n):
    c, f = divmod(x, n)
    return (c, f)

def mul16k(x,y, n = 4):
    x = fn(x, n)
    y = fn(y, n)
    if n == 2:
        b = x[0] * y[0]
        c = x[1] * y[1]
        d1 = x[0] + x[1]
        d2 = y[0] + y[1]
        e = d1 * d2
    else:
        b = mul16k(x[0], y[0], round(n / 2))
        c = mul16k(x[1], y[1], round(n / 2))
        d1 = x[0] + x[1]
        d2 = y[0] + y[1]
        e = mul16k(d1, d2, round(n / 2))
    f = e - c - b
    g = (b << n) + (f << round(n / 2)) + c
    return g

def fast_mul_gen(y):
  print("def f(x):")
  if y % 2 == 0:
    if y == 0:
      print(" return 0")
    i = 2
    while i//2 <= y:
      if i == 2:
        print(f"  x{i} = x + x")
      elif i > y:
        if (i//2 + (i-y)) == y:
          print(f"  x{i-(i-y)} = x{i//2} + x{i-y}")
        elif (i//2) != y:
          print(f"  x{i-(i-y)} = x{i//2} + x{i//2} - x{i-y}")
      else:
        print(f"  x{i} = x{i//2} + x{i//2}")
      i *= 2
    print(f"  return x{y}")
  else:
    if y == 1:
      print(" return x")
    else:
      i = 2
      while i//2 <= y:
        if i == 2:
          print(f"  x{i} = x + x")
        elif i > y:
          if (i - 1) == y:
            string = f"  x{i-(i-y)} = x{i//2} + x{i//2} - x"
          else:
            if (i - i//4) < y:
              delim = i//8
            else:
              delim = i//4
            string = f"  x{i-(i-y)} = x{i//2} + x{i//2} - x{delim}"
            neg = i - delim
            while neg > y:
              if (neg - 1) == y:
                string += " - x"
              else:
                string += f" - x{delim//2}"
              neg -= delim//2
              delim //= 2
          print(string)
        else:
          print(f"  x{i} = x{i//2} + x{i//2}")
        i *= 2
      print(f"  return x{y}")

def fast_pow_gen(y):
  print("def f(x):")
  if y % 2 == 0:
    if y == 0:
      print(" return 1")
    else:
      i = 2
      while i//2 <= y:
        if i == 2:
          print(f"  x{i} = x * x")
        elif i > y:
          if (i//2 + (i-y)) == y:
            print(f"  x{i-(i-y)} = x{i//2} * x{i-y}")
          elif (i//2) != y:
            print(f"  x{i-(i-y)} = x{i//2} * x{i//2} / x{i-y}")
        else:
          print(f"  x{i} = x{i//2} * x{i//2}")
        i *= 2
      print(f"  return x{y}")
  else:
    if y == 1:
      print(" return x")
    else:
      i = 2
      while i//2 <= y:
        if i == 2:
          print(f"  x{i} = x * x")
        elif i > y:
          if (i - 1) == y:
            string = f"  x{i-(i-y)} = x{i//2} * x{i//2} / x"
          else:
            if (i - i//4) < y:
              delim = i//8
            else:
              delim = i//4
            string = f"  x{i-(i-y)} = x{i//2} * x{i//2} / x{delim}"
            neg = i - delim
            while neg > y:
              if (neg - 1) == y:
                string += " / x"
              else:
                string += f" / x{delim//2}"
              neg -= delim//2
              delim //= 2
          print(string)
        else:
          print(f"  x{i} = x{i//2} * x{i//2}")
        i *= 2
      print(f"  return x{y}")

if __name__ == "__main__":
    """print(function1(int(input())))
    print(function2(int(input())))
    print(function3(int(input())))
    for i in range(100):
        x = random.randint(0,101)
        y = random.randint(0,101)
        assert naive_mul(x, y) == (x * y)
        assert fast_mul(x, y) == (x * y)
    print("true naive_mul and fast_mul")
    print(fast_pow(2, 5))
    print(mul16(256,257))
    print(mul16k(256,257))"""
    fast_mul_gen(3)
    fast_pow_gen(3)
