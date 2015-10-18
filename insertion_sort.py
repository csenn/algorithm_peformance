# ( n^2 - n ) / 2
# n^2


def insertion_sort(arr):
    def shift_right(right_index):

        start_val = arr[right_index]

        while right_index >= 1:
            if arr[right_index] >= arr[right_index - 1]:
                break
            temp = arr[right_index]
            arr[right_index] = arr[right_index - 1]
            arr[right_index - 1] = temp
            right_index -= 1

    arr_len = len(arr)
    for idx in range(1, arr_len):
        shift_right(idx)

    return arr
