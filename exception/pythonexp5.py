#!/usr/bin/env python3
import sys
 
def div(a, b):
    try:
        print(c)
        a, b = int(a), int(b)
        return a / b
    except ValueError:
        return "You can only divide integers and floats."
    except ZeroDivisionError:
        return "You cannot divide a number by 0"
    except Exception as e:
        print('Hit an unknown bug')
        return e
 
if __name__ == '__main__':
    print(div(sys.argv[1], sys.argv[2]))
