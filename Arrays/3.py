#quick select algo(divide and conquer strategy) - kth smallest element in O(n) time
#for algo read sem 1 algo notes (SEL<-pdf name)
import math
def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    pivot = math.ceil((l+r)/2)
    #print(arr)
    #print("pivot:: "+str(pivot))
    #print("arr[pivot]:: "+str(arr[pivot]))
    #print("k:: ",k)
    less_than_pivot=[]
    equal_to_pivot = []
    greater_than_pivot = []
    for i in range(r+1):
        if arr[i] < arr[pivot]:
            less_than_pivot.append(arr[i])
        elif arr[i] == arr[pivot]:
            equal_to_pivot.append(arr[i])
        else:
            greater_than_pivot.append(arr[i])
            
    #print(less_than_pivot)
    #print(equal_to_pivot)
    #print(greater_than_pivot)
    #print("----")
    if len(less_than_pivot) == k-1:
        #print("*")
        #print(equal_to_pivot[0])
        return equal_to_pivot[0]
    elif len(less_than_pivot) >= k:
        return kthSmallest(less_than_pivot, 0, len(less_than_pivot)-1, k)        
    else:
        k1 = k-len(less_than_pivot)-len(equal_to_pivot)
        return kthSmallest(greater_than_pivot, 0, len(greater_than_pivot)-1, k1)
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        #print(type(arr))
        print(kthSmallest(arr, 0, n-1, k))