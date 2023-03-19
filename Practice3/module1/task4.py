"""
Можем использовать конструкцию __all__ = ['func1', 'func2']
типо
def func1():
    pass

def func2():
    pass

class MyClass:
    pass

__all__ = ['func1', 'MyClass']

А в другом модуле уже подключить
from my_module import *
"""