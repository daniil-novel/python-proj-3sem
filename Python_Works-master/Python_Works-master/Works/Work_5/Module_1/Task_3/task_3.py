class raises:
    """
    Менеджер контекста, который проверяет, что ошибка определенного типа была выброшена в блоке with.
    Если ошибка не выбрасывается, то возбуждается AssertionError.
    """
    def __init__(self, expected_exception):
        self.expected_exception = expected_exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            raise AssertionError(f"{self.expected_exception.__name__} was not raised.")
        if not issubclass(exc_type, self.expected_exception):
            return False
        return True

with raises(ValueError) as e:
    raise ValueError("Test error")

"""
Если в блоке with не будет выброшено исключение ValueError, то будет возбуждена ошибка AssertionError. Если будет выброшена иная ошибка, то она будет передана дальше вверх по стеку. Если будет выброшено исключение ValueError, то блок with успешно завершится. Объект e будет содержать выброшенное исключение.
"""
