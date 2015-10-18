import math

# n * log(n)
# Fun times, indexes were sort of a pain b/c xrange


def get_middle_index(arr):
    return int(math.floor((len(arr)) / 2))


def _merge(array, p, q, r):

    low_half = []
    high_half = []

    for i in xrange(0, q - p + 1):
        low_half.append(array[p + i])

    for j in xrange(0, r - q):
        high_half.append(array[q + j + 1])

    k = p
    i = 0
    j = 0

    low_length = len(low_half)
    high_length = len(high_half)

    while True:
        if i >= low_length or j >= high_length:
            break
        if low_half[i] < high_half[j]:
            array[k] = low_half[i]
            i += 1
        else:
            array[k] = high_half[j]
            j += 1
        k += 1

    while i < low_length:
        array[k] = low_half[i]
        i += 1
        k += 1

    while j < high_length:
        array[k] = high_half[j]
        j += 1
        k += 1


def _merge_sort(arr, p, r):
    if r > p:
        mid_index = int(math.floor((p+r) / 2))

        _merge_sort(arr, p, mid_index)
        _merge_sort(arr, mid_index + 1, r)
        _merge(arr, p, mid_index, r)


def merge_sort(arr):
    _merge_sort(arr, 0, len(arr) - 1)


