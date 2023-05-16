def bucketsort():
    user_input = input()
    arr = list(map(int, user_input.split()))
    k = max(arr)
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr
