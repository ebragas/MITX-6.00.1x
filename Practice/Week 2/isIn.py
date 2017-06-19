
# Use bisection to search for a character in a sorted string

def isIn(char, aStr):
    print(aStr)
    m = len(aStr) // 2
    if len(aStr) < 1:
        return False
    elif char == aStr[m]:
        return True
    elif char < aStr[m]:
        return isIn(char, aStr[ : m])
    else:
        return isIn(char, aStr[m + 1:])


print(isIn('x', 'abcdefghijklmn'))
