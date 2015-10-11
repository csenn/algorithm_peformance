
# (n + 1)(n / 2)
# n^2
def selection_sort(arr):

	arr_len = len(arr)

	def swap(index_1, index_2):
		temp = arr[index_1]
		arr[index_1] = arr[index_2]
		arr[index_2] = temp

	def find_next_smallest_index(start_idx, value):

		small_index = start_idx
		small_value = value

		for idx in range(start_idx, arr_len):
			if arr[idx] < small_value:
				small_value = arr[idx]
				small_index = idx
		return small_index

	for i in range(0, arr_len):
		swap_idx = find_next_smallest_index(i, arr[i])
		if swap_idx != i:
			swap(i, swap_idx)

	return arr