
def isWordGuessed(SecretWord, LettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
    """
    letters = len(SecretWord)
    counter = 0

    for letter in LettersGuessed:
        if letter in SecretWord:
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
