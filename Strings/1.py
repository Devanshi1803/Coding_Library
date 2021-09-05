# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:04:31 2021

@author: devanshi
"""

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp