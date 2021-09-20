# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:17:16 2021

@author: devanshi
"""
#User function Template for python3
#Do not go for binary search(approach-2) insted go with linear search(approach-1) as approach-2 was not accepted
#approach-1
class Solution:
    def nextPermutation(self, N, arr):
        # code here
        flag=0
        for i in range(N-1,0,-1):
            if arr[i-1]<arr[i]:
                index1 = i-1
                for p in range(N-1,i-1,-1):
                    if arr[p]>arr[index1]:
                        index2 = p
                        break
                arr[index1],arr[index2] = arr[index2],arr[index1] #swap
                print(arr)
                #reverse from i to N-1
                reverse(i,arr)
                flag=1
                break
        if flag==0:
            reverse(0, arr)
        return arr
def reverse(i,arr):
     for m in range(i,(i+(N-1-i)//2)+1):
         arr[m],arr[N-1-(m-i)] = arr[N-1-(m-i)],arr[m]
        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N= int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        ob = Solution()
        answer = ob.nextPermutation(N,arr)
        for i in range(N):
            print(answer[i],end=" ")
        print()
#approach-2
"""
class Solution:
    def nextPermutation(self, N, arr):
        # code here
        flag=0
        for i in range(N-1,0,-1):
            if arr[i-1]<arr[i]:
                index1 = i-1
                index2 = binary_search(N,arr,i)
                arr[index1],arr[index2] = arr[index2],arr[index1] #swap
                print(arr)
                #reverse from i to N-1
                reverse(i,arr)
                flag=1
                break
        if flag==0:
            reverse(0, arr)
        return arr
def reverse(i,arr):
     for m in range(i,(i+(N-1-i)//2)+1):
         arr[m],arr[N-1-(m-i)] = arr[N-1-(m-i)],arr[m]

def binary_search(N,arr,start):  #to find the smallest number which is greater than the number at index- index1
    num = arr[start-1] #number at index->index1
    end = N-1
    mid = (start+end)//2
    if start==end:
        return start
    while(start<end):
        if start+1==end:
            if arr[end]<num:
                return arr.index(arr[start])
            else:
                return arr.index(arr[end])
        if mid > num:
            start = mid
        else: 
            end = mid

        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N= int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        ob = Solution()
        answer = ob.nextPermutation(N,arr)
        for i in range(N):
            print(answer[i],end=" ")
        print()
"""
