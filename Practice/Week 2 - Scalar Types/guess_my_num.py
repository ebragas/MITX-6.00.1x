# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:33:32 2017

@author: ericb
"""

# variables
high = 100
low = 0
response = ''

print('Please think of a number between {} and {}!'.format(low, high))

while True:
    
#    guess = round((high + low) / 2)
    guess = (high + low) // 2  # problem checker expected integer division
    
    print('Is your secret number {}? '.format(guess))
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if response == 'c':
        break
    elif response == 'h':
        high = guess
    elif response == 'l':
        low = guess
    else:
        print('Sorry, I did not understand your input.')
        
print('Game over. Your secret number was: {}'.format(guess))