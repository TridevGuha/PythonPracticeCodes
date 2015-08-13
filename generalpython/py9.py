#!/usr/bin/env python3
'''This program is to evaluate a quadratic equation'''
import math
a=int(input("Enter value of a: "))
b=int(input("Enter value for b: "))
c=int(input("Enter value for c: "))
d = b * b - 4 * a * c
if d < 0:
    print("ROOTS ARE IMAGINARY")
else:
    roota = (-b + math.sqrt(d)) + (2.0 * a)
    rootb = (-b - math.sqrt(d)) + (2.0 * a)
print("Root 1 = ", roota)
print("Root 2 = ", rootb)