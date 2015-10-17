from random import randint


def generate_random_array(len):
    arr = []
    for x in range(0, len):
        y = randint(0, 100)
        arr.append(y)
    return arr


def compare_arrays(arr_1, arr_2):
    arr_1_len = len(arr_1)
    arr_2_len = len(arr_2)

    if arr_1_len != arr_2_len:
        return False

    for i in range(0, arr_1_len):
        if arr_1[i] != arr_2[i]:
            return False

    return True


def factorial(n):
    # Base Case
    if n == 0:
        return 1
    return n * factorial(n - 1)
