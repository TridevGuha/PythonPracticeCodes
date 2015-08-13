#!/usr/bin/env python3
'''An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, 
each containing a single integer n, 1<=n<=100.'''
# For each integer n given at input, display a line with the value of n!
import math
x = int(input("Enter a positive integer number: "))
if x < 0:
    print("The number cannot be negative")
elif x == 0:
    fact = 1
    print(fact)
else:
    N = int(input("Enter a positive integer number: ")
    i = 1
    for i in N:
        fact = N * i
        N += i
    print("Factorial= %d %(fact)")
