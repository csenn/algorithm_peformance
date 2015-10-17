import math


# log(n) lookup
def binary_search(search_value, values):
    def iterate(counter=0, min_index=0, max_index=len(values) - 1):

        counter += 1

        mid_index = int(math.floor((max_index - min_index) / 2)) + min_index

        # Not the best, but I get the point
        if values[mid_index] == search_value or values[mid_index + 1] == search_value:
            return counter

        if values[mid_index] > search_value:
            return iterate(counter, min_index, mid_index)

        if values[mid_index] < search_value:
            return iterate(counter, mid_index, max_index)

    return iterate()
