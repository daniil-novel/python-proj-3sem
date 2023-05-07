class MyClass:
    def __init__(self):
        self.id = 666
        self.name = "Daniil"
        self.active = True

obj = MyClass()
for attr in dir(obj):
    if not attr.startswith("__"):
        print(attr)

    """
    active
    id
    name
    """