#!/usr/bin/python
import sys
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

def main():
    sumoffirstn = sum(firstn(10))
    print("Sum of first 10 = %d \n",sumoffirstn)

if __name__ == '__main__':
    sys.exit(main())
