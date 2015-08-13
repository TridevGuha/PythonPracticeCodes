#!/usr/bin/env python3
'''Let us write a program to evaluate the power series. The series looks like e**x =1+x+x**2/2! +x**3/3! +....+ x**n/n! where 0 < x < 1'''
x = float(input("Enter the value of x: "))
n = term = num = 1
sum = 1.0
while n <= 100:
    term *= x/n
    sum += term
    n += 1
    if term < 0.0001:
        break
print("Number of times = %d and Sum = %f" % (n,sum))