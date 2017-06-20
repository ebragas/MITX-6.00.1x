
# Count the number of values in a dictionary, including the values in nested
# sequences

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Iterative solution
    total = 0
    for i in aDict.values():
        total += len(i)
    return total

print(how_many(animals))
