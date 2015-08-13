#!/usr/bin/env python3
'''Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5,and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US.Calculate Pooja's account balance 
after an attempted transaction.'''

print("Welcome Pooja")
x = int(input("Enter the amount of cash you want to withdraw: "))
if x % 5 == 0 and 0 < x <= 2000:
    print("Withdraw cash: %d" % (x))
    charge = 0.5 * x
    balance = 2000 - x - charge
    print("Charge on transaction: %d" % (charge))
    print("Current Balance: %d" % (balance))
else:
    print("Transaction cannot be proccessed!")
