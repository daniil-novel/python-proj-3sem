import module2

def func1():
    print("This is module1, calling func2 from module2")
    module2.func2()

if __name__ == '__main__':
    func1()
