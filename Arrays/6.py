#read-->https://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/
#video->https://www.youtube.com/watch?v=EQQp4B_CU5Q&feature=youtu.be

#method-1(If given arrays are sorted and no duplicates are allowed)
#union-intersection -> O(m+n) (condition:: given arrays are sorted and no duplicate values)

def doUnion(a,n,b,m): #O(m+n)
    pointer_a=0
    pointer_b=0
    U=[]  #union set
    count=0
    for i in range(n+m):
        if pointer_a == n or pointer_b == m:
            break
        if a[pointer_a]<b[pointer_b]:
           count+=1
           U.append(a[pointer_a])
           pointer_a+=1
        elif a[pointer_a]>b[pointer_b]:
           count+=1
           U.append(b[pointer_b])
           pointer_b+=1
        else:
           count+=1
           U.append(b[pointer_b])
           pointer_b+=1
           pointer_a+=1 
        i+=1
    #print(pointer_a)
    #print(pointer_b)
    if pointer_a == n:
        l=b[pointer_b:]
        count+=len(l)                 
    else:
        l=b[pointer_a:]
        count+=len(l)        
    return count

def doIntersect(a,n,b,m): #o(m+n)
    pointer_a=0
    pointer_b=0
    I=[]  #union set
    count=0
    for i in range(n+m):
        if pointer_a == n or pointer_b == m:
            break
        if a[pointer_a]<b[pointer_b]:
           #count+=1
           #U.append(a[pointer_a])
           pointer_a+=1
        elif a[pointer_a]>b[pointer_b]:
           #count+=1
           #U.append(b[pointer_b])
           pointer_b+=1
        else:
           count+=1
           I.append(b[pointer_b])
           pointer_b+=1
           pointer_a+=1 
        i+=1
    #print(pointer_a)
    #print(pointer_b)        
    return count
    
"""

#method-2
#union-intersection -> O(mn)

def doUnion(a,n,b,m):
    a1=set(a)
    b1=set(b)
    n1 = len(a1)
    m1 = len(b1)
    if n1>m1:
        count = n1
        for i in b1:
            if i not in a1:
                count+=1
    else:
        count = m1
        for i in a1:
            if i not in b1:
                count+=1
    return count


def doIntersect(a,n,b,m):
    a1=set(a)
    b1=set(b)
    count=0
    for i in a1:
        if i in b1:
            count+=1
    return count
"""

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        
        
        print(doUnion(a,n,b,m))
        print(doIntersect(a,n,b,m))
# } Driver Code Ends