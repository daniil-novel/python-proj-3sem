import module1

def func2():
    print("This is module2, calling func1 from module1")
    module1.func1()

if __name__ == '__main__':
    func2()
