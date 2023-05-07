python
>>> import my_package
>>> my_package.module1.hello()
Hello from module1!
>>> my_package.module2.bye()
Bye from module2!
>>> import json
>>> with open('my_package/data.json') as f:
...     data = json.load(f)
...
>>> print(data)
{'name': 'John', 'age': 30, 'city': 'New York'}