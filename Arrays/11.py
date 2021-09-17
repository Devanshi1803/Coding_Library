# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:13:22 2021

@author: devanshi
"""
#approach-1
#O(nlogn)->The sort invocation costs O(nlogn) time in Python and Java, so it dominates the subsequent linear scan.
class Solution:
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
#approach-2
#O(n)->Set in both Python and Java rely on underlying hash tables, so insertion 
#and lookup have amortized constant time complexities. The algorithm is 
#therefore linear, as it consists of a for loop that performs constant work nn 
#times.
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)