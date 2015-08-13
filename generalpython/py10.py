#!/usr/bin/env python3
'''In this example we are going to calculate the salary of a camera salesman. His basic salary is 1500, for every camera he will sell he will get 200 and the commission on the month’s sale is 2 %. The input will be number of cameras sold and total price of the cameras.'''
basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02

numberofcamera = int(input("Enter the number of cameras sold: "))
price = float(input("Enter the total prices: "))
bonus = (bonus_rate * numberofcamera)
commision = (commision_rate * numberofcamera * price)

print("Bonus = %6.2f" % bonus)
print("Commision = %6.2f" % commision)
print(("Gross salary = %6.2f") % (basic_salary + bonus + commision))
