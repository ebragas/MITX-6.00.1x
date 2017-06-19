
# Accept two integers and return the greatest common denominator of the two

def main():
    a, b = 9, 12
    print("gcd({}, {}) = {}".format(a, b, gcdRecur(a, b)))

def gcdRecur(a, b):
    """
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    """
    if a % a == 0 and b % a == 0:
        return a
    else:
        return gcdRecur(b, a % b)

if __name__ == '__main__':
    main()
