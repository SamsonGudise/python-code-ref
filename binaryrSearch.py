#!/usr/bin/python

def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else: 
        midpoint=len(alist)/2
        if alist[midpoint]==item:
            return True
        else:
            if item < alist[midpoint]:
                binarySearch(alist[:midpoint],item)
            else:
                binarySearch(alist[midpoint+1],item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

