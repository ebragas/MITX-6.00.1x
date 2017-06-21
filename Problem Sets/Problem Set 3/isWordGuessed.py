
def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
    """
    letters = len(secretWord)
    counter = 0

    for letter in lettersGuessed:
        if letter in secretWord:
            counter += 1  # count letter
        else:
            pass  # don't count

    if letters == counter:
        return True
    else:
        return False



# Test Cases
SecretWord = 'apple'
LettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# SecretWord = 'eric'
# LettersGuessed = ['e', 'r', 'i', 'c']

print(isWordGuessed(SecretWord, LettersGuessed))
