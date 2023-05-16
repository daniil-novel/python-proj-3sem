import math

import pycodestyle

def f1():
    math.log2 (20)

def f2():
    1+2

def f3():
    a = 1,2,3

def f4():
    def fn(a = "a"):
        return a

def f5():
    def fn1():
        a = 5
    def fn2():
        b = 5

def f6():
    if 5 > 4: x = 5

def f7():
    a = 1 + 5; b = a - 1

def f8():
    var = True
    if var != True:
        False

def f9():
    var = True
    if var == True:
        True



if __name__ == "__main__":
    print("start")