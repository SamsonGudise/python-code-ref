#!/usr/bin/python

import sys
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

def main():
    sumofit = sum(firstn(10))
    print "Sum of first 9 numbers ", sumofit

if __name__ == '__main__':
    sys.exit(main())
