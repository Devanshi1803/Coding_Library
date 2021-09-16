# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:36:24 2021

@author: devanshi
"""

#check whether result is valid shuffle of first and second or not
def valid_Shuffle(first,second,result):
    if len(first)+len(second)!=len(result):
        return 0
    else:
        first = sorted(first)
        second = sorted(second)
        result = sorted(result)
        #print(first)
        #print(second)
        #print(result)
        ptr_to_first = 0
        ptr_to_second = 0
        for i in range(len(result)):
            #print("first: "+str(ptr_to_first))
            #print("second: "+str(ptr_to_second))
            #print("result: "+str(i))
            if ptr_to_first<len(first) and result[i]==first[ptr_to_first]:
                ptr_to_first+=1
            elif ptr_to_second<len(second) and result[i]==second[ptr_to_second]:
                ptr_to_second+=1
            else:
                return 0
        if ptr_to_first<len(first) or ptr_to_second<len(second):
            return 0
        return 1
        
        

first = "1X"
second = "Y2"
#valid shuffles are-> 1XY2,21XY,Y12X,Y1X2,Y21X,.......
result= "XY12"
print(valid_Shuffle(first, second, result))