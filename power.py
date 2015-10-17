def simple_power(base, n):
    total = base
    for i in xrange(1, n):
        # print i
        total *= base
    return total


def recursive_power(base, n):
    # print n
    if n == 0:
        return 1
    elif n > 0 and n % 2 == 0:
        even_power = recursive_power(base, n / 2)
        return even_power * even_power
    elif n > 0:
        return base * recursive_power(base, n - 1)
    else:
        return 1 / recursive_power(base, n * -1)


# Compare number of iterations of each implemenation
# Recursive is much more efficient, as it splits all evens
def speed_power():
    simple_power(2, 21)
    print ' - '
    recursive_power(2, 21)
