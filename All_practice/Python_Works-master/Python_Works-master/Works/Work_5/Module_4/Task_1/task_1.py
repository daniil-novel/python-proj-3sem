from typing import List
import deal


@deal.pre(lambda arr, k: isinstance(arr, List))
@deal.pre(lambda arr, k: isinstance(k, int))
@deal.post(lambda result: all(result[i] <= result[i + 1] for i in range(len(result) - 1)))
@deal.ensure(lambda result, old_result: sorted(old_result) == result)
@deal.raises(AssertionError)
@deal.reason(lambda: True, "The input list should only contain integers in the range 0 to k-1")
@deal.has(lambda arr, k: all(isinstance(x, int) and 0 <= x < k for x in arr))
def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr


bucketsort({1, 2, 3}, "hey")
