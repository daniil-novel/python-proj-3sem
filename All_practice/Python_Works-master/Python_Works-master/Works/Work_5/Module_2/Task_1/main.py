def get_odd_squares(numbers):
    result = []
    for num in numbers:
        if num % 2 != 0:
            result.append(num ** 2)
    return result
