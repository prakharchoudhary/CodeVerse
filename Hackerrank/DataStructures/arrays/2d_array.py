#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
def largest_hourglass(a):
    largest = -10000
    for i in range(1,5):
        for j in range(1,5):
            sum1 = 0
            sum1 += a[i-1][j] + a[i+1][j] + a[i-1][j-1] + a[i-1][j+1] + a[i][j] + a[i+1][j-1] + a[i+1][j+1] 
            if sum1>=largest:
                largest = sum1
    return largest
print largest_hourglass(arr)