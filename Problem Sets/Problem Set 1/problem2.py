# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:50:51 2017

@author: ericb
"""

s = 'azcbobobegghakl'

# string to find
x = 'bob'

count = 0
for i in range(len(s)):
    if s[i] == x[0] and s[i:i + len(x)] == x:
        count += 1
        
print('Number of times bob occurs is:', count)