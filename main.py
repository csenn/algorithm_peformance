from selection_sort import selection_sort
from insertion_sort import insertion_sort
from binary_search import binary_search
import utils


def run_binary_sort():
	print '\nBinary Search'
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	for val in primes:
		print 'Found %d in about %d steps' % (val, binary_search(val, primes))


def run_selection_sort():
	print '\nSelection Sort'
	rand_arr = utils.generate_random_array(100)
	copy = list(rand_arr)

	rand_arr.sort()
	selection_sort(copy)

	if utils.compare_arrays(rand_arr, copy):
		print 'PASS: Correct Sort'


def run_insertion_sort():
	print '\nInsertion Sort'
	rand_arr = utils.generate_random_array(100)
	copy = list(rand_arr)

	rand_arr.sort()
	insertion_sort(copy)

	if utils.compare_arrays(rand_arr, copy):
		print 'PASS: Correct Sort'


def main():
	run_binary_sort()
	run_selection_sort()
	run_insertion_sort()


if __name__ == '__main__':
    main()
