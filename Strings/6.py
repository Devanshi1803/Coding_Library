# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 14:56:51 2021

@author: devanshi
"""


class Solution:
    def find_permutation(self, S):
        # Code here
        S1 = str2list(S)
        ans = []
        permute(S1,0,len(S1),ans)
        return ans
        
def str2list(string):
    list1=[]
    list1[:0]=string
    return list1
    
def permute(S,l,n,ans):
    print("permute(" +str(S)+", "+str(l)+", "+str(n)+", "+str(ans)+")")
    S2 = S[l:]
    S2.sort()               #ljr -> jlr jrl ljr lrj rjl rlj
    S[l:] = S2
    if l==n-1:
        ans.append("".join(S))
        #print("before ret "+str(S))
        #print("*")
        return
    else:  
        for i in range(l,n):
            #print("l: "+str(l))
            #print("i: "+str(i))
            S1=S.copy()
            temp = S1[i]
            S1[i]= S1[l]
            S1[l]= temp
            #print("ANS"+str(ans))
            #print("S: "+str(S))
            permute(S1,l+1,n,ans)
            #print("--")
            #print("ans:"+str(ans))
                    
    
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.find_permutation(S)
        for i in answer:
            print(i,end=' ')
        print()
