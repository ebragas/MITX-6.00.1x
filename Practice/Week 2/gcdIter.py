
# Accept two integers and return the greatest common denominator of the two


def main():
    a, b = 9, 12
    print("gcd({}, {}) = {}".format(a, b, gcdIter(a, b)))

def gcdIter(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    # Setup
    x, y = 0, 0
    if a == b:
        return a
    elif a < b:
        x, y = a, b
    else:
        x, y = b, a

    # Test
    i = x
    while i > 0:
        if x % i == 0 and y % i == 0:
            return i
        else:
            i -= 1

    # No solution found
    return 1

if __name__ == '__main__':
    main()
