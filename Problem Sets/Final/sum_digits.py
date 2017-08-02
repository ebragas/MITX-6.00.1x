
def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    total = 0
    num = 0

    for c in s:
        try:
            num = int(c)
        except ValueError:
            num = 0
    
        total += num
    
    return total

print(sum_digits("a;35d4"))
