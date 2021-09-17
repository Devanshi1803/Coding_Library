# -*- coding: utf-8 -*-
"""
Created on Mon May 17 19:15:18 2021

@author: devanshi
"""

#User function Template for python3
#https://youtu.be/vBdo7wtwlXs
#https://youtu.be/5lPNYiuUl1s

"""
#recursive approach
class Solution:
    def minJumps(self, arr, n):
        if arr[0]==0:
	        return -1
        if n<=1:
	        return 0
        if len(arr)==1:
	        return 1
        curr = arr[0]
        ans= 9999
        for i in range(1,curr+1):
            if i>=n:
                break
            ob1 = Solution()
            ans = min(ob1.minJumps(arr[i:],len(arr[i:])),ans)      
        return ans+1
"""
#linear approach
#understand with example(after watching first video)-> 2 3 1 1 1 4
class Solution:
    def minJumps(self, arr, n):
        if arr[0]==0:
	        return -1
        if n<=1:
	        return 0
        ladder = arr[0]
        stairs = arr[0]
        jump = 1
        for i in range(1,n):
            if i==n-1:
                return jump
            ladder = max(ladder,i+arr[i]) 
            stairs-=1
            if stairs==0:
                jump+=1
                if i>=ladder:
                    return -1
                stairs = ladder-i
                
            
if __name__ =='__main__':
    T=int(input())
    for i in range(T):
        n=int(input())
        Arr = [int(x) for x in input().split()]
        ob =Solution()
        print(ob.minJumps(Arr, n))
      
        
      
    
