from selection_sort import selection_sort
from insertion_sort import insertion_sort
from binary_search import binary_search
import palindrome
import power
import utils


def assertTrue(value, expected, message):
	# Light Weight Test
	if value == expected:
		print '\nPASS: ' + message
	else:
		print '\nFAIL: Expected: %d got: %d' % (expected, value)


def run_factorial():
	assertTrue(utils.factorial(5), 120, 'Factorial 5')


def run_palindrome():
	assertTrue(palindrome.is_palindrome('ROTOR'), True, 'Palindrome Loop')
	assertTrue(palindrome.is_palindrome_recursive('ROTOR'), True, 'Palindrome Recursive')


def run_power():
	assertTrue(power.simple_power(3,4), 81, 'Power - Loop')
	assertTrue(power.recursive_power(3,4), 81, 'Power - Recursive')
	#power.speed_power()


def run_binary_sort():
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	did_pass = True
	for val in primes:
		result = binary_search(val, primes)
		if not isinstance(result, int) or result > 5:
			did_pass = False

	assertTrue(did_pass, True, 'Binary Search')


def run_selection_sort():
	rand_arr = utils.generate_random_array(100)
	copy = list(rand_arr)

	rand_arr.sort()
	approx_iterations = selection_sort(copy)
	assertTrue(utils.compare_arrays(rand_arr, copy), True, 'Selection Sort')


def run_insertion_sort():
	rand_arr = utils.generate_random_array(100)
	copy = list(rand_arr)

	rand_arr.sort()
	insertion_sort(copy)
	assertTrue(utils.compare_arrays(rand_arr, copy), True, 'Insertion Sort')


def main():
	# run_factorial()
	# run_palindrome()
	run_power()
	# run_binary_sort()
	# run_selection_sort()
	# run_insertion_sort()

	print '\nFinish\n'


if __name__ == '__main__':
    main()
