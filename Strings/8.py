# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:20:52 2021

@author: devanshi
"""

#DP
import numpy as np
class Solution:
    def editDistance(self, s, t):
        dp = np.zeros((len(s)+1,len(t)+1),dtype=int)
        dp[0,0]=0
        for i in range(1,len(s)+1):
            dp[i,0] = dp[i-1,0]+1
        for j in range(1,len(t)+1):
            dp[0,j] = dp[0,j-1]+1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i,j] = dp[i-1,j-1]
                else:
                    dp[i,j] = min(dp[i-1,j],dp[i,j-1],dp[i-1,j-1])+1  #insert,delete,replace
        print(dp)
        return dp[-1,-1]
                
        
        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s,t = input().split()
        ob = Solution()
        answer = ob.editDistance(s,t)
        print(answer)

#recursion -> O(3^m)
"""
class Solution:
    def editDistance(self, s, t):
        return IDR(s, t, len(s), len(t))
def IDR(s,t,i,j):
    #print(str(i)+"-"+str(j))
    if i==0:
        return j
    if j ==0:
        return i
    if s[i-1] == t[j-1]:
        i=i-1
        j=j-1
        return IDR(s,t,i,j)
    else:
        return min(IDR(s,t,i,j-1),IDR(s,t,i-1,j),IDR(s,t,i-1,j-1))+1 
        
        
        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s,t = input().split()
        ob = Solution()
        answer = ob.editDistance(s,t)
        print(answer)
"""
