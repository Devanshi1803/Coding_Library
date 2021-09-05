# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:09:00 2021

@author: devanshi
"""

class Solution:
    def isPlaindrome(self, S):
        # code here
        for i in range(len(S)//2):
            if S[i] != S[len(S)-i-1]:
                return 0
        
        return 1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.isPlaindrome(S)
        print(answer)

# } Driver Code Ends