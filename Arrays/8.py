# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:13:10 2021

@author: devanshi
"""

#import math
#Kadane's Algorithm
def maxSubArraySum(a,size):
    max =0 
    temp = 0
    for i in range(size):
        temp = temp + a[i]
        if temp < 0:
            temp =0
        if max<temp:
            max = temp
    return max

def main():
    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        
        print(maxSubArraySum(arr,n))

        T -= 1


if __name__ == "__main__":
    main()