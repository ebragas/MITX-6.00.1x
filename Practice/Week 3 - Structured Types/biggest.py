
# Return the key of the element with the most values. Return a list of keys if
# there is a tie.

# setup
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it.
    """
    # Alternate dictionary of keys and list lengths
    len_dict = {}
    for i in aDict:
        len_dict[i] = len(aDict[i])

    # Find largest length value
    val = max(len_dict.values())

    # Find key with same value
    for i in len_dict:
        if len_dict[i] == val:
            return i

print(biggest(animals))
