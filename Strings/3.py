# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 14:55:21 2021

@author: devanshi
"""

def areRotation(str1,str2):
    if len(str1)!=len(str2):
        return 0
    else:
        temp = str1+str1
        if temp.count(str2)>0:   #count the no of occurence of str2 in temp
            return 1
        else:
            return 0

print(areRotation("ABCD","BCDA"))