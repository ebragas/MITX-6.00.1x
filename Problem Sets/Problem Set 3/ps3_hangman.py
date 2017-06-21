# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
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



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter + ' '
        else:
            word += '_ '

    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letter in lettersGuessed:
        alpha.remove(letter)

    return ''.join(alpha)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    # Variables to track
    guessCount = 8
    lettersGuessed = []
    won = False

    # Print number of letters in secret word
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    print("------------")

    while won != True:
        # Initiate round
        print("You have {} guesses left.".format(guessCount))
        print("Available letters: {}".format(getAvailableLetters(lettersGuessed)))

        # Request guess
        guess = input("Please guess a letter: ").lower()

        # Check validity
        if guess in lettersGuessed:
            print("Oops! You've already guessed "
                  "that letter: {}".format(getAvailableLetters(lettersGuessed)))
        elif guess not in secretWord:
            print("Oops! That letter is not in my "
                  "word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            guessCount -= 1
        else:
            print("Good guess: {}".format(getGuessedWord(secretWord, lettersGuessed)))

        print("------------")

        # Is game won
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            won = True


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = "eric"
hangman(secretWord)
