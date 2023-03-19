print("Example module loaded")


def print_message():
    print("Hello, world!")


"""
В Python модуль загружается только один раз, и последующие импорты того же модуля будут использовать уже загруженный объект модуля из кеша. Это поведение предназначено для повышения производительности и предотвращения избыточной работы.

Example module loaded
Calling print_message() for the first time
Hello, world!
Calling print_message() for the second time
Hello, world!

Как мы видим, сообщение «Пример модуля загружен» печатается только один раз, когда модуль впервые импортируется. Функция print_message()вызывается дважды, но модуль не перезагружается, и сообщение не печатается повторно. Это подтверждает, что модули загружаются в Python только один раз.
"""
