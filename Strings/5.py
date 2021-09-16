# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 16:03:02 2021

@author: devanshi
"""

class Solution:
    def countAndSay(self, n):
        
        string =""
        if n==1:
            return "1"
        ret = Solution().countAndSay(n-1)
        count=1
        print(ret)
        for i in range(1,len(ret)):
            
            if ret[i-1]==ret[i]:
                count+=1
            else:
                string=string+str(count)+ret[i-1]
                count=1
        
        string=string+str(count)+ret[len(ret)-1]                 
        return string

print(Solution().countAndSay(4))