
def task_1_1():
    #import antigravity
    import __hello__
    import braces
    import barry_as_FLUFL
    0 != 1

def task_1_2():
    int = 42
    string = 42
    float = 42.0
    char = "42"
    binary = 0b00101010
    hexadecimal = 0x2A
    octal = 0o52
    charA = '42'
    tuple = (42)
    lst = ["42"," "]

    print(int, string, float, char, binary, hexadecimal, octal, charA, tuple, lst[0])

def task_1_3():
    print(27 ** 560)
    print(27.0001 ** 215)

def task_1_4():
    a = "Hello"
    b = "World"
    return a, b

def task_1_5():
    """
    a = 10
    while a != 0:
        a -= 0.1
        # скрипт выходит за рамки
   # return a
   """

def task_1_6():
    z = 1
    z <<= 40
    #2 ** z
    return(z) # 2 ** 1099511627776

def task_1_7():
    """i = 0
    while i < 10:
        print(i)
        ++i =  +(+i)
    """
    print("Здесь не работает префиксный инкремент. Он равен i")

def task_1_8():
    print( (True * 2 + False) * -True)

#task_1_2()
#task_1_3()
task_1_1()
print(task_1_4())
#print(task_1_5())
print(task_1_6())
task_1_7()
task_1_8()
