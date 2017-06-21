
# oddTuples

# Given a tuple, return another tuple containing the odd (by index) elements of
# the input

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    outTup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            outTup = outTup + (aTup[i],)

    return outTup

print("Name: {}".format(oddTuples(('eric', 'bragas'))))
