
class Solution:
    def middle(self,A,B,C):
        if(A>B and A>C):   # A is largest
            if(B>C):       # B is second largest(middle)   
                return B
            else:        
                return C
        elif(B>C):      # B is largest
            if(A>C):       # A is second largest(middle)
                return A
            else:
                return C
        else:               # C is largest
            if(A>B):
                return A
            else:
                return B
        

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
