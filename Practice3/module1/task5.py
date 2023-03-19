def load_config(filename):
    with open(filename, 'r') as f:
        config = f.read()
    exec(config)

"""
Эта функция считывает содержимое указанного файла в строковую переменную 
config, а затем использует exec для выполнения содержимого файла как кода Python.
"""