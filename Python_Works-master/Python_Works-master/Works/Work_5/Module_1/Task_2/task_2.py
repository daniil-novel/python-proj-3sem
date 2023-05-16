import random


def bucketsort(arr, k):
    counts = [0] * k  # созданный массив будет меньше изначального на 1
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


def bucketsort_new(arr, k):
    # проверка на пустой массив
    if not arr:
        return []

    m = max(arr)
    if m != k:
        raise Exception("Максимальное значение в массиве не совпадает с поступившим значением. K != max(arr)")
    counts = [0] * (m + 1)
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(len(counts)):
        sorted_arr += [i] * counts[i]

    return sorted_arr


def test_bucketsort():
    # проверка сортировки для пустого массива
    arr = []
    k = 10
    res = bucketsort_new(arr, k)
    assert res == [], f'Ошибка: получено {res}, ожидалось []'

    # проверка сортировки для массива из одного элемента
    arr = [5]
    k = 5
    res = bucketsort_new(arr, k)
    assert res == [5], f'Ошибка: получено {res}, ожидалось [5]'

    # проверка сортировки для массива из нескольких элементов
    arr = [5, 2, 8, 3, 5, 1]
    k = 8
    res = bucketsort_new(arr, k)
    assert res == [1, 2, 3, 5, 5, 8], f'Ошибка: получено {res}, ожидалось [1, 2, 3, 5, 5, 8]'

    # проверка сортировки для массива, состоящего из одного и того же элемента
    arr = [2] * 10
    k = 2
    res = bucketsort_new(arr, k)
    assert res == [2] * 10, f'Ошибка: получено {res}, ожидалось {arr}'


def test_bucketsort_random():
    # генерируем случайный массив и значения для k
    arr = [random.randint(0, 99) for _ in range(random.randint(1, 100))]
    k = max(arr)

    # сортируем массив с помощью встроенной функции sorted()
    expected = sorted(arr)

    # сортируем массив с помощью нашей функции bucketsort()
    result = bucketsort_new(arr, k)

    # сравниваем отсортированные массивы
    assert result == expected, f'Ошибка: получено {result}, ожидалось {expected}'


# print(bucketsort([1, 0, 2], 2))
print(bucketsort_new([1, 0, 2], 2))

test_bucketsort()
test_bucketsort_random()
