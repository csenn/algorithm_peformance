import copy
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from binary_search import binary_search
from merge_sort import merge_sort
import palindrome
import power
import towers_of_hanoi
import utils


def assert_true(value, expected, message):
    # Light Weight Test
    if value == expected:
        print '\nPASS: ' + message
    else:
        print '\nFAIL: Expected: %d got: %d' % (expected, value)


def run_factorial():
    assert_true(utils.factorial(5), 120, 'Factorial 5')


def run_palindrome():
    assert_true(palindrome.is_palindrome('ROTOR'), True, 'Palindrome Loop')
    assert_true(palindrome.is_palindrome_recursive('ROTOR'), True, 'Palindrome Recursive')


def run_power():
    assert_true(power.simple_power(3, 4), 81, 'Power - Loop')
    assert_true(power.recursive_power(3, 4), 81, 'Power - Recursive')


def run_towers_of_hanoi():
    towers = towers_of_hanoi.TowersOfHanoi()
    towers.set_initial_state(2)
    initial_towers = copy.deepcopy(towers.towers)
    # Should end in index 1
    towers.solve()
    zipped = zip(initial_towers[0], towers.towers[1])
    does_pass = True
    for match in zipped:
        if match[0] != match[1]: does_pass = False
    assert_true(does_pass, True, 'Towers of Hanoi')


def run_binary_sort():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    did_pass = True
    for val in primes:
        result = binary_search(val, primes)
        if not isinstance(result, int) or result > 5:
            did_pass = False

    assert_true(did_pass, True, 'Binary Search')


def run_selection_sort():
    rand_arr = utils.generate_random_array(100)
    copy = list(rand_arr)

    rand_arr.sort()
    approx_iterations = selection_sort(copy)
    assert_true(utils.compare_arrays(rand_arr, copy), True, 'Selection Sort')


def run_insertion_sort():
    rand_arr = utils.generate_random_array(101)
    rand_copy = list(rand_arr)
    rand_arr.sort()
    insertion_sort(rand_copy)
    assert_true(utils.compare_arrays(rand_arr, rand_copy), True, 'Insertion Sort')


def run_merge_sort():
    rand_arr = utils.generate_random_array(100)
    rand_copy = list(rand_arr)
    rand_arr.sort()
    merge_sort(rand_copy)
    assert_true(utils.compare_arrays(rand_arr, rand_copy), True, 'Merge Sort')


def main():
    run_factorial()
    run_palindrome()
    run_power()
    run_towers_of_hanoi()
    run_binary_sort()
    run_selection_sort()
    run_insertion_sort()
    run_merge_sort()


    print '\nFinish\n'


if __name__ == '__main__':
    main()
