def get_inheritance(cls):
    return f"{cls.__name__} -> {' -> '.join(c.__name__ for c in cls.__mro__[1:])} -> object"

print(get_inheritance(OSError))

"""
OSError -> Exception -> BaseException -> object -> object
"""