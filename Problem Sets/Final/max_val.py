
def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    
    m = None

    for i in t:
        if type(i) == type(0):
            if m == None or i > m:
                m = i
        else:
            n = max_val(i)
            if m == None or n > m:
                m = n
    
    return m

# Test cases
print(max_val((5, (1,2), [[1],[2]])))
print(max_val((5, (1,2), [[1],[9]])))