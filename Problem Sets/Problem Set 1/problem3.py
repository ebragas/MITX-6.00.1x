# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:10:07 2017

@author: ericb
"""

#find the longest sequence of characters that appear in alphabetical order

# input string
s = 'azcbobobegghakl'
#s = 'abcalmost'

# temp string and final result
temp = ''
result = ''

for x in range(len(s)):
    # start new string
    temp = s[x]
    
    # add subsequent alphabetical characters; break when sequential char reached
    for y in s[x + 1:]:
        if y >= temp[-1]:
            temp = temp + y
        else:
            break
        
    if len(temp) > len(result):
        result = temp

print('Longest substring in alphabetical order is:', result)