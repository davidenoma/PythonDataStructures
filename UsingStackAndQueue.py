# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:50:27 2020

@author: kora
"""
from Stack import Stack
from Queue import Queue
    
# Using Stack to Reverse Letters of a word 
word = input("Enter a word: ")
reverse = Stack()
for ch in word:
    reverse.push(ch)
rev_string = ""
i = 0
while i < reverse.len():
    rev_string+=reverse.pop()
print(rev_string)
#To determine whether a word is a palindrome or not
word = input("Enter a word: ")
palStack = Stack()
palQueue = Queue()
for ch in word:
    palQueue.enqueue(ch)
    palStack.push(ch)
j = 0
while i < len(word):    
    if palQueue.dequeue() == palStack.pop():
        j+=1
    i+=1
if j==len(word):
    print(word," is a palindrome")
else:
    print(word,"is not a palindrome")



