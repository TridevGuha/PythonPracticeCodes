#!/usr/bin/env python3
'''Some printing * examples'''
row = int(input("Enter the number of rows:"))
n=row
while n >= 0:
    x = "*" * n
    print(x)
    n -= 1
