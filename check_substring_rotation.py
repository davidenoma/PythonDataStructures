# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:36:03 2020
@author: David Enoma
"""


def isSubstring(s1, s2):
    indicator = 0
    for letter in s2:
        if letter not in s1:
            indicator+=1
    if indicator > 0:
        print("This is not a substring")
    else:
        print("This is a substring!")
    if (s1[::-1]  == s2):
        print("This is a rotation!")
    else:
        print("This is not a rotation")



isSubstring("fesobi", "ibosef")
