
# Write an iterative function iterPower(base, exp) that calculates the
# exponential baseexp by simply using successive multiplication. For example,
# iterPower(base, exp) should compute baseexp by multiplying base times itself
# exp times. Write such a function below.

# This function should take in two values - base can be a float or an integer;
# exp will be an integer ≥ 0. It should return one numerical value. Your code
# must be iterative - use of the ** operator is not allowed.

# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2017/courseware/0de4fecc5a9a4749923133fcf4de181f/38007cdb67c44b46b124cdbce33510b5/

def main():
    print("{} to the {} is {}".format(4, 7, iterPower(4, 7)))

def iterPower(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    else:
        result = base
        for i in range(exp - 1):
            result *= base

    return result

if __name__ == '__main__':
    main()
