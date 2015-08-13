#!/usr/bin/env python3 
import sys
 
def div(a, b):
    try:
        # This could be a block of code with many lines
        return a / b
    except ZeroDivisionError:
        return "You cannot divide a number by 0"
 
if __name__ == '__main__':
    print(div(int(sys.argv[1]), int(sys.argv[2])))
