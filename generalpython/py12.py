#!/usr/bin/env python3
'define functions'
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mult(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

'take input from the user'
c = int(input("Enter 1st number:"))
d = int(input("Enter 2nd number:"))
choice = input("Enter your choice + , - , * , /")

'function calls'
if choice == '+':
    add(c,d)
elif choice == '-':
    sub(c,d)
elif choice == '*':
    mult(c,d)
elif choice == '/':
    div(c,d)
else:
    print("Invalid choice")
