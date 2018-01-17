#!/usr/bin/python
import sys

class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()

def main():
    sumoffirstn=sum(firstn(10))
    print "sum of first 9 number = ",sumoffirstn

if __name__ == '__main__':
   sys.exit(main())
