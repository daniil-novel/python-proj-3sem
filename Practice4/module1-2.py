class MyClass:
    def method1(self):
        print("Метод 1")

    def method2(self):
        print("Метод 2")

    def method3(self):
        print("Метод 3")

obj = MyClass()
method_name = "method2"
method = getattr(obj, method_name)
method()
"""
Метод 2
"""