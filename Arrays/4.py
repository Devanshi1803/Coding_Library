def sort012(arr,n):
    count = dict()  #dictionary to count
    count[0] = 0
    count[1] = 0
    count[2] = 0
    for i in range(n):
        count[arr[i]] = count[arr[i]]+1
    
    for j in range(n):  #replace digits in arr 
        if count[0] > 0:
            arr[j] = 0
            count[0]-=1
        elif count[1] > 0:
            arr[j] = 1
            count[1]-=1
        else:
            arr[j] = 2
            count[2]-=1
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        sort012(arr,n)
        for i in arr:
            print(i,end='')
        print()