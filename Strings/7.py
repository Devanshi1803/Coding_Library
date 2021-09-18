# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:16:11 2021

@author: devanshi
"""

#DP-> recursion has more complexity so, to optimize recursion complexity, we use DP
#https://youtu.be/FVWAEzHSbRo

import numpy as np

class Solution:
    def solveWordWrap(self, nums, k):
        space = np.full((len(nums),len(nums)),276447231,dtype=int)
        for i in range(len(nums)):
            space[i,i] = k-nums[i]
            for j in range(i+1,len(nums)):
                space[i,j] = space[i,j-1] - nums[j] - 1
        print("Space: \n"+str(space))
        cost = np.full((len(nums),len(nums)),276447231,dtype = int)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if space[i,j] < 0:
                    cost[i,j]=276447231
                elif j==len(nums)-1:
                    cost[i,j]=0
                else:
                    cost[i,j] = space[i,j]**2
        print("Cost: \n"+str(cost))
        min_cost_from_starting_to_i = [276447231]*(len(nums)+1)
        min_cost_from_starting_to_i[-1] = 0
        #process of finding 'min_cost_from_starting_to_i'
        #[3,2,2,5] and k=6
        #for i=3 that is we are at 5(or we want to add 5)
        #following options are possible
        #line1->3,2,2,5
        
        #lines_with_min_cost(3)
        #new_line->2,2,5
        
        #lines_with_min_cost(3,2)
        #new_line->2,5
        
        #lines_with_min_cost(3,2,2)
        #new_line->5
        for i in range(len(nums)):
            for j in range(i+1):
                if cost[j][i]!=276447231 and min_cost_from_starting_to_i[j-1]+cost[j][i] < min_cost_from_starting_to_i[i]:
                    min_cost_from_starting_to_i[i] = min_cost_from_starting_to_i[j-1]+cost[j][i]
                    print("j: "+str(j))
        print(min_cost_from_starting_to_i)
        return min_cost_from_starting_to_i[-2]
        
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = int(input())
        nums = list(map(int,input().split()))
        k = int(input())
        ob = Solution()
        answer = ob.solveWordWrap(nums,k)
        print(answer)   

#https://realpython.com/copying-python-objects/
#https://stackoverflow.com/questions/50696181/python-how-does-appending-in-a-list-and-changing-an-element-in-a-list-differs
#recursion-approach-1
"""
import copy
class Solution:
    def solveWordWrap(self, nums, k):
		#Code here
        ans_list = []
        li = []
        li.append(nums[0])
        ans_list.append(li)
        cost = (k-nums[0])**2
        min_cost = my_func(nums,1,ans_list,k,cost)
        return min_cost

def my_func(nums,curr_index,ans_list,k,cost):
    print("curr_index: "+str(curr_index)+" ans_list: "+str(ans_list)+" cost: "+str(cost))
    min_cost = 2764472319
    #base condition
    if curr_index == len(nums):
        #print("here")
        cost = cost - ((k-sum(ans_list[-1])-len(ans_list[-1])+1)**2) #last line cost
        return cost
    
    if (k-sum(ans_list[-1])-len(ans_list[-1])+1)<=nums[curr_index]: #(sum(ans_list[i])+nums[curr_index])>=k:
        ans_list2 = copy.deepcopy(ans_list)
        cost2 = copy.deepcopy(cost)
        ans_list2.append([nums[curr_index]])
        cost2 = cost2+(k-nums[curr_index])**2
        min_cost = min(min_cost,my_func(nums, curr_index+1, ans_list2, k,cost2))
    else:
        ans_list1 = copy.deepcopy(ans_list)
        ans_list2 = copy.deepcopy(ans_list)
        cost1 = copy.deepcopy(cost)
        cost2 = copy.deepcopy(cost)
        ans_list2.append([nums[curr_index]])
        cost1 = cost1 - (k-sum(ans_list1[-1])-len(ans_list1[-1])+1)**2 
        ans_list1[-1].append(nums[curr_index])
        cost1 = cost1 + (k-sum(ans_list1[-1])-len(ans_list1[-1])+1)**2
        cost2 = cost2+(k-nums[curr_index])**2
        min_cost = min(min_cost,my_func(nums, curr_index+1, ans_list1, k,cost1),my_func(nums, curr_index+1, ans_list2, k,cost2))
    return min_cost
    
  
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = int(input())
        nums = list(map(int,input().split()))
        k = int(input())
        ob = Solution()
        answer = ob.solveWordWrap(nums,k)
        print(answer)   

"""
"""
#recursion-approach-2
import copy
class Solution:
    def solveWordWrap(self, nums, k):
		#Code here
        ans_list = []
        li = []
        li.append(nums[0])
        ans_list.append(li)
        cost = my_func(nums,1,ans_list,k)
        return cost

def my_func(nums,curr_index,ans_list,k):
    print("curr_index: "+str(curr_index)+" ans_list: "+str(ans_list))
    #print("local?? "+ str(ans_list1))
    min_cost = 2764472319
    if curr_index == len(nums):
        total_cost = 0
        for i in range(len(ans_list)-1):
            #print("total_cost before: "+ str(sum(ans_list[i])))
            total_cost=total_cost+ (k-sum(ans_list[i])-len(ans_list[i])+1)**2
            print("total_cost after: "+ str(total_cost))
        return total_cost
   
    for i in range(len(ans_list)+1):
        #print("######curr_index: "+str(curr_index)+" ans_list: "+str(ans_list1))
        ans_list2 = copy.deepcopy(ans_list)
        if i == len(ans_list):
            ans_list.append([])
        if (k-sum(ans_list[i])-len(ans_list[i])+1)<=nums[curr_index]: #(sum(ans_list[i])+nums[curr_index])>=k:
            continue
        ans_list[i].append(nums[curr_index])
        cost = my_func(nums, curr_index+1, ans_list, k)
        ans_list = copy.deepcopy(ans_list2)
        #print("-----curr_index: "+str(curr_index)+" ans_list: "+str(ans_list2))
        min_cost = min(min_cost,cost)
    #print("min_cost: "+str(min_cost))
    return min_cost
        
  
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = int(input())
        nums = list(map(int,input().split()))
        k = int(input())
        ob = Solution()
        answer = ob.solveWordWrap(nums,k)
        print(answer)        
"""
