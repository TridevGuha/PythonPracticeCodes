#!/usr/bin/env python3
'''Palindrome are the kind of strings which are same from left or right whichever way you read them. Example “madam”. In this example we will take the word as input from the user and say if it is palindrome or not.'''
s = input("Enter a string: ")
z = s[::-1]
if s == z:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
