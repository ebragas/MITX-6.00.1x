# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 13:47:13 2017

@author: ericb
"""

# do not include
s = 'azcbobobegghakl'

count = 0
for char in s:
    if char in ('a', 'e', 'i', 'o', 'u'):
        count += 1

print('Number of vowels: ', count)